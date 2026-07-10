---
# CSL-compatible fields
title: "Revision Risk in Real-Time Macroeconomic Forecasting"
author:
  - literal: "Yizhou Kuang"
issued:
  date-parts:
    - [2026, 7, 7]
url: "https://arxiv.org/abs/2607.05882"

# Custom fields
paper_id: "2607.05882"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "revision-risk-decomposition"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-10T08:15:11Z"
created_at: "2026-07-10T08:15:11Z"
---

# Revision Risk in Real-Time Macroeconomic Forecasting

**Authors**: Yizhou Kuang
**Date**: 2026-07-07
**Paper ID**: [openalex:2607.05882](https://arxiv.org/abs/2607.05882)

## Summary

This paper addresses the challenge of quantifying macroeconomic forecast uncertainty when outcomes are subject to subsequent data revisions. By decomposing Mean Squared Error into preliminary forecast risk, revision risk, and their covariance, the author quantifies the impact of data updates on target accuracy. The work further provides a strategy for robust uncertainty identification in real-time settings where dependence between errors and revisions is unknown, offering actionable methods for late calibration and dependence-robust transport.

## Key Contributions

- Introduces a decomposition framework for later-outcome Mean Squared Error (MSE) that explicitly separates preliminary forecast risk and revision risk.
- Demonstrates using Survey of Professional Forecasters (SPF) data that revisions contribute significantly more to later-outcome MSE in real-activity targets (8.3%) than in inflation targets (3.6%).
- Proposes methods for partial identification of later-outcome uncertainty using Frechet-Makarov sets and robust dependence modeling for real-time forecast calibration.

## Open Questions & Future Work

- [[optimizing-real-time-forecast-uncertainty-transport]]

## Key Concepts

- [[revision-risk-decomposition]]: A methodology for partitioning mean squared error in macroeconomic forecasts into preliminary risk and revision-induced risk components.

## Archivist Review

The revision risk decomposition is a fundamental conceptual contribution that disentangles sources of forecast error, providing a necessary framework for any system where data updates are a primary source of uncertainty. The open question regarding the optimization of uncertainty transport addresses the trade-off between coverage, stability, and method-specific assumptions in the absence of complete outcome data, which is a major, unresolved bottleneck in real-time forecasting.

### Approved Concepts
- Revision Risk Decomposition: Provides a necessary formal framework to separate uncertainty originating from original forecast error versus uncertainty introduced by later data revisions, a critical distinction in economic and operational time series.

### Approved Open Questions
- Optimizing Real-Time Forecast Uncertainty Transport: Understanding the limitations of uncertainty transport is crucial for reliable macroeconomic policy-making and automated economic reporting systems.

## Links

- [Abstract](https://arxiv.org/abs/2607.05882)
- [PDF](https://arxiv.org/pdf/2607.05882)

