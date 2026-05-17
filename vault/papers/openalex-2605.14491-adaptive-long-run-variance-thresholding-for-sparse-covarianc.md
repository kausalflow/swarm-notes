---
# CSL-compatible fields
title: "Adaptive Long-Run Variance Thresholding for Sparse Covariance Estimation in High-Dimensional Time Series"
author:
  - literal: "Wenhao Zhang"
  - literal: "Zhaoxing Gao"
issued:
  date-parts:
    - [2026, 5, 14]
url: "https://arxiv.org/abs/2605.14491"

# Custom fields
paper_id: "2605.14491"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-long-run-variance-thresholding"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-17T07:30:18Z"
created_at: "2026-05-17T07:30:18Z"
---

# Adaptive Long-Run Variance Thresholding for Sparse Covariance Estimation in High-Dimensional Time Series

**Authors**: Wenhao Zhang, Zhaoxing Gao
**Date**: 2026-05-14
**Paper ID**: [openalex:2605.14491](https://arxiv.org/abs/2605.14491)

## Summary

This paper addresses the challenge of sparse covariance estimation in high-dimensional time series, where temporal dependence renders standard independent-data thresholding methods ineffective. The authors propose a thresholding procedure that integrates long-run variance to adapt to temporal dependencies, ensuring consistency under the spectral norm. Theoretical results confirm that the method achieves optimal convergence rates and support recovery consistency, outperforming traditional approaches in simulated and real-world scenarios.

## Key Contributions

- Introduces an adaptive thresholding procedure for high-dimensional time series covariance estimation that incorporates long-run variance.
- Proves that the proposed estimator attains optimal consistency under the spectral norm and achieves support recovery consistency.
- Demonstrates via theoretical analysis and empirical simulations that traditional independent-data thresholding methods fail to recover covariance support in the presence of autocorrelation.

## Open Questions & Future Work

- [[tuning-parameter-selection-theory-for-covariance-thresholding]]

## Key Concepts

- [[adaptive-long-run-variance-thresholding]]: A sparse covariance estimation technique that uses entry-specific thresholds scaled by long-run variance to maintain consistency in autocorrelated time series.

## Archivist Review

I approved the core methodology (Adaptive Long-Run Variance Thresholding) as it addresses a fundamental problem in time-series statistics by incorporating temporal variance explicitly. I also approved the open question regarding threshold tuning, as the transition from heuristic to theoretical consistency is a significant bottleneck in high-dimensional statistical inference. Other candidates were rejected for being overly broad or representing generic future work paths.

### Approved Concepts
- Adaptive Long-Run Variance Thresholding: It provides a theoretically grounded framework to adjust thresholding for temporal dependence, which is a major failure point for standard independent-data estimators in high-dimensional settings.

### Approved Open Questions
- Consistency of Threshold Tuning: Statistical consistency of the resulting sparse estimator depends heavily on optimal parameter selection, and the absence of such theory limits the applicability of these models in critical infrastructure or research environments.

### Rejected Candidates
- [open_question] Generalization to Complex Dependence (`complex-dependence-theory`) - low_impact: This is a generic 'extend to more complex settings' direction that does not define a specific bottleneck mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.14491)
- [PDF](https://arxiv.org/pdf/2605.14491)

