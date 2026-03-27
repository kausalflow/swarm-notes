"""Tests for watcher.py."""

from collections.abc import Generator
from email.message import Message
import socket
import urllib.error
from unittest.mock import MagicMock, patch

import pytest

from swarm_notes.watcher import _query_arxiv, _respect_arxiv_rate_limit, fetch_papers

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


@pytest.fixture(autouse=True)
def reset_arxiv_rate_limit_state() -> Generator[None, None, None]:
    with patch("swarm_notes.watcher._last_arxiv_request_started_at", None):
        yield


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


@patch("swarm_notes.watcher.time.sleep")
@patch("swarm_notes.watcher._respect_arxiv_rate_limit")
@patch("urllib.request.urlopen")
def test_query_arxiv_retries_transient_timeout(
    mock_urlopen: MagicMock,
    mock_rate_limit: MagicMock,
    mock_sleep: MagicMock,
) -> None:
    """Transient network failures should be retried before succeeding."""
    mock_response = MagicMock()
    mock_response.read.return_value = MOCK_ATOM_XML
    mock_response.__enter__.return_value = mock_response
    mock_urlopen.side_effect = [socket.timeout("timed out"), mock_response]

    papers = _query_arxiv("test", 1)

    assert len(papers) == 1
    assert papers[0].arxiv_id == "2301.12345"
    assert mock_urlopen.call_count == 2
    assert mock_rate_limit.call_count == 2
    mock_sleep.assert_called_once_with(2.0)


@patch("swarm_notes.watcher.time.sleep")
@patch("swarm_notes.watcher._respect_arxiv_rate_limit")
@patch("urllib.request.urlopen")
def test_query_arxiv_honors_retry_after_for_429(
    mock_urlopen: MagicMock,
    mock_rate_limit: MagicMock,
    mock_sleep: MagicMock,
) -> None:
    """429 responses should use Retry-After when the server provides one."""
    headers = Message()
    headers["Retry-After"] = "9"
    retry_error = urllib.error.HTTPError(
        url="https://export.arxiv.org/api/query",
        code=429,
        msg="Too Many Requests",
        hdrs=headers,
        fp=None,
    )
    mock_response = MagicMock()
    mock_response.read.return_value = MOCK_ATOM_XML
    mock_response.__enter__.return_value = mock_response
    mock_urlopen.side_effect = [retry_error, mock_response]

    papers = _query_arxiv("test", 1)

    assert len(papers) == 1
    assert papers[0].arxiv_id == "2301.12345"
    assert mock_urlopen.call_count == 2
    assert mock_rate_limit.call_count == 2
    mock_sleep.assert_called_once_with(9.0)


@patch("swarm_notes.watcher.time.sleep")
@patch("swarm_notes.watcher._respect_arxiv_rate_limit")
@patch("urllib.request.urlopen")
def test_query_arxiv_does_not_retry_non_transient_http_error(
    mock_urlopen: MagicMock,
    mock_rate_limit: MagicMock,
    mock_sleep: MagicMock,
) -> None:
    """Permanent upstream errors should fail fast without retrying."""
    mock_urlopen.side_effect = urllib.error.HTTPError(
        url="https://export.arxiv.org/api/query",
        code=400,
        msg="Bad Request",
        hdrs=Message(),
        fp=None,
    )

    papers = _query_arxiv("test", 1)

    assert papers == []
    assert mock_urlopen.call_count == 1
    assert mock_rate_limit.call_count == 1
    mock_sleep.assert_not_called()


@patch("swarm_notes.watcher.time.sleep")
@patch("swarm_notes.watcher.time.monotonic", side_effect=[10.0, 11.0, 14.5])
def test_respect_arxiv_rate_limit_spaces_requests(mock_monotonic: MagicMock, mock_sleep: MagicMock) -> None:
    """Sequential ArXiv requests should be spaced to avoid rate limiting."""
    _respect_arxiv_rate_limit()
    _respect_arxiv_rate_limit()

    mock_sleep.assert_called_once_with(2.0)


@pytest.mark.integration
def test_fetch_papers_integration() -> None:
    """Integration test for fetch_papers.

    This test makes a real network request to the ArXiv API to ensure the
    XML parsing and data structure generation is working correctly.
    """
    papers = fetch_papers(keywords=["large language models"], max_per_keyword=2, total_cap=2)

    if not papers:
        pytest.skip("ArXiv was temporarily unavailable or timed out during the integration test")

    assert len(papers) > 0
    assert len(papers) <= 2
    assert hasattr(papers[0], "arxiv_id")
    assert papers[0].arxiv_id
    assert papers[0].url.startswith("https://arxiv.org/abs/")
    assert len(papers[0].title) > 0
