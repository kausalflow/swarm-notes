---
# CSL-compatible fields
title: "Fast Data Inversion for High-Dimensional Ornstein–Uhlenbeck Processes from Noisy Measurements"
author:
  - literal: "Yizi Lin"
  - literal: "Xubo Liu"
  - literal: "P. Segall"
  - literal: "Mengyang Gu"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2501.01324"

# Custom fields
paper_id: "2501.01324"
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
processed_at: "2026-08-01T07:23:40Z"
created_at: "2026-08-01T07:23:40Z"
---

# Fast Data Inversion for High-Dimensional Ornstein–Uhlenbeck Processes from Noisy Measurements

**Authors**: Yizi Lin, Xubo Liu, P. Segall, Mengyang Gu
**Date**: 2026-07-29
**Paper ID**: [openalex:2501.01324](https://arxiv.org/abs/2501.01324)

## Summary

This paper develops a scalable latent factor model for high-dimensional dynamical systems governed by Ornstein-Uhlenbeck processes from noisy measurements. By employing an orthogonal factor loading matrix and deriving closed-form expectation-maximization updates, the method avoids costly posterior covariance inversions during Kalman filtering. Extensive simulations and an application to geodetic measurements of slow slip events in the Cascadia region demonstrate substantial acceleration, superior accuracy, and better agreement with seismic tremor data compared to existing alternatives.

## Key Contributions

- Develops a scalable approach for flexible latent factor models in high-dimensional dynamical systems driven by Ornstein-Uhlenbeck processes.
- Utilizes an orthogonal factor loading matrix to eliminate posterior covariance matrix inversions during Kalman filtering.
- Derives closed-form expressions in an expectation-maximization algorithm for exact parameter estimation without approximations.
- Demonstrates superior accuracy and scalability on simulated data and better agreement with seismic tremor data when estimating slow slip events in the Cascadia region.

## Archivist Review

After careful review, all candidates were rejected. The proposed concept is a paper-local algorithmic implementation for high-dimensional Ornstein-Uhlenbeck processes, and the open questions are either standard technical extensions or generic missing-data challenges.

### Rejected Candidates
- [concept] Fast Data Inversion for High-Dimensional Ornstein–Uhlenbeck Processes (`fast-data-inversion-for-high-dimensional-ornstein-uhlenbeck-processes`) - paper_local: Paper-local methodological combination of orthogonal factor loadings and EM updates for Ornstein-Uhlenbeck processes, lacking broad standalone reusability across diverse machine learning contexts.
- [open_question] Extension to Matérn Gaussian Processes (`matern-gaussian-process-extension`) - low_impact: A standard technical extension of a specific kernel class within a geostatistical/stochastic differential equation framework rather than a broad machine learning bottleneck.
- [open_question] Handling Irregular Missing Values (`irregular-missing-values-generalization`) - generic: A generic missing data handling extension that applies broadly across state-space models and time series forecasting rather than a novel structural research gap unique to this work.

## Links

- [Abstract](https://arxiv.org/abs/2501.01324)
- [PDF](https://arxiv.org/pdf/2501.01324)

