"""Tests for watcher.py."""

from email.message import Message
import urllib.error
from unittest.mock import MagicMock, patch

import pytest
import requests

from swarm_notes.watcher import (
    ArxivPaperProvider,
    RawPaper,
    SemanticScholarPaperProvider,
    _build_paper_provider,
    _query_arxiv,
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
            "publicationDate": "2025-03-12",
            "year": 2025,
            "url": "https://www.semanticscholar.org/paper/paper-1",
            "externalIds": {"ArXiv": "2503.01234v2"},
            "openAccessPdf": {"url": "https://arxiv.org/pdf/2503.01234.pdf"},
        },
        {
            "paperId": "paper-2",
            "title": "No Arxiv ID",
            "abstract": "Should be skipped.",
            "authors": [{"name": "John Doe"}],
            "publicationDate": "2024-07-01",
            "year": 2024,
            "url": "https://www.semanticscholar.org/paper/paper-2",
            "externalIds": {"DOI": "10.1234/example"},
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


@patch("swarm_notes.watcher.time.sleep")
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
            published="2025-03-12",
            url="https://arxiv.org/abs/2503.01234",
            primary_category="",
            source="semantic_scholar",
            keywords_matched=["time series"],
        )
    ]
    mock_session.get.assert_called_once()
    assert mock_session.get.call_args.kwargs["headers"]["x-api-key"] == "semantic-scholar-key"


@patch("swarm_notes.watcher.time.sleep")
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
