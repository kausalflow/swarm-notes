---
# CSL-compatible fields
title: "Volatility-Corrected Prediction Intervals: Locally Adaptive Uncertainty Quantification for Probabilistic Time-Series Forecasting"
author:
  - literal: "Jason B. Cho"
  - literal: "David S. Matteson"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31621"

# Custom fields
paper_id: "2610.31621"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "evaluation"
  - "baseline"
architectures:
  []
datasets:
  []
concept_slugs:
  - "volatility-corrected-prediction-intervals"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:29:05Z"
created_at: "2026-10-25T09:29:05Z"
---

# Volatility-Corrected Prediction Intervals: Locally Adaptive Uncertainty Quantification for Probabilistic Time-Series Forecasting

**Authors**: Jason B. Cho, David S. Matteson
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31621](https://arxiv.org/abs/2610.31621)

## Summary

This paper identifies local scale miscalibration in probabilistic time-series forecasting—where models attain nominal marginal coverage but fail locally due to serially dependent errors and heteroskedasticity—and introduces Volatility-Corrected Prediction Intervals (VCPI). VCPI leverages a GARCH model on standardized forecast residuals to apply a multiplicative correction to the forecaster's baseline scale, producing locally adaptive prediction intervals. Evaluated across major time-series foundation models on real-world datasets, VCPI achieves stable local coverage and robust theoretical guarantees compared to model-agnostic conformal baselines.

## Key Contributions

- Identified local scale miscalibration in time-series foundation models, where intervals achieve nominal marginal coverage but suffer from systematic temporal variation in local coverage.
- Proposed Volatility-Corrected Prediction Intervals (VCPI), a GARCH-based post-hoc calibration framework utilizing standardized forecast residuals for locally adaptive uncertainty quantification.
- Provided theoretical analysis of interval adaptation following abrupt volatility shifts.
- Demonstrated empirically across multiple real-world datasets that VCPI yields more stable local coverage than conformal baselines while preserving marginal coverage and interval width.

## Open Questions & Future Work

- [[mitigating-parametric-misspecification-multi-step-garch-vcpi]]

## Key Concepts

- [[volatility-corrected-prediction-intervals]]: A post-hoc calibration procedure using GARCH modeling on forecast residuals to produce locally adaptive prediction intervals for time-series forecasters.

## Archivist Review

Approved the overarching calibration method VCPI as a highly reusable post-hoc uncertainty quantification technique, along with an open question concerning its parametric misspecification and multi-horizon variance mean-reversion. No datasets were approved because Chronos, Moirai, and TimesFM are foundation models rather than dataset benchmarks.

### Approved Concepts
- Volatility-Corrected Prediction Intervals: Introduces a novel post-hoc calibration framework using GARCH modeling on standardized residuals to correct for local scale miscalibration in time-series foundation models.

### Approved Open Questions
- Mitigating Parametric Misspecification in VCPI: Overcoming parametric misspecification and multi-step variance mean-reversion is crucial for extending locally adaptive volatility-correction methods to longer forecast horizons and extreme confidence levels without sacrificing robustness.

## Links

- [Abstract](https://arxiv.org/abs/2610.31621)
- [PDF](https://arxiv.org/pdf/2610.31621)

