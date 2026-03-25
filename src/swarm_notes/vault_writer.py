"""Vault Writer: transforms PaperAnalysis into Markdown files.

Writes to the staging ``tmp_vault/`` directories.  Also maintains the
rolling ``public_feed.json`` file for the Hive Mind federation.
"""

from __future__ import annotations

import json
import logging
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

import frontmatter

from swarm_notes.analyst import PaperAnalysis, OpenQuestion
from swarm_notes.config import settings

logger = logging.getLogger(__name__)

# YAML frontmatter template
_FRONTMATTER_TEMPLATE = """\
---
# CSL-compatible fields
title: "{title}"
author:
{author_lines}
issued:
  date-parts:
    - [{date_parts}]
url: "{url}"

# Custom fields
arxiv_id: "{arxiv_id}"
domain: "{domain}"
tags:
{tag_lines}
architectures:
{architecture_lines}
datasets:
{dataset_lines}
skill: "{skill}"
processed_at: "{processed_at}"
created_at: "{created_at}"
---
"""


def write_paper(analysis: PaperAnalysis, skill_name: str) -> Path:
    """Write a paper Markdown file to the staging directory.

    Parameters
    ----------
    analysis:
        Structured extraction result from the Analyst.
    skill_name:
        Name of the Skill used (stored in frontmatter for traceability).

    Returns
    -------
    Path
        Path to the written staging file.
    """
    slug = _make_slug(analysis.arxiv_id, analysis.title)
    out_path = settings.tmp_papers_dir / f"{slug}.md"

    frontmatter = _build_frontmatter(analysis, skill_name)
    body = _build_body(analysis)
    content = f"{frontmatter}\n{body}\n"

    out_path.write_text(content, encoding="utf-8")
    logger.info("VaultWriter: wrote paper → %s", out_path)

    # Write concept stubs for any new concepts
    for concept in analysis.concepts:
        _write_concept_stub(concept.slug, concept.display_name, concept.one_liner)

    return out_path


def _build_frontmatter(analysis: PaperAnalysis, skill_name: str) -> str:
    """Render the YAML frontmatter block."""
    author_lines = "\n".join(
        f'  - literal: "{_yaml_escape(a)}"' for a in analysis.authors
    )
    if not author_lines:
        author_lines = "  []"

    # issued date-parts: [YYYY, MM, DD]
    try:
        dt = datetime.strptime(analysis.published, "%Y-%m-%d")
        date_parts = f"{dt.year}, {dt.month}, {dt.day}"
    except ValueError:
        date_parts = "null"

    tag_lines = "\n".join(f'  - "{t}"' for t in analysis.tags) or "  []"
    architecture_lines = (
        "\n".join(f'  - "{a}"' for a in analysis.architectures) or "  []"
    )
    dataset_lines = "\n".join(f'  - "{d}"' for d in analysis.datasets) or "  []"

    now_utc = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    return _FRONTMATTER_TEMPLATE.format(
        title=_yaml_escape(analysis.title),
        author_lines=author_lines,
        date_parts=date_parts,
        url=analysis.url,
        arxiv_id=analysis.arxiv_id,
        domain=analysis.domain,
        tag_lines=tag_lines,
        architecture_lines=architecture_lines,
        dataset_lines=dataset_lines,
        skill=skill_name,
        processed_at=now_utc,
        created_at=now_utc,
    )


