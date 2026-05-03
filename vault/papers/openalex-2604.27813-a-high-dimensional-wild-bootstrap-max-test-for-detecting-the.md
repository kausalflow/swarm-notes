---
# CSL-compatible fields
title: "A High Dimensional Wild Bootstrap Max-Test for Detecting the Presence of Significant Predictors"
author:
  - literal: "Jonathan B. Hill"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27813"

# Custom fields
paper_id: "2604.27813"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "high-dimensional-wild-bootstrap-max-test"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:45Z"
created_at: "2026-05-03T07:14:45Z"
---

# A High Dimensional Wild Bootstrap Max-Test for Detecting the Presence of Significant Predictors

**Authors**: Jonathan B. Hill
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27813](https://arxiv.org/abs/2604.27813)

## Summary

The paper develops a block bootstrap max-test for detecting significant predictors in high-dimensional settings where the number of covariates grows exponentially with the sample size. The approach assumes physical dependence in time series and avoids the computational and inferential hurdles of covariance matrix estimation and Bonferroni corrections. By using a multiplier (wild) block bootstrap, it effectively approximates the non-standard limit distribution of the max-statistic, providing reliable size control and performance against weak signals. The method is validated through simulations and an empirical application involving the VIX volatility index.

## Key Contributions

- Proposes a block bootstrap max-test for high-dimensional predictor screening that remains valid when p >> n and growth is exponential.
- Eliminates the need for explicit covariance matrix estimation and post-hoc Bonferroni corrections by leveraging the properties of the max-statistic.
- Demonstrates robustness for weakly dependent and non-stationary data under physical dependence assumptions.

## Open Questions & Future Work

- [[inference-for-adaptively-selected-covariates]]

## Key Concepts

- [[high-dimensional-wild-bootstrap-max-test]]: A bootstrap-based max-test for detecting significant predictors in high-dimensional settings with weakly dependent, heterogeneous data.

## Archivist Review

I approved the primary contribution of the high-dimensional max-test as it provides a distinct, non-asymptotic approach to variable screening in high-dimensional time series. I also approved the open question regarding inference for adaptively selected predictors, as this remains a fundamental bottleneck in the field of high-dimensional statistics and time series modeling. Other candidates were rejected to maintain strict vault standards against paper-local terminology or routine extensions.

### Approved Concepts
- High-Dimensional Wild Bootstrap Max-Test: It provides a methodology for high-dimensional significance testing while avoiding covariance matrix estimation and Bonferroni corrections.

### Approved Open Questions
- Inference for adaptively selected covariates: Formalizing inference for endogenously selected predictors is critical for the reliability of predictive modeling in high-dimensional regimes.

## Links

- [Abstract](https://arxiv.org/abs/2604.27813)
- [PDF](https://arxiv.org/pdf/2604.27813)

