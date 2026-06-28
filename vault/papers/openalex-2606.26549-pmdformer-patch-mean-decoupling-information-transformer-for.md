---
# CSL-compatible fields
title: "PMDformer: Patch-Mean Decoupling Information Transformer for Long-term Forecasting"
author:
  - literal: "Ao Hu"
  - literal: "Liangjian Wen"
  - literal: "Jiang Duan"
  - literal: "Y Sophia Dai"
  - literal: "He Yan"
  - literal: "Dongkai Wang"
  - literal: "Jun Wang"
  - literal: "Yukun Zhang"
  - literal: "Ruoxi Jiang"
  - literal: "Zhewei Xu"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26549"

# Custom fields
paper_id: "2606.26549"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "patch-mean-decoupling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:52Z"
created_at: "2026-06-28T08:15:52Z"
---

# PMDformer: Patch-Mean Decoupling Information Transformer for Long-term Forecasting

**Authors**: Ao Hu, Liangjian Wen, Jiang Duan, Y Sophia Dai, He Yan, Dongkai Wang, Jun Wang, Yukun Zhang, Ruoxi Jiang, Zhewei Xu
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26549](https://arxiv.org/abs/2606.26549)

## Summary

PMDformer is a transformer-based architecture for long-term time series forecasting that addresses challenges in modeling shape similarities across variable scales. It introduces a Patch-Mean Decoupling (PMD) strategy to isolate trend and residual information, ensuring attention mechanisms operate on normalized shapes. The model also integrates Trend Restoration Attention (TRA) for trend reintegration and Proximal Variable Attention (PVA) to prioritize relevant recent cross-variable correlations, outperforming existing state-of-the-art methods.

## Key Contributions

- Introduces Patch-Mean Decoupling (PMD) to improve shape similarity modeling by separating trend and residual components.
- Develops Trend Restoration Attention (TRA) for explicit trend integration and Proximal Variable Attention (PVA) for dynamic cross-variable correlation modeling.
- PMDformer achieves state-of-the-art stability and accuracy on long-term time series forecasting (LTSF) benchmarks.

## Open Questions & Future Work

- [[temporal-scope-cross-variable-attention]]

## Key Concepts

- [[patch-mean-decoupling]]: A technique that separates trend and residual information in time-series patches by subtracting patch means to improve shape-similarity modeling.

## Archivist Review

I approved Patch-Mean Decoupling because it is a fundamental, reusable normalization technique for patch-based time series models. Trend Restoration Attention was rejected because it is a specific architectural subcomponent tightly coupled to the PMD framework. The open question regarding the temporal scope of cross-variable attention was approved as it targets a significant bottleneck in modeling non-stationary multivariate relationships.

### Approved Concepts
- Patch-Mean Decoupling (PMD): It is the core architectural innovation to resolve scale sensitivity in patch-based forecasting models.

### Approved Open Questions
- Optimal Temporal Scope for Cross-Variable Attention: Understanding the temporal extent of inter-variable dependencies is critical for balancing model capacity and robustness against non-stationary noise. This problem is fundamental to improving both the accuracy and efficiency of Transformer-based models in high-dimensional multivariate settings.

### Rejected Candidates
- [concept] Trend Restoration Attention (TRA) (`trend-restoration-attention`) - subcomponent_of_broader_mechanism: This is a specific subcomponent of the PMD architecture and does not appear distinct or reusable enough to warrant a standalone entry compared to the overarching PMD mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.26549)
- [PDF](https://arxiv.org/pdf/2606.26549)

