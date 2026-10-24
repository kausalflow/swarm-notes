---
# CSL-compatible fields
title: "SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning"
author:
  - literal: "Jingbo Wang"
  - literal: "Kegeng Tang"
  - literal: "Zihao Wang"
  - literal: "Shaogang Ren"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29992"

# Custom fields
paper_id: "2610.29992"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:12:42Z"
created_at: "2026-10-24T09:12:42Z"
---

# SCDM: Scalable Causal Discovery in Nonlinear Temporal Systems with Meta-Learning

**Authors**: Jingbo Wang, Kegeng Tang, Zihao Wang, Shaogang Ren
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29992](https://arxiv.org/abs/2610.29992)

## Summary

Causal discovery in high-dimensional nonlinear temporal systems is often bottlenecked by expensive target-wise fitting or graph-search procedures. To address this, the paper introduces SCDM, a shared-parameter meta-learning framework that treats each target variable as a task while learning a shared temporal predictor and a shared causal-strength matrix. Through episodic updates and a post-training graph readout, SCDM efficiently accumulates structural evidence across the full system. Theoretical recovery guarantees and evaluations on high-dimensional synthetic and real-world benchmarks demonstrate superior scalability and causal recovery performance.

## Key Contributions

- Proposes SCDM, a scalable meta-learning framework for causal discovery in nonlinear multivariate time series that avoids exhaustive target-wise optimization.
- Formulates each target variable as a meta-task while learning a shared temporal predictor and a shared causal-strength matrix.
- Establishes a finite-error recovery principle proving that thresholding learned causal scores recovers the underlying graph under specific risk-gap and error conditions.
- Demonstrates competitive causal recovery and improved scalability on high-dimensional synthetic, neuroimaging-inspired, and real-world temporal benchmarks.

## Open Questions & Future Work

- [[adaptive-lag-selection-and-hidden-confounders]]

## Archivist Review

Applied strict selection criteria. No reusable time-series forecasting mechanism or dataset warrants permanent vault storage, but the open question regarding adaptive lag selection and hidden confounders in causal discovery provides a solid, specific direction for future research.

### Approved Open Questions
- Adaptive Lags and Hidden Confounders: Important for extending scalable meta-learning causal discovery frameworks to handle realistic real-world settings with unobserved confounding and unknown temporal delays.

## Links

- [Abstract](https://arxiv.org/abs/2610.29992)
- [PDF](https://arxiv.org/pdf/2610.29992)

