"""Discussant module: Analyses a batch of papers to produce a daily discussion."""

import os
import logging
from pydantic_ai import Agent

from swarm_cruise.analyst import PaperAnalysis
from swarm_cruise.config import settings

logger = logging.getLogger(__name__)

discussant_agent = Agent(
    model=settings.llm_model,
    system_prompt=(
        "You are a senior AI researcher reviewing the daily influx of new papers. "
        "Your goal is to write a cohesive, insightful markdown discussion tying together the "
        "key trends, interesting concepts, and notable architectures from today's batch. "
        "Do not just list them one by one. Try to synthesise and highlight the most impactful ideas, "
        "contrasting differing approaches if applicable. Keep the discussion concise, analytical, and well-formatted."
    )
)

def discuss_papers(analyses: list[PaperAnalysis]) -> str:
    """Generates a cohesive discussion from a list of paper analyses."""
    if not analyses:
        return "No new research processed in this batch."

    prompt = "Here are the parsed summaries of the new papers:\n\n"
    for a in analyses:
        prompt += f"--- Title: {a.title} ({a.arxiv_id}) ---\n"
        prompt += f"Summary: {a.summary}\n"
        prompt += f"Key Contributions: {', '.join(a.key_contributions)}\n"
        prompt += f"Novelty: {a.novelty_assessment}\n\n"

    try:
        # Patching google auth for pydantic_ai via explicit kwargs matching analyst if needed
        # Or relying on os.environ directly like in analyst.py logic.
        # But wait, analyst uses default API key implicitly if GEMINI_API_KEY is available.
        logger.info("Discussant: synthesising insights from %d papers...", len(analyses))
        result = discussant_agent.run_sync(prompt)
        return result.data
    except Exception as exc:
        logger.error("Discussant: Failed to generate daily discussion: %s", exc)
        return f"Failed to generate discussion. Error: {exc}"
