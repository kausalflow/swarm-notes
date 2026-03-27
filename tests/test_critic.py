"""Tests for critic.py."""

from unittest.mock import MagicMock, patch

from swarm_notes.analyst import ConceptLink, OpenQuestion, PaperAnalysis, RejectedCandidate
from swarm_notes.critic import review_analysis
from swarm_notes.router import SkillSpec
from swarm_notes.watcher import RawPaper


def _build_paper() -> RawPaper:
    return RawPaper(
        arxiv_id="2603.25708",
        title="Selective Research Notes",
        abstract="A paper about deciding which ideas deserve persistent notes.",
        authors=["Test Author"],
        published="2026-03-27",
        url="https://arxiv.org/abs/2603.25708",
        primary_category="cs.LG",
    )


def _build_skill() -> SkillSpec:
    return SkillSpec(
        id="general-ml",
        name="GeneralMLSkill",
        description="Fallback skill.",
        extra_system_prompt="Analyse the paper.",
    )


def _build_analysis() -> PaperAnalysis:
    return PaperAnalysis(
        title="Selective Research Notes",
        authors=["Test Author"],
        published="2026-03-27",
        arxiv_id="2603.25708",
        source="arxiv",
        url="https://arxiv.org/abs/2603.25708",
        summary="A concise summary.",
        key_contributions=["Contribution one."],
        tags=["benchmark"],
        architectures=[],
        datasets=[],
        concepts=[],
        limitations="",
        domain="nlp",
        open_questions=[],
    )


def test_review_analysis_skips_agent_when_no_candidates() -> None:
    analysis = _build_analysis()

    with patch("swarm_notes.critic.Agent") as mock_agent:
        result = review_analysis(analysis, _build_paper(), _build_skill())

    assert result is analysis
    mock_agent.assert_not_called()


@patch("swarm_notes.critic.Agent")
def test_review_analysis_generates_fallback_summary_when_missing(mock_agent_class: MagicMock) -> None:
    analysis = _build_analysis()
    analysis.concepts = [
        ConceptLink(
            slug="state-space-mixer",
            display_name="State Space Mixer",
            one_liner="A selective mixer for long-horizon dynamics.",
        )
    ]

    mock_result = MagicMock()
    mock_result.output.approved_concepts = analysis.concepts
    mock_result.output.approved_open_questions = []
    mock_result.output.approved_datasets = []
    mock_result.output.review_summary = ""
    mock_result.output.rejected_candidates = []

    mock_agent = mock_agent_class.return_value
    mock_agent.run_sync.return_value = mock_result

    result = review_analysis(analysis, _build_paper(), _build_skill())

    assert result.critic_review_summary == (
        "Archivist review kept only candidates judged central to the paper and reusable across future work. "
        "Approved 1 concept(s), 0 open question(s), and 0 dataset(s), with 0 rejected candidate note(s)."
    )


@patch("swarm_notes.critic.Agent")
def test_review_analysis_replaces_candidates_with_approved_items(mock_agent_class: MagicMock) -> None:
    analysis = _build_analysis()
    analysis.concepts = [
        ConceptLink(
            slug="state-space-mixer",
            display_name="State Space Mixer",
            one_liner="A selective mixer for long-horizon dynamics.",
            importance_reason="Core mechanism of the paper.",
            reusability_reason="Likely to recur in sequence modeling papers.",
            evidence_excerpt="We introduce a state-space mixer for long-range forecasting.",
        )
    ]
    analysis.open_questions = [
        OpenQuestion(
            slug="shift-robust-calibration",
            title="Shift-Robust Calibration",
            background="Calibration degrades under distribution shift.",
            description="It remains unresolved how to preserve uncertainty quality under combined drift.",
            importance_reason="Reliability is central to deployment.",
            evidence_excerpt="Future work includes robust calibration under drift.",
        )
    ]
    analysis.datasets = ["ETTh1", "10 real-world datasets"]

    approved_concept = ConceptLink(
        slug="state-space-mixer",
        display_name="State Space Mixer",
        one_liner="A selective mixer for long-horizon dynamics.",
    )
    approved_question = OpenQuestion(
        slug="shift-robust-calibration",
        title="Shift-Robust Calibration",
        background="Calibration degrades under distribution shift.",
        description="It remains unresolved how to preserve uncertainty quality under combined drift.",
    )

    mock_result = MagicMock()
    mock_result.output.approved_concepts = [approved_concept]
    mock_result.output.approved_open_questions = [approved_question]
    mock_result.output.approved_datasets = ["ETTh1"]
    mock_result.output.review_summary = "Approved one concept and one open question."
    mock_result.output.rejected_candidates = [
        RejectedCandidate(
            candidate_type="dataset",
            candidate_slug="10-real-world-datasets",
            candidate_title="10 real-world datasets",
            reason_code="generic",
            reason="Aggregate dataset label with no specific reusable benchmark identity.",
        )
    ]

    mock_agent = mock_agent_class.return_value
    mock_agent.run_sync.return_value = mock_result

    result = review_analysis(analysis, _build_paper(), _build_skill())

    assert result.concepts == [approved_concept]
    assert result.open_questions == [approved_question]
    assert result.datasets == ["ETTh1"]
    assert result.critic_review_summary == "Approved one concept and one open question."
    assert result.critic_rejected_candidates == [
        RejectedCandidate(
            candidate_type="dataset",
            candidate_slug="10-real-world-datasets",
            candidate_title="10 real-world datasets",
            reason_code="generic",
            reason="Aggregate dataset label with no specific reusable benchmark identity.",
        )
    ]