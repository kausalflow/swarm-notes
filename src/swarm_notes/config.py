"""Configuration and settings for the research-cruise agent system."""

import os
from pathlib import Path
from typing import Any, Literal, cast

from pydantic import BaseModel, Field
import yaml  # type: ignore[import-untyped]
from dotenv import load_dotenv

load_dotenv()

REPO_ROOT = Path(__file__).parent.parent.parent.resolve()

_DEFAULT_PAPER_KEYWORDS = [
    "large language model",
    "transformer",
    "diffusion model",
    "state space model",
    "mamba",
    "retrieval augmented generation",
    "multimodal",
    "vision language model",
    "mixture of experts",
]


def _default_paper_source() -> Literal["arxiv", "semantic_scholar", "openalex"]:
    source_name = os.environ.get("PAPER_SOURCE", "arxiv").strip().lower().replace("-", "_")
    if source_name == "semantic_scholar":
        return "semantic_scholar"
    if source_name == "openalex":
        return "openalex"
    return "arxiv"


def _default_paper_keywords() -> list[str]:
    raw = os.environ.get("PAPER_KEYWORDS") or os.environ.get("ARXIV_KEYWORDS")
    if not raw:
        return list(_DEFAULT_PAPER_KEYWORDS)
    return [item.strip() for item in raw.split(",") if item.strip()]


def _default_paper_max_results_per_keyword() -> int:
    raw = os.environ.get("PAPER_MAX_RESULTS_PER_KEYWORD") or os.environ.get("ARXIV_MAX_RESULTS_PER_KEYWORD")
    if not raw:
        return 5
    try:
        return int(raw)
    except ValueError:
        return 5


def _default_paper_total_cap() -> int:
    raw = os.environ.get("PAPER_TOTAL_CAP") or os.environ.get("ARXIV_TOTAL_CAP")
    if not raw:
        return 20
    try:
        return int(raw)
    except ValueError:
        return 20

