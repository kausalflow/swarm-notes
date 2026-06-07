---
# CSL-compatible fields
title: "Wasserstein Exponential Smoothing"
author:
  - literal: "Takuo Matsubara"
  - literal: "Peiwen Jiang"
  - literal: "Minh-Ngoc Tran"
  - literal: "Wilson Ye Chen"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05560"

# Custom fields
paper_id: "2606.05560"
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
  - "wasserstein-exponential-smoothing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:32Z"
created_at: "2026-06-07T08:19:32Z"
---

# Wasserstein Exponential Smoothing

**Authors**: Takuo Matsubara, Peiwen Jiang, Minh-Ngoc Tran, Wilson Ye Chen
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05560](https://arxiv.org/abs/2606.05560)

## Summary

This paper extends the classical exponential smoothing (ES) methodology to distributional time series, where observations are probability distributions rather than scalar values. The proposed Wasserstein Exponential Smoothing (WES) retains the simplicity and parsimony of traditional ES while operating within the Wasserstein space. Theoretical consistency for parameter estimation is established by minimizing Wasserstein distance, and empirical results confirm its effectiveness in forecasting complex financial and utility datasets.

## Key Contributions

- Introduces Wasserstein Exponential Smoothing (WES), an extension of classical exponential smoothing to distributional time series data.
- Develops a consistent estimation method for the smoothing parameter based on minimizing Wasserstein distances.
- Demonstrates superior practical effectiveness over existing methods on high-frequency financial returns and household electricity demand datasets.

## Open Questions & Future Work

- [[multivariate-wasserstein-exponential-smoothing]]

## Key Concepts

- [[wasserstein-exponential-smoothing]]: A generalization of classical exponential smoothing for time series of probability distributions using the Wasserstein distance.

## Archivist Review

I approved the core Wasserstein Exponential Smoothing concept as a generalizable methodology for distributional time series forecasting. The open question regarding the multivariate extension of this framework addresses a clear technical limitation that is central to the future scalability and utility of this class of models. No datasets were approved as none were specifically named or provided as central novel contributions.

### Approved Concepts
- Wasserstein Exponential Smoothing: It provides a foundational extension of classic exponential smoothing to distributional data using the Wasserstein metric.

### Approved Open Questions
- Multivariate Wasserstein Exponential Smoothing: This is critical because many real-world distributional time series, such as multivariate financial assets or multi-dimensional biosensor readings, naturally reside in higher-dimensional spaces. Without this extension, the applicability of the WES framework remains fundamentally limited.

## Links

- [Abstract](https://arxiv.org/abs/2606.05560)
- [PDF](https://arxiv.org/pdf/2606.05560)

