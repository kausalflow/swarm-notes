"""Watcher: queries the ArXiv API for recent papers matching configured keywords."""

from __future__ import annotations

import logging
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone

from src.config import (
    ARXIV_KEYWORDS,
    ARXIV_MAX_RESULTS_PER_KEYWORD,
    ARXIV_TOTAL_CAP,
)

logger = logging.getLogger(__name__)

_ARXIV_API_BASE = "https://export.arxiv.org/api/query"
_ATOM_NS = "http://www.w3.org/2005/Atom"
_ARXIV_NS = "http://arxiv.org/schemas/atom"


@dataclass
class RawPaper:
    """Raw data fetched directly from the ArXiv API."""

    arxiv_id: str
    title: str
    abstract: str
    authors: list[str]
    published: str          # ISO-8601 date string (YYYY-MM-DD)
    url: str
    primary_category: str
    keywords_matched: list[str] = field(default_factory=list)


def fetch_papers(
    keywords: list[str] | None = None,
    max_per_keyword: int | None = None,
    total_cap: int | None = None,
) -> list[RawPaper]:
    """Fetch papers from ArXiv for the given *keywords*.

    Parameters
    ----------
    keywords:
        Search terms.  Defaults to ``ARXIV_KEYWORDS`` from config.
    max_per_keyword:
        Maximum results per keyword query.
    total_cap:
        Hard cap on the total number of unique papers returned.

    Returns
    -------
    list[RawPaper]
        Deduplicated list of papers ordered by relevance/recency.
    """
    if keywords is None:
        keywords = ARXIV_KEYWORDS
    if max_per_keyword is None:
        max_per_keyword = ARXIV_MAX_RESULTS_PER_KEYWORD
    if total_cap is None:
        total_cap = ARXIV_TOTAL_CAP

    seen_ids: set[str] = set()
    papers: list[RawPaper] = []

    for keyword in keywords:
        if len(papers) >= total_cap:
            break

        remaining = total_cap - len(papers)
        batch = _query_arxiv(keyword, min(max_per_keyword, remaining))

        for paper in batch:
            if paper.arxiv_id not in seen_ids:
                seen_ids.add(paper.arxiv_id)
                papers.append(paper)
            else:
                # Annotate existing paper with additional matched keyword
                for existing in papers:
                    if existing.arxiv_id == paper.arxiv_id:
                        if keyword not in existing.keywords_matched:
                            existing.keywords_matched.append(keyword)
                        break

        logger.info("Keyword '%s': fetched %d paper(s)", keyword, len(batch))

    logger.info("Watcher: %d unique paper(s) collected in total", len(papers))
    return papers


def _query_arxiv(keyword: str, max_results: int) -> list[RawPaper]:
    """Execute a single ArXiv API query and return parsed ``RawPaper`` objects."""
    params = urllib.parse.urlencode(
        {
            "search_query": f"all:{keyword}",
            "start": 0,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    url = f"{_ARXIV_API_BASE}?{params}"
    logger.debug("ArXiv query: %s", url)

    try:
        with urllib.request.urlopen(url, timeout=30) as response:  # noqa: S310
            xml_bytes = response.read()
    except Exception as exc:
        logger.error("Failed to query ArXiv for '%s': %s", keyword, exc)
        return []

    return _parse_atom_feed(xml_bytes, keyword)


def _parse_atom_feed(xml_bytes: bytes, keyword: str) -> list[RawPaper]:
    """Parse an ArXiv Atom feed and return a list of ``RawPaper`` objects."""
    try:
        root = ET.fromstring(xml_bytes)  # noqa: S314
    except ET.ParseError as exc:
        logger.error("Failed to parse ArXiv Atom feed: %s", exc)
        return []

    papers: list[RawPaper] = []

    for entry in root.findall(f"{{{_ATOM_NS}}}entry"):
        arxiv_id = _text(entry, f"{{{_ATOM_NS}}}id") or ""
        # Normalise ID to short form: "2301.12345v1" → "2301.12345"
        arxiv_id = arxiv_id.rstrip("/").split("/")[-1]
        if "v" in arxiv_id:
            arxiv_id = arxiv_id.rsplit("v", 1)[0]

        title = _text(entry, f"{{{_ATOM_NS}}}title") or "Untitled"
        title = " ".join(title.split())  # Collapse whitespace

        abstract = _text(entry, f"{{{_ATOM_NS}}}summary") or ""
        abstract = " ".join(abstract.split())

        published_raw = _text(entry, f"{{{_ATOM_NS}}}published") or ""
        try:
            published = datetime.fromisoformat(
                published_raw.replace("Z", "+00:00")
            ).strftime("%Y-%m-%d")
        except ValueError:
            published = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")

        authors = [
            _text(author, f"{{{_ATOM_NS}}}name") or ""
            for author in entry.findall(f"{{{_ATOM_NS}}}author")
        ]

        primary_category_el = entry.find(f"{{{_ARXIV_NS}}}primary_category")
        primary_category = (
            primary_category_el.get("term", "") if primary_category_el is not None else ""
        )

        # Build the canonical PDF/abstract URL
        paper_url = f"https://arxiv.org/abs/{arxiv_id}"

        papers.append(
            RawPaper(
                arxiv_id=arxiv_id,
                title=title,
                abstract=abstract,
                authors=authors,
                published=published,
                url=paper_url,
                primary_category=primary_category,
                keywords_matched=[keyword],
            )
        )

    return papers


def _text(element: ET.Element, tag: str) -> str | None:
    """Return the text content of a child element, or *None* if not found."""
    child = element.find(tag)
    return child.text if child is not None else None
