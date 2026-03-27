from __future__ import annotations

import logging
import socket
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

from swarm_notes.paper_search.base import RawPaper
from swarm_notes.paper_search.common import (
    _ARXIV_NS,
    _ATOM_NS,
    _TRANSIENT_HTTP_STATUS_CODES,
    collapse_whitespace,
    normalise_arxiv_id,
    normalise_publication_date,
    text,
)

logger = logging.getLogger(__name__)

_ARXIV_API_BASE = "https://export.arxiv.org/api/query"
_ARXIV_QUERY_TIMEOUT_SECONDS = 30
_ARXIV_RETRY_DELAYS_SECONDS = (2.0, 5.0)
_ARXIV_MIN_INTERVAL_SECONDS = 3.0
_ARXIV_USER_AGENT = "swarm-notes/0.1 (+https://github.com/kausalflow/swarm-notes)"


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
                return parse_arxiv_atom_feed(xml_bytes, keyword)
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


def parse_arxiv_atom_feed(xml_bytes: bytes, keyword: str) -> list[RawPaper]:
    try:
        root = ET.fromstring(xml_bytes)  # noqa: S314
    except ET.ParseError as exc:
        logger.error("Failed to parse ArXiv Atom feed: %s", exc)
        return []

    papers: list[RawPaper] = []
    for entry in root.findall(f"{{{_ATOM_NS}}}entry"):
        arxiv_id = text(entry, f"{{{_ATOM_NS}}}id") or ""
        arxiv_id = normalise_arxiv_id(arxiv_id.rstrip("/").split("/")[-1]) or ""

        primary_category_el = entry.find(f"{{{_ARXIV_NS}}}primary_category")

        papers.append(
            RawPaper(
                arxiv_id=arxiv_id,
                title=collapse_whitespace(text(entry, f"{{{_ATOM_NS}}}title") or "Untitled"),
                abstract=collapse_whitespace(text(entry, f"{{{_ATOM_NS}}}summary") or ""),
                authors=[
                    text(author, f"{{{_ATOM_NS}}}name") or ""
                    for author in entry.findall(f"{{{_ATOM_NS}}}author")
                ],
                published=normalise_publication_date(text(entry, f"{{{_ATOM_NS}}}published"), None),
                url=f"https://arxiv.org/abs/{arxiv_id}",
                primary_category=primary_category_el.get("term", "") if primary_category_el is not None else "",
                source="arxiv",
                keywords_matched=[keyword],
            )
        )

    return papers
