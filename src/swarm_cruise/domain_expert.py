"""Domain Expert module: Scrapes ArXiv HTML and extracts deep insights like open questions."""

import logging
import requests
from bs4 import BeautifulSoup
from pydantic_ai import Agent

from swarm_cruise.config import settings

logger = logging.getLogger(__name__)

def extract_open_questions(arxiv_id: str) -> list[str]:
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
        
        # Defining inline purely for concise structured output typing per run
        agent: Agent[None, list[str]] = Agent(
            model=settings.llm_model,
            output_type=list[str],
            system_prompt=(
                "You are a meticulous Domain Expert in machine learning. "
                "Carefully read the provided full text of a research paper and "
                "extract explicit 'open questions', 'future work', or 'unresolved problems' "
                "mentioned by the authors. Return them as a precise, concise list of strings. "
                "If none are specified, return an empty list."
            )
        )
        
        # Capping context window safely around 250k characters.
        result = agent.run_sync(text_content[:250000])
        return result.data
        
    except Exception as exc:
        logger.error("DomainExpert: failed to extract open questions for %s: %s", arxiv_id, exc)
        return []
