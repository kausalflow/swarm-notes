"""Librarian — standalone cron-job script for tag unification in the vault.

Usage
-----
    python librarian.py [--vault VAULT_DIR] [--taxonomy TAXONOMY_PATH]
                        [--model MODEL] [--apply]

The librarian:
1. Scans all ``.md`` files in the vault and collects every ``[[tag]]``.
2. Calls an LLM to identify near-duplicate tags
   (e.g. ``[[SSM]]`` and ``[[State Space Models]]``).
3. Prints the proposed merge mapping.
4. If ``--apply`` is passed, executes find-and-replace across the vault and
   updates ``taxonomy.json``.
"""

from __future__ import annotations

import json
import logging
import re
import sys
from pathlib import Path
from typing import Optional

import click
from pydantic import BaseModel
from pydantic_ai import Agent

logger = logging.getLogger(__name__)

_DEFAULT_VAULT = Path(__file__).parent / "vault"
_DEFAULT_TAXONOMY = Path(__file__).parent / "taxonomy.json"
_DEFAULT_MODEL = "openai:gpt-4o"


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


class MergeProposal(BaseModel):
    """A set of proposed tag merges suggested by the LLM."""

    merges: dict[str, str]
    """Mapping from *source* tag to *canonical* tag (e.g. ``{"SSM": "State Space Models"}``)."""

    reasoning: str
    """Brief human-readable explanation of why these merges were proposed."""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _collect_tags_from_vault(vault_dir: Path) -> list[str]:
    """Return a deduplicated, sorted list of all ``[[tags]]`` in the vault."""
    tags: set[str] = set()
    for md_file in vault_dir.glob("**/*.md"):
        text = md_file.read_text(encoding="utf-8", errors="replace")
        tags.update(re.findall(r"\[\[([^\]]+)\]\]", text))
    return sorted(tags)


def _propose_merges(
    tags: list[str],
    model: str = _DEFAULT_MODEL,
) -> MergeProposal:
    """Ask the LLM to identify near-duplicate tags and propose canonical names."""
    tag_list = "\n".join(f"- {t}" for t in tags)
    system_prompt = (
        "You are a knowledge-graph librarian. "
        "Your job is to identify near-duplicate or semantically equivalent tags "
        "in a personal research knowledge base and propose which ones should be "
        "merged into a single canonical form. "
        "Only suggest merges where you are highly confident the tags refer to the "
        "same concept. Prefer longer, more descriptive canonical names. "
        "Return a JSON object with two keys: "
        "'merges' (dict mapping source tag → canonical tag) and "
        "'reasoning' (brief explanation)."
    )
    user_message = (
        f"Here are all the tags currently in the vault:\n\n{tag_list}\n\n"
        "Please identify near-duplicates and return a merge mapping."
    )

    agent: Agent[None, MergeProposal] = Agent(
        model=model,
        output_type=MergeProposal,
        system_prompt=system_prompt,
    )
    result = agent.run_sync(user_message)
    return result.output


def _apply_merges(
    vault_dir: Path,
    merges: dict[str, str],
    taxonomy_path: Optional[Path] = None,
) -> None:
    """Execute find-and-replace across the vault for each proposed merge.

    Also updates ``taxonomy.json`` to reflect the new canonical tags.
    """
    if not merges:
        logger.info("No merges to apply.")
        return

    md_files = list(vault_dir.glob("**/*.md"))
    for md_file in md_files:
        text = md_file.read_text(encoding="utf-8", errors="replace")
        modified = text
        for source, canonical in merges.items():
            modified = modified.replace(f"[[{source}]]", f"[[{canonical}]]")
        if modified != text:
            md_file.write_text(modified, encoding="utf-8")
            logger.info("Updated: %s", md_file.name)

    if taxonomy_path and taxonomy_path.exists():
        try:
            existing: list[str] = json.loads(taxonomy_path.read_text())
        except (json.JSONDecodeError, OSError):
            existing = []
        # Remove source tags, ensure canonical tags are present
        updated = set(existing)
        for source, canonical in merges.items():
            updated.discard(source)
            updated.add(canonical)
        taxonomy_path.write_text(json.dumps(sorted(updated), indent=2))
        logger.info("Taxonomy updated.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


@click.command()
@click.option(
    "--vault",
    "vault_dir",
    default=str(_DEFAULT_VAULT),
    show_default=True,
    type=click.Path(file_okay=False, path_type=Path),
    help="Path to the Obsidian vault directory.",
)
@click.option(
    "--taxonomy",
    "taxonomy_path",
    default=str(_DEFAULT_TAXONOMY),
    show_default=True,
    type=click.Path(dir_okay=False, path_type=Path),
    help="Path to taxonomy.json.",
)
@click.option(
    "--model",
    default=_DEFAULT_MODEL,
    show_default=True,
    help="pydantic-ai model identifier.",
)
@click.option(
    "--apply",
    is_flag=True,
    default=False,
    help="Apply the proposed merges (default: dry-run only).",
)
def main(
    vault_dir: Path,
    taxonomy_path: Path,
    model: str,
    apply: bool,
) -> None:
    """Scan the vault, identify near-duplicate tags, and optionally unify them."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if not vault_dir.exists():
        click.echo(f"Vault directory not found: {vault_dir}", err=True)
        sys.exit(1)

    click.echo(f"Scanning vault: {vault_dir}")
    tags = _collect_tags_from_vault(vault_dir)

    if not tags:
        click.echo("No [[tags]] found in the vault. Nothing to do.")
        return

    click.echo(f"Found {len(tags)} unique tag(s). Asking LLM for merge proposals…")
    proposal = _propose_merges(tags, model=model)

    click.echo("\n=== Proposed Merges ===")
    if proposal.merges:
        for source, canonical in proposal.merges.items():
            click.echo(f"  [[{source}]] → [[{canonical}]]")
    else:
        click.echo("  (none — all tags appear unique)")

    click.echo(f"\nReasoning: {proposal.reasoning}")

    if apply:
        if proposal.merges:
            click.echo("\nApplying merges…")
            _apply_merges(vault_dir, proposal.merges, taxonomy_path=taxonomy_path)
            click.echo("Done.")
        else:
            click.echo("\nNothing to apply.")
    else:
        click.echo(
            "\nDry-run mode. Pass --apply to execute the merges."
        )


if __name__ == "__main__":
    main()
