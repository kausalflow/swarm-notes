---
# CSL-compatible fields
title: "A Hybrid Framework Combining Autoregression and Common Factors for Matrix Time Series"
author:
  - literal: "Zhiyun Fan"
  - literal: "Xiaoyu Zhang"
  - literal: "Di Wang"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2503.05340"

# Custom fields
paper_id: "2503.05340"
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
  - "matrix-autoregressive-model-with-common-factors"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-14T10:11:07Z"
created_at: "2026-09-14T10:11:07Z"
---

# A Hybrid Framework Combining Autoregression and Common Factors for Matrix Time Series

**Authors**: Zhiyun Fan, Xiaoyu Zhang, Di Wang
**Date**: 2026-09-14
**Paper ID**: [openalex:2503.05340](https://arxiv.org/abs/2503.05340)

## Summary

This paper introduces the Matrix Autoregressive model with Common Factors (MARCF), a unified modeling framework for high-dimensional matrix time series that bridges matrix autoregression and matrix factor models. By decomposing coefficient matrices into common, predictor-specific, and response-specific parts, MARCF captures structural overlaps for effective dimension reduction while maintaining modeling flexibility. The authors develop a regularized gradient descent estimation procedure, prove its local linear convergence and statistical consistency, and validate its efficacy via simulations and global macroeconomic forecasting.

## Key Contributions

- Proposes the Matrix Autoregressive model with Common Factors (MARCF) framework to bridge the gap between matrix autoregression and matrix factor models.
- Decomposes coefficient matrices into common, predictor-specific, and response-specific components to achieve dimension reduction while retaining structural flexibility.
- Develops a regularized gradient descent estimator with established local linear convergence and statistical consistency under high-dimensional scaling.

## Open Questions & Future Work

- [[matrix-time-series-inference]]

## Key Concepts

- [[matrix-autoregressive-model-with-common-factors]]: A unified matrix time series framework that decomposes coefficient matrices into common, predictor-specific, and response-specific components.

## Archivist Review

Approved the core matrix autoregressive model with common factors framework as a reusable methodological contribution for matrix time series, along with its specific open inference question. No named benchmark datasets were present.

### Approved Concepts
- Matrix Autoregressive model with Common Factors: Introduces a novel hybrid modeling framework bridging matrix autoregression and matrix factor models for high-dimensional matrix time series.

### Approved Open Questions
- Statistical Inference for MARCF: Statistical inference, hypothesis testing, and uncertainty quantification for factor-driven matrix autoregressive models are critical for empirical applications but lack rigorous asymptotic frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2503.05340)
- [PDF](https://arxiv.org/pdf/2503.05340)

