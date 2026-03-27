"""Tests for watcher.py."""

from email.message import Message
import urllib.error
from unittest.mock import MagicMock, patch

import pytest
import requests

from swarm_notes.watcher import (
    ArxivPaperProvider,
    OpenAlexPaperProvider,
    RawPaper,
    SemanticScholarPaperProvider,
    _build_openalex_search_query,
    _build_paper_provider,
    _is_keyword_relevant_openalex_result,
    _match_keywords_openalex_result,
    _query_arxiv,
    _reconstruct_openalex_abstract,
    fetch_papers,
)

MOCK_ATOM_XML = b'''<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom" xmlns:arxiv="http://arxiv.org/schemas/atom">
  <entry>
    <id>http://arxiv.org/abs/2301.12345v1</id>
    <title>Mock Paper Title</title>
    <summary>Mock paper abstract.</summary>
    <author><name>John Doe</name></author>
    <published>2023-01-01T12:00:00Z</published>
    <arxiv:primary_category term="cs.AI"/>
  </entry>
</feed>
'''

MOCK_SEMANTIC_SCHOLAR_JSON = {
    "total": 2,
    "offset": 0,
    "data": [
        {
            "paperId": "paper-1",
            "title": "Semantic Scholar Paper",
            "abstract": "Semantic Scholar abstract.",
            "authors": [{"name": "Jane Doe"}],
            "publicationDate": "2026-03-25",
            "year": 2026,
            "url": "https://www.semanticscholar.org/paper/paper-1",
            "externalIds": {"ArXiv": "2503.01234v2"},
            "openAccessPdf": {"url": "https://arxiv.org/pdf/2503.01234.pdf"},
        },
        {
            "paperId": "paper-2",
            "title": "No Arxiv ID",
            "abstract": "Should be skipped.",
            "authors": [{"name": "John Doe"}],
            "publicationDate": "2026-03-20",
            "year": 2026,
            "url": "https://www.semanticscholar.org/paper/paper-2",
            "externalIds": {"DOI": "10.1234/example"},
        },
    ],
}


MOCK_OPENALEX_JSON = {
    "meta": {"count": 2, "db_response_time_ms": 12, "page": 1, "per_page": 10},
    "results": [
        {
            "id": "https://openalex.org/W3001234567",
            "display_name": "OpenAlex Time Series ArXiv Paper",
            "abstract_inverted_index": {
                "Abstract": [0],
                "of": [1],
                "time": [2],
                "series": [3],
                "openalex": [4],
                "paper": [5],
            },
            "authorships": [
                {"author": {"display_name": "Alice Smith"}},
                {"author": {"display_name": "Bob Jones"}},
            ],
            "publication_date": "2026-03-25",
            "ids": {
                "openalex": "https://openalex.org/W3001234567",
                "arxiv": "https://arxiv.org/abs/2503.11111",
            },
        },
        {
            "id": "https://openalex.org/W3009999999",
            "display_name": "OpenAlex No-ArXiv Paper (should be skipped)",
            "abstract_inverted_index": {"Skip": [0], "me": [1]},
            "authorships": [{"author": {"display_name": "Carol White"}}],
            "publication_date": "2026-03-24",
            "ids": {
                "openalex": "https://openalex.org/W3009999999",
                "doi": "https://doi.org/10.1234/example",
            },
        },
    ],
}


@patch("urllib.request.urlopen")
def test_fetch_papers(mock_urlopen: MagicMock) -> None:
    """Test the fetch_papers function.

    Mocks urllib.request.urlopen to simulate an ArXiv API response
    and verifies that the paper is successfully parsed and returned.

    Args:
        mock_urlopen: The mock object for urllib.request.urlopen.
    """
    mock_response = MagicMock()
    mock_response.read.return_value = MOCK_ATOM_XML
    mock_response.__enter__.return_value = mock_response
    mock_urlopen.return_value = mock_response

    papers = fetch_papers(keywords=["test"], max_per_keyword=1, total_cap=1)

    assert len(papers) == 1
    assert papers[0].arxiv_id == "2301.12345"
    assert papers[0].title == "Mock Paper Title"
    assert papers[0].primary_category == "cs.AI"
    assert papers[0].authors == ["John Doe"]


