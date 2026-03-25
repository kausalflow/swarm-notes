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

from src.config import (
    TMP_CONCEPTS_DIR,
    TMP_DATASETS_DIR,
    TMP_PAPERS_DIR,
    TMP_VAULT_DIR,
    VAULT_CONCEPTS_DIR,
    VAULT_DATASETS_DIR,
    VAULT_DIR,
    VAULT_PAPERS_DIR,
)

logger = logging.getLogger(__name__)


def init_vault() -> None:
    """Create the primary vault directories if they do not exist."""
    for directory in (VAULT_PAPERS_DIR, VAULT_CONCEPTS_DIR, VAULT_DATASETS_DIR):
        directory.mkdir(parents=True, exist_ok=True)
    logger.info("Vault directories initialised at %s", VAULT_DIR)


def init_staging() -> None:
    """Create (or recreate) the staging ``tmp_vault/`` directories."""
    if TMP_VAULT_DIR.exists():
        shutil.rmtree(TMP_VAULT_DIR)
        logger.debug("Removed stale tmp_vault at %s", TMP_VAULT_DIR)

    for directory in (TMP_PAPERS_DIR, TMP_CONCEPTS_DIR, TMP_DATASETS_DIR):
        directory.mkdir(parents=True, exist_ok=True)

    logger.info("Staging directory initialised at %s", TMP_VAULT_DIR)


def commit_staging() -> None:
    """Move staged files from ``tmp_vault/`` into the live ``vault/``.

    Files in staging *overwrite* existing vault files of the same name.
    New files are simply moved.  The staging directory is removed on
    completion.
    """
    if not TMP_VAULT_DIR.exists():
        logger.warning("commit_staging called but tmp_vault does not exist – nothing to do")
        return

    _merge_directory(TMP_PAPERS_DIR, VAULT_PAPERS_DIR)
    _merge_directory(TMP_CONCEPTS_DIR, VAULT_CONCEPTS_DIR)
    _merge_directory(TMP_DATASETS_DIR, VAULT_DATASETS_DIR)

    shutil.rmtree(TMP_VAULT_DIR)
    logger.info("Staging committed to vault and tmp_vault removed")


def discard_staging() -> None:
    """Remove ``tmp_vault/`` without touching the live vault."""
    if TMP_VAULT_DIR.exists():
        shutil.rmtree(TMP_VAULT_DIR)
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
