---
# CSL-compatible fields
title: "Principled Koopman Representations with Kalman Inference for Efficient Time-Series Prediction"
author:
  - literal: "Ruiquan Li"
  - literal: "Yuheng Bu"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17815"

# Custom fields
paper_id: "2609.17815"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "k2svd"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:16:46Z"
created_at: "2026-09-18T09:16:46Z"
---

# Principled Koopman Representations with Kalman Inference for Efficient Time-Series Prediction

**Authors**: Ruiquan Li, Yuheng Bu
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17815](https://arxiv.org/abs/2609.17815)

## Summary

The paper introduces K^2SVD, a principled framework for time-series prediction that learns valid low-rank Koopman operator representations via a Hilbert-Schmidt objective. By combining this compact latent space with a linear Gaussian state-space model and Kalman filtering for inference, the method effectively mitigates noise accumulation during multi-step forecasting. Empirical evaluations demonstrate state-of-the-art accuracy, dramatically reduced latent dimensions, and faster computational speeds compared to existing baselines.

## Key Contributions

- Introduces K^2SVD, which explicitly learns the leading singular functions of the Koopman operator by optimizing a Hilbert-Schmidt objective to construct a mathematically consistent low-rank latent space.
- Employs a linear Gaussian state-space model in the learned Koopman space and performs inference via Kalman filtering to mitigate noise accumulation during multi-step forecasting.
- Achieves superior performance and significantly faster prediction speeds with a compact latent space using under 10% of the dimensions of prior methods across multiple datasets.

## Open Questions & Future Work

- [[adaptive-koopman-rank-and-time-varying-operators]]

## Key Concepts

- [[k2svd]]: A principled time-series prediction method that learns leading singular functions of the Koopman operator via a Hilbert-Schmidt objective and performs Kalman inference in a compact latent space.

## Archivist Review

Approved the core principled Koopman framework (K2SVD) and its associated open question regarding adaptive ranks and time-varying operators, strictly following scarcity limits and vault standards.

### Approved Concepts
- K2SVD: K^2SVD introduces a principled way to learn valid low-rank Koopman representations using singular functions and Kalman inference, addressing mathematical inconsistencies in prior neural Koopman methods.

### Approved Open Questions
- Adaptive Koopman Rank and Time-Varying Operators: Crucial for handling non-stationary time series and distribution shifts where a fixed low-rank transition operator fails to capture evolving system physics.

## Links

- [Abstract](https://arxiv.org/abs/2609.17815)
- [PDF](https://arxiv.org/pdf/2609.17815)