def _build_body(analysis: PaperAnalysis) -> str:
    """Build the Markdown body of the paper note."""
    lines: list[str] = []

    lines.append(f"# {analysis.title}\n")
    lines.append(f"**Authors**: {', '.join(analysis.authors)}")
    lines.append(f"**Date**: {analysis.published}")
    lines.append(f"**ArXiv**: [{analysis.arxiv_id}]({analysis.url})\n")

    lines.append("## Summary\n")
    lines.append(f"{analysis.summary}\n")

    lines.append("## Key Contributions\n")
    for contrib in analysis.key_contributions:
        lines.append(f"- {contrib}")
    lines.append("")

    if analysis.limitations:
        lines.append("## Limitations\n")
        lines.append(f"{analysis.limitations}\n")

    if analysis.open_questions:
        lines.append("## Open Questions & Future Work\n")
        for q in analysis.open_questions:
            lines.append(f"- [[{q.slug}]]")
            _create_open_question(q, analysis)
        lines.append("")

    # Concepts
    if analysis.concepts:
        lines.append("## Key Concepts\n")
        for concept in analysis.concepts:
            rel_link = f"[{concept.display_name}](../concepts/{concept.slug}.md)"
            lines.append(f"- {rel_link}: {concept.one_liner}")
        lines.append("")

    # Datasets
    if analysis.datasets:
        lines.append("## Datasets\n")
        for ds in analysis.datasets:
            ds_slug = _slugify(ds)
            rel_link = f"[{ds}](../datasets/{ds_slug}.md)"
            lines.append(f"- {rel_link}")
        lines.append("")

    # Limitations
    if analysis.limitations:
        lines.append("## Limitations\n")
        lines.append(f"{analysis.limitations}\n")

    # Links
    lines.append("## Links\n")
    lines.append(f"- [ArXiv Abstract]({analysis.url})")
    lines.append(f"- [PDF]({analysis.url.replace('abs', 'pdf')})")
    lines.append("")

    return "\n".join(lines)


def _write_concept_stub(slug: str, display_name: str, one_liner: str) -> None:
    """Write a concept stub Markdown file if one does not already exist."""
    # Check staging first, then live vault (avoid overwriting existing)
    from swarm_notes.config import settings

    staging_path = settings.tmp_concepts_dir / f"{slug}.md"
    vault_path = settings.vault_concepts_dir / f"{slug}.md"

    if staging_path.exists() or vault_path.exists():
        logger.debug("Concept stub already exists for '%s' – skipping", slug)
        return

    now_utc = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    content = f"""\
---
title: "{_yaml_escape(display_name)}"
slug: "{slug}"
type: concept
generated_stub: true
processed_at: "{now_utc}"
created_at: "{now_utc}"
---

# {display_name}

> *Auto-generated stub. Edit this file to add more details.*

{one_liner}

## Related Papers

<!-- Papers that mention this concept will be linked here -->
"""
    staging_path.write_text(content, encoding="utf-8")
    logger.info("VaultWriter: created concept stub → %s", staging_path)


def _create_open_question(question: OpenQuestion, analysis: PaperAnalysis) -> None:
    """Create or update an open question file with frontmatter tracking sources."""
    slug = _slugify(question.slug)
    filename = f"{slug}.md"
    live_path = settings.vault_open_questions_dir / filename
    staging_path = settings.tmp_open_questions_dir / filename

    is_new = not staging_path.exists() and not live_path.exists()

    if live_path.exists() and not staging_path.exists():
        shutil.copy2(live_path, staging_path)

    now_utc = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    papers = []
    content = f"**Background:** {question.background}\n\n**Question / Future Work:** {question.description}"
    existing_created_at: str | None = None

    if staging_path.exists():
        try:
            post = frontmatter.load(staging_path)
            papers = post.metadata.get("source_papers", [])
            if not isinstance(papers, list):
                papers = [papers]
            # Retain original deeper description instead of wiping it
            content = post.content if post.content.strip() else content
            existing_created_at = post.metadata.get("created_at")
        except Exception as exc:
            logger.warning("VaultWriter: Failed to parse existing frontmatter for %s: %s", slug, exc)

    paper_slug = _make_slug(analysis.arxiv_id, analysis.title)
    paper_id = f"[[{paper_slug}]]"
    if paper_id not in papers:
        papers.append(paper_id)

    metadata: dict = {
        "title": question.title,
        "source_papers": papers,
        "created_at": existing_created_at if existing_created_at else now_utc,
    }
    if not is_new:
        metadata["modified_at"] = now_utc

    post = frontmatter.Post(content, **metadata)
    with staging_path.open("wb") as f:
        frontmatter.dump(post, f)

    logger.info("VaultWriter: tracked open question → %s", staging_path)


