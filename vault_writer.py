"""Vault Writer — formats PaperMetadata into Obsidian-compatible Markdown.

Output format
-------------
Each paper is written to ``<vault_dir>/<Sanitised_Title>.md`` with:

* **YAML frontmatter** — authors, date, metrics, and extracted fields.
* **Body** — a synthesised summary followed by the original abstract.
* **Obsidian tags** — every conceptual tag is wrapped in ``[[…]]`` links.

After writing, the writer updates ``taxonomy.json`` with any newly encountered
tags.
"""

from __future__ import annotations

import json
import logging
import re
from datetime import date
from pathlib import Path
from typing import Any

from skills.base import PaperMetadata

logger = logging.getLogger(__name__)

_DEFAULT_VAULT = Path(__file__).parent / "vault"
_DEFAULT_TAXONOMY = Path(__file__).parent / "taxonomy.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def sanitise_filename(title: str) -> str:
    """Convert a paper title to a safe filesystem name.

    Spaces are replaced with underscores, and any character that is not
    alphanumeric, an underscore, or a hyphen is removed.
    """
    name = title.strip().replace(" ", "_")
    name = re.sub(r"[^\w\-]", "", name)
    return name or "Untitled"


def _obsidian_link(tag: str) -> str:
    """Wrap *tag* in an Obsidian bidirectional link."""
    return f"[[{tag}]]"


def _tags_to_links(tags: list[str]) -> str:
    """Return a space-separated string of Obsidian links for *tags*."""
    return " ".join(_obsidian_link(t) for t in tags)


def _extract_bracket_tags(text: str) -> list[str]:
    """Extract all ``[[tag]]`` values from *text*."""
    return re.findall(r"\[\[([^\]]+)\]\]", text)


def _load_taxonomy(taxonomy_path: Path) -> list[str]:
    """Load the current tag list from *taxonomy_path*."""
    if not taxonomy_path.exists():
        return []
    try:
        data = json.loads(taxonomy_path.read_text())
        return list(data) if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Could not read taxonomy: %s", exc)
        return []


def _save_taxonomy(taxonomy_path: Path, tags: list[str]) -> None:
    """Persist *tags* to *taxonomy_path*, preserving order and deduplicating."""
    taxonomy_path.write_text(json.dumps(sorted(set(tags)), indent=2))


def _metadata_to_yaml(metadata: PaperMetadata) -> str:
    """Serialise *metadata* into a YAML frontmatter block."""
    lines: list[str] = ["---"]

    def _yaml_scalar(value: Any) -> str:
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, (int, float)):
            return str(value)
        return f'"{value}"'

    def _yaml_list(items: list[Any]) -> str:
        if not items:
            return "[]"
        return "\n" + "\n".join(f"  - {_yaml_scalar(i)}" for i in items)

    lines.append(f"title: {_yaml_scalar(metadata.title)}")
    lines.append(f"authors: {_yaml_list(metadata.authors)}")
    lines.append(f"ingested_date: {date.today().isoformat()}")
    lines.append(f"tags: {_yaml_list(metadata.tags)}")

    # Include any extra fields defined by the subclass.
    # Use the class-level exclusion set so this stays in sync with PaperMetadata.
    base_fields = getattr(type(metadata), "_yaml_base_fields", frozenset())
    extra = metadata.model_fields_set - base_fields
    for field_name in sorted(extra):
        value = getattr(metadata, field_name, None)
        if value is None:
            continue
        if isinstance(value, list):
            lines.append(f"{field_name}: {_yaml_list(value)}")
        elif isinstance(value, bool):
            lines.append(f"{field_name}: {str(value).lower()}")
        else:
            lines.append(f"{field_name}: {_yaml_scalar(value)}")

    lines.append("---")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def write_paper(
    metadata: PaperMetadata,
    *,
    vault_dir: Path = _DEFAULT_VAULT,
    taxonomy_path: Path = _DEFAULT_TAXONOMY,
) -> Path:
    """Write *metadata* to an Obsidian Markdown file in *vault_dir*.

    Returns the path of the newly created (or overwritten) file.

    Side-effect: appends any new tags found in the document to
    ``taxonomy.json``.
    """
    vault_dir.mkdir(parents=True, exist_ok=True)

    filename = sanitise_filename(metadata.title) + ".md"
    output_path = vault_dir / filename

    frontmatter = _metadata_to_yaml(metadata)

    tag_links = _tags_to_links(metadata.tags)
    body = (
        f"## Summary\n\n"
        f"{metadata.summary}\n\n"
        f"## Tags\n\n"
        f"{tag_links}\n\n"
        f"## Abstract\n\n"
        f"{metadata.abstract}\n"
    )

    content = f"{frontmatter}\n\n{body}"
    output_path.write_text(content, encoding="utf-8")
    logger.info("Wrote vault file: %s", output_path)

    # Update taxonomy with any new [[tags]] found in the file
    existing_tags = _load_taxonomy(taxonomy_path)
    found_tags = _extract_bracket_tags(content)
    merged = list(set(existing_tags) | set(found_tags))
    _save_taxonomy(taxonomy_path, merged)
    new_tags = [t for t in found_tags if t not in existing_tags]
    if new_tags:
        logger.info("Added %d new tag(s) to taxonomy: %s", len(new_tags), new_tags)

    return output_path
