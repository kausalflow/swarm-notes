---
# CSL-compatible fields
title: "TS-ICL: A Flexible Time-Indexed Foundation Model for Time Series via In-Context Learning"
author:
  - literal: "Etienne Le Naour"
  - literal: "Tahar Nabil"
  - literal: "Adrien Petralia"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05878"

# Custom fields
paper_id: "2606.05878"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "transformer"
  - "in-context-learning"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ts-icl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:18:21Z"
created_at: "2026-06-07T08:18:21Z"
---

# TS-ICL: A Flexible Time-Indexed Foundation Model for Time Series via In-Context Learning

**Authors**: Etienne Le Naour, Tahar Nabil, Adrien Petralia
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05878](https://arxiv.org/abs/2606.05878)

## Summary

TS-ICL is a probabilistic foundation model that shifts the focus from purely autoregressive forecasting to a more versatile encoder-regressor framework. By formulating time series tasks as timestamp-aligned regression, the model effectively handles irregular and partial observations. The method incorporates a novel causal data prior for synthetic training, leading to strong empirical results in both imputation and covariate-aware forecasting benchmarks.

## Key Contributions

- Introduces TS-ICL, a transformer-based foundation model that unifies time series forecasting and imputation through timestamp-aligned regression.
- Proposes a novel causal data prior for training on synthetic dependency structures, enabling robust handling of irregular observations and covariates.
- Achieves state-of-the-art performance in time series imputation while maintaining competitiveness in forecasting, particularly under conditions of partially observed look-back windows.

## Open Questions & Future Work

- [[ts-icl-inference-efficiency-optimization]]

## Key Concepts

- [[ts-icl]]: A probabilistic encoder-regressor Transformer that unifies time series forecasting and imputation through timestamp-aligned in-context learning.

## Archivist Review

I approved the TS-ICL concept as it represents a meaningful shift from autoregressive to encoder-regressor paradigms in time series foundation models. The open question on pointwise forecasting efficiency was approved because it addresses a specific, technically quantifiable trade-off inherent in modern time-indexed models. Other candidates were rejected for being generic or lacking sufficient architectural novelty.

### Approved Concepts
- TS-ICL: It introduces a shift from purely autoregressive models to a timestamp-aligned encoder-regressor framework, which is a reusable pattern for unifying imputation and forecasting tasks.

### Approved Open Questions
- Pointwise Forecasting Efficiency Bottlenecks: As foundation models move toward broader deployment, reconciling flexibility with computational efficiency remains a critical engineering bottleneck.

### Rejected Candidates
- [open_question] Enhancing Zero-Shot Generalization via Prior Diversity (`ts-icl-data-prior-diversity`) - generic: Suggesting that more diverse data improves performance is a generic observation applicable to all machine learning models, rather than a specific research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2606.05878)
- [PDF](https://arxiv.org/pdf/2606.05878)

