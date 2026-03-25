"""Federation Agent: consumes external public_feed.json files.

Implements Path 1 – The RSS/JSON Feed Swarm.

For each external feed URL:
  1. Fetch and parse the JSON feed.
  2. For each entry:
     - If the paper does NOT exist locally → treat it as a new discovery and
       write it to the staging area as a lightweight paper note.
     - If the paper ALREADY EXISTS in the local vault → append the external
       agent's summary under a ``### External Perspectives`` section without
       overwriting any local metadata.
"""

from __future__ import annotations

import json
import logging
import re
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from swarm_notes.config import settings

logger = logging.getLogger(__name__)

_EXTERNAL_PERSPECTIVES_HEADER = "### External Perspectives"


def run_federation(feed_urls: list[str] | None = None) -> None:
    """Run the federation agent.

    Parameters
    ----------
    feed_urls:
        URLs of external ``public_feed.json`` files.  Defaults to
        ``settings.federation_feeds`` from config.
    """
    if feed_urls is None:
        feed_urls = settings.federation_feeds

    if not feed_urls:
        logger.info("Federation: no external feeds configured – skipping")
        return

    for url in feed_urls:
        logger.info("Federation: fetching feed from %s", url)
        entries = _fetch_feed(url)
        if not entries:
            logger.warning("Federation: empty or invalid feed at %s", url)
            continue

        source_label = _label_from_url(url)
        for entry in entries:
            arxiv_id = entry.get("arxiv_id", "")
            if not arxiv_id:
                continue
            _process_entry(entry, source_label)

    logger.info("Federation run complete")


def _process_entry(entry: dict, source_label: str) -> None:
    """Handle a single feed entry against the local vault."""
    arxiv_id = entry.get("arxiv_id", "")
    title = entry.get("title", "Untitled")
    summary = entry.get("summary", "")

    # Look for existing file in vault or staging
    existing_path = _find_existing_paper(arxiv_id)

    if existing_path is None:
        # New paper – write a lightweight stub into staging
        _write_federated_stub(entry, source_label)
        logger.info("Federation: new paper %s added from %s", arxiv_id, source_label)
    else:
        # Paper exists – append external perspective without overwriting
        _append_external_perspective(existing_path, summary, title, source_label, arxiv_id)
        logger.info(
            "Federation: appended perspective from %s to %s",
            source_label,
            existing_path.name,
        )


def _find_existing_paper(arxiv_id: str) -> Path | None:
    """Return the path of an existing paper file in staging or vault, or None."""
    # Check staging first (files written in the current run)
    for path in settings.tmp_papers_dir.iterdir():
        if path.is_file() and arxiv_id in path.name:
            return path
    # Then the live vault
    for path in settings.vault_papers_dir.iterdir():
        if path.is_file() and arxiv_id in path.name:
            return path
    return None


def _append_external_perspective(
    paper_path: Path,
    summary: str,
    title: str,
    source_label: str,
    arxiv_id: str,
) -> None:
    """Append an external summary block to an existing paper file.

    If the file lives in the live vault (not staging), copy it to staging
    first so edits are part of the atomic commit.
    """
    staging_path = settings.tmp_papers_dir / paper_path.name
    if not staging_path.exists():
        # Copy live vault file into staging before modifying
        import shutil

        shutil.copy2(paper_path, staging_path)

    content = staging_path.read_text(encoding="utf-8")

    # Add the header if it is not already present
    if _EXTERNAL_PERSPECTIVES_HEADER not in content:
        content = content.rstrip() + f"\n\n{_EXTERNAL_PERSPECTIVES_HEADER}\n\n"

    perspective_block = (
        f"> \"{_md_escape(summary)}\" - @{source_label}\n"
        f"> *(Retrieved {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')})*\n\n"
    )
    content += perspective_block

    staging_path.write_text(content, encoding="utf-8")


def _write_federated_stub(entry: dict, source_label: str) -> None:
    """Write a lightweight Markdown stub for a paper discovered via federation."""
    arxiv_id = entry.get("arxiv_id", "unknown")
    title = entry.get("title", "Untitled")
    authors = entry.get("authors", [])
    published = entry.get("published", "")
    url = entry.get("url", "")
    tags = entry.get("tags", [])
    domain = entry.get("domain", "")
    summary = entry.get("summary", "")

    slug = _make_slug(arxiv_id, title)
    out_path = settings.tmp_papers_dir / f"{slug}.md"

    if out_path.exists():
        return  # Already written this run

    author_lines = "\n".join(f'  - literal: "{a}"' for a in authors) or "  []"
    tag_lines = "\n".join(f'  - "{t}"' for t in tags) or "  []"

    try:
        dt = datetime.strptime(published, "%Y-%m-%d")
        date_parts = f"{dt.year}, {dt.month}, {dt.day}"
    except ValueError:
        date_parts = "null"

    processed_at = datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    content = f"""\
---
title: "{_yaml_escape(title)}"
author:
{author_lines}
issued:
  date-parts:
    - [{date_parts}]
url: "{url}"
arxiv_id: "{arxiv_id}"
domain: "{domain}"
tags:
{tag_lines}
federated_from: "{source_label}"
processed_at: "{processed_at}"
---

# {title}

## Summary

{summary}

{_EXTERNAL_PERSPECTIVES_HEADER}

> \"{_md_escape(summary)}\" - @{source_label}
> *(Federated {datetime.now(tz=timezone.utc).strftime('%Y-%m-%d')})*

## Links

- [ArXiv Abstract]({url})
- [PDF]({url.replace('abs', 'pdf')})
"""
    out_path.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _fetch_feed(url: str) -> list[dict]:
    """Fetch and parse a remote ``public_feed.json`` file."""
    try:
        with urllib.request.urlopen(url, timeout=15) as response:  # noqa: S310
            raw = response.read()
        data = json.loads(raw)
        if isinstance(data, list):
            return data
        logger.warning("Federation: unexpected feed format at %s", url)
    except Exception as exc:
        logger.error("Federation: failed to fetch %s – %s", url, exc)
    return []


def _label_from_url(url: str) -> str:
    """Derive a short agent label from a GitHub raw URL.

    For example::

        https://raw.githubusercontent.com/alice/research-cruise/main/public_feed.json
        → Agent_alice
    """
    match = re.search(r"githubusercontent\.com/([^/]+)/", url)
    if match:
        return f"Agent_{match.group(1)}"
    # Fallback: use the domain
    match = re.search(r"https?://([^/]+)", url)
    if match:
        return f"Agent_{match.group(1).replace('.', '_')}"
    return "Agent_unknown"


def _make_slug(arxiv_id: str, title: str) -> str:
    title_slug = _slugify(title)[:60].rstrip("-")
    return f"{arxiv_id}-{title_slug}"


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def _yaml_escape(text: str) -> str:
    return text.replace('"', '\\"')


def _md_escape(text: str) -> str:
    """Prepare text for use inside a Markdown blockquote.

    Double quotes do not need escaping in Markdown; returning the text
    as-is ensures the rendered output is readable.
    """
    return text
