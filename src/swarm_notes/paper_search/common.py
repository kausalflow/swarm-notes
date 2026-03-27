from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any, Mapping


_ATOM_NS = "http://www.w3.org/2005/Atom"
_ARXIV_NS = "http://arxiv.org/schemas/atom"
_TRANSIENT_HTTP_STATUS_CODES = frozenset({429, 500, 502, 503, 504})
_ARXIV_ID_IN_URL_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/([^/?#]+)")


def collapse_whitespace(text: str) -> str:
    return " ".join(text.split())


def text(element: ET.Element, tag: str) -> str | None:
    child = element.find(tag)
    return child.text if child is not None else None


def normalise_arxiv_id(value: str) -> str | None:
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


def extract_arxiv_id_from_url(url: str) -> str | None:
    match = _ARXIV_ID_IN_URL_RE.search(url)
    if not match:
        return None
    return normalise_arxiv_id(match.group(1))


def extract_arxiv_id_from_doi(doi: str) -> str | None:
    lower_doi = doi.strip().lower()
    if "arxiv." not in lower_doi:
        return None
    arxiv_part = doi.strip().rsplit("arXiv.", 1)[-1].rsplit("arxiv.", 1)[-1]
    return normalise_arxiv_id(arxiv_part)


def extract_nested_url(value: Any) -> str | None:
    if isinstance(value, Mapping):
        nested_url = value.get("url")
        if isinstance(nested_url, str):
            return nested_url
        landing_page_url = value.get("landing_page_url")
        if isinstance(landing_page_url, str):
            return landing_page_url
    return None


def extract_nested_pdf_url(value: Any) -> str | None:
    if isinstance(value, Mapping):
        nested_pdf_url = value.get("pdf_url")
        if isinstance(nested_pdf_url, str):
            return nested_pdf_url
    return None


def normalise_publication_date(publication_date: Any, year: Any) -> str:
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
