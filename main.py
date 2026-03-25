"""research-cruise — CLI entry point.

Usage examples
--------------

Process a paper by arXiv ID::

    python main.py arxiv 2310.06625

Process a paper from a local abstract text file::

    python main.py file path/to/abstract.txt --title "My Paper Title"

Options
-------
--model     Override the default pydantic-ai model (default: openai:gpt-4o).
--vault     Override the vault output directory (default: ./vault).
--taxonomy  Override the taxonomy file path (default: ./taxonomy.json).
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import click

from analyst import analyse_paper
from router import route_paper
from vault_writer import write_paper

logger = logging.getLogger(__name__)

_DEFAULT_VAULT = Path(__file__).parent / "vault"
_DEFAULT_TAXONOMY = Path(__file__).parent / "taxonomy.json"
_DEFAULT_MODEL = "openai:gpt-4o"


# ---------------------------------------------------------------------------
# arXiv helper
# ---------------------------------------------------------------------------


def _fetch_arxiv(arxiv_id: str) -> tuple[str, str, str]:
    """Return (title, abstract, full_text) for the given arXiv ID.

    ``full_text`` is the abstract repeated (arXiv API does not provide full PDF
    text); callers may substitute a real PDF parser if desired.
    """
    try:
        import arxiv  # type: ignore[import-untyped]
    except ImportError:
        click.echo(
            "The 'arxiv' package is required. Install it with: pip install arxiv",
            err=True,
        )
        sys.exit(1)

    client = arxiv.Client()
    search = arxiv.Search(id_list=[arxiv_id], max_results=1)
    results = list(client.results(search))

    if not results:
        click.echo(f"No paper found for arXiv ID: {arxiv_id}", err=True)
        sys.exit(1)

    paper = results[0]
    title: str = paper.title
    abstract: str = paper.summary
    # Full-text extraction from PDF is out of scope; use abstract as proxy.
    full_text: str = abstract
    return title, abstract, full_text


# ---------------------------------------------------------------------------
# Shared processing logic
# ---------------------------------------------------------------------------


def _process(
    title: str,
    abstract: str,
    full_text: str,
    model: str,
    vault_dir: Path,
    taxonomy_path: Path,
) -> None:
    """Route, analyse, and write a single paper."""
    skill_cls = route_paper(title, abstract)
    if skill_cls is None:
        click.echo(
            f"No matching skill found for paper: '{title}'. "
            "Skipping (no generic fallback configured).",
            err=True,
        )
        sys.exit(0)

    click.echo(f"Using skill: {skill_cls.name()}")

    metadata = analyse_paper(
        title=title,
        abstract=abstract,
        full_text=full_text,
        skill_cls=skill_cls,
        model=model,
        taxonomy_path=taxonomy_path,
    )

    output_path = write_paper(
        metadata,
        vault_dir=vault_dir,
        taxonomy_path=taxonomy_path,
    )
    click.echo(f"✓ Written to: {output_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


@click.group()
@click.option(
    "--model",
    default=_DEFAULT_MODEL,
    show_default=True,
    envvar="RESEARCH_CRUISE_MODEL",
    help="pydantic-ai model identifier.",
)
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
    "--verbose",
    "-v",
    is_flag=True,
    default=False,
    help="Enable verbose logging.",
)
@click.pass_context
def cli(
    ctx: click.Context,
    model: str,
    vault_dir: Path,
    taxonomy_path: Path,
    verbose: bool,
) -> None:
    """research-cruise: ingest academic papers into an Obsidian knowledge vault."""
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    ctx.ensure_object(dict)
    ctx.obj["model"] = model
    ctx.obj["vault_dir"] = vault_dir
    ctx.obj["taxonomy_path"] = taxonomy_path


@cli.command()
@click.argument("arxiv_id")
@click.pass_context
def arxiv(ctx: click.Context, arxiv_id: str) -> None:
    """Fetch and process a paper by ARXIV_ID (e.g. 2310.06625)."""
    click.echo(f"Fetching arXiv paper: {arxiv_id}")
    title, abstract, full_text = _fetch_arxiv(arxiv_id)
    click.echo(f"Title: {title}")

    _process(
        title=title,
        abstract=abstract,
        full_text=full_text,
        model=ctx.obj["model"],
        vault_dir=ctx.obj["vault_dir"],
        taxonomy_path=ctx.obj["taxonomy_path"],
    )


@cli.command()
@click.argument("file_path", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.option(
    "--title",
    default=None,
    help="Paper title (defaults to the file stem if omitted).",
)
@click.pass_context
def file(ctx: click.Context, file_path: Path, title: str | None) -> None:
    """Process a raw abstract text FILE_PATH."""
    abstract = file_path.read_text(encoding="utf-8").strip()
    paper_title = title or file_path.stem.replace("_", " ")

    click.echo(f"Processing file: {file_path}")
    click.echo(f"Title: {paper_title}")

    _process(
        title=paper_title,
        abstract=abstract,
        full_text=abstract,
        model=ctx.obj["model"],
        vault_dir=ctx.obj["vault_dir"],
        taxonomy_path=ctx.obj["taxonomy_path"],
    )


if __name__ == "__main__":
    cli()
