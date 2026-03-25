"""Tests for watcher.py."""

from unittest.mock import MagicMock, patch

import pytest

from swarm_notes.watcher import fetch_papers

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


@pytest.mark.integration
def test_fetch_papers_integration() -> None:
    """Integration test for fetch_papers.

    This test makes a real network request to the ArXiv API to ensure the
    XML parsing and data structure generation is working correctly.
    """
    papers = fetch_papers(keywords=["large language models"], max_per_keyword=2, total_cap=2)

    assert len(papers) > 0
    assert len(papers) <= 2
    assert hasattr(papers[0], "arxiv_id")
    assert papers[0].arxiv_id
    assert papers[0].url.startswith("https://arxiv.org/abs/")
    assert len(papers[0].title) > 0
