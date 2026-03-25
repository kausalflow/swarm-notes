"""Configuration and settings for the research-cruise agent system."""

from __future__ import annotations

import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Repository root
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).parent.parent.resolve()

# ---------------------------------------------------------------------------
# Vault paths
# ---------------------------------------------------------------------------
VAULT_DIR = REPO_ROOT / "vault"
VAULT_PAPERS_DIR = VAULT_DIR / "papers"
VAULT_CONCEPTS_DIR = VAULT_DIR / "concepts"
VAULT_DATASETS_DIR = VAULT_DIR / "datasets"

# Staging directory – agents write here; on success files are moved to VAULT_DIR
TMP_VAULT_DIR = REPO_ROOT / "tmp_vault"
TMP_PAPERS_DIR = TMP_VAULT_DIR / "papers"
TMP_CONCEPTS_DIR = TMP_VAULT_DIR / "concepts"
TMP_DATASETS_DIR = TMP_VAULT_DIR / "datasets"

# ---------------------------------------------------------------------------
# Data files
# ---------------------------------------------------------------------------
TAXONOMY_FILE = REPO_ROOT / "taxonomy.json"
PUBLIC_FEED_FILE = REPO_ROOT / "public_feed.json"

# ---------------------------------------------------------------------------
# LLM / API keys
# ---------------------------------------------------------------------------
LLM_API_KEY: str = os.environ.get("LLM_API_KEY", "")
OPENAI_API_KEY: str = os.environ.get("OPENAI_API_KEY", LLM_API_KEY)

# Model to use for extraction (can be overridden via env var)
LLM_MODEL: str = os.environ.get("LLM_MODEL", "openai:gpt-4o-mini")

# ---------------------------------------------------------------------------
# Watcher configuration
# ---------------------------------------------------------------------------
# Keywords to search on ArXiv (comma-separated env var or defaults)
_DEFAULT_KEYWORDS = (
    "large language model,transformer,diffusion model,"
    "state space model,mamba,retrieval augmented generation,"
    "multimodal,vision language model,mixture of experts"
)
ARXIV_KEYWORDS: list[str] = [
    kw.strip()
    for kw in os.environ.get("ARXIV_KEYWORDS", _DEFAULT_KEYWORDS).split(",")
    if kw.strip()
]

# Maximum papers to fetch per keyword per run
ARXIV_MAX_RESULTS_PER_KEYWORD: int = int(
    os.environ.get("ARXIV_MAX_RESULTS_PER_KEYWORD", "5")
)

# Total cap across all keywords to avoid excessive API calls
ARXIV_TOTAL_CAP: int = int(os.environ.get("ARXIV_TOTAL_CAP", "20"))

# ---------------------------------------------------------------------------
# Federation configuration
# ---------------------------------------------------------------------------
# Comma-separated list of external public_feed.json raw URLs
_DEFAULT_FEDERATION_FEEDS = os.environ.get("FEDERATION_FEEDS", "")
FEDERATION_FEEDS: list[str] = [
    url.strip()
    for url in _DEFAULT_FEDERATION_FEEDS.split(",")
    if url.strip()
]

# How many papers to keep in the rolling public_feed.json
PUBLIC_FEED_MAX_ITEMS: int = int(os.environ.get("PUBLIC_FEED_MAX_ITEMS", "20"))
