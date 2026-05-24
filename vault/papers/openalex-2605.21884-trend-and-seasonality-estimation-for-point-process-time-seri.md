---
# CSL-compatible fields
title: "Trend and seasonality estimation for point-process time series"
author:
  - literal: "Daniel Gervini"
  - literal: "Simon A. Kopischke"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.21884"

# Custom fields
paper_id: "2605.21884"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:45:52Z"
created_at: "2026-05-24T07:45:52Z"
---

# Trend and seasonality estimation for point-process time series

**Authors**: Daniel Gervini, Simon A. Kopischke
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.21884](https://arxiv.org/abs/2605.21884)

## Summary

This paper addresses the estimation of trend and seasonality for point-process time series modeled via doubly-stochastic Poisson processes with log-Gaussian intensity functions. The authors propose computationally efficient M-estimators and provide a theoretical foundation for their asymptotic properties. The effectiveness of these estimators is validated through numerical simulations and an empirical study of urban bike-sharing demand. This work bridges a gap in temporal point-process modeling by providing interpretable and statistically grounded trend and seasonality decomposition.

## Key Contributions

- Introduces a novel M-estimator for trend and seasonality specifically designed for point-process time series.
- Models point processes using a doubly-stochastic Poisson framework with log-Gaussian intensity functions.
- Provides rigorous derivation of the asymptotic distribution of the proposed estimators to support inference.
- Demonstrates practical utility and predictive performance by analyzing bike demand patterns in the Chicago Divvy system.

## Open Questions & Future Work

- [[asymptotic-variance-estimation-point-process-models]]

## Archivist Review

I have approved one open question related to asymptotic variance in point-process models, as it represents a fundamental statistical bottleneck in applying these estimators to real-world data. No concepts were approved because the proposed M-estimator for point-process trend/seasonality is a specific methodological contribution that does not yet possess the broad, reusable identity required for a permanent vault note. I have updated the slug of the open question to be more descriptive and compliant with existing taxonomy.

### Approved Open Questions
- Asymptotic variance for point-process models: This bottleneck prevents the reliable construction of confidence intervals and hypothesis testing for trend and seasonality estimates in point-process time series models.

### Rejected Candidates
- [open_question] Asymptotic variance estimation for point-process models (`asymptotic-variance-estimation-point-process`) - duplicate_existing: The slug was slightly modified to better align with vault naming conventions (adding 'models').

## Links

- [Abstract](https://arxiv.org/abs/2605.21884)
- [PDF](https://arxiv.org/pdf/2605.21884)

