#!/usr/bin/env python3
"""Migrate legacy vault artifacts to source-aware paper IDs.

What this script can migrate:
- vault/papers filenames:
  - from: <paper_id>-<title>.md
  - to:   arxiv-<paper_id>-<title>.md
- Paper markdown frontmatter:
  - arxiv_id -> paper_id (adds paper_source: "arxiv")
- Paper markdown body link label:
  - **ArXiv**: [<id>](...) -> **Paper ID**: [arxiv:<id>](...)
- vault/public_feed.json entries:
  - add paper_id from arxiv_id when missing
  - add paper_source="arxiv" when missing

By default the script runs in dry-run mode and prints what would change.
Use --apply to write changes.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

LEGACY_FILENAME_RE = re.compile(r"^(\d{4}\.\d{4,5})-(.+)\.md$")


def _split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---\n"):
        return None, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text

    frontmatter = text[4:end]
    body = text[end + 5 :]
    return frontmatter, body


def _migrate_frontmatter(frontmatter: str) -> tuple[str, bool]:
    changed = False
    lines = frontmatter.splitlines()

    has_paper_id = any(line.strip().startswith("paper_id:") for line in lines)
    has_paper_source = any(line.strip().startswith("paper_source:") for line in lines)

    out: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("arxiv_id:") and not has_paper_id:
            line = line.replace("arxiv_id:", "paper_id:", 1)
            changed = True
        out.append(line)

    if not has_paper_source:
        inserted = False
        for i, line in enumerate(out):
            if line.strip().startswith("paper_id:"):
                out.insert(i + 1, 'paper_source: "arxiv"')
                changed = True
                inserted = True
                break
        if not inserted:
            out.append('paper_source: "arxiv"')
            changed = True

    return "\n".join(out), changed


def _migrate_body(body: str) -> tuple[str, bool]:
    pattern = re.compile(r"\*\*ArXiv\*\*:\s*\[(\d{4}\.\d{4,5})\]\(([^)]+)\)")
    updated = pattern.sub(r"**Paper ID**: [arxiv:\1](\2)", body)
    return updated, updated != body


def _migrate_paper_file(path: Path, apply: bool) -> dict[str, int]:
    stats = {
        "renamed": 0,
        "frontmatter_updated": 0,
        "body_updated": 0,
    }

    target_path = path
    match = LEGACY_FILENAME_RE.match(path.name)
    if match:
        target_path = path.with_name(f"arxiv-{match.group(1)}-{match.group(2)}.md")
        if target_path != path:
            stats["renamed"] = 1

    text = path.read_text(encoding="utf-8")
    frontmatter, body = _split_frontmatter(text)

    new_text = text
    if frontmatter is not None:
        new_frontmatter, fm_changed = _migrate_frontmatter(frontmatter)
        new_body, body_changed = _migrate_body(body)
        if fm_changed or body_changed:
            new_text = f"---\n{new_frontmatter}\n---\n{new_body}"
        if fm_changed:
            stats["frontmatter_updated"] = 1
        if body_changed:
            stats["body_updated"] = 1

    if apply:
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
        if target_path != path:
            if target_path.exists():
                raise FileExistsError(
                    f"Cannot rename {path.name} -> {target_path.name}: target already exists"
                )
            path.rename(target_path)

    return stats


def _migrate_public_feed(feed_path: Path, apply: bool) -> dict[str, int]:
    stats = {
        "feed_entries_updated": 0,
        "feed_added_paper_id": 0,
        "feed_added_paper_source": 0,
    }

    if not feed_path.exists():
        return stats

    content = json.loads(feed_path.read_text(encoding="utf-8"))
    if not isinstance(content, list):
        return stats

    for entry in content:
        if not isinstance(entry, dict):
            continue

        changed = False
        if not entry.get("paper_id") and isinstance(entry.get("arxiv_id"), str):
            entry["paper_id"] = entry["arxiv_id"]
            stats["feed_added_paper_id"] += 1
            changed = True

        if not entry.get("paper_source"):
            entry["paper_source"] = "arxiv"
            stats["feed_added_paper_source"] += 1
            changed = True

        if changed:
            stats["feed_entries_updated"] += 1

    if apply and stats["feed_entries_updated"]:
        feed_path.write_text(
            json.dumps(content, ensure_ascii=True, indent=2) + "\n",
            encoding="utf-8",
        )

    return stats


def migrate(vault_dir: Path, apply: bool) -> int:
    papers_dir = vault_dir / "papers"
    feed_path = vault_dir / "public_feed.json"

    if not papers_dir.exists():
        raise FileNotFoundError(f"Papers directory not found: {papers_dir}")

    totals = {
        "files_scanned": 0,
        "renamed": 0,
        "frontmatter_updated": 0,
        "body_updated": 0,
        "feed_entries_updated": 0,
        "feed_added_paper_id": 0,
        "feed_added_paper_source": 0,
    }

    for path in sorted(papers_dir.glob("*.md")):
        if path.name == ".gitkeep":
            continue
        totals["files_scanned"] += 1
        result = _migrate_paper_file(path, apply=apply)
        for key, value in result.items():
            totals[key] += value

    feed_stats = _migrate_public_feed(feed_path, apply=apply)
    for key, value in feed_stats.items():
        totals[key] += value

    mode = "APPLY" if apply else "DRY RUN"
    print(f"[{mode}] Vault migration summary")
    print(f"  papers scanned:        {totals['files_scanned']}")
    print(f"  filenames renamed:     {totals['renamed']}")
    print(f"  frontmatter updated:   {totals['frontmatter_updated']}")
    print(f"  body labels updated:   {totals['body_updated']}")
    print(f"  feed entries updated:  {totals['feed_entries_updated']}")
    print(f"    added paper_id:      {totals['feed_added_paper_id']}")
    print(f"    added paper_source:  {totals['feed_added_paper_source']}")

    if not apply:
        print("\nNo files were modified. Re-run with --apply to write changes.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate legacy vault papers to source-aware IDs")
    parser.add_argument(
        "--vault-dir",
        default="vault",
        help="Vault directory containing papers/ and public_feed.json (default: vault)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes (default is dry-run)",
    )
    args = parser.parse_args()

    return migrate(Path(args.vault_dir), apply=args.apply)


if __name__ == "__main__":
    raise SystemExit(main())