def test_build_paper_provider_arxiv() -> None:
    provider = _build_paper_provider("arxiv")

    assert isinstance(provider, ArxivPaperProvider)


def test_build_paper_provider_semantic_scholar() -> None:
    provider = _build_paper_provider("semantic_scholar")

    assert isinstance(provider, SemanticScholarPaperProvider)


@patch("swarm_notes.paper_search.arxiv.time.sleep")
@patch("urllib.request.urlopen")
def test_query_arxiv_honors_retry_after_for_429(mock_urlopen: MagicMock, mock_sleep: MagicMock) -> None:
    """ArXiv provider should honor Retry-After when rate limited."""
    mock_urlopen.side_effect = urllib.error.HTTPError(
        url="https://export.arxiv.org/api/query",
        code=429,
        msg="Too Many Requests",
        hdrs=Message(),
        fp=None,
    )
    mock_urlopen.side_effect.headers["Retry-After"] = "9"

    papers = _query_arxiv("test", 1)

    assert papers == []
    assert mock_urlopen.call_count == 3
    assert mock_sleep.call_args_list[0].args == (9.0,)


def test_semantic_scholar_provider_parses_arxiv_backed_results() -> None:
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_SEMANTIC_SCHOLAR_JSON
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = SemanticScholarPaperProvider(
        api_key="semantic-scholar-key",
        api_url="https://api.semanticscholar.org/graph/v1/paper/search",
        session=mock_session,
    )
    papers = provider.search("time series", 5)

    assert papers == [
        RawPaper(
            arxiv_id="2503.01234",
            title="Semantic Scholar Paper",
            abstract="Semantic Scholar abstract.",
            authors=["Jane Doe"],
            published="2026-03-25",
            url="https://arxiv.org/abs/2503.01234",
            primary_category="",
            source="semantic_scholar",
            keywords_matched=["time series"],
        )
    ]
    mock_session.get.assert_called_once()
    assert mock_session.get.call_args.kwargs["headers"]["x-api-key"] == "semantic-scholar-key"


@patch("swarm_notes.paper_search.semantic_scholar.time.sleep")
def test_semantic_scholar_provider_retries_429(mock_sleep: MagicMock) -> None:
    response = requests.Response()
    response.status_code = 429
    response.headers["Retry-After"] = "7"
    retry_error = requests.HTTPError("rate limited", response=response)

    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_SEMANTIC_SCHOLAR_JSON
    mock_response.raise_for_status.return_value = None
    mock_session.get.side_effect = [retry_error, mock_response]

    provider = SemanticScholarPaperProvider(
        api_key="semantic-scholar-key",
        api_url="https://api.semanticscholar.org/graph/v1/paper/search",
        session=mock_session,
    )
    papers = provider.search("time series", 5)

    assert len(papers) == 1
    assert mock_session.get.call_count == 2
    mock_sleep.assert_called_once_with(7.0)


def test_fetch_papers_uses_selected_provider() -> None:
    mock_provider = MagicMock()
    mock_provider.search.side_effect = [
        [
            RawPaper(
                arxiv_id="1234.56789",
                title="Provider Paper",
                abstract="Abstract.",
                authors=["Author"],
                published="2024-01-01",
                url="https://arxiv.org/abs/1234.56789",
                primary_category="",
                keywords_matched=["forecasting"],
            )
        ]
    ]

    with patch("swarm_notes.watcher._build_paper_provider", return_value=mock_provider) as mock_factory:
        papers = fetch_papers(
            keywords=["forecasting"],
            max_per_keyword=5,
            total_cap=5,
            provider_name="semantic_scholar",
        )

    assert len(papers) == 1
    assert papers[0].arxiv_id == "1234.56789"
    mock_factory.assert_called_once_with("semantic_scholar")


@pytest.mark.integration
def test_fetch_papers_integration() -> None:
    """Integration test for fetch_papers.

    This test makes a real network request to the ArXiv API to ensure the
    XML parsing and data structure generation is working correctly.
    """
    papers = fetch_papers(
        keywords=["large language models"],
        max_per_keyword=2,
        total_cap=2,
        provider_name="arxiv",
    )

    if not papers:
        pytest.skip("ArXiv was temporarily unavailable or timed out during the integration test")

    assert len(papers) > 0
    assert len(papers) <= 2
    assert hasattr(papers[0], "arxiv_id")
    assert papers[0].arxiv_id
    assert papers[0].url.startswith("https://arxiv.org/abs/")
    assert len(papers[0].title) > 0


