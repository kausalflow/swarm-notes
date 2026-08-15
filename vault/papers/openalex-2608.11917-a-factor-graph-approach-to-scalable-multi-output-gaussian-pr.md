---
# CSL-compatible fields
title: "A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression"
author:
  - literal: "Wouter W. L. Nuijten"
  - literal: "Esther G. van Pelt"
  - literal: "Albert Podusenko"
  - literal: "İsmai̇l Şenöz"
  - literal: "Wouter M. Kouw"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.11917"

# Custom fields
paper_id: "2608.11917"
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
processed_at: "2026-08-15T05:15:22Z"
created_at: "2026-08-15T05:15:22Z"
---

# A Factor Graph Approach to Scalable Multi-Output Gaussian Process Regression

**Authors**: Wouter W. L. Nuijten, Esther G. van Pelt, Albert Podusenko, İsmai̇l Şenöz, Wouter M. Kouw
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.11917](https://arxiv.org/abs/2608.11917)

## Summary

This paper presents a scalable factor graph approach for multi-output Gaussian process regression by mapping inputs onto a nearest-neighbor chain and using linear-Gaussian transition factors with the linear model of coregionalization. Posterior computation is performed via exact Gaussian message passing with linear scaling in the number of data points and robust handling of missing observations. Evaluated on synthetic data and electricity time series forecasting, the method matches exact and approximate baselines in accuracy while offering superior computational scalability.

## Key Contributions

- Expresses multi-output Gaussian process regression as a Forney-style factor graph using a nearest-neighbor chain to order inputs into a 1D sequence
- Reduces posterior computation to exact Gaussian message passing along the chain with a complexity of O(C(DL^2 + L^3))
- Achieves linear scaling in the number of data points while matching exact kernel-matrix and sparse variational baselines in forecast accuracy on electricity time series forecasting

## Limitations

Best suited to candidate sets in low input dimension, with performance gaps growing gradually as input dimension increases

## Archivist Review

Applied rigorous filtering standards: no concepts or datasets met the strict novelty and reusability criteria, and the open question was rejected as routine future work evaluating on larger datasets.

### Rejected Candidates
- [open_question] High-Dimensional Real-World MOGP Evaluation (`high-dimensional-real-world-mogp-evaluation`) - low_impact: Standard future work proposing evaluation on higher-dimensional real-world datasets rather than addressing an intrinsic methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.11917)
- [PDF](https://arxiv.org/pdf/2608.11917)

