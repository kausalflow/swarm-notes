---
# CSL-compatible fields
title: "Forecasting Inflation with Microdata: An Adaptive Machine Learning Approach"
author:
  - literal: "Catherine Chen"
  - literal: "Chen Gao"
  - literal: "Jonathon Hazell"
  - literal: "Lihua Lei"
  - literal: "Chen Lian"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12345"

# Custom fields
paper_id: "2607.12345"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "scan-test-for-forecasting-performance"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:09:53Z"
created_at: "2026-07-17T07:09:53Z"
---

# Forecasting Inflation with Microdata: An Adaptive Machine Learning Approach

**Authors**: Catherine Chen, Chen Gao, Jonathon Hazell, Lihua Lei, Chen Lian
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12345](https://arxiv.org/abs/2607.12345)

## Summary

This paper investigates the utility of microeconomic heterogeneity for forecasting aggregate inflation in non-stationary settings. The authors introduce a scan test to identify intermittent periods of forecasting superiority and an adaptive pipeline that utilizes high-dimensional microdata distributions via gradient boosted trees. Empirical results on UK data show that this adaptive approach significantly outperforms univariate benchmarks, specifically following the volatile economic period post-2020.

## Key Contributions

- Proposed a scan test to detect periods of relative forecasting outperformance in non-stationary time series.
- Developed an adaptive machine learning pipeline that dynamically integrates microdata-driven forecasts based on detected performance regimes.
- Demonstrated that microeconomic data significantly improves aggregate inflation forecasting performance, particularly following major economic shocks since 2020.

## Open Questions & Future Work

- [[microdata-inflation-forecasting-limits]]

## Key Concepts

- [[scan-test-for-forecasting-performance]]: A statistical test for identifying windows of relative forecasting superiority with unknown timing and duration.

## Archivist Review

The scan test is approved as a formal, reusable statistical methodology for evaluating intermittent model superiority. The open question is approved for its focus on the fundamental tension between microdata high-dimensionality and macroeconomic non-stationarity. Other candidates were rejected for being overly generic architectural descriptions.

### Approved Concepts
- Scan Test for Forecasting Performance: Provides a principled, model-agnostic method to detect transient regimes of forecasting superiority in non-stationary time series.

### Approved Open Questions
- Microdata Inflation Forecasting Limits: This addresses the trade-off between utilizing big-data micro sources and the statistical limits of macroeconomic forecasting, crucial for model reliability in real-world policy contexts.

### Rejected Candidates
- [concept] Adaptive Machine Learning Pipeline (`adaptive-ml-inflation-pipeline`) - generic: The concept of an adaptive pipeline is too generic and lacks the specific algorithmic structure required for a permanent vault note.

## Links

- [Abstract](https://arxiv.org/abs/2607.12345)
- [PDF](https://arxiv.org/pdf/2607.12345)

