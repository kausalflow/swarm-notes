"""Tests for vault_writer review rendering."""

from unittest.mock import patch

from swarm_notes.analyst import ConceptLink, OpenQuestion, PaperAnalysis
from swarm_notes.vault_writer import _build_body


def test_build_body_includes_archivist_review_details() -> None:
    analysis = PaperAnalysis(
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
        concepts=[
            ConceptLink(
                slug="state-space-mixer",
                display_name="State Space Mixer",
                one_liner="A selective mixer for long-horizon dynamics.",
                importance_reason="Core mechanism behind the reported gains.",
            )
        ],
        limitations="",
        domain="nlp",
        open_questions=[
            OpenQuestion(
                slug="shift-robust-calibration",
                title="Shift-Robust Calibration",
                background="Calibration degrades under shift.",
                description="It remains unresolved how to preserve uncertainty quality under combined drift.",
                importance_reason="Reliable deployment depends on it.",
            )
        ],
        critic_review_summary="Approved one concept and one open question.",
        critic_rejected_candidates=["Rejected 'benchmark setup' because it is generic and paper-local."],
    )

    with patch("swarm_notes.vault_writer._create_open_question"):
        body = _build_body(analysis)

    assert "## Archivist Review" in body
    assert "Approved one concept and one open question." in body
    assert "### Approved Concepts" in body
    assert "Core mechanism behind the reported gains." in body
    assert "### Approved Open Questions" in body
    assert "Reliable deployment depends on it." in body
    assert "### Rejected Candidates" in body
    assert "Rejected 'benchmark setup' because it is generic and paper-local." in body