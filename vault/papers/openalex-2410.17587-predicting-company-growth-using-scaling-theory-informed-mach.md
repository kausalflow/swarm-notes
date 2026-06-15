---
# CSL-compatible fields
title: "Predicting company growth using scaling theory informed machine learning"
author:
  - literal: "Ruyi Tao"
  - literal: "Veronica R. Cappelli"
  - literal: "Kaiwei Liu"
  - literal: "Marcus J. Hamilton"
  - literal: "Christopher P. Kempes"
  - literal: "Geoffrey B. West"
  - literal: "Jiang Zhang"
issued:
  date-parts:
    - [2026, 6, 12]
url: "https://arxiv.org/abs/2410.17587"

# Custom fields
paper_id: "2410.17587"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "scaling-theory-informed-machine-learning-stiml"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-15T10:50:33Z"
created_at: "2026-06-15T10:50:33Z"
---

# Predicting company growth using scaling theory informed machine learning

**Authors**: Ruyi Tao, Veronica R. Cappelli, Kaiwei Liu, Marcus J. Hamilton, Christopher P. Kempes, Geoffrey B. West, Jiang Zhang
**Date**: 2026-06-12
**Paper ID**: [openalex:2410.17587](https://arxiv.org/abs/2410.17587)

## Summary

The authors propose a Scaling-Theory-Informed Machine Learning (STIML) framework to predict company growth by merging mechanistic scaling laws with data-driven residual forecasting. By decomposing growth into trend-driven and fluctuation-driven components, the model achieves superior performance on 16 financial indicators compared to standalone approaches. The framework offers new insights into the interplay between company size and predictive signals, while interpretability analysis reveals the limitations of traditional growth models in capturing asymmetric deviations.

## Key Contributions

- Introduces the Scaling-Theory-Informed Machine Learning (STIML) framework, which decomposes company growth into mechanism-driven trends and fluctuation-driven residuals.
- Demonstrates that STIML outperforms both pure scaling models and purely data-driven baselines across 16 financial indicators using Compustat data.
- Establishes that the predictive contribution of growth trends versus residuals varies predictably with company size, providing new interpretability for financial dynamics.

## Open Questions & Future Work

- [[mechanistic-asymmetric-growth-modeling]]

## Key Concepts

- [[scaling-theory-informed-machine-learning-stiml]]: A hybrid forecasting framework that integrates structural mechanistic scaling laws for average growth trends with data-driven models for residual fluctuations.

## Archivist Review

I have approved the STIML framework concept because it provides a clear, reusable pattern for integrating mechanistic priors with data-driven residuals in time-series forecasting. The open question regarding asymmetric growth modeling is also approved, as it captures a fundamental limitation in the current application of power-law scaling models to non-symmetric economic phenomena. The dataset 'Compustat' was rejected as it is a common financial database frequently referenced in literature and does not warrant a standalone note in this context.

### Approved Concepts
- Scaling-Theory-Informed Machine Learning (STIML): It introduces a novel hybrid modeling approach that combines mechanistic scaling laws with data-driven residuals to improve company growth prediction.

### Approved Open Questions
- Mechanistic Modeling of Asymmetric Growth: The identified asymmetry is a significant limitation of existing mechanistic models that rely on symmetric power-law dynamics, and addressing this is essential for accurately modeling the non-Gaussian, constrained nature of company growth.

## Links

- [Abstract](https://arxiv.org/abs/2410.17587)
- [PDF](https://arxiv.org/pdf/2410.17587)

