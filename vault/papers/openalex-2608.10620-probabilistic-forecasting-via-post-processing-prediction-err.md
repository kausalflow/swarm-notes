---
# CSL-compatible fields
title: "Probabilistic forecasting via post-processing prediction errors: In- or out-of-sample?"
author:
  - literal: "Piotr Zaborowski"
  - literal: "Arkadiusz Lipiecki"
  - literal: "Fotios Petropoulos"
  - literal: "Rafał Weron"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10620"

# Custom fields
paper_id: "2608.10620"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "m4-competition-dataset"
concept_slugs:
  []
dataset_slugs:
  - "m4-competition-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:38Z"
created_at: "2026-08-14T06:07:38Z"
---

# Probabilistic forecasting via post-processing prediction errors: In- or out-of-sample?

**Authors**: Piotr Zaborowski, Arkadiusz Lipiecki, Fotios Petropoulos, Rafał Weron
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10620](https://arxiv.org/abs/2608.10620)

## Summary

This paper investigates whether forecast error post-processing methods can systematically improve traditional Gaussian predictive distributions derived from in-sample residuals. The authors propose a hybrid framework that combines post-processing with model-specific scaling of forecast uncertainty across horizons. Evaluating historical simulation, conformal prediction, quantile regression, and GARCH-based post-processing on point forecasts from Theta, exponential smoothing, and ARIMA models across 14,407 monthly series from the M4 competition, they show improvements of up to 4.6% in CRPS. Furthermore, the results demonstrate that in-sample calibration generally outperforms out-of-sample calibration, particularly at longer forecast horizons.

## Key Contributions

- Investigates whether post-processing methods can systematically improve traditional Gaussian predictive distributions constructed from in-sample residuals using point forecasts from Theta, exponential smoothing, and ARIMA models.
- Proposes a hybrid framework combining forecast error post-processing with model-specific scaling of forecast uncertainty across horizons.
- Evaluates across 14,407 monthly series from the M4 competition and forecast horizons of 1 to 12 months using CRPS and rank-based statistical comparisons, showing gains of up to 4.6%.
- Finds that in-sample calibration outperforms its out-of-sample counterpart in 11 of 12 model-method combinations, with the advantage increasing at longer horizons.

## Open Questions & Future Work

- [[data-frequency-calibration-size-impact]]

## Archivist Review

Approved the M4 dataset as a standard evaluation benchmark and one open question regarding data frequency and calibration sample size. No concepts met the stringent bar for standalone reusability since the paper focuses on empirical comparison of established post-processing methods rather than introducing a novel architectural or algorithmic primitive.

### Approved Open Questions
- Data Frequency and Calibration Size: Understanding the impact of data frequency and sample size on post-processing helps determine the boundary conditions and generalizability of in-sample versus out-of-sample calibration strategies across diverse application domains.

### Rejected Candidates
- [open_question] Alternative Horizon-Scaling Procedures (`alternative-horizon-scaling-procedures`) - low_impact: Paper-local extension of a specific scaling component in the framework without broad theoretical impact.

## Datasets

- [[m4-competition-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2608.10620)
- [PDF](https://arxiv.org/pdf/2608.10620)

