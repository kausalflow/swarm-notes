---
# CSL-compatible fields
title: "TEFL: Prediction-Residual-Guided Rolling Forecasting for Multi-Horizon Time Series"
author:
  - literal: "Xiannan Huang"
  - literal: "Shen Fang"
  - literal: "Shuhan Qiu"
  - literal: "Chengcheng Yu"
  - literal: "Jiayuan Du"
  - literal: "Chao Yang"
issued:
  date-parts:
    - [2026, 2, 26]
url: "https://arxiv.org/abs/2602.22520"

# Custom fields
paper_id: "2602.22520"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "rolling-forecasting"
  - "evaluation"
  - "model_parameter-efficient-fine-tuning"
architectures:
  []
datasets:
  - "10 real-world datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:15Z"
created_at: "2026-03-27T14:09:15Z"
---

# TEFL: Prediction-Residual-Guided Rolling Forecasting for Multi-Horizon Time Series

**Authors**: Xiannan Huang, Shen Fang, Shuhan Qiu, Chengcheng Yu, Jiayuan Du, Chao Yang
**Date**: 2026-02-26
**Paper ID**: [openalex:2602.22520](https://arxiv.org/abs/2602.22520)

## Summary

This paper introduces Temporal Error Feedback Learning (TEFL), a novel framework designed to enhance deep multi-horizon time series forecasting by explicitly utilizing historical prediction residuals generated during rolling evaluation. TEFL addresses the partial observability of residuals in multi-step settings by selecting observable errors and integrating them via an efficient, lightweight low-rank adapter to prevent overfitting. The method employs a two-stage training procedure to jointly optimize the base forecasting model and the error feedback module. Extensive experiments demonstrate that TEFL provides a general and effective enhancement, yielding consistent accuracy gains (5-10% MAE reduction) and superior robustness against distribution shifts compared to standard point-wise loss minimization training.

## Key Contributions

- Proposed TEFL, a unified framework that explicitly incorporates historical prediction residuals from rolling forecasts into deep forecasting models.
- Addressed challenges of selecting observable multi-step residuals and integrating them via a lightweight low-rank adapter for efficiency.
- Designed a two-stage training procedure that jointly optimizes the base forecaster and the error feedback module.
- Achieved consistent accuracy improvements (5-10% average MAE reduction) across 5 backbone architectures and 10 datasets, demonstrating strong robustness to distribution shifts.

## Limitations

The paper focuses on improving accuracy via residual feedback; further exploration into *why* specific residuals correlate with future error could lead to more theoretically grounded improvements.

## Open Questions & Future Work

- [[tefl-extension-to-online-learning]]

## Key Concepts

- [Temporal Error Feedback Learning](../concepts/temporal-error-feedback-learning.md): A unified framework that explicitly incorporates historical prediction residuals from rolling forecasts into the deep time series forecasting pipeline during both training and evaluation.

## Datasets

- [10 real-world datasets](../datasets/10-real-world-datasets.md)

## Limitations

The paper focuses on improving accuracy via residual feedback; further exploration into *why* specific residuals correlate with future error could lead to more theoretically grounded improvements.

## Links

- [Abstract](https://arxiv.org/abs/2602.22520)
- [PDF](https://arxiv.org/pdf/2602.22520)

