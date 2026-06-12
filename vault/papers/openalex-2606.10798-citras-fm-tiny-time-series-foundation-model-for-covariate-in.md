---
# CSL-compatible fields
title: "CITRAS-FM: Tiny Time Series Foundation Model for Covariate-Informed Zero-Shot Forecasting"
author:
  - literal: "Yosuke Yamaguchi"
  - literal: "Issei Suemitsu"
  - literal: "Yuki Kajihara"
  - literal: "Wenpeng Wei"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10798"

# Custom fields
paper_id: "2606.10798"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "transformer"
  - "attention-mechanism"
  - "decoder-only"
  - "pre-training"
  - "zero-shot-learning"
  - "efficient-transformer"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "shifted-attention"
  - "covsynth"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:52:58Z"
created_at: "2026-06-12T08:52:58Z"
---

# CITRAS-FM: Tiny Time Series Foundation Model for Covariate-Informed Zero-Shot Forecasting

**Authors**: Yosuke Yamaguchi, Issei Suemitsu, Yuki Kajihara, Wenpeng Wei
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10798](https://arxiv.org/abs/2606.10798)

## Summary

CITRAS-FM is a lightweight 7M-parameter time series foundation model designed for covariate-informed zero-shot forecasting on CPU hardware. The architecture utilizes a decoder-only Transformer with a novel Shifted Attention mechanism to incorporate known future covariates effectively. To address the lack of covariate-rich data for pretraining, the authors introduce CovSynth, which generates synthetic covariates from target series decomposition. Empirical evaluation on the 100-task fev-bench shows the model achieves state-of-the-art accuracy for its size class with inference latency under 0.1 seconds.

## Key Contributions

- CITRAS-FM, a 7M-parameter decoder-only transformer model, enables univariate, multivariate, and covariate-informed zero-shot forecasting.
- Introduces Shifted Attention, a cross-variate mechanism that integrates future-known covariates into the forecasting process.
- Develops CovSynth, a component-based synthesis framework that mitigates the scarcity of high-quality covariate-rich pretraining corpora.
- Demonstrates SOTA zero-shot performance among sub-10M parameter TSFMs on the 100-task fev-bench while enabling real-time CPU inference.

## Open Questions & Future Work

- [[efficient-covariate-aware-tsfms]]

## Key Concepts

- [[shifted-attention]]: A cross-variate attention mechanism designed to integrate known exogenous covariates throughout the forecasting horizon.
- [[covsynth]]: A data synthesis method that generates realistic covariates by decomposing target time series into components.

## Archivist Review

Approved concepts reflect specific, reusable methods for incorporating exogenous knowledge into time series transformers. The open question was refined to capture the tension between model efficiency and the capacity to utilize heterogeneous covariate information, which is a known research gap. The dataset 'fev-bench' was rejected as it represents a routine benchmark collection within this specific paper's context and lacks the required standalone significance for the vault.

### Approved Concepts
- Shifted Attention: It is the primary architectural novelty enabling effective covariate utilization in the forecasting task.
- CovSynth: It addresses the specific bottleneck of data scarcity for covariate-informed forecasting models.

### Approved Open Questions
- Efficient Covariate-Informed TSFMs: Improving the covariate-informed forecasting capability of tiny TSFMs is essential for enabling real-time, low-latency intelligence in resource-constrained environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.10798)
- [PDF](https://arxiv.org/pdf/2606.10798)

