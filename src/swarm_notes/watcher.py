"""Watcher: queries a configured paper provider for recent papers."""

from __future__ import annotations

import logging
import re
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Mapping, Protocol

import requests

from swarm_notes.config import settings

logger = logging.getLogger(__name__)

_ATOM_NS = "http://www.w3.org/2005/Atom"
_ARXIV_API_BASE = "https://export.arxiv.org/api/query"
_ARXIV_NS = "http://arxiv.org/schemas/atom"
_ARXIV_QUERY_TIMEOUT_SECONDS = 30
_ARXIV_RETRY_DELAYS_SECONDS = (2.0, 5.0)
_ARXIV_MIN_INTERVAL_SECONDS = 3.0
_ARXIV_USER_AGENT = "swarm-notes/0.1 (+https://github.com/kausalflow/swarm-notes)"

_SEMANTIC_SCHOLAR_FIELDS = (
    "title,abstract,authors,publicationDate,year,url,externalIds,openAccessPdf"
)
_SEMANTIC_SCHOLAR_QUERY_TIMEOUT_SECONDS = 30
_SEMANTIC_SCHOLAR_RETRY_DELAYS_SECONDS = (2.0, 5.0)

_TRANSIENT_HTTP_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
_PAPER_SOURCE_ALIASES = {
    "arxiv": "arxiv",
    "semantic_scholar": "semantic_scholar",
    "semantic-scholar": "semantic_scholar",
    "semanticscholar": "semantic_scholar",
}
_ARXIV_ID_IN_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([^/?#]+)")


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


class ArxivPaperProvider:
    """Fetch papers from the ArXiv Atom API."""

    def __init__(self) -> None:
        self._last_request_started_at: float | None = None

    def search(self, keyword: str, max_results: int) -> list[RawPaper]:
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
                self._respect_rate_limit()
                with urllib.request.urlopen(request, timeout=_ARXIV_QUERY_TIMEOUT_SECONDS) as response:  # noqa: S310
                    xml_bytes = response.read()
                return _parse_arxiv_atom_feed(xml_bytes, keyword)
            except Exception as exc:
                if attempt == max_attempts or not self._is_retryable_error(exc):
                    logger.error("Failed to query ArXiv for '%s': %s", keyword, exc)
                    return []

                delay = self._get_retry_delay(exc, attempt)
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

    def _respect_rate_limit(self) -> None:
        now = time.monotonic()
        if self._last_request_started_at is not None:
            elapsed = now - self._last_request_started_at
            remaining = _ARXIV_MIN_INTERVAL_SECONDS - elapsed
            if remaining > 0:
                logger.debug("Waiting %.2f second(s) before the next ArXiv request", remaining)
                time.sleep(remaining)
                now = time.monotonic()

        self._last_request_started_at = now

    def _is_retryable_error(self, exc: Exception) -> bool:
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

    def _get_retry_delay(self, exc: Exception, attempt: int) -> float:
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


class SemanticScholarPaperProvider:
    """Fetch ArXiv-backed papers via the Semantic Scholar Graph API."""

    def __init__(
        self,
        *,
        api_key: str,
        api_url: str,
        session: requests.Session | None = None,
    ) -> None:
        self._api_key = api_key
        self._api_url = api_url
        self._session = session or requests.Session()

    def search(self, keyword: str, max_results: int) -> list[RawPaper]:
        params = {
            "query": keyword,
            "limit": str(max_results),
            "fields": _SEMANTIC_SCHOLAR_FIELDS,
        }
        headers = {"User-Agent": _ARXIV_USER_AGENT}
        if self._api_key:
            headers["x-api-key"] = self._api_key

        max_attempts = len(_SEMANTIC_SCHOLAR_RETRY_DELAYS_SECONDS) + 1
        for attempt in range(1, max_attempts + 1):
            try:
                response = self._session.get(
                    self._api_url,
                    params=params,
                    headers=headers,
                    timeout=_SEMANTIC_SCHOLAR_QUERY_TIMEOUT_SECONDS,
                )
                response.raise_for_status()
                return self._parse_search_response(response.json(), keyword)
            except requests.RequestException as exc:
                if attempt == max_attempts or not self._is_retryable_error(exc):
                    logger.error("Failed to query Semantic Scholar for '%s': %s", keyword, exc)
                    return []

                delay = self._get_retry_delay(exc, attempt)
                logger.warning(
                    "Transient Semantic Scholar query failure for '%s' on attempt %d/%d: %s. Retrying in %.0f second(s).",
                    keyword,
                    attempt,
                    max_attempts,
                    exc,
                    delay,
                )
                time.sleep(delay)

        return []

    def _is_retryable_error(self, exc: requests.RequestException) -> bool:
        if isinstance(exc, requests.Timeout):
            return True

        response = exc.response
        return response is not None and response.status_code in _TRANSIENT_HTTP_STATUS_CODES

    def _get_retry_delay(self, exc: requests.RequestException, attempt: int) -> float:
        default_delay = _SEMANTIC_SCHOLAR_RETRY_DELAYS_SECONDS[attempt - 1]
        response = exc.response
        if response is None or response.status_code != 429:
            return default_delay

        retry_after = response.headers.get("Retry-After")
        if retry_after is None:
            return default_delay

        try:
            return max(default_delay, float(retry_after))
        except ValueError:
            return default_delay

    def _parse_search_response(self, payload: Mapping[str, Any], keyword: str) -> list[RawPaper]:
        papers: list[RawPaper] = []
        for item in payload.get("data", []):
            if not isinstance(item, Mapping):
                continue

            arxiv_id = _extract_semantic_scholar_arxiv_id(item)
            if not arxiv_id:
                logger.debug(
                    "Semantic Scholar result '%s' has no ArXiv identifier; skipping",
                    item.get("paperId", "unknown"),
                )
                continue

            authors = [
                author.get("name", "")
                for author in item.get("authors", [])
                if isinstance(author, Mapping) and author.get("name")
            ]

            papers.append(
                RawPaper(
                    arxiv_id=arxiv_id,
                    title=_collapse_whitespace(item.get("title") or "Untitled"),
                    abstract=_collapse_whitespace(item.get("abstract") or ""),
                    authors=authors,
                    published=_normalise_publication_date(
                        item.get("publicationDate"),
                        item.get("year"),
                    ),
                    url=f"https://arxiv.org/abs/{arxiv_id}",
                    primary_category="",
                    source="semantic_scholar",
                    keywords_matched=[keyword],
                )
            )

        return papers


def fetch_papers(
    keywords: list[str] | None = None,
    max_per_keyword: int | None = None,
    total_cap: int | None = None,
    provider_name: str | None = None,
) -> list[RawPaper]:
    """Fetch papers from the configured provider for the given keywords."""
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


def _build_paper_provider(provider_name: str | None = None) -> PaperProvider:
    source_name = _normalise_paper_source(provider_name or settings.paper_source)
    if source_name == "arxiv":
        return ArxivPaperProvider()
    if source_name == "semantic_scholar":
        return SemanticScholarPaperProvider(
            api_key=settings.semantic_scholar_api_key,
            api_url=settings.semantic_scholar_api_url,
        )
    raise ValueError(f"Unsupported paper_source '{provider_name or settings.paper_source}'")


def _normalise_paper_source(source_name: str) -> str:
    normalised = source_name.strip().lower().replace("-", "_")
    return _PAPER_SOURCE_ALIASES.get(normalised, normalised)


def _query_arxiv(keyword: str, max_results: int) -> list[RawPaper]:
    return ArxivPaperProvider().search(keyword, max_results)


def _query_semantic_scholar(keyword: str, max_results: int) -> list[RawPaper]:
    return SemanticScholarPaperProvider(
        api_key=settings.semantic_scholar_api_key,
        api_url=settings.semantic_scholar_api_url,
    ).search(keyword, max_results)


def _parse_arxiv_atom_feed(xml_bytes: bytes, keyword: str) -> list[RawPaper]:
    try:
        root = ET.fromstring(xml_bytes)  # noqa: S314
    except ET.ParseError as exc:
        logger.error("Failed to parse ArXiv Atom feed: %s", exc)
        return []

    papers: list[RawPaper] = []
    for entry in root.findall(f"{{{_ATOM_NS}}}entry"):
        arxiv_id = _text(entry, f"{{{_ATOM_NS}}}id") or ""
        arxiv_id = _normalise_arxiv_id(arxiv_id.rstrip("/").split("/")[-1]) or ""

        primary_category_el = entry.find(f"{{{_ARXIV_NS}}}primary_category")

        papers.append(
            RawPaper(
                arxiv_id=arxiv_id,
                title=_collapse_whitespace(_text(entry, f"{{{_ATOM_NS}}}title") or "Untitled"),
                abstract=_collapse_whitespace(_text(entry, f"{{{_ATOM_NS}}}summary") or ""),
                authors=[
                    _text(author, f"{{{_ATOM_NS}}}name") or ""
                    for author in entry.findall(f"{{{_ATOM_NS}}}author")
                ],
                published=_normalise_publication_date(_text(entry, f"{{{_ATOM_NS}}}published"), None),
                url=f"https://arxiv.org/abs/{arxiv_id}",
                primary_category=primary_category_el.get("term", "") if primary_category_el is not None else "",
                source="arxiv",
                keywords_matched=[keyword],
            )
        )

    return papers


def _extract_semantic_scholar_arxiv_id(paper: Mapping[str, Any]) -> str | None:
    external_ids = paper.get("externalIds")
    if isinstance(external_ids, Mapping):
        for key in ("ArXiv", "ARXIV"):
            value = external_ids.get(key)
            if isinstance(value, str):
                arxiv_id = _normalise_arxiv_id(value)
                if arxiv_id:
                    return arxiv_id

    for candidate in (paper.get("url"), _extract_nested_url(paper.get("openAccessPdf"))):
        if isinstance(candidate, str):
            arxiv_id = _extract_arxiv_id_from_url(candidate)
            if arxiv_id:
                return arxiv_id

    return None


def _extract_nested_url(value: Any) -> str | None:
    if isinstance(value, Mapping):
        nested_url = value.get("url")
        if isinstance(nested_url, str):
            return nested_url
    return None


def _extract_arxiv_id_from_url(url: str) -> str | None:
    match = _ARXIV_ID_IN_URL_RE.search(url)
    if not match:
        return None
    return _normalise_arxiv_id(match.group(1))


def _normalise_arxiv_id(value: str) -> str | None:
    candidate = value.strip()
    if not candidate:
        return None
    if candidate.upper().startswith("ARXIV:"):
        candidate = candidate.split(":", 1)[1]
    if candidate.endswith(".pdf"):
        candidate = candidate[:-4]
    if "v" in candidate:
        candidate = candidate.rsplit("v", 1)[0]
    return candidate or None


def _normalise_publication_date(publication_date: Any, year: Any) -> str:
    if isinstance(publication_date, str) and publication_date:
        for fmt, output in (
            ("%Y-%m-%d", "%Y-%m-%d"),
            ("%Y-%m", "%Y-%m-01"),
            ("%Y", "%Y-01-01"),
        ):
            try:
                return datetime.strptime(publication_date, fmt).strftime(output)
            except ValueError:
                continue
        try:
            return datetime.fromisoformat(publication_date.replace("Z", "+00:00")).strftime("%Y-%m-%d")
        except ValueError:
            pass

    if isinstance(year, int):
        return f"{year:04d}-01-01"
    if isinstance(year, str) and year.isdigit():
        return f"{int(year):04d}-01-01"
    return datetime.now(tz=timezone.utc).strftime("%Y-%m-%d")


def _collapse_whitespace(text: str) -> str:
    return " ".join(text.split())


def _text(element: ET.Element, tag: str) -> str | None:
    child = element.find(tag)
    return child.text if child is not None else None
