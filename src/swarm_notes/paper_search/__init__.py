from __future__ import annotations

from swarm_notes.config import settings
from swarm_notes.paper_search.arxiv import ArxivPaperProvider
from swarm_notes.paper_search.base import PaperProvider, RawPaper
from swarm_notes.paper_search.openalex import (
    OpenAlexPaperProvider,
    build_openalex_search_query,
    is_keyword_relevant_openalex_result,
    match_keywords_openalex_result,
    reconstruct_openalex_abstract,
)
from swarm_notes.paper_search.semantic_scholar import SemanticScholarPaperProvider

_PAPER_SOURCE_ALIASES = {
    "arxiv": "arxiv",
    "semantic_scholar": "semantic_scholar",
    "semantic-scholar": "semantic_scholar",
    "semanticscholar": "semantic_scholar",
    "openalex": "openalex",
    "open_alex": "openalex",
    "open-alex": "openalex",
}


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

    provider = build_paper_provider(provider_name)

    # OpenAlex supports boolean search expressions; query once across all keywords.
    if isinstance(provider, OpenAlexPaperProvider):
        return provider.search_many(keywords, min(total_cap, max_per_keyword * len(keywords)))[:total_cap]

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

    return papers


def build_paper_provider(provider_name: str | None = None) -> PaperProvider:
    source_name = normalise_paper_source(provider_name or settings.paper_source)
    if source_name == "arxiv":
        return ArxivPaperProvider(max_history_days=settings.paper_max_history_days)
    if source_name == "semantic_scholar":
        return SemanticScholarPaperProvider(
            api_key=settings.semantic_scholar_api_key,
            api_url=settings.semantic_scholar_api_url,
            max_history_days=settings.paper_max_history_days,
        )
    if source_name == "openalex":
        return OpenAlexPaperProvider(
            api_key=settings.openalex_api_key,
            mailto=settings.openalex_mailto,
            relevance_mode=settings.openalex_relevance_mode,
            max_pages_per_window=settings.openalex_max_pages_per_window,
            max_history_days=settings.paper_max_history_days,
        )
    raise ValueError(f"Unsupported paper_source '{provider_name or settings.paper_source}'")


def normalise_paper_source(source_name: str) -> str:
    normalised = source_name.strip().lower().replace("-", "_")
    return _PAPER_SOURCE_ALIASES.get(normalised, normalised)


def query_arxiv(keyword: str, max_results: int) -> list[RawPaper]:
    return ArxivPaperProvider().search(keyword, max_results)


def query_semantic_scholar(keyword: str, max_results: int) -> list[RawPaper]:
    return SemanticScholarPaperProvider(
        api_key=settings.semantic_scholar_api_key,
        api_url=settings.semantic_scholar_api_url,
    ).search(keyword, max_results)


__all__ = [
    "ArxivPaperProvider",
    "OpenAlexPaperProvider",
    "PaperProvider",
    "RawPaper",
    "SemanticScholarPaperProvider",
    "build_openalex_search_query",
    "build_paper_provider",
    "fetch_papers",
    "is_keyword_relevant_openalex_result",
    "match_keywords_openalex_result",
    "normalise_paper_source",
    "query_arxiv",
    "query_semantic_scholar",
    "reconstruct_openalex_abstract",
]