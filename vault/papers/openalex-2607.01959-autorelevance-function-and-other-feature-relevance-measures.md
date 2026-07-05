---
# CSL-compatible fields
title: "Autorelevance function and other feature relevance measures for univariate time series"
author:
  - literal: "Julian Cardenas"
  - literal: "Jamie Arjona"
  - literal: "Pedro Delicado"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01959"

# Custom fields
paper_id: "2607.01959"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "recurrent-neural-network"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  - "auto-relevance-function"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:51:41Z"
created_at: "2026-07-05T07:51:41Z"
---

# Autorelevance function and other feature relevance measures for univariate time series

**Authors**: Julian Cardenas, Jamie Arjona, Pedro Delicado
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01959](https://arxiv.org/abs/2607.01959)

## Summary

This paper introduces a model-agnostic methodology for measuring lag relevance in univariate time series forecasting by leveraging the frameworks of ghost variables and Shapley values. The authors define auto-relevance and partial auto-relevance functions to assign importance values to specific lags. Furthermore, they propose a novel approach for feature substitution in coalition-based importance methods by using one-step-ahead model predictions. The framework is validated against seasonal ARMA and recurrent neural network models, showing robust recovery of underlying lag structures.

## Key Contributions

- Introduces the auto-relevance and partial auto-relevance functions as model-agnostic measures for quantifying lag importance in univariate time series.
- Proposes a method for replacing absent features in coalition-based relevance estimation using one-step-ahead forecasts from the target model.
- Demonstrates the efficacy of the proposed relevance measures in recovering known lag structures across ARMA and RNN architectures on simulated and empirical data.

## Open Questions & Future Work

- [[robust-imputation-time-series-relevance]]
- [[multivariate-time-series-relevance]]

## Key Concepts

- [[auto-relevance-function]]: A model-agnostic measure of lag relevance in univariate time series forecasting using coalition-based importance values.

## Archivist Review

The paper proposes a novel, model-agnostic approach to quantifying temporal lag importance in univariate forecasting. I have approved the auto-relevance function as a reusable concept for interpreting temporal models, and two open questions regarding the robustness of imputation strategies and the extension to multivariate data, both of which are central challenges for interpretability in time series forecasting.

### Approved Concepts
- Auto-relevance function: Provides a novel, model-agnostic way to quantify lag importance in univariate time series forecasting.

### Approved Open Questions
- Robustness to Model Performance: Establishing a reliable interpretability framework that does not rely on the high performance of the base model is essential for the valid application of XAI methods in real-world scenarios where models may not be fully optimized.
- Multivariate Time Series Extension: Real-world forecasting tasks rarely rely on univariate data, making the extension to multivariate settings a primary requirement for the practical adoption of these interpretability tools.

## Links

- [Abstract](https://arxiv.org/abs/2607.01959)
- [PDF](https://arxiv.org/pdf/2607.01959)

