"""Configuration and settings for the research-cruise agent system."""

import os
from pathlib import Path
from pydantic import BaseModel, Field
import yaml
from dotenv import load_dotenv

load_dotenv()

REPO_ROOT = Path(__file__).parent.parent.parent.resolve()

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
    arxiv_keywords: list[str] = Field(default_factory=lambda: [
        "large language model", "transformer", "diffusion model",
        "state space model", "mamba", "retrieval augmented generation",
        "multimodal", "vision language model", "mixture of experts"
    ])
    arxiv_max_results_per_keyword: int = 5
    arxiv_total_cap: int = 20
    
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

    @classmethod
    def load_from_yaml(cls, yaml_path: str | Path | None = None) -> "Settings":
        data = {}
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

        return cls(**data)

settings = Settings.load_from_yaml()

def load_yaml_config(yaml_path: str | Path) -> None:
    """Override configuration variables from a YAML file."""
    global settings
    settings = Settings.load_from_yaml(yaml_path)
