"""Watcher: queries the ArXiv API for recent papers matching configured keywords."""

from __future__ import annotations

import logging
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone

from swarm_notes.config import settings

logger = logging.getLogger(__name__)

_ARXIV_API_BASE = "https://export.arxiv.org/api/query"
_ATOM_NS = "http://www.w3.org/2005/Atom"
_ARXIV_NS = "http://arxiv.org/schemas/atom"
_ARXIV_QUERY_TIMEOUT_SECONDS = 30
_ARXIV_RETRY_DELAYS_SECONDS = (2.0, 5.0)
_ARXIV_MIN_INTERVAL_SECONDS = 3.0
_TRANSIENT_HTTP_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
_ARXIV_USER_AGENT = "swarm-notes/0.1 (+https://github.com/kausalflow/swarm-notes)"

_last_arxiv_request_started_at: float | None = None


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
        Search terms.  Defaults to ``settings.arxiv_keywords`` from config.
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
        keywords = settings.arxiv_keywords
    if max_per_keyword is None:
        max_per_keyword = settings.arxiv_max_results_per_keyword
    if total_cap is None:
        total_cap = settings.arxiv_total_cap

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
    request = urllib.request.Request(url, headers={"User-Agent": _ARXIV_USER_AGENT})

    max_attempts = len(_ARXIV_RETRY_DELAYS_SECONDS) + 1

    for attempt in range(1, max_attempts + 1):
        try:
            _respect_arxiv_rate_limit()
            with urllib.request.urlopen(request, timeout=_ARXIV_QUERY_TIMEOUT_SECONDS) as response:  # noqa: S310
                xml_bytes = response.read()
            return _parse_atom_feed(xml_bytes, keyword)
        except Exception as exc:
            if attempt == max_attempts or not _is_retryable_arxiv_error(exc):
                logger.error("Failed to query ArXiv for '%s': %s", keyword, exc)
                return []

            delay = _get_arxiv_retry_delay(exc, attempt)
            logger.warning(
                "Transient ArXiv query failure for '%s' on attempt %d/%d: %s. Retrying in %.0f second(s).",
                keyword,
                attempt,
                max_attempts,
                exc,
                delay,
            )
            time.sleep(delay)

    return []


def _respect_arxiv_rate_limit() -> None:
    """Sleep as needed so requests stay under ArXiv's rate limit guidance."""
    global _last_arxiv_request_started_at

    now = time.monotonic()
    if _last_arxiv_request_started_at is not None:
        elapsed = now - _last_arxiv_request_started_at
        remaining = _ARXIV_MIN_INTERVAL_SECONDS - elapsed
        if remaining > 0:
            logger.debug("Waiting %.2f second(s) before the next ArXiv request", remaining)
            time.sleep(remaining)
            now = time.monotonic()

    _last_arxiv_request_started_at = now


def _is_retryable_arxiv_error(exc: Exception) -> bool:
    """Return ``True`` when a query failed due to a transient network condition."""
    if isinstance(exc, (TimeoutError, socket.timeout)):
        return True

    if isinstance(exc, urllib.error.HTTPError):
        return exc.code in _TRANSIENT_HTTP_STATUS_CODES

    if isinstance(exc, urllib.error.URLError):
        reason = exc.reason
        if isinstance(reason, (TimeoutError, socket.timeout)):
            return True
        return isinstance(reason, str) and "timed out" in reason.lower()

    return False


def _get_arxiv_retry_delay(exc: Exception, attempt: int) -> float:
    """Return retry delay for transient ArXiv failures, honoring Retry-After when present."""
    default_delay = _ARXIV_RETRY_DELAYS_SECONDS[attempt - 1]
    if not isinstance(exc, urllib.error.HTTPError) or exc.code != 429:
        return default_delay

    retry_after = exc.headers.get("Retry-After") if exc.headers is not None else None
    if retry_after is None:
        return default_delay

    try:
        return max(default_delay, float(retry_after))
    except ValueError:
        return default_delay


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
