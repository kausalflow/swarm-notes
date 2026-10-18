---
# CSL-compatible fields
title: "DIAL: Dynamic and Informed Adjustment of the Native Stochastic Law for Reliable Weather Ensembles"
author:
  - literal: "Yucheng Wang"
  - literal: "Haonan Guo"
  - literal: "Tianhao Zhao"
  - literal: "Di Wang"
  - literal: "Yu Wu"
  - literal: "Zengmao Wang"
  - literal: "Bo Du"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21639"

# Custom fields
paper_id: "2610.21639"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "uncertainty"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:36Z"
created_at: "2026-10-18T09:13:36Z"
---

# DIAL: Dynamic and Informed Adjustment of the Native Stochastic Law for Reliable Weather Ensembles

**Authors**: Yucheng Wang, Haonan Guo, Tianhao Zhao, Di Wang, Yu Wu, Zengmao Wang, Bo Du
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21639](https://arxiv.org/abs/2610.21639)

## Summary

Ensemble weather forecasts often suffer from miscalibrated spread across different variables, spatial scales, and lead times, while existing post-processing or backpropagation-heavy guidance approaches struggle with stability and expense. To address this, the paper introduces Dynamic and Informed Adjustment of the Native Stochastic Law (DIAL), which dynamically controls a frozen weather model's native stochasticity through step-by-step noise updates guided by past forecast errors. Evaluated on FourCastNet 3 using ERA5 data, DIAL surpasses learned post-processing baselines and achieves an 8.27% improvement in multiscale CRPS compared to the unmodified native reference.

## Key Contributions

- Introduces DIAL (Dynamic and Informed Adjustment of the Native Stochastic Law) to control a frozen model's native stochasticity during weather forecasting without retraining or backpropagating through chaotic steps.
- Learns from past forecasts to predict variable- and scale-specific spread adjustments by estimating how noise changes affect future forecast accuracy and reliability.
- Evaluated on FourCastNet 3 (FCN3) using unseen ERA5 years, achieving an 8.27% improvement in the primary multiscale continuous ranked probability score (CRPS) over the unmodified Native FCN3 reference.

## Archivist Review

Applied strict filtering criteria: rejected the paper-specific open question because it deals with narrow actuator libraries for weather models rather than a broadly reusable machine learning research question. No concepts or datasets met the strict novelty and reusability standard.

### Rejected Candidates
- [open_question] Richer Actuator Libraries for Weather Ensembles (`richer-actuator-libraries-weather-ensembles`) - not_reusable: The open question addresses a paper-specific extension regarding actuator libraries and basis functions for weather ensembles, which lacks broad generalizability across diverse forecasting domains.

## Links

- [Abstract](https://arxiv.org/abs/2610.21639)
- [PDF](https://arxiv.org/pdf/2610.21639)

