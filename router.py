"""Router Agent — lightweight triage that selects the best Skill for a paper.

The router evaluates each registered Skill's keyword trigger against the paper
title and abstract.  The first matching skill is returned.  If no skill
matches, ``None`` is returned and the caller should fall back to generic
processing or skip the paper.
"""

from __future__ import annotations

import logging
from typing import Optional, Type

from skills.base import Skill
from skills.registry import SkillRegistry

logger = logging.getLogger(__name__)


def route_paper(
    title: str,
    abstract: str,
    registry: Optional[SkillRegistry] = None,
) -> Optional[Type[Skill]]:
    """Return the first Skill whose keywords match *title* or *abstract*.

    Parameters
    ----------
    title:
        Raw paper title.
    abstract:
        Raw paper abstract.
    registry:
        Optional :class:`~skills.registry.SkillRegistry` to use.  When
        ``None``, a default registry containing all built-in skills is used.

    Returns
    -------
    Type[Skill] | None
        The matched Skill class, or ``None`` if no skill matches.
    """
    if registry is None:
        registry = SkillRegistry()

    for skill_cls in registry.all_skills():
        if skill_cls.matches(title, abstract):
            logger.info("Routed paper '%s' → %s", title, skill_cls.name())
            return skill_cls

    logger.warning("No skill matched for paper '%s'. Dropping paper.", title)
    return None
