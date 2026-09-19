---
# CSL-compatible fields
title: "Exponential Smoothing for Time Series of Random Objects"
author:
  - literal: "Takuo Matsubara"
  - literal: "Peiwen Jiang"
  - literal: "Wilson Ye Chen"
  - literal: "Minh-Ngoc Tran"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20274"

# Custom fields
paper_id: "2609.20274"
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
  - "geodesic-exponential-smoothing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:03:03Z"
created_at: "2026-09-19T09:03:03Z"
---

# Exponential Smoothing for Time Series of Random Objects

**Authors**: Takuo Matsubara, Peiwen Jiang, Wilson Ye Chen, Minh-Ngoc Tran
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20274](https://arxiv.org/abs/2609.20274)

## Summary

The paper introduces geodesic exponential smoothing, extending standard exponential smoothing to time series of random objects residing in Hadamard spaces. By utilizing geodesics, the method updates forecasts in constant time per observation using a single scalar parameter without requiring stationarity. Theoretical guarantees, including almost-sure consistency, are established, and the approach is evaluated on covariance-matrix, distributional, and functional time series applications.

## Key Contributions

- Introduces geodesic exponential smoothing as a generalization of exponential smoothing for time series in Hadamard spaces.
- Proposes an innovations mechanism providing a metric-space analog of the innovations state-space model with constant-time online updates.
- Establishes sample-path properties and almost-sure consistency of the smoothing-parameter estimator via quasilinearization in Hadamard spaces.
- Demonstrates forecasting performance across covariance-matrix, distributional, and functional time series real-data applications.

## Open Questions & Future Work

- [[curvature-serial-dependence-decay]]

## Key Concepts

- [[geodesic-exponential-smoothing]]: A generalization of exponential smoothing to time series in Hadamard spaces where the forecast level moves along the geodesic toward each new observation.

## Archivist Review

Approved the central concept of geodesic exponential smoothing and a well-defined theoretical open question concerning serial dependence decay under curvature. Rejected the second open question as it outlines future model extensions rather than a core theoretical limitation. No standalone named dataset was present.

### Approved Concepts
- Geodesic Exponential Smoothing: Central methodological contribution, extending exponential smoothing to object-valued time series in metric spaces via geodesics.

### Approved Open Questions
- Serial Dependence Decay under Curvature: Understanding the precise decay of serial dependence under curvature is crucial for extending inference and testing tools from Euclidean or Hilbert space settings to general non-Euclidean metric spaces.

### Rejected Candidates
- [open_question] Trend and Seasonal Geodesic Smoothing (`geodesic-trend-corrected-smoothing`) - low_impact: Speculative future work extending level-only smoothing to trends without a concrete foundational bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.20274)
- [PDF](https://arxiv.org/pdf/2609.20274)

