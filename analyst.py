"""Analyst Agent — contextual extraction using pydantic-ai.

The analyst:
1. Reads the current taxonomy (flat list of existing tags).
2. Injects those tags into the LLM prompt so the model re-uses existing
   concepts instead of minting synonyms.
3. Calls pydantic-ai with the Skill's schema to extract structured metadata.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Type

from pydantic_ai import Agent

from skills.base import PaperMetadata, Skill

logger = logging.getLogger(__name__)

_DEFAULT_TAXONOMY = Path(__file__).parent / "taxonomy.json"
_DEFAULT_MODEL = "openai:gpt-4o"


def _load_taxonomy(taxonomy_path: Path) -> list[str]:
    """Read the taxonomy file and return the current tag list."""
    if not taxonomy_path.exists():
        return []
    try:
        data = json.loads(taxonomy_path.read_text())
        if isinstance(data, list):
            return [str(t) for t in data]
        return []
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("Could not read taxonomy at %s: %s", taxonomy_path, exc)
        return []


def _build_taxonomy_context(tags: list[str]) -> str:
    """Format the taxonomy list into an LLM-friendly instruction block."""
    if not tags:
        return (
            "No existing tags are available yet. "
            "Create clear, concise tags as needed."
        )
    tag_str = ", ".join(f'"{t}"' for t in tags)
    return (
        f"Existing taxonomy tags: [{tag_str}]. "
        "Always prioritise reusing these exact tags for architectures, datasets, "
        "and concepts. Only create a new tag if the concept is entirely novel."
    )


def analyse_paper(
    title: str,
    abstract: str,
    full_text: str,
    skill_cls: Type[Skill],
    *,
    model: str = _DEFAULT_MODEL,
    taxonomy_path: Path = _DEFAULT_TAXONOMY,
) -> PaperMetadata:
    """Run the analyst agent and return structured paper metadata.

    Parameters
    ----------
    title:
        Paper title.
    abstract:
        Paper abstract.
    full_text:
        Full paper text (or abstract-only if full text is unavailable).
    skill_cls:
        The :class:`~skills.base.Skill` subclass selected by the router.
    model:
        pydantic-ai model identifier (default: ``openai:gpt-4o``).
    taxonomy_path:
        Path to the ``taxonomy.json`` file.

    Returns
    -------
    PaperMetadata
        An instance of the Skill's schema populated by the LLM.
    """
    taxonomy_tags = _load_taxonomy(taxonomy_path)
    taxonomy_ctx = _build_taxonomy_context(taxonomy_tags)

    combined_system_prompt = (
        f"{skill_cls.system_prompt}\n\n"
        f"{taxonomy_ctx}\n\n"
        "When listing tags, authors, datasets, architectures, or metrics, "
        "output them as plain strings without brackets."
    )

    agent: Agent[None, PaperMetadata] = Agent(
        model=model,
        output_type=skill_cls.schema,
        system_prompt=combined_system_prompt,
    )

    user_message = (
        f"Title: {title}\n\n"
        f"Abstract:\n{abstract}\n\n"
        f"Full text (may be truncated):\n{full_text}"
    )

    result = agent.run_sync(user_message)
    return result.output
