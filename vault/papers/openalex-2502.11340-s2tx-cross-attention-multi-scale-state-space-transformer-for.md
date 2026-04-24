---
# CSL-compatible fields
title: "S2TX: Cross-Attention Multi-Scale State-Space Transformer for Time Series Forecasting"
author:
  - literal: "Zihao Wu"
  - literal: "Juncheng Dong"
  - literal: "Haoming Yang"
  - literal: "Vahid Tarokh"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2502.11340"

# Custom fields
paper_id: "2502.11340"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mamba"
  - "transformer"
  - "state-space-model"
  - "attention-mechanism"
  - "cross-attention"
architectures:
  - "mamba"
  - "transformer"
datasets:
  []
concept_slugs:
  - "s2tx"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:58:28Z"
created_at: "2026-04-24T06:58:28Z"
---

# S2TX: Cross-Attention Multi-Scale State-Space Transformer for Time Series Forecasting

**Authors**: Zihao Wu, Juncheng Dong, Haoming Yang, Vahid Tarokh
**Date**: 2026-04-21
**Paper ID**: [openalex:2502.11340](https://arxiv.org/abs/2502.11340)

## Summary

S2TX is a novel multi-scale forecasting architecture that addresses the challenges of capturing cross-variate dependencies and multi-resolution temporal patterns. It achieves this by combining Mamba models for long-range global context with Transformer layers for local window attention. Through a specialized cross-attention mechanism, the model enables effective information flow between global and local representations, resulting in superior performance on standard benchmarks compared to existing state-of-the-art methods.

## Key Contributions

- Introduces S2TX, a hybrid forecasting architecture that leverages Mamba for cross-variate context and Transformer with local window attention.
- Utilizes cross-attention to facilitate interaction between global and local representations, overcoming limitations of independent processing in existing models.
- Demonstrates state-of-the-art forecasting performance across six benchmark datasets while maintaining low computational memory overhead.

## Open Questions & Future Work

- [[local-cross-variate-correlation-modeling]]
- [[multi-scale-hierarchical-forecasting]]

## Key Concepts

- [[s2tx]]: A multi-scale time series forecasting architecture that combines Mamba-based global context modeling with transformer-based local window attention via cross-attention.

## Archivist Review

I approved the S2TX architecture concept as it reflects a significant hybrid design pattern combining Mamba and Transformers that is likely to be reused. The open questions regarding local cross-variate modeling and multi-scale hierarchies were approved because they define substantial structural limitations beyond mere performance improvements. I rejected no candidates because the initial set was highly focused and relevant.

### Approved Concepts
- S2TX: The primary novel architecture proposed that integrates Mamba with transformer cross-attention to unify global and local time series modeling, representing an emerging trend in hybrid time series architectures.

### Approved Open Questions
- Local Cross-Variate Correlation Modeling: This highlights a bottleneck in existing patch-based forecasting methods, as effectively modeling local dependencies is crucial for high-dimensional time series forecasting.
- Multi-Scale Hierarchical Forecasting: Moving beyond binary (local vs. global) scale hierarchies is a substantial research direction for capturing multi-scale phenomena in time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2502.11340)
- [PDF](https://arxiv.org/pdf/2502.11340)

