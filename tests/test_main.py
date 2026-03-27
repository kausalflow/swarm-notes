from types import SimpleNamespace
from unittest.mock import call, patch

import pytest

from swarm_notes.main import _is_retryable_paper_error, _process_paper_with_retries
from swarm_notes.router import SkillSpec
from swarm_notes.watcher import RawPaper


class TransientModelError(RuntimeError):
    def __init__(self, status_code: int, message: str) -> None:
        super().__init__(message)
        self.status_code = status_code


def _build_paper() -> RawPaper:
    return RawPaper(
        arxiv_id="2603.25708",
        title="Retry Me Once More",
        abstract="A transient upstream failure should not lose this paper.",
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


def test_process_paper_with_retries_retries_transient_failure() -> None:
    paper = _build_paper()
    skill = _build_skill()
    src_config = SimpleNamespace(settings=SimpleNamespace(enable_domain_expert=False))
    analysis = SimpleNamespace(open_questions=[])

    with patch("swarm_notes.analyst.analyse", side_effect=[
        TransientModelError(503, "high demand"),
        TransientModelError(503, "high demand"),
        analysis,
    ]) as mock_analyse, patch("swarm_notes.vault_writer.write_paper") as mock_write_paper, patch(
        "swarm_notes.main.time.sleep"
    ) as mock_sleep:
        result = _process_paper_with_retries(paper, skill, src_config)

    assert result is analysis
    assert mock_analyse.call_count == 3
    mock_sleep.assert_has_calls([call(30.0), call(90.0)])
    mock_write_paper.assert_called_once_with(analysis, skill.name)


def test_process_paper_with_retries_does_not_retry_non_transient_failure() -> None:
    paper = _build_paper()
    skill = _build_skill()
    src_config = SimpleNamespace(settings=SimpleNamespace(enable_domain_expert=False))

    with patch("swarm_notes.analyst.analyse", side_effect=ValueError("bad prompt")) as mock_analyse, patch(
        "swarm_notes.main.time.sleep"
    ) as mock_sleep:
        with pytest.raises(ValueError, match="bad prompt"):
            _process_paper_with_retries(paper, skill, src_config)

    mock_analyse.assert_called_once_with(paper, skill)
    mock_sleep.assert_not_called()


def test_is_retryable_paper_error_checks_exception_chain() -> None:
    retryable = RuntimeError("wrapped")
    retryable.__cause__ = TransientModelError(503, "high demand")

    assert _is_retryable_paper_error(retryable) is True
    assert _is_retryable_paper_error(TransientModelError(400, "bad request")) is False