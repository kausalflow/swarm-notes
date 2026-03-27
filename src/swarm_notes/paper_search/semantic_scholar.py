from __future__ import annotations

import logging
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Mapping

import requests

from swarm_notes.paper_search.base import RawPaper
from swarm_notes.paper_search.common import (
    _TRANSIENT_HTTP_STATUS_CODES,
    collapse_whitespace,
    extract_arxiv_id_from_url,
    extract_nested_url,
    normalise_arxiv_id,
    normalise_publication_date,
)

logger = logging.getLogger(__name__)

_SEMANTIC_SCHOLAR_FIELDS = "title,abstract,authors,publicationDate,year,url,externalIds"
_SEMANTIC_SCHOLAR_QUERY_TIMEOUT_SECONDS = 30
_SEMANTIC_SCHOLAR_RETRY_DELAYS_SECONDS = (2.0, 5.0)
_SEMANTIC_SCHOLAR_USER_AGENT = "swarm-notes/0.1 (+https://github.com/kausalflow/swarm-notes)"


class SemanticScholarPaperProvider:
    """Fetch ArXiv-backed papers via the Semantic Scholar Graph API."""

    def __init__(
        self,
        *,
        api_key: str,
        api_url: str,
        max_history_days: int = 365,
        session: requests.Session | None = None,
    ) -> None:
        self._api_key = api_key
        self._api_url = api_url
        self._max_history_days = max(1, max_history_days)
        self._session = session or requests.Session()

    def search(self, keyword: str, max_results: int) -> list[RawPaper]:
        params = {
            "query": keyword,
            "limit": str(max_results),
            "fields": _SEMANTIC_SCHOLAR_FIELDS,
        }
        headers = {"User-Agent": _SEMANTIC_SCHOLAR_USER_AGENT}
        if self._api_key:
            headers["x-api-key"] = self._api_key
            logger.debug(
                "Semantic Scholar: using API key (***%s)",
                self._api_key[-6:] if len(self._api_key) > 6 else "...",
            )
        else:
            logger.warning(
                "Semantic Scholar: no API key configured. This may result in 403 Forbidden errors. "
                "Set SEMANTIC_SCHOLAR_API_KEY in your .env or config."
            )

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
        cutoff_date = (datetime.now(tz=timezone.utc) - timedelta(days=self._max_history_days)).date()

        for item in payload.get("data", []):
            if not isinstance(item, Mapping):
                continue

            arxiv_id = extract_semantic_scholar_arxiv_id(item)
            if not arxiv_id:
                logger.debug(
                    "Semantic Scholar result '%s' has no ArXiv identifier; skipping",
                    item.get("paperId", "unknown"),
                )
                continue

            pub_date_str = item.get("publicationDate")
            if pub_date_str:
                try:
                    pub_date = datetime.strptime(pub_date_str, "%Y-%m-%d").date()
                    if pub_date < cutoff_date:
                        logger.debug(
                            "Semantic Scholar result %s published %s is older than %s; skipping",
                            arxiv_id,
                            pub_date_str,
                            cutoff_date,
                        )
                        continue
                except (ValueError, TypeError):
                    pass

            authors = [
                author.get("name", "")
                for author in item.get("authors", [])
                if isinstance(author, Mapping) and author.get("name")
            ]

            papers.append(
                RawPaper(
                    arxiv_id=arxiv_id,
                    title=collapse_whitespace(item.get("title") or "Untitled"),
                    abstract=collapse_whitespace(item.get("abstract") or ""),
                    authors=authors,
                    published=normalise_publication_date(item.get("publicationDate"), item.get("year")),
                    url=f"https://arxiv.org/abs/{arxiv_id}",
                    primary_category="",
                    source="semantic_scholar",
                    keywords_matched=[keyword],
                )
            )

        return papers


def extract_semantic_scholar_arxiv_id(paper: Mapping[str, Any]) -> str | None:
    external_ids = paper.get("externalIds")
    if isinstance(external_ids, Mapping):
        for key in ("ArXiv", "ARXIV"):
            value = external_ids.get(key)
            if isinstance(value, str):
                arxiv_id = normalise_arxiv_id(value)
                if arxiv_id:
                    return arxiv_id

    for candidate in (paper.get("url"), extract_nested_url(paper.get("openAccessPdf"))):
        if isinstance(candidate, str):
            arxiv_id = extract_arxiv_id_from_url(candidate)
            if arxiv_id:
                return arxiv_id

    return None
