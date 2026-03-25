"""Analyst: structured extraction agent powered by pydantic-ai.

Reads the abstract, injects the taxonomy, and returns a fully typed
:class:`PaperAnalysis` object using the domain-specific skill prompt.
"""

from __future__ import annotations

import json
import logging
from typing import Annotated

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from swarm_notes.config import settings
from swarm_notes.router import Skill
from swarm_notes.vault_manager import get_existing_concept_slugs
from swarm_notes.watcher import RawPaper

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Output schema
# ---------------------------------------------------------------------------

class ConceptLink(BaseModel):
    """A concept mentioned in the paper that deserves its own vault entry."""

    slug: str = Field(
        description=(
            "URL-safe slug for the concept (e.g. 'flash-attention', 'mamba'). "
            "Use hyphens, no spaces."
        )
    )
    display_name: str = Field(
        description="Human-readable display name (e.g. 'Flash Attention', 'Mamba')."
    )
    one_liner: str = Field(
        description="One sentence that defines this concept in the context of the paper."
    )


class OpenQuestion(BaseModel):
    """An explicit open question, unresolved problem, or future work direction."""
    slug: str = Field(
        description=("URL-safe slug for the question (e.g. 'llm-reasoning-limits'). "
                     "Use hyphens, no spaces.")
    )
    title: str = Field(
        description="A concise, 3-5 word title for the open question."
    )
    background: str = Field(
        description="A highly concise, standalone 1-2 sentence background context unifying the open question. Must be written objectively as a universal encyclopedic fact. DO NOT use phrases like 'this paper', 'the authors', or 'this study'."
    )
    description: str = Field(
        description="Detailed explanation of the open question or future work."
    )


class PaperAnalysis(BaseModel):
    """Structured extraction output for a single academic paper."""

    title: str = Field(description="Clean, full title of the paper.")
    authors: list[str] = Field(description="List of author full names.")
    published: str = Field(description="Publication date as YYYY-MM-DD.")
    arxiv_id: str = Field(description="ArXiv identifier (e.g. '2301.12345').")
    url: str = Field(description="Canonical URL of the paper.")

    summary: Annotated[
        str,
        Field(
            description=(
                "A concise 3-5 sentence summary of the paper's core contribution, "
                "methodology, and key results. Written for a technical ML researcher."
            )
        ),
    ]

    key_contributions: list[str] = Field(
        description="Bullet-point list of 3-5 key contributions."
    )

    tags: list[str] = Field(
        description=(
            "Relevant tags from the provided taxonomy. "
            "Choose only tags that genuinely apply. Maximum 10 tags."
        )
    )

    architectures: list[str] = Field(
        default_factory=list,
        description=(
            "Architecture names used or proposed (from the taxonomy architectures list). "
            "Leave empty if not applicable."
        ),
    )

    datasets: list[str] = Field(
        default_factory=list,
        description=(
            "Names of datasets used for evaluation or training "
            "(e.g. 'ImageNet', 'ETTh1', 'LAION-5B')."
        ),
    )

    concepts: list[ConceptLink] = Field(
        default_factory=list,
        description=(
            "Key concepts introduced or heavily used by the paper that "
            "should have their own vault entry (e.g. a new architecture, "
            "technique, or dataset). Maximum 5."
        ),
    )

    limitations: str = Field(
        default="",
        description="Brief statement of known limitations or future work.",
    )

    domain: str = Field(
        description=(
            "Primary domain from the taxonomy domains list "
            "(e.g. 'nlp', 'computer-vision', 'time-series')."
        )
    )

    open_questions: list[OpenQuestion] = Field(
        default_factory=list,
        description="List of open questions or future research identified by the domain expert.",
    )


# ---------------------------------------------------------------------------
# Agent factory
# ---------------------------------------------------------------------------

def _build_system_prompt(skill: Skill, taxonomy: dict) -> str:
    tags_list = ", ".join(taxonomy.get("tags", []))
    architectures_list = ", ".join(taxonomy.get("architectures", []))
    domains_list = ", ".join(taxonomy.get("domains", []))
    
    existing_concepts_list = get_existing_concept_slugs()
    existing_concepts_str = ", ".join(existing_concepts_list) if existing_concepts_list else "(No concepts currently exist in the vault)"

    return f"""You are an expert academic paper analyst specialising in machine learning research.

Your task is to analyse the provided paper abstract and extract structured information.

TAXONOMY (use ONLY these values for tags/architectures/domains):
- Available tags: {tags_list}
- Available architectures: {architectures_list}
- Available domains: {domains_list}

EXISTING CONCEPTS IN VAULT:
{existing_concepts_str}

SKILL CONTEXT ({skill.name}):
{skill.extra_system_prompt}

IMPORTANT RULES:
1. Select tags ONLY from the taxonomy tag list above.
2. Select domain ONLY from the taxonomy domains list above.
3. Select architectures ONLY from the taxonomy architectures list above (or leave empty).
4. The summary must be 3-5 sentences, technically precise but accessible.
5. Key contributions must be specific, not generic ("we propose X" → "X achieves Y on Z benchmark").
6. For concepts, ALWAYS check the EXISTING CONCEPTS IN VAULT list. If a highly synonymous concept already exists, you MUST exactly reuse its slug. Only create entirely new concepts if they represent a genuinely novel idea.
"""


def analyse(paper: RawPaper, skill: Skill) -> PaperAnalysis:
    """Run the analyst agent on *paper* using the provided *skill* context.

    Parameters
    ----------
    paper:
        Raw paper data from the watcher.
    skill:
        Domain skill selected by the router.

    Returns
    -------
    PaperAnalysis
        Structured extraction result.
    """
    taxonomy = _load_taxonomy()
    system_prompt = _build_system_prompt(skill, taxonomy)

    agent: Agent[None, PaperAnalysis] = Agent(
        model=settings.llm_model,
        output_type=PaperAnalysis,
        system_prompt=system_prompt,
    )

    user_message = (
        f"Title: {paper.title}\n\n"
        f"Authors: {', '.join(paper.authors)}\n\n"
        f"Published: {paper.published}\n\n"
        f"ArXiv ID: {paper.arxiv_id}\n\n"
        f"URL: {paper.url}\n\n"
        f"Abstract:\n{paper.abstract}"
    )

    logger.info("Analyst: analysing paper %s with skill %s", paper.arxiv_id, skill.name)

    result = agent.run_sync(user_message)
    analysis: PaperAnalysis = result.output

    # Ensure metadata from the raw paper is preserved accurately
    analysis.arxiv_id = paper.arxiv_id
    analysis.url = paper.url
    analysis.published = paper.published
    if not analysis.authors:
        analysis.authors = paper.authors

    logger.debug(
        "Analyst: paper %s → %d tags, %d concepts",
        paper.arxiv_id,
        len(analysis.tags),
        len(analysis.concepts),
    )
    return analysis


def _load_taxonomy() -> dict:
    """Load taxonomy.json, returning an empty dict on failure."""
    try:
        with settings.taxonomy_file.open() as fh:
            return json.load(fh)
    except Exception as exc:
        logger.warning("Could not load taxonomy: %s", exc)
        return {}