# ---------------------------------------------------------------------------
# OpenAlex provider tests
# ---------------------------------------------------------------------------


def test_build_paper_provider_openalex() -> None:
    provider = _build_paper_provider("openalex")

    assert isinstance(provider, OpenAlexPaperProvider)


def test_openalex_provider_skips_papers_without_arxiv_id() -> None:
    """Provider must only return results that carry an ArXiv identifier."""
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_OPENALEX_JSON
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = OpenAlexPaperProvider(session=mock_session)
    papers = provider.search("time series", 10)

    assert len(papers) == 1
    assert papers[0].arxiv_id == "2503.11111"
    assert papers[0].title == "OpenAlex Time Series ArXiv Paper"
    assert papers[0].authors == ["Alice Smith", "Bob Jones"]
    assert papers[0].published == "2026-03-25"
    assert papers[0].url == "https://arxiv.org/abs/2503.11111"
    assert papers[0].source == "openalex"
    assert papers[0].keywords_matched == ["time series"]


def test_openalex_provider_reconstructs_abstract() -> None:
    """Abstract inverted index is correctly converted to plain text."""
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_OPENALEX_JSON
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = OpenAlexPaperProvider(session=mock_session)
    papers = provider.search("time series", 10)

    assert papers[0].abstract == "Abstract of time series openalex paper"


def test_openalex_provider_extracts_arxiv_id_from_locations() -> None:
    payload = {
        "results": [
            {
                "id": "https://openalex.org/W3011111111",
                "display_name": "Location-backed test ArXiv Paper",
                "abstract_inverted_index": {"test": [0], "text": [1]},
                "authorships": [{"author": {"display_name": "A"}}],
                "publication_date": "2026-03-25",
                "ids": {
                    "openalex": "https://openalex.org/W3011111111",
                    "doi": "https://doi.org/10.1234/example",
                },
                "best_oa_location": {
                    "landing_page_url": "https://arxiv.org/abs/2503.22222v1"
                },
            }
        ]
    }

    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = payload
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = OpenAlexPaperProvider(session=mock_session)
    papers = provider.search("test", 10)

    assert len(papers) == 1
    assert papers[0].arxiv_id == "2503.22222"
    assert papers[0].url == "https://arxiv.org/abs/2503.22222"


def test_reconstruct_openalex_abstract_empty() -> None:
    assert _reconstruct_openalex_abstract(None) == ""
    assert _reconstruct_openalex_abstract({}) == ""


def test_reconstruct_openalex_abstract_basic() -> None:
    index = {"Hello": [0], "world": [1]}
    assert _reconstruct_openalex_abstract(index) == "Hello world"


def test_reconstruct_openalex_abstract_out_of_order() -> None:
    index = {"world": [1], "Hello": [0]}
    assert _reconstruct_openalex_abstract(index) == "Hello world"


@patch("swarm_notes.paper_search.openalex.time.sleep")
def test_openalex_provider_retries_429(mock_sleep: MagicMock) -> None:
    response = requests.Response()
    response.status_code = 429
    response.headers["Retry-After"] = "5"
    retry_error = requests.HTTPError("rate limited", response=response)

    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = MOCK_OPENALEX_JSON
    mock_response.raise_for_status.return_value = None
    mock_session.get.side_effect = [retry_error, mock_response]

    provider = OpenAlexPaperProvider(session=mock_session)
    papers = provider.search("time series", 1)

    assert len(papers) == 1
    assert mock_session.get.call_count == 2
    mock_sleep.assert_called_once_with(5.0)


def test_openalex_provider_passes_api_key_and_mailto() -> None:
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = {"results": []}
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = OpenAlexPaperProvider(
        api_key="mykey123",
        mailto="researcher@example.com",
        session=mock_session,
    )
    provider.search("test", 5)

    call_params = mock_session.get.call_args.kwargs["params"]
    assert call_params["api_key"] == "mykey123"
    assert call_params["mailto"] == "researcher@example.com"


