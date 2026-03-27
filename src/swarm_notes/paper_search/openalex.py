from __future__ import annotations

import logging
import re
import time
from datetime import datetime, timedelta, timezone
from typing import Any, Mapping

import requests

from swarm_notes.paper_search.base import RawPaper
from swarm_notes.paper_search.common import (
    _TRANSIENT_HTTP_STATUS_CODES,
    collapse_whitespace,
    extract_arxiv_id_from_doi,
    extract_arxiv_id_from_url,
    extract_nested_pdf_url,
    extract_nested_url,
    normalise_arxiv_id,
    normalise_publication_date,
)

logger = logging.getLogger(__name__)

_OPENALEX_API_BASE = "https://api.openalex.org/works"
_OPENALEX_QUERY_TIMEOUT_SECONDS = 30
_OPENALEX_RETRY_DELAYS_SECONDS = (2.0, 5.0)
_OPENALEX_FALLBACK_RECENT_DAYS = (7, 30, 90, 365)
_OPENALEX_MAX_PAGES_PER_WINDOW = 5
_OPENALEX_SELECT_FIELDS = (
    "id,display_name,abstract_inverted_index,authorships,publication_date,ids,"
    "best_oa_location,primary_location,locations"
)


class OpenAlexPaperProvider:
    """Fetch papers from the OpenAlex API."""

    def __init__(
        self,
        *,
        api_key: str = "",
        api_url: str = _OPENALEX_API_BASE,
        mailto: str = "",
        relevance_mode: str = "phrase",
        max_pages_per_window: int = _OPENALEX_MAX_PAGES_PER_WINDOW,
        max_history_days: int = 365,
        session: requests.Session | None = None,
    ) -> None:
        self._api_key = api_key
        self._api_url = api_url
        self._mailto = mailto
        self._relevance_mode = relevance_mode
        self._max_pages_per_window = max(1, max_pages_per_window)
        self._max_history_days = max(1, max_history_days)
        self._session = session or requests.Session()

    def search(self, keyword: str, max_results: int) -> list[RawPaper]:
        return self.search_many([keyword], max_results)

    def search_many(self, keywords: list[str], max_results: int) -> list[RawPaper]:
        """Search OpenAlex once using a combined keyword Boolean expression."""
        if not keywords:
            return []

        combined_search = build_openalex_search_query(keywords)
        collected: dict[str, RawPaper] = {}

        for recent_days in self._recent_windows():
            batch = self._search_with_recent_window(
                combined_search,
                keywords,
                max_results,
                recent_days,
            )
            for paper in batch:
                collected.setdefault(paper.arxiv_id, paper)

            if len(collected) >= max_results:
                break

            if collected:
                logger.info(
                    "OpenAlex: found %d ArXiv-backed paper(s) for query '%s' in the last %d day(s); widening window for more",
                    len(collected),
                    combined_search,
                    recent_days,
                )

        return list(collected.values())[:max_results]

    def _recent_windows(self) -> list[int]:
        windows: list[int] = [days for days in _OPENALEX_FALLBACK_RECENT_DAYS if days <= self._max_history_days]
        if self._max_history_days not in windows:
            windows.append(self._max_history_days)
        return sorted(set(windows))

    def _search_with_recent_window(
        self,
        query: str,
        keywords: list[str],
        max_results: int,
        recent_days: int,
    ) -> list[RawPaper]:
        today = datetime.now(tz=timezone.utc).date()
        cutoff = today - timedelta(days=recent_days)
        per_page = min(200, max(max_results * 20, 50))
        params_base: dict[str, str] = {
            "search": query,
            "per_page": str(per_page),
            "select": _OPENALEX_SELECT_FIELDS,
            "filter": (
                f"from_publication_date:{cutoff},"
                f"to_publication_date:{today},"
                "has_abstract:true,type:article|preprint"
            ),
        }
        if self._api_key:
            params_base["api_key"] = self._api_key
        if self._mailto:
            params_base["mailto"] = self._mailto

        collected: dict[str, RawPaper] = {}
        for page in range(1, self._max_pages_per_window + 1):
            params = dict(params_base)
            params["page"] = str(page)

            payload = self._fetch_with_retries(params, query, recent_days, page)
            if payload is None:
                break

            batch = self._parse_search_response(payload, keywords, oldest_allowed_date=cutoff)
            for paper in batch:
                collected.setdefault(paper.arxiv_id, paper)
                if len(collected) >= max_results:
                    break
            if len(collected) >= max_results:
                break

            results = payload.get("results", [])
            if not isinstance(results, list) or not results:
                break

            meta = payload.get("meta")
            if isinstance(meta, Mapping):
                total_count = meta.get("count")
                if isinstance(total_count, int) and page * per_page >= total_count:
                    break

        return list(collected.values())

    def _fetch_with_retries(
        self,
        params: dict[str, str],
        query: str,
        recent_days: int,
        page: int,
    ) -> Mapping[str, Any] | None:
        max_attempts = len(_OPENALEX_RETRY_DELAYS_SECONDS) + 1
        for attempt in range(1, max_attempts + 1):
            try:
                prepared_url = requests.Request("GET", self._api_url, params=params).prepare().url
                logger.debug(
                    "OpenAlex API call (query='%s', window_days=%d, page=%d, attempt=%d/%d): %s",
                    query,
                    recent_days,
                    page,
                    attempt,
                    max_attempts,
                    prepared_url,
                )
                response = self._session.get(
                    self._api_url,
                    params=params,
                    timeout=_OPENALEX_QUERY_TIMEOUT_SECONDS,
                )
                response.raise_for_status()
                payload = response.json()
                return payload if isinstance(payload, Mapping) else None
            except requests.RequestException as exc:
                if attempt == max_attempts or not self._is_retryable_error(exc):
                    logger.error(
                        "Failed to query OpenAlex for '%s' (last %d day window, page %d): %s",
                        query,
                        recent_days,
                        page,
                        exc,
                    )
                    return None

                delay = self._get_retry_delay(exc, attempt)
                logger.warning(
                    "Transient OpenAlex query failure for '%s' (last %d day window, page %d) on attempt %d/%d: %s. Retrying in %.0f second(s).",
                    query,
                    recent_days,
                    page,
                    attempt,
                    max_attempts,
                    exc,
                    delay,
                )
                time.sleep(delay)

        return None

    def _is_retryable_error(self, exc: requests.RequestException) -> bool:
        if isinstance(exc, requests.Timeout):
            return True
        response = exc.response
        return response is not None and response.status_code in _TRANSIENT_HTTP_STATUS_CODES

    def _get_retry_delay(self, exc: requests.RequestException, attempt: int) -> float:
        default_delay = _OPENALEX_RETRY_DELAYS_SECONDS[attempt - 1]
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

    def _parse_search_response(
        self,
        payload: Mapping[str, Any],
        keywords: list[str],
        *,
        oldest_allowed_date,
    ) -> list[RawPaper]:
        papers: list[RawPaper] = []
        today = datetime.now(tz=timezone.utc).date()
        for item in payload.get("results", []):
            if not isinstance(item, Mapping):
                continue

            arxiv_id = extract_openalex_arxiv_id(item)
            if not arxiv_id:
                logger.debug(
                    "OpenAlex result '%s' has no ArXiv identifier; skipping",
                    item.get("id", "unknown"),
                )
                continue

            abstract = reconstruct_openalex_abstract(item.get("abstract_inverted_index"))
            title = collapse_whitespace(item.get("display_name") or "Untitled")
            matched_keywords = match_keywords_openalex_result(
                keywords,
                title,
                abstract,
                self._relevance_mode,
            )
            if not matched_keywords:
                continue

            published = normalise_publication_date(item.get("publication_date"), None)
            try:
                published_date = datetime.strptime(published, "%Y-%m-%d").date()
                if published_date > today:
                    logger.debug(
                        "OpenAlex result %s has future publication_date %s; skipping",
                        arxiv_id,
                        published,
                    )
                    continue
                if published_date < oldest_allowed_date:
                    logger.debug(
                        "OpenAlex result %s published %s is older than %s; skipping",
                        arxiv_id,
                        published,
                        oldest_allowed_date,
                    )
                    continue
            except ValueError:
                pass

            authors = [
                authorship["author"]["display_name"]
                for authorship in item.get("authorships", [])
                if isinstance(authorship, Mapping)
                and isinstance(authorship.get("author"), Mapping)
                and authorship["author"].get("display_name")
            ]

            papers.append(
                RawPaper(
                    arxiv_id=arxiv_id,
                    title=title,
                    abstract=collapse_whitespace(abstract),
                    authors=authors,
                    published=published,
                    url=f"https://arxiv.org/abs/{arxiv_id}",
                    primary_category="",
                    source="openalex",
                    keywords_matched=matched_keywords,
                )
            )

        return papers


