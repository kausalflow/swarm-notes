---
# CSL-compatible fields
title: "Bias Correction of Long-memory Estimator of Functional Time Series via the Prefiltered Sieve Bootstrap"
author:
  - literal: "Chang Liu"
  - literal: "Han Lin Shang"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28177"

# Custom fields
paper_id: "2607.28177"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prefiltered-sieve-bootstrap"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:26:43Z"
created_at: "2026-08-02T07:26:43Z"
---

# Bias Correction of Long-memory Estimator of Functional Time Series via the Prefiltered Sieve Bootstrap

**Authors**: Chang Liu, Han Lin Shang
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28177](https://arxiv.org/abs/2607.28177)

## Summary

This paper investigates a sieve bootstrap-based bias correction procedure for estimating the long-memory parameter d in stationary and nonstationary fractionally integrated processes. The method relies on prefiltering data using a preliminary long-memory estimate—specifically recommending the local polynomial Whittle with noise (LPWN) estimator to handle strong short-range autoregressive dependence. Simulation studies demonstrate that this sieve bootstrap enhancement substantially reduces estimation bias while also generating reliable confidence intervals for the memory parameter.

## Key Contributions

- Proposed a bias correction procedure for estimating the long-memory parameter d in stationary and nonstationary fractionally integrated processes using sieve bootstrapping on prefiltered data.
- Recommended the local polynomial Whittle with noise (LPWN) estimator for initial estimation to mitigate strong short-range autoregressive dependence bias.
- Demonstrated via simulation studies that sieve bootstrap enhancement significantly improves the bias of long-memory estimators and provides reliable confidence intervals.

## Open Questions & Future Work

- [[joint-estimation-short-range-long-memory-functional-time-series]]

## Key Concepts

- [[prefiltered-sieve-bootstrap]]: A resampling-based bias correction method that applies the sieve bootstrap to prefiltered data to improve long-memory parameter estimation.

## Archivist Review

We approved the central methodological concept of prefiltered sieve bootstrap for long-memory parameter estimation and the open question concerning joint short-range and long-memory estimation, as they represent enduring, reusable contributions to time-series econometrics and functional time-series analysis.

### Approved Concepts
- Prefiltered Sieve Bootstrap: It introduces a novel sieve bootstrap procedure on prefiltered data specifically designed to correct estimation bias for long-memory parameters in fractionally integrated time series.

### Approved Open Questions
- Joint Short-Range and Long-Memory Estimation: Addressing the joint estimation of short-range dependence and long memory is critical for robust automated modeling of complex functional time series across demography and finance.

## Links

- [Abstract](https://arxiv.org/abs/2607.28177)
- [PDF](https://arxiv.org/pdf/2607.28177)

