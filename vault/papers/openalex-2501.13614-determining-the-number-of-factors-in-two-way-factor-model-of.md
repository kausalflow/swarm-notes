---
# CSL-compatible fields
title: "Determining the Number of Factors in Two-way Factor Model of High-dimensional Matrix-variate Time Series: a White-noise Based Method for Serial Correlation Models"
author:
  - literal: "Qiang Xia"
  - literal: "W.K. Li"
  - literal: "Rubing Liang"
  - literal: "Qiang Xia"
  - literal: "W.K. Li"
  - literal: "Rubing Liang"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2501.13614"

# Custom fields
paper_id: "2501.13614"
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
  - "ratio-based-factor-estimation"
  - "reparameterized-matrix-factor-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:40:05Z"
created_at: "2026-06-06T07:40:05Z"
---

# Determining the Number of Factors in Two-way Factor Model of High-dimensional Matrix-variate Time Series: a White-noise Based Method for Serial Correlation Models

**Authors**: Qiang Xia, W.K. Li, Rubing Liang, Qiang Xia, W.K. Li, Rubing Liang
**Date**: 2026-06-03
**Paper ID**: [openalex:2501.13614](https://arxiv.org/abs/2501.13614)

## Summary

This paper presents a new two-way factor modeling framework for analyzing high-dimensional matrix-variate time series by leveraging white noise properties. The authors introduce ratio-based estimators for determining the dimensions of row and column factor spaces, utilizing both element-wise maximum and Frobenius norms of autocovariance matrices. Furthermore, they propose a reparameterization technique to address factor strength heterogeneity, ensuring robust estimation performance under regularity conditions. The methodology is rigorously supported by theoretical consistency proofs and validated through both Monte Carlo simulations and empirical application.

## Key Contributions

- Introduces a two-way factor modeling framework for high-dimensional matrix-variate time series that identifies white noise components to determine row and column factor dimensions.
- Develops ratio-based estimators using element-wise maximum norm and Frobenius norm of sample autocovariance matrices for consistent factor estimation.
- Proposes a reparameterization method to mitigate the impact of cross-row and cross-column factor strength heterogeneity in the original matrix factor model.

## Open Questions & Future Work

- [[robust-factor-number-estimation]]

## Key Concepts

- [[ratio-based-factor-estimation]]: An estimation method for determining the dimensions of row and column factor spaces in matrix-variate time series by analyzing autocovariance matrix norms.
- [[reparameterized-matrix-factor-model]]: A technique that simplifies matrix-variate factor models by decomposing them into separate row and column loading frameworks to mitigate factor strength heterogeneity.

## Archivist Review

The review focused on identifying the core methodological contributions for factor identification in matrix-variate time series. I approved the ratio-based estimation approach and the reparameterization technique as they represent distinct, reusable methodological shifts in handling factor dimensionality. I also formalized the open question regarding the robustness of factor estimation, as it represents a significant, recurring challenge in high-dimensional time series modeling.

### Approved Concepts
- Ratio-based Factor Estimation: This method provides a theoretically grounded approach for high-dimensional matrix-variate time series where standard eigenvalue-ratio methods fail due to serial correlation or factor heterogeneity.
- Reparameterized Matrix Factor Model: This technique decouples row and column factor effects, allowing for more stable estimation of dimensions in complex high-dimensional systems.

### Approved Open Questions
- Robust Factor Number Estimation: This is a central limitation in applying factor models to real-world high-dimensional time series, where misspecification of factor counts directly compromises predictive accuracy.

### Rejected Candidates
- [concept] White-noise Based Method (`white-noise-based-method`) - generic: This is a generic statistical property utilized by the authors rather than a standalone methodology deserving a permanent entry.

## Links

- [Abstract](https://arxiv.org/abs/2501.13614)
- [PDF](https://arxiv.org/pdf/2501.13614)

