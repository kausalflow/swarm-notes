"""TimeSeriesSkill — extraction schema and prompt for time-series papers."""

from __future__ import annotations

from typing import ClassVar, Optional, Type

from pydantic import BaseModel, Field

from skills.base import PaperMetadata, Skill


class TimeSeriesMetadata(PaperMetadata):
    """Structured output for time-series and forecasting papers."""

    datasets: list[str] = Field(
        default_factory=list,
        description=(
            "Benchmark datasets used for evaluation (e.g. ETTh1, M4, Weather)."
        ),
    )
    architectures: list[str] = Field(
        default_factory=list,
        description=(
            "Model architectures introduced or compared "
            "(e.g. Transformer, Mamba, TimesNet)."
        ),
    )
    forecast_horizons: list[int] = Field(
        default_factory=list,
        description="Prediction horizon lengths evaluated (e.g. 96, 192, 720).",
    )
    metrics: list[str] = Field(
        default_factory=list,
        description="Evaluation metrics reported (e.g. MSE, MAE, CRPS).",
    )
    is_probabilistic: bool = Field(
        default=False,
        description="True if the method produces probabilistic/distributional forecasts.",
    )
    code_url: Optional[str] = Field(
        default=None,
        description="URL to the official code repository, if mentioned.",
    )


class TimeSeriesSkill(Skill):
    """Skill for analysing time-series forecasting papers."""

    keywords: ClassVar[list[str]] = [
        "time series",
        "time-series",
        "forecasting",
        "temporal",
        "autoregressive",
        "sequence modeling",
        "long-range dependency",
        "ett",
        "m4",
        "m5",
        "etth",
        "ettm",
        "traffic forecasting",
        "electricity",
        "multivariate forecasting",
    ]

    system_prompt: ClassVar[str] = (
        "You are an expert in time-series analysis and forecasting research. "
        "Extract structured metadata from the provided academic paper. "
        "Focus on: the model architecture(s) proposed or compared, "
        "benchmark datasets used, forecast horizons, evaluation metrics, "
        "and whether the method is probabilistic. "
        "Be precise and concise. Use only information explicitly stated in the paper."
    )

    schema: ClassVar[Type[TimeSeriesMetadata]] = TimeSeriesMetadata

    @classmethod
    def name(cls) -> str:
        return "TimeSeriesSkill"
