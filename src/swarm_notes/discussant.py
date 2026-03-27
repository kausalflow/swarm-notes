"""Discussant module: Analyses a batch of papers to produce a daily discussion."""

import os
import logging
from pydantic_ai import Agent

from swarm_notes.analyst import PaperAnalysis
from swarm_notes.config import settings
from swarm_notes.router import SkillSpec

logger = logging.getLogger(__name__)


def discuss_papers(analyses: list[PaperAnalysis], skill: SkillSpec | None = None) -> str:
    """Generates a cohesive discussion from a list of paper analyses."""
    if not analyses:
        return "No new research processed in this batch."

    system_prompt = (
        "You are a senior AI researcher reviewing the daily influx of new papers. "
        "Your goal is to write a cohesive, insightful markdown discussion tying together the "
        "key trends, interesting concepts, and notable architectures from today's batch. "
        "Do not just list them one by one. Try to synthesise and highlight the most impactful ideas, "
        "contrasting differing approaches if applicable. Keep the discussion concise, analytical, and well-formatted."
    )
    if skill and skill.discussant_context:
        system_prompt += f"\n\nSKILL-SPECIFIC CONTEXT:\n{skill.discussant_context}"

    discussant_agent = Agent(
        model=settings.llm_model,
        system_prompt=system_prompt
    )

    prompt = "Here are the parsed summaries of the new papers:\n\n"
    for a in analyses:
        prompt += f"--- Title: {a.title} ({a.arxiv_id}) ---\n"
        prompt += f"Summary: {a.summary}\n"
        prompt += f"Key Contributions: {', '.join(a.key_contributions)}\n"
        prompt += f"Limitations: {a.limitations}\n\n"

    logger.info("Discussant: synthesising insights from %d papers...", len(analyses))
    result = discussant_agent.run_sync(prompt)
    return result.output
