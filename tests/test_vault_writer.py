"""Tests for vault_writer review rendering."""

from unittest.mock import patch

from swarm_notes.analyst import ConceptLink, OpenQuestion, PaperAnalysis, RejectedCandidate
from swarm_notes.config import settings
from swarm_notes.vault_writer import _build_body, _write_concept_stub
import frontmatter


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
        critic_rejected_candidates=[
            RejectedCandidate(
                candidate_type="concept",
                candidate_slug="benchmark-setup",
                candidate_title="Benchmark Setup",
                reason_code="generic",
                reason="Generic benchmark setup with no reusable methodological novelty.",
            )
        ],
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
    assert "[concept] Benchmark Setup" in body
    assert "benchmark-setup" in body
    assert "generic" in body


def test_build_body_uses_wiki_links_for_concepts() -> None:
    analysis = PaperAnalysis(
        title="Concept Link Style",
        authors=["Test Author"],
        published="2026-03-27",
        arxiv_id="2603.99999",
        source="arxiv",
        url="https://arxiv.org/abs/2603.99999",
        summary="A concise summary.",
        key_contributions=["Contribution one."],
        tags=["benchmark"],
        architectures=[],
        datasets=[],
        concepts=[
            ConceptLink(
                slug="kr-excitation-regulation-framework",
                display_name="KR Excitation Regulation Framework",
                one_liner="A framework for deriving robust CSD indicators.",
            )
        ],
        limitations="",
        domain="time-series",
        open_questions=[],
    )

    body = _build_body(analysis)
    assert "[[../concepts/kr-excitation-regulation-framework|KR Excitation Regulation Framework]]" in body


def test_write_concept_stub_tracks_related_paper_link(tmp_path, monkeypatch) -> None:
    tmp_concepts = tmp_path / "tmp-concepts"
    vault_concepts = tmp_path / "vault-concepts"
    tmp_concepts.mkdir(parents=True)
    vault_concepts.mkdir(parents=True)

    monkeypatch.setattr(settings, "tmp_concepts_dir", tmp_concepts)
    monkeypatch.setattr(settings, "vault_concepts_dir", vault_concepts)

    _write_concept_stub(
        slug="uncertainty-guided-label-rebalancing",
        display_name="Uncertainty-Guided Label Rebalancing",
        one_liner="A relabeling mechanism based on uncertainty.",
        paper_slug="openalex-2603-25670-uncertainty-guided-label-rebalancing-for-cps-safety-monitoring",
    )

    concept_path = tmp_concepts / "uncertainty-guided-label-rebalancing.md"
    post = frontmatter.load(concept_path)
    assert "[[openalex-2603-25670-uncertainty-guided-label-rebalancing-for-cps-safety-monitoring]]" in post.metadata["source_papers"]
    assert "## Related Papers" in post.content
    assert "- [[openalex-2603-25670-uncertainty-guided-label-rebalancing-for-cps-safety-monitoring]]" in post.content