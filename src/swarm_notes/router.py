"""Router (Skill Registry): maps a raw paper abstract to a domain skill.

The router evaluates the abstract and primary ArXiv category to determine
which domain-specific extraction schema and system-prompt to use.  This
keeps each analyst prompt tight and domain-focused.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from swarm_notes.watcher import RawPaper

logger = logging.getLogger(__name__)


from pathlib import Path
import yaml
from pydantic import BaseModel, Field

from swarm_notes.config import settings
from swarm_notes.watcher import RawPaper

logger = logging.getLogger(__name__)


class SkillSpec(BaseModel):
    """Represents a domain extraction skill loaded from YAML."""
    id: str = Field(description="Skill ID, usually the folder name.")
    name: str
    description: str
    extra_system_prompt: str
    preferred_tags: list[str] = Field(default_factory=list)
    arxiv_categories: list[str] = Field(default_factory=list)
    
    # Per-agent overrides (optional)
    analyst_system_prompt_override: str | None = None
    discussant_context: str | None = None
    domain_expert_context: str | None = None


# Global registry populated at runtime
_SKILL_REGISTRY: list[SkillSpec] = []


def load_skills() -> None:
    """Load skills from the skills_dir into the global registry.
    
    If settings.active_skills is set, only load those IDs.
    Always ensures a 'general-ml' skill is available as fallback.
    """
    global _SKILL_REGISTRY
    skills_dir = settings.skills_dir
    if not skills_dir.exists():
        logger.warning("Skills directory not found at %s", skills_dir)
        return

    active_ids = settings.active_skills
    loaded = []
    
    # Iterate through subdirectories in skills_dir
    for skill_path in skills_dir.iterdir():
        if not skill_path.is_dir():
            continue
        
        skill_id = skill_path.name
        if active_ids and skill_id not in active_ids and skill_id != "general-ml":
            continue
            
        yaml_file = skill_path / "skill.yaml"
        if not yaml_file.exists():
            continue
            
        try:
            with open(yaml_file, encoding="utf-8") as f:
                data = yaml.safe_load(f)
                spec = SkillSpec(id=skill_id, **data)
                loaded.append(spec)
        except Exception as e:
            logger.error("Failed to load skill from %s: %s", yaml_file, e)

    _SKILL_REGISTRY = loaded
    logger.info("Router: loaded %d skills", len(loaded))


def get_general_skill() -> SkillSpec:
    """Return the general skill fallback."""
    for s in _SKILL_REGISTRY:
        if s.id == "general-ml":
            return s
    # Hardcoded fallback if not even general-ml exists on disk
    return SkillSpec(
        id="general-ml",
        name="GeneralMLSkill",
        description="Fallback skill.",
        extra_system_prompt="Analyse the paper.",
    )


def route(paper: RawPaper) -> SkillSpec:
    """Select the best-matching skill for *paper* from the loaded registry."""
    if not _SKILL_REGISTRY:
        # Lazy load if not already done (e.g. in tests)
        load_skills()

    combined_text = f"{paper.title} {paper.abstract}".lower()

    # 1. Direct ArXiv category match (if skill defines it)
    for skill in _SKILL_REGISTRY:
        if paper.primary_category in skill.arxiv_categories:
            if _count_signals(combined_text, skill.preferred_tags) > 0:
                logger.debug(
                    "Router: '%s' → %s (via category %s)",
                    paper.arxiv_id, skill.name, paper.primary_category,
                )
                return skill

    # 2. Keyword-signal scoring
    best_skill: SkillSpec = get_general_skill()
    best_score: int = 0

    for skill in _SKILL_REGISTRY:
        if skill.id == "general-ml":
            continue
        score = _count_signals(combined_text, skill.preferred_tags)
        if score > best_score:
            best_score = score
            best_skill = skill

    logger.debug(
        "Router: '%s' → %s (score=%d)", paper.arxiv_id, best_skill.name, best_score
    )
    return best_skill


def _count_signals(text: str, tags: list[str]) -> int:
    """Count how many *tags* appear as whole-word substrings in *text*.
    
    Identical logic to legacy router.
    """
    count = 0
    for tag in tags:
        parts = re.split(r"[-_]", tag)
        escaped_parts = [re.escape(p) for p in parts if p]
        if not escaped_parts:
            continue
        pattern = r"[-_ ]?".join(escaped_parts)
        if re.search(pattern, text, re.IGNORECASE):
            count += 1
    return count


# Backward compatibility exports for existing tests
# These will be resolved dynamically if used, but normally the registry is loaded in main()
class _SkillCompat:
    @property
    def GENERAL_SKILL(self): return get_general_skill()
    @property
    def VISION_SKILL(self): 
        for s in _SKILL_REGISTRY:
            if "vision" in s.id: return s
        return get_general_skill()

# We can't easily export variables that change after module load unless we use a proxy
# But since this is a refactor, I'll just keep the route() as the main API.
# Existing tests import VISION_SKILL from router. I'll need to patch them or export a dummy.
# Actually, I'll export a function to get them if needed, or just let tests break and I'll fix them.
# Better: export them as None and populate them in load_skills? No, that's messy.
# I'll update the tests.
