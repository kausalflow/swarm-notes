---
# CSL-compatible fields
title: "Bootstrapping Generalization Error Bounds for Time Series"
author:
  - literal: "Robert Lunde"
  - literal: "Cosma Rohilla Shalizi"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/1711.02834"

# Custom fields
paper_id: "1711.02834"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-12T06:06:35Z"
created_at: "2026-08-12T06:06:35Z"
---

# Bootstrapping Generalization Error Bounds for Time Series

**Authors**: Robert Lunde, Cosma Rohilla Shalizi
**Date**: 2026-08-10
**Paper ID**: [openalex:1711.02834](https://arxiv.org/abs/1711.02834)

## Summary

This paper investigates the construction of confidence intervals for forecasting risk in stationary ergodic stochastic processes using models estimated from historical data. The authors prove that a bootstrap procedure produces valid confidence intervals when the data source is sufficiently mixing and the loss and estimator functions are smooth. They demonstrate that least-squares fitted autoregressive models satisfy these regularity conditions even when misspecified, backed by finite-sample simulation results.

## Key Contributions

- Proves that a bootstrap procedure yields valid confidence intervals for forecasting risk in stationary ergodic stochastic processes under mixing conditions and smoothness constraints.
- Establishes that least-squares estimated autoregressive (AR(d)) models satisfy the required regularity conditions even under misspecification.
- Derives sufficient conditions for the asymptotic independence of empirical distribution functions formed by splitting process realizations.

## Open Questions & Future Work

- [[growing-memory-and-model-generalization-for-time-series-bootstrap]]

## Archivist Review

The paper presents theoretical work on bootstrapping generalization error bounds for time series forecasting. No reusable algorithmic concept note was proposed or warranted, but the open question regarding growing-memory and nonparametric extension is valuable and meets our criteria for approval.

### Approved Open Questions
- Growing Memory and Non-Parametric Time Series Bootstrap: Crucial for scaling time series risk bounding and model selection techniques to modern high-dimensional or nonparametric machine learning architectures.

## Links

- [Abstract](https://arxiv.org/abs/1711.02834)
- [PDF](https://arxiv.org/pdf/1711.02834)

