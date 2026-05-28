---
# CSL-compatible fields
title: "ADMFormer: An Adaptive-Decomposition Transformer with Time-Varying Masked Spatial Attention for Traffic Forecasting"
author:
  - literal: "Ruiwen Gu"
  - literal: "Qitai Tan"
  - literal: "Yahao Liu"
  - literal: "Xiao-Ping Zhang"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25543"

# Custom fields
paper_id: "2605.25543"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "self-attention"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-node-adaptive-gating-mechanism"
  - "time-varying-masked-spatial-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:37:56Z"
created_at: "2026-05-28T08:37:56Z"
---

# ADMFormer: An Adaptive-Decomposition Transformer with Time-Varying Masked Spatial Attention for Traffic Forecasting

**Authors**: Ruiwen Gu, Qitai Tan, Yahao Liu, Xiao-Ping Zhang
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25543](https://arxiv.org/abs/2605.25543)

## Summary

ADMFormer is an adaptive-decomposition transformer designed for traffic forecasting, addressing the challenges of heterogeneous temporal patterns and redundant spatial attention. By decoupling traffic signals into stable regularities and residual fluctuations through a time-node gating mechanism, the model captures fine-grained dynamics more effectively. Additionally, its time-varying masked spatial attention dynamically sparsifies interactions to preserve only relevant dependencies, leading to improved predictive accuracy on four real-world benchmarks.

## Key Contributions

- Introduces the time-node adaptive gating mechanism to decouple complex traffic series into regular periodic patterns and residual fluctuations.
- Designs a dual-branch temporal module that processes regularities and irregularities separately to improve modeling of fine-grained dynamics.
- Develops a time-varying masked spatial attention mechanism that sparsifies redundant interactions based on real-time traffic state, achieving state-of-the-art results on four traffic datasets.

## Open Questions & Future Work

- [[disentangling-temporal-spatial-dynamics]]

## Key Concepts

- [[time-node-adaptive-gating-mechanism]]: A gating module that decomposes time series into periodic regularities and event-driven fluctuations adaptively across time and spatial nodes.
- [[time-varying-masked-spatial-attention]]: An attention mechanism that dynamically prunes spatial interactions based on real-time input signal states to reduce noise and computational redundancy.

## Archivist Review

I approved the two core mechanisms as they represent reusable architectures for spatiotemporal modeling (adaptive signal decomposition and state-dependent attention sparsification). I approved the open question regarding the disentanglement of spatio-temporal dynamics as it identifies a fundamental bottleneck in the field. All concepts and questions were evaluated for their broad utility beyond traffic forecasting.

### Approved Concepts
- Time-Node Adaptive Gating Mechanism: Central to handling heterogeneous temporal patterns by separating them into regular and residual components.
- Time-Varying Masked Spatial Attention: Directly addresses the limitations of dense attention in sparse, dynamic graph-like dependencies.

### Approved Open Questions
- Disentangling Spatio-Temporal Dynamics: Crucial for improving robustness and interpretability in traffic forecasting, as current models often compress diverse patterns into shared representations or rely on noise-amplifying dense attention.

## Links

- [Abstract](https://arxiv.org/abs/2605.25543)
- [PDF](https://arxiv.org/pdf/2605.25543)