class Settings(BaseModel):
    # Vault paths
    vault_dir: Path = Field(default=REPO_ROOT / "vault")
    vault_papers_dir: Path = Field(default=REPO_ROOT / "vault" / "papers")
    vault_concepts_dir: Path = Field(default=REPO_ROOT / "vault" / "concepts")
    vault_datasets_dir: Path = Field(default=REPO_ROOT / "vault" / "datasets")
    vault_discussions_dir: Path = Field(default=REPO_ROOT / "vault" / "discussions")
    vault_daily_dir: Path = Field(default=REPO_ROOT / "vault" / "discussions" / "daily")
    vault_open_questions_dir: Path = Field(default=REPO_ROOT / "vault" / "open-questions")
    
    # Staging paths
    tmp_vault_dir: Path = Field(default=REPO_ROOT / "tmp_vault")
    tmp_papers_dir: Path = Field(default=REPO_ROOT / "tmp_vault" / "papers")
    tmp_concepts_dir: Path = Field(default=REPO_ROOT / "tmp_vault" / "concepts")
    tmp_datasets_dir: Path = Field(default=REPO_ROOT / "tmp_vault" / "datasets")
    tmp_discussions_dir: Path = Field(default=REPO_ROOT / "tmp_vault" / "discussions")
    tmp_daily_dir: Path = Field(default=REPO_ROOT / "tmp_vault" / "discussions" / "daily")
    tmp_open_questions_dir: Path = Field(default=REPO_ROOT / "tmp_vault" / "open-questions")
    
    # Data files
    taxonomy_file: Path = Field(default=REPO_ROOT / "vault" / "taxonomy.json")
    public_feed_file: Path = Field(default=REPO_ROOT / "public_feed.json")
    
    # LLM keys and model
    llm_api_key: str = Field(default_factory=lambda: os.environ.get("LLM_API_KEY", ""))
    openai_api_key: str = Field(default_factory=lambda: os.environ.get("OPENAI_API_KEY", os.environ.get("LLM_API_KEY", "")))
    gemini_api_key: str = Field(default_factory=lambda: os.environ.get("GEMINI_API_KEY", os.environ.get("GOOGLE_API_KEY", "")))
    llm_model: str = Field(default="openai:gpt-4o-mini")
    
    # Watcher config
    paper_source: Literal["arxiv", "semantic_scholar", "openalex"] = Field(
        default_factory=_default_paper_source
    )
    paper_keywords: list[str] = Field(default_factory=_default_paper_keywords)
    paper_max_results_per_keyword: int = Field(default_factory=_default_paper_max_results_per_keyword)
    paper_total_cap: int = Field(default_factory=_default_paper_total_cap)
    semantic_scholar_api_key: str = Field(
        default_factory=lambda: os.environ.get("SEMANTIC_SCHOLAR_API_KEY", "")
    )
    semantic_scholar_api_url: str = Field(
        default_factory=lambda: os.environ.get(
            "SEMANTIC_SCHOLAR_API_URL",
            "https://api.semanticscholar.org/graph/v1/paper/search",
        )
    )

    # OpenAlex config (key and mailto are both optional)
    openalex_api_key: str = Field(
        default_factory=lambda: os.environ.get("OPENALEX_API_KEY", "")
    )
    openalex_mailto: str = Field(
        default_factory=lambda: os.environ.get("OPENALEX_MAILTO", "")
    )
    openalex_relevance_mode: Literal["phrase", "all_tokens"] = Field(
        default_factory=lambda: os.environ.get("OPENALEX_RELEVANCE_MODE", "phrase").strip().lower()
    )
    
    # Federation config
    federation_feeds: list[str] = Field(default_factory=lambda: [
        f for f in os.environ.get("FEDERATION_FEEDS", "").split(",") if f.strip()
    ])
    public_feed_max_items: int = 20

    # Skill config
    active_skills: list[str] = Field(
        default_factory=list,
        description=(
            "List of skill IDs (folder names) to load. "
            "If empty, all skills in `skills_dir` are loaded. "
            "The router will pick the best match from this subset."
        ),
    )
    skills_dir: Path = Field(
        default=REPO_ROOT / "skills",
        description="Root directory that contains skill subfolders.",
    )

    # Experimental features
    enable_domain_expert: bool = False

    # Site identity (written to website/src/content/site-config.json)
    site_name: str = "Swarm Notes"
    site_description: str = "Automated research paper tracking and knowledge synthesis."

    # Backward-compatible aliases for pre-refactor names.
    @property
    def arxiv_keywords(self) -> list[str]:
        return self.paper_keywords

    @property
    def arxiv_max_results_per_keyword(self) -> int:
        return self.paper_max_results_per_keyword

    @property
    def arxiv_total_cap(self) -> int:
        return self.paper_total_cap

    @classmethod
    def load_from_yaml(cls, yaml_path: str | Path | None = None) -> "Settings":
        data: dict[str, Any] = {}
        if yaml_path and Path(yaml_path).exists():
            with open(yaml_path, encoding="utf-8") as f:
                yaml_data = yaml.safe_load(f) or {}
                data.update(yaml_data)
                
        if "llm_model" not in data:
            explicit = os.environ.get("settings.llm_model", "")
            if explicit:
                data["llm_model"] = explicit
            elif os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY") or os.environ.get("LLM_API_KEY", "").startswith("AIzaSy"):
                data["llm_model"] = "gemini-flash-lite-latest"
                
        llm_key = data.get("llm_api_key", os.environ.get("LLM_API_KEY", ""))
        gem_key = data.get("gemini_api_key", os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY", ""))
        if not gem_key and llm_key.startswith("AIzaSy"):
            os.environ["GEMINI_API_KEY"] = llm_key
            data["gemini_api_key"] = llm_key

        if "paper_source" in data and isinstance(data["paper_source"], str):
            data["paper_source"] = data["paper_source"].strip().lower().replace("-", "_")

        # Backward compatibility with older arxiv_* YAML keys
        if "paper_keywords" not in data and "arxiv_keywords" in data:
            data["paper_keywords"] = data["arxiv_keywords"]
        if "paper_max_results_per_keyword" not in data and "arxiv_max_results_per_keyword" in data:
            data["paper_max_results_per_keyword"] = data["arxiv_max_results_per_keyword"]
        if "paper_total_cap" not in data and "arxiv_total_cap" in data:
            data["paper_total_cap"] = data["arxiv_total_cap"]

        return cls(**cast(dict[str, Any], data))

settings = Settings.load_from_yaml()

def load_yaml_config(yaml_path: str | Path) -> None:
    """Override configuration variables from a YAML file."""
    global settings
    settings = Settings.load_from_yaml(yaml_path)
