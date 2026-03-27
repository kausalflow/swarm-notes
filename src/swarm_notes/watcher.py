"""Compatibility facade for paper search providers.

Provider-specific implementations live under ``swarm_notes.paper_search``.
This module re-exports the public watcher API to avoid breaking existing imports.
"""

from swarm_notes.paper_search import ArxivPaperProvider
from swarm_notes.paper_search import OpenAlexPaperProvider
from swarm_notes.paper_search import PaperProvider
from swarm_notes.paper_search import RawPaper
from swarm_notes.paper_search import SemanticScholarPaperProvider
from swarm_notes.paper_search import build_arxiv_search_query as _build_arxiv_search_query
from swarm_notes.paper_search import fetch_papers as _fetch_papers
from swarm_notes.paper_search import build_paper_provider as _build_paper_provider
from swarm_notes.paper_search import build_openalex_search_query as _build_openalex_search_query
from swarm_notes.paper_search import is_keyword_relevant_openalex_result as _is_keyword_relevant_openalex_result
from swarm_notes.paper_search import match_keywords_openalex_result as _match_keywords_openalex_result
from swarm_notes.paper_search import query_arxiv as _query_arxiv
from swarm_notes.paper_search import query_semantic_scholar as _query_semantic_scholar
from swarm_notes.paper_search import reconstruct_openalex_abstract as _reconstruct_openalex_abstract


def fetch_papers(
    keywords: list[str] | None = None,
    max_per_keyword: int | None = None,
    total_cap: int | None = None,
    provider_name: str | None = None,
) -> list[RawPaper]:
    return _fetch_papers(
        keywords=keywords,
        max_per_keyword=max_per_keyword,
        total_cap=total_cap,
        provider_name=provider_name,
    )

__all__ = [
    "ArxivPaperProvider",
    "OpenAlexPaperProvider",
    "PaperProvider",
    "RawPaper",
    "SemanticScholarPaperProvider",
    "_build_arxiv_search_query",
    "_build_paper_provider",
    "_build_openalex_search_query",
    "_is_keyword_relevant_openalex_result",
    "_match_keywords_openalex_result",
    "_query_arxiv",
    "_query_semantic_scholar",
    "_reconstruct_openalex_abstract",
    "fetch_papers",
]