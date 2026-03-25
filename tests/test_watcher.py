"""Tests for watcher.py."""

from unittest.mock import MagicMock, patch

from src.watcher import fetch_papers

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
