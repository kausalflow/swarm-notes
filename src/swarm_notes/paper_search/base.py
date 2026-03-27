from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class RawPaper:
    """Raw data fetched directly from a paper provider."""

    arxiv_id: str
    title: str
    abstract: str
    authors: list[str]
    published: str
    url: str
    primary_category: str
    source: str = "arxiv"
    keywords_matched: list[str] = field(default_factory=list)


class PaperProvider(Protocol):
    """Abstract paper search provider."""

    def search(self, keyword: str, max_results: int) -> list[RawPaper]:
        """Return up to ``max_results`` papers for a keyword."""

    def search_many(self, keywords: list[str], max_results: int) -> list[RawPaper]:
        """Return up to ``max_results`` papers for many keywords."""
