---
# CSL-compatible fields
title: "Model-agnostic noise reduction for high-dimensional time series data"
author:
  - literal: "Bram Wouters"
  - literal: "Cees Diks"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27614"

# Custom fields
paper_id: "2609.27614"
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
processed_at: "2026-09-26T09:36:52Z"
created_at: "2026-09-26T09:36:52Z"
---

# Model-agnostic noise reduction for high-dimensional time series data

**Authors**: Bram Wouters, Cees Diks
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27614](https://arxiv.org/abs/2609.27614)

## Summary

This paper develops a model-agnostic noise reduction framework for high-dimensional time series designed to recover low-dimensional latent dynamic components contaminated by observational white noise. Assuming latent dynamics inhabit a low-dimensional linear dynamic subspace, the authors characterize the optimal linear projection using lagged covariance matrices, bootstrap dimension selection, and low-rank noise representations. Theoretical proofs establish that the denoised series converges at the standard parametric rate under mild conditions. Extensive simulations and empirical applications to high-dimensional stock returns and macroeconomic indicators demonstrate superior subspace estimation, reconstruction error, and one-step-ahead forecast accuracy compared to standard orthogonal projection and raw data baselines.

## Key Contributions

- Developed a model-agnostic noise reduction framework for high-dimensional time series that targets recovery of low-dimensional latent dynamic components under observational white noise.
- Characterized the optimal linear projection onto the dynamic subspace and provided a geometric description of residual error via signal-noise space orientation.
- Proposed robust estimators using lagged covariance matrices, bootstrap dimension selection, and structured low-rank noise representation, proving parametric convergence rates.
- Demonstrated through simulations and empirical applications to stock returns and macroeconomic indicators that the method improves subspace estimation and one-step-ahead forecasting.

## Archivist Review

The paper proposes a model-agnostic noise reduction method using lagged covariance matrices and linear projections for high-dimensional time series. Since this builds upon classical linear subspace methods and covariance estimation rather than introducing a distinct reusable architectural concept or a high-impact open question, all candidates were rejected to maintain vault rigor.

### Rejected Candidates
- [open_question] Regularization for High-Dimensional Denoising (`regularization-for-high-dimensional-denoising`) - low_impact: The question concerns standard ridge regularization and overfitting in high-dimensional estimation, which is broad and lacks specific methodological novelty beyond general high-dimensional statistics.

## Links

- [Abstract](https://arxiv.org/abs/2609.27614)
- [PDF](https://arxiv.org/pdf/2609.27614)

