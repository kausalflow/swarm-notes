"""Main entry point: orchestrates the full agent pipeline."""

from __future__ import annotations

import logging
import sys
import time
from pathlib import Path

import typer

app = typer.Typer(help="Swarm Notes Orchestrator")

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%SZ",
)
logger = logging.getLogger(__name__)

_TRANSIENT_HTTP_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
_PAPER_RETRY_DELAYS_SECONDS = (30.0, 90.0)
_MAX_PAPER_RETRY_WAIT_SECONDS = 120.0


def _is_retryable_paper_error(exc: Exception) -> bool:
    """Return ``True`` for transient upstream failures worth retrying."""
    seen: set[int] = set()
    current: BaseException | None = exc

    while current is not None and id(current) not in seen:
        seen.add(id(current))
        if getattr(current, "status_code", None) in _TRANSIENT_HTTP_STATUS_CODES:
            return True
        current = current.__cause__ or current.__context__

    return False


def _process_single_paper(paper, skill, src_config):
    """Process one paper once and return its analysis."""
    from swarm_notes import analyst
    from swarm_notes.vault_writer import write_paper

    analysis = analyst.analyse(paper, skill)

    if src_config.settings.enable_domain_expert:
        from swarm_notes.domain_expert import extract_open_questions

        analysis.open_questions = extract_open_questions(paper.arxiv_id, skill)

    write_paper(analysis, skill.name)
    return analysis


def _process_paper_with_retries(paper, skill, src_config):
    """Retry transient upstream failures for one paper with a bounded wait budget."""
    total_wait = 0.0
    max_attempts = len(_PAPER_RETRY_DELAYS_SECONDS) + 1

    for attempt in range(1, max_attempts + 1):
        try:
            return _process_single_paper(paper, skill, src_config)
        except Exception as exc:
            is_retryable = _is_retryable_paper_error(exc)
            if not is_retryable or attempt == max_attempts:
                if is_retryable:
                    logger.error(
                        "Paper %s failed after %d attempt(s): %s",
                        paper.arxiv_id,
                        attempt,
                        exc,
                    )
                raise

            remaining_wait = _MAX_PAPER_RETRY_WAIT_SECONDS - total_wait
            delay = min(_PAPER_RETRY_DELAYS_SECONDS[attempt - 1], remaining_wait)
            if delay <= 0:
                raise

            logger.warning(
                "Transient failure processing paper %s on attempt %d/%d: %s. Retrying in %.0f second(s).",
                paper.arxiv_id,
                attempt,
                max_attempts,
                exc,
                delay,
            )
            time.sleep(delay)
            total_wait += delay


@app.command()
def run(config: str = typer.Option("config.yaml", "--config", "-c", help="Path to config.yaml")) -> None:
    """Run the full pipeline."""
    from swarm_notes import config as src_config
    if Path(config).exists():
        src_config.load_yaml_config(config)
    else:
        logger.info("No config.yaml found at '%s', using environment variables / defaults.", config)

    from swarm_notes import federation, router, watcher
    from swarm_notes.vault_manager import commit_staging, discard_staging, init_staging, init_vault, get_existing_arxiv_ids
    from swarm_notes.vault_writer import update_public_feed, write_site_config

    # Load skills from disk based on config
    router.load_skills()

    # ------------------------------------------------------------------
    # 1. Initialise vault directories
    # ------------------------------------------------------------------
    logger.info("=== research-cruise pipeline starting ===")
    init_vault()
    write_site_config()

    # ------------------------------------------------------------------
    # 2. Prepare the staging area
    # ------------------------------------------------------------------
    init_staging()

    try:
        # ------------------------------------------------------------------
        # 3. Federation Agent – run BEFORE the watcher
        # ------------------------------------------------------------------
        logger.info("--- Step 3: Federation Agent ---")
        federation.run_federation()

        # ------------------------------------------------------------------
        # 4. Watcher – fetch recent papers from ArXiv
        # ------------------------------------------------------------------
        logger.info("--- Step 4: Watcher ---")
        papers = watcher.fetch_papers()

        if not papers:
            logger.warning("Watcher returned no papers – nothing to process")
            # Still a valid (empty) run; commit any federation changes
            commit_staging()
            raise typer.Exit(0)

        # ------------------------------------------------------------------
        # 4b. Deduplicate – skip papers already in the vault
        # ------------------------------------------------------------------
        existing_ids = get_existing_arxiv_ids()
        new_papers = [p for p in papers if p.arxiv_id not in existing_ids]
        skipped = len(papers) - len(new_papers)
        if skipped:
            logger.info(
                "Deduplication: skipping %d already-processed paper(s), %d new to process",
                skipped, len(new_papers),
            )
        papers = new_papers

        if not papers:
            logger.info("All fetched papers already exist in the vault – nothing to do")
            commit_staging()
            raise typer.Exit(0)

        # ------------------------------------------------------------------
        # 5. Router + Analyst + Vault Writer – process each paper
        # ------------------------------------------------------------------
        logger.info("--- Step 5: Router / Analyst / Vault Writer (%d papers) ---", len(papers))
        analyses = []
        skills_used_map = {}

        for paper in papers:
            try:
                skill = router.route(paper)
                logger.info(
                    "Processing %s with skill %s", paper.arxiv_id, skill.name
                )
                skills_used_map[skill.id] = skill
                analysis = _process_paper_with_retries(paper, skill, src_config)
                analyses.append(analysis)
            except Exception as exc:
                logger.error(
                    "Failed to process paper %s: %s", paper.arxiv_id, exc, exc_info=True
                )
                # Continue with other papers

        # ------------------------------------------------------------------
        # 6. Discussant – Synthesise insights
        # ------------------------------------------------------------------
        if analyses:
            logger.info("--- Step 6: Discussant (%d papers) ---", len(analyses))
            from swarm_notes.discussant import discuss_papers
            
            # If all papers used the same skill, pass it to the discussant for better focus
            primary_skill = None
            if len(skills_used_map) == 1:
                primary_skill = next(iter(skills_used_map.values()))
            
            discussion_md = discuss_papers(analyses, primary_skill)
            from swarm_notes.vault_writer import append_daily_discussion
            append_daily_discussion(discussion_md)

        # ------------------------------------------------------------------
        # 7. Update the public feed
        # ------------------------------------------------------------------
        if analyses:
            logger.info("--- Step 7: Update public feed (%d papers) ---", len(analyses))
            update_public_feed(analyses)

        # ------------------------------------------------------------------
        # 8. Atomic commit: move staging → vault
        # ------------------------------------------------------------------
        logger.info("--- Step 8: Committing staging to vault ---")
        commit_staging()

        logger.info(
            "=== Pipeline complete: %d/%d papers processed successfully ===",
            len(analyses),
            len(papers),
        )

    except typer.Exit:
        # Re-raise Typer exit as-is
        raise
    except Exception as exc:
        logger.critical("Pipeline crashed: %s", exc, exc_info=True)
        discard_staging()
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
