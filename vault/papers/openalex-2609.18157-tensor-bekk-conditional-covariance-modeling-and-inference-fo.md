---
# CSL-compatible fields
title: "Tensor-BEKK: Conditional Covariance Modeling and Inference for Tensor-Valued Time Series"
author:
  - literal: "Huan Gong"
  - literal: "Feiyu Jiang"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18157"

# Custom fields
paper_id: "2609.18157"
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
  - "tensor-bekk"
  - "tensor-factor-bekk"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:03:40Z"
created_at: "2026-09-19T09:03:40Z"
---

# Tensor-BEKK: Conditional Covariance Modeling and Inference for Tensor-Valued Time Series

**Authors**: Huan Gong, Feiyu Jiang
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18157](https://arxiv.org/abs/2609.18157)

## Summary

This paper introduces the Tensor-BEKK (T-BEKK) and Tensor-Factor-BEKK (TF-BEKK) models for conditional covariance modeling of tensor-valued time series. By imposing Kronecker structures on the BEKK specification, the proposed framework successfully reduces parameter dimensionality while preserving positive definiteness and providing mode-specific interpretations of volatility dynamics. The authors establish theoretical asymptotic properties, develop dedicated score tests and portmanteau diagnostics, and demonstrate the empirical utility using currency futures and Chinese equity tensor portfolios.

## Key Contributions

- Proposes the Tensor-BEKK (T-BEKK) model to capture conditional covariance dynamics of tensor-valued time series using Kronecker-structured parameterizations on intercept, ARCH, and GARCH matrices.
- Establishes theoretical properties including stationarity, identification, and asymptotic properties of the Gaussian quasi-maximum likelihood estimator.
- Develops mode-specific restricted score tests, spillover intensity inference procedures, and a portmanteau diagnostic test based on quadratic form residuals.
- Introduces the Tensor-Factor-BEKK (TF-BEKK) model for higher-dimensional settings with an asymptotically equivalent feasible second-step QMLE.

## Open Questions & Future Work

- [[extensions-of-tensor-bekk-models]]

## Key Concepts

- [[tensor-bekk]]: A tensor-structured BEKK model for conditional covariance dynamics in tensor-valued time series that imposes Kronecker structures on parameters to reduce dimensionality.
- [[tensor-factor-bekk]]: A factor-based extension of the Tensor-BEKK model designed for high-dimensional tensor-valued time series.

## Archivist Review

Approved the two canonical tensor-based conditional covariance models (Tensor-BEKK and Tensor-Factor-BEKK) and a key open question regarding their extensions to asymmetries and high-dimensional sparsity. These entries expand the vault's coverage of tensor-valued time series modeling and volatility forecasting.

### Approved Concepts
- Tensor-BEKK: Introduces a tensor-structured extension of the classical BEKK model for conditional covariance modeling of tensor-valued time series.
- Tensor-Factor-BEKK: Provides a factor-based dimensionality reduction extension for high-dimensional tensor-valued conditional covariance modeling.

### Approved Open Questions
- Extensions of Tensor-BEKK Models: Crucial for enhancing the modeling flexibility of tensor-based conditional covariance frameworks to handle financial asymmetries and extremely high ambient dimensions.

## Links

- [Abstract](https://arxiv.org/abs/2609.18157)
- [PDF](https://arxiv.org/pdf/2609.18157)

