---
# CSL-compatible fields
title: "DeepLévy: Learning Heavy-Tailed Uncertainty in Highly Volatile Time Series"
author:
  - literal: "Yang Yang"
  - literal: "Du Yin"
  - literal: "Hao Xue"
  - literal: "Flora D. Salim"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10364"

# Custom fields
paper_id: "2605.10364"
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
  - "deeplevy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:37:05Z"
created_at: "2026-05-14T07:37:05Z"
---

# DeepLévy: Learning Heavy-Tailed Uncertainty in Highly Volatile Time Series

**Authors**: Yang Yang, Du Yin, Hao Xue, Flora D. Salim
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10364](https://arxiv.org/abs/2605.10364)

## Summary

DeepLévy is a probabilistic forecasting framework designed to model heavy-tailed distributions in volatile time series. By learning mixtures of Lévy stable distributions through the minimization of empirical and parametric characteristic functions, the model bypasses the intractability of Lévy probability density functions. The approach adaptively captures context-dependent uncertainty over multiple horizons, offering robust predictive performance for extreme events that traditional deep learning models typically underestimate.

## Key Contributions

- DeepLévy improves tail risk estimation in highly volatile time series by learning mixtures of Lévy stable distributions.
- Minimizing characteristic function discrepancy provides a robust alternative to likelihood-based inference for intractable heavy-tailed distributions.
- DeepLévy achieves superior performance over state-of-the-art deep probabilistic models in uncertainty quantification under extreme volatility scenarios.

## Open Questions & Future Work

- [[multivariate-levy-stable-forecasting]]
- [[temporal-dynamics-tail-parameters]]

## Key Concepts

- [[deeplevy]]: A neural framework for modeling heavy-tailed uncertainty in time series by minimizing characteristic function discrepancies.

## Archivist Review

The paper presents a novel approach to modeling heavy-tailed time series by utilizing characteristic functions to bypass the intractability of Lévy probability density functions. I approved the core framework and two substantial open questions regarding multivariate extensions and latent temporal dynamics of the tail parameters, both of which represent significant bottlenecks in probabilistic forecasting. No datasets were approved as none were highlighted as central, novel, or reusable benchmarks.

### Approved Concepts
- DeepLévy: It enables probabilistic forecasting for heavy-tailed time series where standard density-based likelihoods are intractable.

### Approved Open Questions
- Multivariate Lévy Stable Forecasting: Many real-world forecasting tasks involve multi-variate dependencies where extreme events are correlated, making multivariate extensions critical for robust risk assessment.
- Temporal Dynamics of Tail Parameters: Explicit modeling of tail dynamics is essential for detecting regime shifts from stable conditions to extreme volatility, which is crucial for dynamic risk management.

## Links

- [Abstract](https://arxiv.org/abs/2605.10364)
- [PDF](https://arxiv.org/pdf/2605.10364)