def test_openalex_provider_omits_api_key_when_empty() -> None:
    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = {"results": []}
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = OpenAlexPaperProvider(session=mock_session)
    provider.search("test", 5)

    call_params = mock_session.get.call_args.kwargs["params"]
    assert "api_key" not in call_params
    assert "mailto" not in call_params


def test_keyword_relevance_openalex_result() -> None:
    assert _is_keyword_relevant_openalex_result("time series", "A time series model", "")
    assert _is_keyword_relevant_openalex_result("forecasting", "", "short-term forecasting")
    assert not _is_keyword_relevant_openalex_result("time series", "graph partitions", "fair cuts")


def test_keyword_relevance_openalex_phrase_mode_strict() -> None:
    assert _is_keyword_relevant_openalex_result(
        "time series",
        "A time-series model",
        "",
        "phrase",
    )
    assert not _is_keyword_relevant_openalex_result(
        "time series",
        "A time model",
        "series appears elsewhere",
        "phrase",
    )


def test_keyword_relevance_openalex_all_tokens_mode_broader() -> None:
    assert _is_keyword_relevant_openalex_result(
        "time series",
        "A time model",
        "series appears elsewhere",
        "all_tokens",
    )


def test_match_keywords_openalex_result_multiple_hits() -> None:
    matched = _match_keywords_openalex_result(
        ["time series", "forecasting", "diffusion"],
        "Time-series forecasting with transformers",
        "",
        "all_tokens",
    )
    assert matched == ["time series", "forecasting"]


def test_build_openalex_search_query_boolean_or() -> None:
    query = _build_openalex_search_query(["time series", "forecasting", "timeseries"])
    assert query == '("time series" OR forecasting OR timeseries)'


def test_build_openalex_search_query_single() -> None:
    assert _build_openalex_search_query(["forecasting"]) == "forecasting"


def test_build_openalex_search_query_empty() -> None:
    assert _build_openalex_search_query(["", "   "]) == ""


def test_openalex_provider_paginates_until_cap() -> None:
    payload_page_1 = {
        "meta": {"count": 2},
        "results": [
            {
                "id": "https://openalex.org/W1",
                "display_name": "Time series paper",
                "abstract_inverted_index": {"time": [0], "series": [1]},
                "authorships": [{"author": {"display_name": "A"}}],
                "publication_date": "2026-03-20",
                "ids": {"arxiv": "https://arxiv.org/abs/2601.00001"},
            }
        ],
    }
    payload_page_2 = {
        "meta": {"count": 2},
        "results": [
            {
                "id": "https://openalex.org/W2",
                "display_name": "Forecasting paper",
                "abstract_inverted_index": {"forecasting": [0]},
                "authorships": [{"author": {"display_name": "B"}}],
                "publication_date": "2026-03-19",
                "ids": {"arxiv": "https://arxiv.org/abs/2601.00002"},
            }
        ],
    }

    mock_session = MagicMock()
    response_1 = MagicMock()
    response_1.raise_for_status.return_value = None
    response_1.json.return_value = payload_page_1
    response_2 = MagicMock()
    response_2.raise_for_status.return_value = None
    response_2.json.return_value = payload_page_2
    mock_session.get.side_effect = [response_1, response_2]

    provider = OpenAlexPaperProvider(session=mock_session, max_pages_per_window=2)
    papers = provider.search_many(["time series", "forecasting"], 2)

    assert len(papers) == 2
    assert {paper.arxiv_id for paper in papers} == {"2601.00001", "2601.00002"}
    assert mock_session.get.call_count == 2


def test_openalex_provider_skips_future_publication_date() -> None:
    payload = {
        "results": [
            {
                "id": "https://openalex.org/W3022222222",
                "display_name": "Forecasting with diffusion",
                "abstract_inverted_index": {"forecasting": [0]},
                "authorships": [{"author": {"display_name": "A"}}],
                "publication_date": "2050-01-01",
                "ids": {
                    "openalex": "https://openalex.org/W3022222222",
                    "arxiv": "https://arxiv.org/abs/2601.12345",
                },
            }
        ]
    }

    mock_session = MagicMock()
    mock_response = MagicMock()
    mock_response.json.return_value = payload
    mock_response.raise_for_status.return_value = None
    mock_session.get.return_value = mock_response

    provider = OpenAlexPaperProvider(session=mock_session)
    papers = provider.search("forecasting", 10)

    assert papers == []

