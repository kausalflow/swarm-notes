"""Research Critic: approves only high-value concepts and open questions."""

from __future__ import annotations

import json
import logging

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from swarm_notes.analyst import ConceptLink, OpenQuestion, PaperAnalysis
from swarm_notes.config import settings
from swarm_notes.router import SkillSpec
from swarm_notes.vault_manager import get_existing_concept_slugs
from swarm_notes.watcher import RawPaper

logger = logging.getLogger(__name__)


class CriticReview(BaseModel):
    """Final approved knowledge artifacts after critic review."""

    approved_concepts: list[ConceptLink] = Field(
        default_factory=list,
        description=(
            "Only the concept candidates that deserve permanent standalone vault notes. "
            "Return an empty list if none qualify."
        ),
    )
    approved_open_questions: list[OpenQuestion] = Field(
        default_factory=list,
        description=(
            "Only the open-question candidates that deserve permanent standalone vault notes. "
            "Return an empty list if none qualify."
        ),
    )
    review_summary: str = Field(
        default="",
        description="Short note summarizing why items were approved or rejected.",
    )
    rejected_candidates: list[str] = Field(
        default_factory=list,
        description="Short rejection notes for candidates that were not approved.",
    )


def _build_system_prompt(skill: SkillSpec) -> str:
    existing_concepts = get_existing_concept_slugs()
    existing_concepts_str = ", ".join(existing_concepts) if existing_concepts else "(No concepts currently exist in the vault)"

    prompt = f"""You are a highly selective research archivist protecting a long-lived ML knowledge vault.

You will receive one paper analysis with candidate concepts and candidate open questions.
Your job is to decide which candidates deserve permanent standalone notes.

EXISTING CONCEPTS IN VAULT:
{existing_concepts_str}

SKILL CONTEXT ({skill.name}):
{skill.extra_system_prompt}

REVIEW POLICY:
1. Do NOT invent new candidates. Only approve, reject, or rewrite the candidates you were given.
2. Default to approving nothing if the candidates are weak.
3. Approve a concept only if it is central to the paper's contribution, likely to recur across future papers, and distinct enough to deserve its own note.
4. Reject generic ML vocabulary, one-off implementation details, routine datasets, routine benchmarks, and paper-local terminology.
5. Approve an open question only if it is a substantial unresolved bottleneck or research question that remains useful beyond this one paper.
6. Reject boilerplate future work such as more experiments, larger models, more data, or better performance unless the candidate identifies a specific unresolved mechanism or limitation.
7. Reuse an existing concept slug when the candidate is synonymous with something already in the vault.
8. Be scarce. Approve at most 2 concepts and at most 2 open questions.
9. Preserve evidence_excerpt and rationale fields when they help justify the approved item.
"""
    if skill.critic_context:
        prompt += f"\n\nSKILL-SPECIFIC REVIEW CONTEXT:\n{skill.critic_context}"
    return prompt


def review_analysis(analysis: PaperAnalysis, paper: RawPaper, skill: SkillSpec) -> PaperAnalysis:
    """Review candidate concepts and open questions before writing to the vault."""
    if not analysis.concepts and not analysis.open_questions:
        logger.debug("Critic: no candidate concepts or open questions for %s", paper.arxiv_id)
        return analysis

    agent: Agent[None, CriticReview] = Agent(
        model=settings.llm_model,
        output_type=CriticReview,
        system_prompt=_build_system_prompt(skill),
    )

    payload = {
        "paper": {
            "title": paper.title,
            "abstract": paper.abstract,
            "authors": paper.authors,
            "published": paper.published,
            "arxiv_id": paper.arxiv_id,
            "url": paper.url,
        },
        "analysis": analysis.model_dump(mode="json"),
    }

    logger.info(
        "Critic: reviewing paper %s with %d concept candidate(s) and %d open-question candidate(s)",
        paper.arxiv_id,
        len(analysis.concepts),
        len(analysis.open_questions),
    )
    result = agent.run_sync(json.dumps(payload, ensure_ascii=False, indent=2))
    review = result.output

    analysis.concepts = review.approved_concepts
    analysis.open_questions = review.approved_open_questions
    analysis.critic_review_summary = review.review_summary
    analysis.critic_rejected_candidates = review.rejected_candidates

    logger.info(
        "Critic: paper %s approved %d concept(s) and %d open question(s)",
        paper.arxiv_id,
        len(analysis.concepts),
        len(analysis.open_questions),
    )
    if review.review_summary:
        logger.debug("Critic summary for %s: %s", paper.arxiv_id, review.review_summary)

    return analysis