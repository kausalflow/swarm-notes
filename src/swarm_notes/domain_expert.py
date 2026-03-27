"""Domain Expert module: Scrapes ArXiv HTML and extracts deep insights like open questions."""

import logging
import requests
from bs4 import BeautifulSoup
from pydantic_ai import Agent

from swarm_notes.analyst import OpenQuestion
from swarm_notes.config import settings
from swarm_notes.router import SkillSpec

logger = logging.getLogger(__name__)

def extract_open_questions(arxiv_id: str, skill: SkillSpec | None = None) -> list[OpenQuestion]:
    """Scrape the ArXiv HTML page and extract open questions using the LLM.
    
    If the HTML is not available (404), fails gracefully.
    """
    url = f"https://arxiv.org/html/{arxiv_id}"
    logger.info("DomainExpert: Fetching HTML for paper %s at %s", arxiv_id, url)
    
    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code == 404:
            logger.warning("DomainExpert: HTML view not found or disabled for %s", arxiv_id)
            return []
        resp.raise_for_status()
        
        soup = BeautifulSoup(resp.text, "html.parser")
        text_content = soup.get_text(separator="\n", strip=True)
        
        logger.info("DomainExpert: Analysing full text of %s (%d chars)", arxiv_id, len(text_content))
        
        system_prompt = (
            "You are a meticulous Domain Expert in machine learning. "
            "Carefully read the provided full text of a research paper and "
            "extract explicit 'open questions', 'future work', or 'unresolved problems' "
            "mentioned by the authors. Return them as a precise, concise list of structured candidate objects. "
            "If none are explicitly specified with sufficient detail, return an empty list! DO NOT hallucinate open questions if the authors don't discuss them. "
            "If multiple papers share generic open questions, ensure the titles and slugs are general enough to be reusable. "
            "CRUCIAL: When writing the background and description, write them as universal, standalone concepts. DO NOT use phrases like 'In this paper', 'The authors', or 'This study'. Frame the context objectively. "
            "These are candidate proposals for later archivist review, so default to zero unless the question is technically substantial, broadly reusable, and clearly unresolved. "
            "For every proposed open question, fill importance_reason and evidence_excerpt with specific justification from the paper text. "
            "Reject generic future work such as 'improve performance', 'run more experiments', or 'collect more data' unless the authors identify a specific unresolved bottleneck. "
            "Prefer 0-2 excellent open-question candidates over a long list."
        )
        if skill and skill.domain_expert_context:
            system_prompt += f"\n\nSKILL-SPECIFIC CONTEXT:\n{skill.domain_expert_context}"

        # Defining inline purely for concise structured output typing per run
        agent: Agent[None, list[OpenQuestion]] = Agent(
            model=settings.llm_model,
            output_type=list[OpenQuestion],
            system_prompt=system_prompt
        )
        
        # Capping context window safely around 250k characters.
        result = agent.run_sync(text_content[:250000])
        return result.output
        
    except Exception as exc:
        logger.error("DomainExpert: failed to extract open questions for %s: %s", arxiv_id, exc)
        return []
