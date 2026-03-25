"""Main entry point: orchestrates the full agent pipeline."""

from __future__ import annotations

import logging
import sys
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


@app.command()
def run(config: str = typer.Option("config.yaml", "--config", "-c", help="Path to config.yaml")) -> None:
    """Run the full pipeline."""
    from swarm_cruise import config as src_config
    if Path(config).exists():
        src_config.load_yaml_config(config)
    else:
        logger.info("No config.yaml found at '%s', using environment variables / defaults.", config)

    from swarm_cruise import analyst, federation, router, watcher
    from swarm_cruise.vault_manager import commit_staging, discard_staging, init_staging, init_vault
    from swarm_cruise.vault_writer import update_public_feed, write_paper

    # ------------------------------------------------------------------
    # 1. Initialise vault directories
    # ------------------------------------------------------------------
    logger.info("=== research-cruise pipeline starting ===")
    init_vault()

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
        # 5. Router + Analyst + Vault Writer – process each paper
        # ------------------------------------------------------------------
        logger.info("--- Step 5: Router / Analyst / Vault Writer (%d papers) ---", len(papers))
        analyses = []

        for paper in papers:
            try:
                skill = router.route(paper)
                logger.info(
                    "Processing %s with skill %s", paper.arxiv_id, skill.name
                )
                analysis = analyst.analyse(paper, skill)
                
                # Check Domain Expert Configuration
                if src_config.settings.enable_domain_expert:
                    from swarm_cruise.domain_expert import extract_open_questions
                    questions = extract_open_questions(paper.arxiv_id)
                    analysis.open_questions = questions
                    
                write_paper(analysis, skill.name)
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
            from swarm_cruise.discussant import discuss_papers
            discussion_md = discuss_papers(analyses)
            from swarm_cruise.vault_writer import append_daily_discussion
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

    except Exception as exc:
        logger.critical("Pipeline crashed: %s", exc, exc_info=True)
        discard_staging()
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
