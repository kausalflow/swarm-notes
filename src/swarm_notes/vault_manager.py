"""Vault manager: staging pattern for atomic writes.

All agents write to ``tmp_vault/`` during a run.  On success, call
``commit_staging()`` to atomically move the staged files into ``vault/``.
On failure, call ``discard_staging()`` to remove ``tmp_vault/`` and prevent
partial corruption of the live vault.
"""

from __future__ import annotations

import logging
import shutil
from pathlib import Path

from swarm_notes.config import settings

logger = logging.getLogger(__name__)


def init_vault() -> None:
    """Create the primary vault directories if they do not exist."""
    settings.vault_papers_dir.mkdir(parents=True, exist_ok=True)
    settings.vault_concepts_dir.mkdir(parents=True, exist_ok=True)
    settings.vault_datasets_dir.mkdir(parents=True, exist_ok=True)
    settings.vault_discussions_dir.mkdir(parents=True, exist_ok=True)
    settings.vault_daily_dir.mkdir(parents=True, exist_ok=True)
    settings.vault_open_questions_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Vault structure initialised at %s", settings.vault_dir)


def init_staging() -> None:
    """Create (or recreate) the staging ``tmp_vault/`` directories."""
    if settings.tmp_vault_dir.exists():
        shutil.rmtree(settings.tmp_vault_dir)
        logger.debug("Removed stale tmp_vault at %s", settings.tmp_vault_dir)

    settings.tmp_papers_dir.mkdir(parents=True, exist_ok=True)
    settings.tmp_concepts_dir.mkdir(parents=True, exist_ok=True)
    settings.tmp_datasets_dir.mkdir(parents=True, exist_ok=True)
    settings.tmp_discussions_dir.mkdir(parents=True, exist_ok=True)
    settings.tmp_daily_dir.mkdir(parents=True, exist_ok=True)
    settings.tmp_open_questions_dir.mkdir(parents=True, exist_ok=True)
    logger.debug("Staging area initialised at %s", settings.tmp_vault_dir)


def commit_staging() -> None:
    """Move staged files from ``tmp_vault/`` into the live ``vault/``.

    Files in staging *overwrite* existing vault files of the same name.
    New files are simply moved.  The staging directory is removed on
    completion.
    """
    if not settings.tmp_vault_dir.exists():
        logger.warning("commit_staging called but tmp_vault does not exist – nothing to do")
        return

    _merge_directory(settings.tmp_papers_dir, settings.vault_papers_dir)
    _merge_directory(settings.tmp_concepts_dir, settings.vault_concepts_dir)
    _merge_directory(settings.tmp_datasets_dir, settings.vault_datasets_dir)
    _merge_directory(settings.tmp_daily_dir, settings.vault_daily_dir)
    _merge_directory(settings.tmp_discussions_dir, settings.vault_discussions_dir)
    _merge_directory(settings.tmp_open_questions_dir, settings.vault_open_questions_dir)

    # 3. Clean up stagings.tmp_vault_dir)
    shutil.rmtree(settings.tmp_vault_dir)
    logger.info("Staging committed to vault and tmp_vault removed")


def discard_staging() -> None:
    """Remove ``tmp_vault/`` without touching the live vault."""
    if settings.tmp_vault_dir.exists():
        shutil.rmtree(settings.tmp_vault_dir)
        logger.info("Staging discarded – tmp_vault removed")
    else:
        logger.debug("discard_staging called but tmp_vault does not exist")


def _merge_directory(src: Path, dst: Path) -> None:
    """Copy all files from *src* into *dst*, overwriting on conflict."""
    dst.mkdir(parents=True, exist_ok=True)
    for src_file in src.iterdir():
        if src_file.is_file():
            dst_file = dst / src_file.name
            shutil.copy2(src_file, dst_file)
            logger.debug("Staged %s → %s", src_file, dst_file)


def get_existing_concept_slugs() -> list[str]:
    """Return a list of all concept slugs currently in the live vault."""
    if not settings.vault_concepts_dir.exists():
        return []
    return [f.stem for f in settings.vault_concepts_dir.glob("*.md")]


def make_storage_id(source: str, paper_id: str) -> str:
    """Return the normalized storage identifier used for deduplication."""
    return f"{source.strip().lower()}:{paper_id.strip()}"


def get_existing_storage_ids() -> set[str]:
    """Return source-aware paper IDs already present in vault and staging.

    Supported filename formats:
    - New: ``<source>-<paper_id>-<title-slug>.md``
    - Legacy: ``<paper_id>-<title-slug>.md`` (assumed source ``arxiv``)
    """
    import re

    new_pattern = re.compile(r"^([a-z0-9_]+)-(\d{4}\.\d{4,5})-")
    legacy_pattern = re.compile(r"^(\d{4}\.\d{4,5})-")
    ids: set[str] = set()

    for search_dir in (settings.vault_papers_dir, settings.tmp_papers_dir):
        if not search_dir.exists():
            continue
        for file_path in search_dir.glob("*.md"):
            new_match = new_pattern.match(file_path.name)
            if new_match:
                ids.add(make_storage_id(new_match.group(1), new_match.group(2)))
                continue

            legacy_match = legacy_pattern.match(file_path.name)
            if legacy_match:
                ids.add(make_storage_id("arxiv", legacy_match.group(1)))

    return ids


def get_existing_arxiv_ids() -> set[str]:
    """Backward-compatible ArXiv-only view of existing storage IDs."""
    return {
        storage_id.split(":", 1)[1]
        for storage_id in get_existing_storage_ids()
        if storage_id.startswith("arxiv:")
    }
