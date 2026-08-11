---
# CSL-compatible fields
title: "Load forecasting for households and energy communities: Are deep learning models worth the effort?"
author:
  - literal: "Lukas Moosbrugger"
  - literal: "Valentin Seiler"
  - literal: "Philipp Wohlgenannt"
  - literal: "Sebastian Hegenbart"
  - literal: "Sashko Ristov"
  - literal: "Elias Eder"
  - literal: "Peter Kepplinger"
issued:
  date-parts:
    - [2026, 8, 8]
url: "https://arxiv.org/abs/2501.05000"

# Custom fields
paper_id: "2501.05000"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "xlstm"
  - "transformer"
  - "reinforcement-learning"
  - "transfer-learning"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-11T05:45:47Z"
created_at: "2026-08-11T05:45:47Z"
---

# Load forecasting for households and energy communities: Are deep learning models worth the effort?

**Authors**: Lukas Moosbrugger, Valentin Seiler, Philipp Wohlgenannt, Sebastian Hegenbart, Sashko Ristov, Elias Eder, Peter Kepplinger
**Date**: 2026-08-08
**Paper ID**: [openalex:2501.05000](https://arxiv.org/abs/2501.05000)

## Summary

This study evaluates the effectiveness of deep learning models (LSTM, xLSTM, Transformers) versus traditional benchmarks (KNN, persistence) for short-term load forecasting in energy communities under varying data availability. The findings reveal that simple persistence outperforms deep learning when training data is under six months, and simple baselines yield statistically equivalent cost savings in model predictive control settings, questioning the universal necessity of complex deep learning. Additionally, transfer learning with synthetic load profiles is shown to effectively mitigate data scarcity.

## Key Contributions

- Evaluates state-of-the-art deep learning models (LSTM, xLSTM, Transformers) against traditional benchmarks (KNN, persistence) across varying community sizes, historical data availability, and model complexity for energy community load forecasting.
- Demonstrates that with less than six months of training data, simple persistence predictions outperform deep learning architectures in forecast accuracy.
- Shows that transfer learning using synthetic load profiles improves normalized mean absolute error by 1.97 percentage points when only two months of training data are available.
- Applies model predictive control for energy communities with a shared battery, showing that while top deep learning models achieve an 8.06% financial cost reduction for 50 households, persistence and KNN yield cost savings statistically indistinguishable from deep learning methods.

## Limitations

Focuses primarily on short-term load forecasting and model predictive control setups for specific energy community configurations.

## Archivist Review

Applied strict selectivity according to the review policy. The study provides an empirical evaluation comparing deep learning and traditional baselines for energy community load forecasting, but does not introduce a novel foundational concept or methodological advance that qualifies for standalone vault entry. The single candidate open question was evaluated and rejected for being too application-specific to energy management systems rather than representing a general algorithmic or theoretical bottleneck in time series analysis.

### Rejected Candidates
- [open_question] Forecasting Sensitivity on Alternative Objectives (`forecasting-sensitivity-alternative-objectives`) - low_impact: Addresses domain-specific energy community optimization trade-offs rather than a foundational methodological gap in time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2501.05000)
- [PDF](https://arxiv.org/pdf/2501.05000)

