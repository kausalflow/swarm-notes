---
# CSL-compatible fields
title: "SCORE: Spectral Correlation Estimation for Multivariate Gaussians"
author:
  - literal: "Christopher Bülte"
  - literal: "Emil Partow"
  - literal: "Astha Gupta"
  - literal: "Pascal Eßer"
  - literal: "Gitta Kutyniok"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12096"

# Custom fields
paper_id: "2610.12096"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "score-spectral-correlation-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:04:49Z"
created_at: "2026-10-11T11:04:49Z"
---

# SCORE: Spectral Correlation Estimation for Multivariate Gaussians

**Authors**: Christopher Bülte, Emil Partow, Astha Gupta, Pascal Eßer, Gitta Kutyniok
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12096](https://arxiv.org/abs/2610.12096)

## Summary

We propose SCORE, a scalable framework for neural network-based predictive modeling with high-dimensional structured Gaussian targets that combines scoring rule training with spectral covariance approximation. By decomposing the learning task into marginals and a structured correlation matrix, the approach achieves linear storage and O(d log d) computational cost while handling degenerate covariances via closed-form Gaussian kernel scores. Theoretical analysis includes finite-sample PAC bounds demonstrating additive stage errors and exact invariance under unitary transforms. Evaluations across time-series forecasting, monocular depth estimation, and spatial weather prediction demonstrate improved performance at reduced computational cost.

## Key Contributions

- Proposes SCORE, a scalable framework combining scoring rule training with spectral covariance approximation for high-dimensional Gaussian targets.
- Decomposes the learning task into marginal distributions and a structured correlation matrix, achieving linear storage and O(d log d) cost.
- Utilizes closed-form Gaussian kernel scores that remain well-defined for degenerate covariances and provide bounded gradients.
- Establishes finite-sample PAC bounds showing additive error behavior between the two learning stages.

## Open Questions & Future Work

- [[beyond-circulant-covariance-spectral-estimation]]

## Key Concepts

- [[score-spectral-correlation-estimation]]: A scalable framework for high-dimensional Gaussian targets that combines scoring rule training with spectral covariance approximation.

## Archivist Review

Approved the core SCORE concept and the open question regarding extending spectral covariance estimation beyond circulant structures. No datasets met the naming criteria for permanent standalone vault notes.

### Approved Concepts
- SCORE (Spectral Correlation Estimation): Provides a scalable framework combining scoring rule training with spectral covariance approximation for high-dimensional multivariate Gaussian targets.

### Approved Open Questions
- Beyond Circulant Covariance in Spectral Estimation: Addresses the primary structural limitation of circulant spectral covariance approximations in multivariate predictive modeling.

## Links

- [Abstract](https://arxiv.org/abs/2610.12096)
- [PDF](https://arxiv.org/pdf/2610.12096)

