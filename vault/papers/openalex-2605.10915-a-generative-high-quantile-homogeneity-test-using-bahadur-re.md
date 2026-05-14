---
# CSL-compatible fields
title: "A Generative High Quantile Homogeneity Test Using Bahadur Representation for Heteroskedastic High Quantile Regression of Tail Dependent Time Series"
author:
  - literal: "Ting Zhang"
  - literal: "Fangwei Wu"
  - literal: "Jingying Gao"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10915"

# Custom fields
paper_id: "2605.10915"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bahadur-representation-for-high-quantile-regression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:11Z"
created_at: "2026-05-14T07:38:11Z"
---

# A Generative High Quantile Homogeneity Test Using Bahadur Representation for Heteroskedastic High Quantile Regression of Tail Dependent Time Series

**Authors**: Ting Zhang, Fangwei Wu, Jingying Gao
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10915](https://arxiv.org/abs/2605.10915)

## Summary

This paper addresses the problem of testing homogeneity across different high quantiles in tail-dependent, heteroskedastic time series. The authors introduce a novel Bahadur representation theorem that provides an explicit error bound, effectively linearizing complex nonlinear high quantile estimators. This theoretical foundation is then utilized to construct a generative homogeneity test capable of identifying invariant effects of explanatory variables within the tail distribution. The approach is validated on both synthetic data and real-world financial or environmental time series applications.

## Key Contributions

- Developed a novel Bahadur representation for high quantile regression estimators in tail-dependent time series under heteroskedastic conditions.
- Proposed a generative high quantile homogeneity test that identifies whether explanatory variables have constant effects across different tail quantiles.
- Demonstrated the test's efficacy in handling non-stationary auxiliary processes and heteroskedasticity through both synthetic and empirical data analysis.

## Open Questions & Future Work

- [[unifying-asymptotic-inference-regimes-for-high-quantile-tests]]

## Key Concepts

- [[bahadur-representation-for-high-quantile-regression]]: A linear approximation framework for nonlinear high quantile regression estimators in tail-dependent, heteroskedastic time series.

## Archivist Review

I approved the Bahadur representation concept as a fundamental theoretical tool for high-quantile time series analysis and the open question regarding the unification of asymptotic inference regimes, as both address substantial, reusable challenges in non-stationary tail-dependent modeling. The proposed generative test itself was rejected as a paper-local application of the representation theorem. No datasets were approved as none were specifically named as central, standardized benchmarks in the provided text.

### Approved Concepts
- Bahadur Representation for High Quantile Regression: Provides a foundational linear approximation for nonlinear high quantile estimators, enabling theoretical analysis under non-stationarity and heteroskedasticity.

### Approved Open Questions
- Unifying Asymptotic Inference Regimes: This is a fundamental bottleneck for the practical deployment of high-quantile homogeneity tests, as it directly impacts the validity and reproducibility of statistical conclusions in applied time series analysis.

## Links

- [Abstract](https://arxiv.org/abs/2605.10915)
- [PDF](https://arxiv.org/pdf/2605.10915)