# ---------------------------------------------------------------------------
# Public feed maintenance
# ---------------------------------------------------------------------------


def update_public_feed(analyses: list[PaperAnalysis]) -> None:
    """Add *analyses* to ``public_feed.json``, keeping the last N entries.

    The feed is updated in the repo root (not staging) so that it is always
    current and accessible as a raw URL for federation consumers.

    Parameters
    ----------
    analyses:
        List of :class:`PaperAnalysis` objects from the current run.
    """
    existing: list[dict] = _load_feed()
    existing_ids = {entry["arxiv_id"] for entry in existing}

    new_entries = [
        _analysis_to_feed_entry(a)
        for a in analyses
        if a.arxiv_id not in existing_ids
    ]

    combined = new_entries + existing
    trimmed = combined[:settings.public_feed_max_items]

    settings.public_feed_file.write_text(
        json.dumps(trimmed, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info(
        "Public feed updated: %d new, %d total entries",
        len(new_entries),
        len(trimmed),
    )


def append_daily_discussion(content: str) -> None:
    """Appends the discussion content to today's daily note in staging.

    Creates the file with a ``created_at`` frontmatter timestamp if it is new,
    or prepends / updates a ``modified_at`` timestamp on subsequent appends.
    """
    today_str = datetime.now().date().isoformat()
    filename = f"{today_str}.md"

    live_path = settings.vault_daily_dir / filename
    staging_path = settings.tmp_daily_dir / filename

    # If not already staged, but exists in live vault, copy it over first
    if not staging_path.exists() and live_path.exists():
        shutil.copy2(live_path, staging_path)

    is_new = not staging_path.exists()
    now_utc = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"\n\n## Discussion for {now_str}\n\n"

    if is_new:
        # Write frontmatter + heading first
        front = f"---\ncreated_at: \"{now_utc}\"\n---\n\n# Daily Notes: {today_str}\n"
        staging_path.write_text(front, encoding="utf-8")
        with staging_path.open("a", encoding="utf-8") as f:
            f.write(header + content + "\n")
    else:
        # Update modified_at in existing frontmatter then append
        try:
            post = frontmatter.load(staging_path)
            post.metadata["modified_at"] = now_utc
            with staging_path.open("wb") as f:
                frontmatter.dump(post, f)
        except Exception as exc:
            logger.warning("VaultWriter: could not update modified_at for %s: %s", filename, exc)
        with staging_path.open("a", encoding="utf-8") as f:
            f.write(header + content + "\n")

    logger.info("VaultWriter: appended to daily discussion → %s", staging_path)


def _analysis_to_feed_entry(analysis: PaperAnalysis) -> dict:
    return {
        "arxiv_id": analysis.arxiv_id,
        "title": analysis.title,
        "authors": analysis.authors,
        "published": analysis.published,
        "url": analysis.url,
        "domain": analysis.domain,
        "tags": analysis.tags,
        "summary": analysis.summary,
        "processed_at": datetime.now(tz=timezone.utc).isoformat(),
    }


def _load_feed() -> list[dict]:
    try:
        with settings.public_feed_file.open() as fh:
            data = json.load(fh)
            if isinstance(data, list):
                return data
    except Exception:
        pass
    return []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_slug(arxiv_id: str, title: str) -> str:
    """Create a filename slug: ``<arxiv_id>-<title-slug>``."""
    title_slug = _slugify(title)[:60].rstrip("-")
    return f"{arxiv_id}-{title_slug}"


def _slugify(text: str) -> str:
    """Convert *text* to a lowercase hyphen-separated slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def _yaml_escape(text: str) -> str:
    """Escape double quotes in YAML string values."""
    return text.replace('"', '\\"')
