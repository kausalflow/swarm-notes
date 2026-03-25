"""Skill Registry — discovers and manages all available Skill subclasses."""

from __future__ import annotations

from typing import Optional, Type

from skills.base import Skill
from skills.time_series import TimeSeriesSkill

# All registered skills, evaluated in order. First match wins.
_REGISTERED_SKILLS: list[Type[Skill]] = [
    TimeSeriesSkill,
]


class SkillRegistry:
    """Central registry of all domain Skills."""

    def __init__(self, skills: Optional[list[Type[Skill]]] = None) -> None:
        self._skills: list[Type[Skill]] = skills if skills is not None else list(_REGISTERED_SKILLS)

    def register(self, skill: Type[Skill]) -> None:
        """Add a new skill to the registry."""
        self._skills.append(skill)

    def all_skills(self) -> list[Type[Skill]]:
        """Return all registered skill classes."""
        return list(self._skills)
