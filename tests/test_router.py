"""Tests for router.py."""

from swarm_notes.router import GENERAL_SKILL, VISION_SKILL, route
from swarm_notes.watcher import RawPaper


def test_route_category() -> None:
    """Test router directly based on category with keyword support.

    Ensures that a paper with a known category and a matching keyword
    maps to the correct domain skill.
    """
    paper = RawPaper(
        arxiv_id="123",
        title="Test Computer Vision",
        abstract="Test abstract about object-detection in images.",
        authors=["Author"],
        published="2023-01-01",
        url="http://url",
        primary_category="cs.CV",
    )
    skill = route(paper)
    assert skill == VISION_SKILL


def test_route_fallback() -> None:
    """Test router fallback to the general skill.

    Ensures that a paper with an unknown category and no matching keywords
    falls back to using the GENERAL_SKILL.
    """
    paper = RawPaper(
        arxiv_id="123",
        title="Generic Paper",
        abstract="Nothing related to specific domains here.",
        authors=["Author"],
        published="2023-01-01",
        url="http://url",
        primary_category="math.GN",
    )
    skill = route(paper)
    assert skill == GENERAL_SKILL
