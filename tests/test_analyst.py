"""Tests for analyst.py."""

from unittest.mock import MagicMock, patch

from swarm_cruise.analyst import analyse
from swarm_cruise.router import GENERAL_SKILL
from swarm_cruise.watcher import RawPaper


class MockOutput:
    """Mock structure for PaperAnalysis output."""
    arxiv_id: str = ""
    url: str = ""
    published: str = ""
    authors: list[str] = []
    tags: list[str] = []
    concepts: list[str] = []


@patch("swarm_cruise.analyst.Agent")
@patch("swarm_cruise.analyst._load_taxonomy")
def test_analyse(mock_load_taxonomy: MagicMock, mock_agent_class: MagicMock) -> None:
    """Test the analyse function.

    Mocks the Pydantic AI Agent and taxonomy loader to simulate extracting
    information from a paper without calling the LLM.

    Args:
        mock_load_taxonomy: Mock for the taxonomy loader.
        mock_agent_class: Mock for the Agent class.
    """
    mock_load_taxonomy.return_value = {
        "tags": ["llm"],
        "architectures": ["transformer"],
        "domains": ["nlp"],
    }

    mock_instance = mock_agent_class.return_value
    mock_result = MagicMock()

    mock_result.output = MockOutput()
    mock_instance.run_sync.return_value = mock_result

    paper = RawPaper(
        arxiv_id="12345",
        title="Test Title",
        abstract="Test abstract",
        authors=["Author Name"],
        published="2023-01-01",
        url="http://url",
        primary_category="cs.CL",
    )

    result = analyse(paper, GENERAL_SKILL)

    assert result.arxiv_id == "12345"
    assert result.url == "http://url"
    assert result.published == "2023-01-01"
    assert result.authors == ["Author Name"]
