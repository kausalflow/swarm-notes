---
# CSL-compatible fields
title: "DC-Mamber: A Dual Channel Prediction Model Based on Mamba and Linear Transformer for Multivariate Time Series Forecasting"
author:
  - literal: "Bing Fan"
  - literal: "Shusen Ma"
  - literal: "Yun‐Bo Zhao"
  - literal: "Gang Xu"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2507.04381"

# Custom fields
paper_id: "2507.04381"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mamba"
  - "ssm"
  - "transformer"
  - "attention-mechanism"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dc-mamber"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:59:06Z"
created_at: "2026-04-24T06:59:06Z"
---

# DC-Mamber: A Dual Channel Prediction Model Based on Mamba and Linear Transformer for Multivariate Time Series Forecasting

**Authors**: Bing Fan, Shusen Ma, Yun‐Bo Zhao, Gang Xu
**Date**: 2026-04-21
**Paper ID**: [openalex:2507.04381](https://arxiv.org/abs/2507.04381)

## Summary

DC-Mamber addresses the trade-offs between local pattern extraction and global dependency modeling in multivariate time series forecasting. By employing a dual-channel strategy, the model uses Mamba for efficient local feature capture and a linear Transformer to handle global dependencies with reduced complexity. This architecture leverages the strengths of both SSMs and linear attention mechanisms to achieve improved performance across diverse datasets.

## Key Contributions

- Introduces DC-Mamber, a dual-channel architecture that bifurcates processing into a local SSM-based stream and a global linear Transformer-based stream.
- Utilizes a Dual-Channel Embedding Layer and Feature-fusion module to effectively integrate divergent representations of local and global temporal dependencies.
- Achieves superior accuracy on four multivariate time series forecasting benchmarks compared to existing channel-independent and channel-mixing approaches.

## Open Questions & Future Work

- [[adaptive-strategy-allocation-mtsf]]

## Key Concepts

- [[dc-mamber]]: A hybrid multivariate time series forecasting architecture that bifurcates input processing into a local SSM-based stream and a global linear attention-based stream.

## Archivist Review

I approved the DC-Mamber architecture because it represents a clear, reusable pattern for hybridizing SSMs and linear Transformers in multivariate time series forecasting. I also approved the open question regarding adaptive strategy allocation, as it addresses a core limitation of static hybrid designs in handling heterogeneous temporal patterns. Other architectural subcomponents were rejected as routine or specific to the paper's implementation.

### Approved Concepts
- DC-Mamber: The architecture provides a concrete example of hybridizing state space models (Mamba) with linear Transformers to address the local/global modeling trade-off in multivariate forecasting.

### Approved Open Questions
- Adaptive Strategy Allocation for MTSF: Static hybridization may be suboptimal for complex datasets where different variables or time-steps possess varying sensitivity to local versus global modeling techniques.

### Rejected Candidates
- [concept] Dual-Channel Embedding Layer (`dual-channel-embedding-layer`) - subcomponent_of_broader_mechanism: This is a subcomponent specific to the proposed architecture and not a widely applicable or distinct methodology.
- [concept] Feature-fusion module (`feature-fusion-module`) - not_novel: Feature fusion is a standard architectural practice and this specific implementation is not sufficiently novel or reusable as a standalone concept.

## Links

- [Abstract](https://arxiv.org/abs/2507.04381)
- [PDF](https://arxiv.org/pdf/2507.04381)

