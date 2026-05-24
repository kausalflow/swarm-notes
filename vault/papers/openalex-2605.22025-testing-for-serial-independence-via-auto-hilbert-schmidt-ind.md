---
# CSL-compatible fields
title: "Testing for Serial Independence via Auto Hilbert-Schmidt Independence Criterion"
author:
  - literal: "Muyi Li"
  - literal: "Yuqing Xu"
  - literal: "Zhou Zhou"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22025"

# Custom fields
paper_id: "2605.22025"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "autohsic"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:47:10Z"
created_at: "2026-05-24T07:47:10Z"
---

# Testing for Serial Independence via Auto Hilbert-Schmidt Independence Criterion

**Authors**: Muyi Li, Yuqing Xu, Zhou Zhou
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22025](https://arxiv.org/abs/2605.22025)

## Summary

This paper introduces AutoHSIC, a kernel-based framework designed to test for serial independence in strictly stationary time series. By constructing a lagged U-statistic, the method effectively detects nonlinear serial dependence across multivariate, functional, and matrix-valued data. The authors address the non-pivotal nature of the null distribution by providing an asymtotically valid wild bootstrap procedure and extend the approach for robust residual-based model diagnostics.

## Key Contributions

- Introduces AutoHSIC, a kernel-based statistic for detecting nonlinear serial dependence by measuring dependence between observations and their lagged counterparts.
- Establishes the limiting behavior of single-lag and portmanteau tests under the null and alternative hypotheses, accounting for the degeneracy of lagged U-statistics.
- Develops a wild bootstrap procedure to approximate critical values for the non-pivotal limiting null distribution, ensuring asymptotic validity.
- Extends the framework to residual-based diagnostics for model verification.

## Open Questions & Future Work

- [[non-euclidean-residual-diagnostics-theory]]

## Key Concepts

- [[autohsic]]: A kernel-based framework for testing serial independence in stationary time series by measuring the dependence between observations and their lags.

## Archivist Review

I approved AutoHSIC as a reusable kernel-based diagnostic tool for non-linear serial dependence and added a refined open question concerning the non-Euclidean theoretical foundations of residual-based diagnostics. The second open question was rejected for being speculative and lacking a clear technical bottleneck. No datasets were approved as none were central to the paper's claimed novelty.

### Approved Concepts
- Auto Hilbert-Schmidt Independence Criterion: It provides a rigorous kernel-based statistical framework for detecting complex nonlinear serial dependencies in time series, addressing limitations of traditional linear autocorrelation tests.

### Approved Open Questions
- Non-Euclidean Residual Diagnostic Theory: This is a critical gap for applying robust model diagnostic tools to complex time series data where Euclidean assumptions are invalid.

### Rejected Candidates
- [open_question] Spectral Kernel Independence Tests (`spectral-kernel-independence-tests`) - low_impact: The proposal for spectral approaches is speculative and does not clearly define a technical bottleneck beyond typical feature selection or hyperparameter tuning issues.

## Links

- [Abstract](https://arxiv.org/abs/2605.22025)
- [PDF](https://arxiv.org/pdf/2605.22025)

