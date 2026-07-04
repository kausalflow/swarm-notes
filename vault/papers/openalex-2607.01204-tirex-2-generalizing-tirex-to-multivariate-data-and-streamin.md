---
# CSL-compatible fields
title: "TiRex-2: Generalizing TiRex to Multivariate Data and Streaming"
author:
  - literal: "Patrick Podest"
  - literal: "Marco Pichler"
  - literal: "Elias Bürger"
  - literal: "Levente Zólyomi"
  - literal: "Bernhard Voggenberger"
  - literal: "Wilhelm Berghammer"
  - literal: "Daniel Klotz"
  - literal: "Sebastian Böck, Günter Klambauer"
  - literal: "Sepp Hochreiter"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.01204"

# Custom fields
paper_id: "2607.01204"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "streaming"
  - "multivariate-forecasting"
architectures:
  - "mamba"
datasets:
  - "gift-eval"
  - "fev-bench"
concept_slugs:
  - "synthetic-coupling-pipeline"
dataset_slugs:
  - "gift-eval"
  - "fev-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:08Z"
created_at: "2026-07-04T07:36:08Z"
---

# TiRex-2: Generalizing TiRex to Multivariate Data and Streaming

**Authors**: Patrick Podest, Marco Pichler, Elias Bürger, Levente Zólyomi, Bernhard Voggenberger, Wilhelm Berghammer, Daniel Klotz, Sebastian Böck, Günter Klambauer, Sepp Hochreiter
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.01204](https://arxiv.org/abs/2607.01204)

## Summary

TiRex-2 is an xLSTM-based foundation model designed for multivariate time series forecasting that addresses the quadratic complexity and streaming limitations of Transformer models. By utilizing a recurrent design with a bidirectional time mixer and an asymmetric grouped-attention variate mixer, the model handles multivariate inputs and future covariates with constant per-patch inference costs. Furthermore, the authors present a synthetic coupling pipeline to bridge the gap between univariate corpora and multivariate pretraining requirements, resulting in state-of-the-art zero-shot forecasting performance.

## Key Contributions

- Introduces TiRex-2, a recurrent xLSTM-based time series foundation model supporting multivariate data with future-known covariates at constant per-patch inference cost.
- Proposes a synthetic coupling pipeline that enables scaling multivariate pretraining by composing diverse multivariate samples from univariate corpora.
- Achieves state-of-the-art zero-shot performance on GIFT-Eval and fev-bench while maintaining stability under streaming conditions.

## Open Questions & Future Work

- [[dynamic-covariate-selection-tsfm]]

## Key Concepts

- [[synthetic-coupling-pipeline]]: A data augmentation strategy that dynamically generates multivariate time series samples from univariate corpora for scalable foundation model pretraining.

## Archivist Review

The synthetic coupling pipeline is approved as it addresses the key data-scaling bottleneck for multivariate time series foundation models. The datasets GIFT-Eval and fev-bench are approved as they serve as the central zero-shot performance benchmarks in the paper. The open question regarding dynamic covariate selection is approved as it highlights a clear, specific bottleneck for future TSFM development.

### Approved Concepts
- Synthetic Coupling Pipeline: It enables scaling multivariate pretraining by transforming abundant univariate data into multivariate samples, which is central to the foundation model's capability.

### Approved Open Questions
- Dynamic Covariate Selection in TSFMs: Efficiently handling high-dimensional covariate sets without increasing inference latency is a significant bottleneck for scaling time series foundation models.

## Datasets

- [[gift-eval]]
- [[fev-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01204)
- [PDF](https://arxiv.org/pdf/2607.01204)

