"""Tests for federation.py."""

from unittest.mock import MagicMock, patch

from swarm_notes.federation import run_federation


@patch("swarm_notes.federation._fetch_feed")
@patch("swarm_notes.federation._process_entry")
def test_run_federation(mock_process: MagicMock, mock_fetch: MagicMock) -> None:
    """Test the run_federation function.

    Mocks fetching remote feeds and processing them to verify
    the loop handles valid data points correctly.

    Args:
        mock_process: Mock for _process_entry.
        mock_fetch: Mock for _fetch_feed.
    """
    mock_fetch.return_value = [{"arxiv_id": "123", "title": "Test Title"}]

    run_federation(feed_urls=["http://test.com/public_feed.json"])

    mock_fetch.assert_called_once_with("http://test.com/public_feed.json")
    mock_process.assert_called_once()
