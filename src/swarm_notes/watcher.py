"""Compatibility facade for paper search providers.

Provider-specific implementations live under ``swarm_notes.paper_search``.
This module re-exports the public watcher API to avoid breaking existing imports.
"""

import logging

from swarm_notes.config import settings
from swarm_notes.paper_search import ArxivPaperProvider
from swarm_notes.paper_search import OpenAlexPaperProvider
from swarm_notes.paper_search import PaperProvider
from swarm_notes.paper_search import RawPaper
from swarm_notes.paper_search import SemanticScholarPaperProvider
from swarm_notes.paper_search import build_paper_provider as _build_paper_provider
from swarm_notes.paper_search import build_openalex_search_query as _build_openalex_search_query
from swarm_notes.paper_search import is_keyword_relevant_openalex_result as _is_keyword_relevant_openalex_result
from swarm_notes.paper_search import match_keywords_openalex_result as _match_keywords_openalex_result
from swarm_notes.paper_search import query_arxiv as _query_arxiv
from swarm_notes.paper_search import query_semantic_scholar as _query_semantic_scholar
from swarm_notes.paper_search import reconstruct_openalex_abstract as _reconstruct_openalex_abstract

logger = logging.getLogger(__name__)


def fetch_papers(
    keywords: list[str] | None = None,
    max_per_keyword: int | None = None,
    total_cap: int | None = None,
    provider_name: str | None = None,
) -> list[RawPaper]:
    if keywords is None:
        keywords = settings.paper_keywords
    if max_per_keyword is None:
        max_per_keyword = settings.paper_max_results_per_keyword
    if total_cap is None:
        total_cap = settings.paper_total_cap

    provider = _build_paper_provider(provider_name)
    seen_ids: set[str] = set()
    papers: list[RawPaper] = []

    for keyword in keywords:
        if len(papers) >= total_cap:
            break

        remaining = total_cap - len(papers)
        batch = provider.search(keyword, min(max_per_keyword, remaining))

        for paper in batch:
            if paper.arxiv_id not in seen_ids:
                seen_ids.add(paper.arxiv_id)
                papers.append(paper)
            else:
                for existing in papers:
                    if existing.arxiv_id == paper.arxiv_id:
                        if keyword not in existing.keywords_matched:
                            existing.keywords_matched.append(keyword)
                        break

        logger.info("Keyword '%s': fetched %d paper(s)", keyword, len(batch))

    logger.info("Watcher: %d unique paper(s) collected in total", len(papers))
    return papers

__all__ = [
    "ArxivPaperProvider",
    "OpenAlexPaperProvider",
    "PaperProvider",
    "RawPaper",
    "SemanticScholarPaperProvider",
    "_build_paper_provider",
    "_build_openalex_search_query",
    "_is_keyword_relevant_openalex_result",
    "_match_keywords_openalex_result",
    "_query_arxiv",
    "_query_semantic_scholar",
    "_reconstruct_openalex_abstract",
    "fetch_papers",
]