def extract_openalex_arxiv_id(item: Mapping[str, Any]) -> str | None:
    ids = item.get("ids")
    if isinstance(ids, Mapping):
        arxiv_value = ids.get("arxiv")
        if isinstance(arxiv_value, str):
            arxiv_id = extract_arxiv_id_from_url(arxiv_value) or normalise_arxiv_id(arxiv_value)
            if arxiv_id:
                return arxiv_id

        doi_value = ids.get("doi")
        if isinstance(doi_value, str):
            arxiv_id = extract_arxiv_id_from_doi(doi_value)
            if arxiv_id:
                return arxiv_id

    best_oa_location = item.get("best_oa_location")
    for candidate in (
        extract_nested_url(best_oa_location),
        extract_nested_pdf_url(best_oa_location),
        extract_nested_url(item.get("primary_location")),
        extract_nested_pdf_url(item.get("primary_location")),
    ):
        if isinstance(candidate, str):
            arxiv_id = extract_arxiv_id_from_url(candidate)
            if arxiv_id:
                return arxiv_id

    locations = item.get("locations")
    if isinstance(locations, list):
        for location in locations:
            if not isinstance(location, Mapping):
                continue
            for candidate in (extract_nested_url(location), extract_nested_pdf_url(location)):
                if isinstance(candidate, str):
                    arxiv_id = extract_arxiv_id_from_url(candidate)
                    if arxiv_id:
                        return arxiv_id

    return None


