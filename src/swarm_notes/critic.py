"""Research Critic: approves only high-value concepts and open questions."""

from __future__ import annotations

import json
import logging

from pydantic import BaseModel, Field
from pydantic_ai import Agent

from swarm_notes.analyst import ConceptLink, OpenQuestion, PaperAnalysis, RejectedCandidate
from swarm_notes.config import settings
from swarm_notes.router import SkillSpec
from swarm_notes.vault_manager import get_existing_concept_slugs
from swarm_notes.watcher import RawPaper

logger = logging.getLogger(__name__)


def _fallback_review_summary(review: CriticReview) -> str:
    """Return a deterministic review summary when the model omits one."""
    return (
        "Archivist review kept only candidates judged central to the paper and reusable across future work. "
        f"Approved {len(review.approved_concepts)} concept(s), {len(review.approved_open_questions)} open question(s), and {len(review.approved_datasets)} dataset(s), "
        f"with {len(review.rejected_candidates)} rejected candidate note(s)."
    )


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
    approved_datasets: list[str] = Field(
        default_factory=list,
        description=(
            "Only critical named datasets that deserve standalone notes. "
            "Return an empty list if none qualify."
        ),
    )
    review_summary: str = Field(
        default="",
        description="Short note summarizing why items were approved or rejected.",
    )
    rejected_candidates: list[RejectedCandidate] = Field(
        default_factory=list,
        description="Structured rejection records for candidates that were not approved.",
    )


def _build_system_prompt(skill: SkillSpec) -> str:
    existing_concepts = get_existing_concept_slugs()
    existing_concepts_str = ", ".join(existing_concepts) if existing_concepts else "(No concepts currently exist in the vault)"

    prompt = f"""You are a highly selective research archivist protecting a long-lived ML knowledge vault.

You will receive one paper analysis with candidate concepts, candidate open questions, and candidate datasets.
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
5. Reject paper-internal subcomponents, helper modules, or local implementation details unless they are clearly reusable ideas that future papers would likely name and discuss in their own right.
6. If both an overarching mechanism and one of its supporting submodules are proposed, prefer the overarching mechanism and reject the submodule unless the submodule is independently important.
7. Approve an open question only if it is a substantial unresolved bottleneck or research question that remains useful beyond this one paper.
8. Reject boilerplate future work such as more experiments, larger models, more data, or better performance unless the candidate identifies a specific unresolved mechanism or limitation.
9. Approve a dataset only if it is a specific named dataset central to evaluation claims and useful as a reusable standalone note.
10. Reject generic, aggregate, or counting-style dataset labels such as "real-world datasets", "benchmark datasets", "10 datasets", or unnamed proprietary buckets.
11. Be scarce for datasets too: approve at most 2 datasets.
12. Reuse an existing concept slug when the candidate is synonymous with something already in the vault.
13. Be scarce. Approve at most 2 concepts and at most 2 open questions.
14. Preserve evidence_excerpt and rationale fields when they help justify the approved item.
15. Always fill review_summary with 2-4 sentences explaining the approval standard you applied.
16. For every rejected candidate, you MUST append a structured object to rejected_candidates with ALL required fields:
    - candidate_type: "concept" or "open_question" or "dataset"
    - candidate_slug: slug string
    - candidate_title: display name/title string
    - reason_code: one of [generic, paper_local, not_novel, not_reusable, weak_evidence, low_impact, duplicate_existing, subcomponent_of_broader_mechanism, other]
    - reason: concise explanation (1 sentence)
"""
    if skill.critic_context:
        prompt += f"\n\nSKILL-SPECIFIC REVIEW CONTEXT:\n{skill.critic_context}"
    return prompt


def review_analysis(analysis: PaperAnalysis, paper: RawPaper, skill: SkillSpec) -> PaperAnalysis:
    """Review candidate concepts, open questions, and datasets before writing to the vault."""
    if not analysis.concepts and not analysis.open_questions and not analysis.datasets:
        logger.debug("Critic: no candidate concepts, open questions, or datasets for %s", paper.arxiv_id)
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
        "Critic: reviewing paper %s with %d concept candidate(s), %d open-question candidate(s), and %d dataset candidate(s)",
        paper.arxiv_id,
        len(analysis.concepts),
        len(analysis.open_questions),
        len(analysis.datasets),
    )
    result = agent.run_sync(json.dumps(payload, ensure_ascii=False, indent=2))
    review = result.output

    analysis.concepts = review.approved_concepts
    analysis.open_questions = review.approved_open_questions
    analysis.datasets = review.approved_datasets
    analysis.critic_review_summary = review.review_summary or _fallback_review_summary(review)
    analysis.critic_rejected_candidates = review.rejected_candidates

    logger.info(
        "Critic: paper %s approved %d concept(s), %d open question(s), and %d dataset(s)",
        paper.arxiv_id,
        len(analysis.concepts),
        len(analysis.open_questions),
        len(analysis.datasets),
    )
    if review.review_summary:
        logger.debug("Critic summary for %s: %s", paper.arxiv_id, review.review_summary)

    return analysis