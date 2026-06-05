---
# CSL-compatible fields
title: "TiWeaver: Unified Temporal Dynamics Modeling via Contextual Patching"
author:
  - literal: "Zhe Li"
  - literal: "Jindong Tian"
  - literal: "Hao Miao"
  - literal: "Zhi Lei"
  - literal: "Chenjuan Guo"
  - literal: "Bin Yang"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03121"

# Custom fields
paper_id: "2606.03121"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "attention-mechanism"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "graph-guided-adaptive-tokenizer-g2at"
  - "fine-grained-asynchronous-dependency-extractor-fade"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:38:59Z"
created_at: "2026-06-05T08:38:59Z"
---

# TiWeaver: Unified Temporal Dynamics Modeling via Contextual Patching

**Authors**: Zhe Li, Jindong Tian, Hao Miao, Zhi Lei, Chenjuan Guo, Bin Yang
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03121](https://arxiv.org/abs/2606.03121)

## Summary

TiWeaver is a unified time-series forecasting framework designed to address the challenges of diverse temporal dynamics and irregular sampling in multivariate data. The approach features two key novel components: the Graph-Guided Adaptive Tokenizer (G2AT) for coherent patch segmentation and the Fine-grained Asynchronous Dependency Extractor (FADE) for modeling asynchronous inter-channel dependencies. Empirical evaluations across 12 datasets confirm that TiWeaver achieves state-of-the-art forecasting performance and demonstrates high robustness to data irregularities.

## Key Contributions

- Introduced TiWeaver, a unified time-series forecasting framework that adaptively models complex, irregular temporal dynamics.
- Proposed the Graph-Guided Adaptive Tokenizer (G2AT) for coherent patch segmentation based on temporal density and representation consistency.
- Developed the Fine-grained Asynchronous Dependency Extractor (FADE) to model asynchronous inter-channel dependencies and long-term history.
- Achieved state-of-the-art performance on 12 diverse real-world benchmarks with performance improvements of up to 25% over existing methods.

## Open Questions & Future Work

- [[unified-adaptive-tokenization-irregular-mts]]

## Key Concepts

- [[graph-guided-adaptive-tokenizer-g2at]]: A patching mechanism that segments time series data by balancing temporal density and representation consistency through graph-guided learning.
- [[fine-grained-asynchronous-dependency-extractor-fade]]: A dependency extraction module designed to capture fine-grained asynchronous inter-channel relationships and long-term historical context.

## Archivist Review

The paper introduces novel mechanisms for handling irregular multivariate time series via graph-guided tokenization and asynchronous dependency extraction. I approved these two concepts because they represent generalizable architectural advances in the field of time-series forecasting. I also approved the open question on unified adaptive tokenization as it addresses a persistent, structural challenge in the field that transcends the specific model proposed here.

### Approved Concepts
- Graph-Guided Adaptive Tokenizer (G2AT): This approach introduces a novel graph-centric methodology for adaptive patching, moving beyond fixed-window strategies in time-series transformers.
- Fine-grained Asynchronous Dependency Extractor (FADE): The module addresses the fundamental challenge of asynchronous inter-channel dependencies in multivariate forecasting, which is a major bottleneck in irregular time-series modeling.

### Approved Open Questions
- Unified Adaptive Tokenization for MTS: Standardizing adaptive tokenization is critical to moving away from dataset-specific hyperparameter tuning in time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.03121)
- [PDF](https://arxiv.org/pdf/2606.03121)