def reconstruct_openalex_abstract(inverted_index: Mapping[str, list[int]] | None) -> str:
    if not inverted_index:
        return ""
    max_pos = max(pos for positions in inverted_index.values() for pos in positions)
    words: list[str] = [""] * (max_pos + 1)
    for word, positions in inverted_index.items():
        for pos in positions:
            if 0 <= pos <= max_pos:
                words[pos] = word
    return " ".join(w for w in words if w)


def is_keyword_relevant_openalex_result(
    keyword: str,
    title: str,
    abstract: str,
    relevance_mode: str = "phrase",
) -> bool:
    text = f"{title} {abstract}".lower()
    normalized = " ".join(keyword.lower().split())
    normalized_text = " ".join(re.split(r"\W+", text))
    if not normalized:
        return True

    if normalized in text or normalized in normalized_text:
        return True

    if relevance_mode == "phrase":
        return False

    tokens = [token for token in re.split(r"\W+", normalized) if len(token) >= 3]
    if not tokens:
        return True

    return all(token in text for token in tokens)


def match_keywords_openalex_result(
    keywords: list[str],
    title: str,
    abstract: str,
    relevance_mode: str = "phrase",
) -> list[str]:
    matched: list[str] = []
    for keyword in keywords:
        if is_keyword_relevant_openalex_result(keyword, title, abstract, relevance_mode):
            matched.append(keyword)
    return matched


def build_openalex_search_query(keywords: list[str]) -> str:
    """Build a single OpenAlex boolean search expression from keywords.

    Example output: ("time series" OR forecasting OR timeseries)
    """
    cleaned = [kw.strip() for kw in keywords if kw and kw.strip()]
    if not cleaned:
        return ""

    parts: list[str] = []
    for keyword in cleaned:
        escaped = keyword.replace('"', '\\"')
        if any(ch.isspace() for ch in escaped):
            parts.append(f'"{escaped}"')
        else:
            parts.append(escaped)

    if len(parts) == 1:
        return parts[0]
    return f"({' OR '.join(parts)})"
