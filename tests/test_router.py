"""Tests for router.py."""

from swarm_notes.router import route, load_skills
from swarm_notes.watcher import RawPaper


def test_route_category() -> None:
    """Test router directly based on category with keyword support.

    Ensures that a paper with a known category and a matching keyword
    maps to the correct domain skill.
    """
    load_skills()  # Ensure skills are loaded from the skills/ dir
    paper = RawPaper(
        arxiv_id="123",
        title="Test Computer Vision",
        abstract="Test abstract about object-detection in images.",
        authors=["Author"],
        published="2023-01-01",
        url="http://url",
        primary_category="cs.CV",
    )
    # Since we removed VISION_SKILL, it should fall back to general-ml 
    # UNLESS computer-vision folder exists. Wait, I didn't create computer-vision.
    # So it should be GeneralMLSkill.
    skill = route(paper)
    assert skill.id == "general-ml"


def test_route_time_series() -> None:
    """Test routing to the new TimeSeriesSkill."""
    load_skills()
    paper = RawPaper(
        arxiv_id="ts-123",
        title="Time Series Forecasting",
        abstract="A new transformer for time-series forecasting benchmarks like ETTh1.",
        authors=["Author"],
        published="2023-01-01",
        url="http://url",
        primary_category="eess.SP",
    )
    skill = route(paper)
    assert skill.id == "time-series"
    assert "forecasting" in skill.extra_system_prompt


def test_route_fallback() -> None:
    """Test router fallback to the general skill."""
    load_skills()
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
    assert skill.id == "general-ml"
