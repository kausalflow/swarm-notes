---
# CSL-compatible fields
title: "Speaking Numbers to LLMs: Multi-Wavelet Number Embeddings for Time Series Forecasting"
author:
  - literal: "Defu Cao"
  - literal: "Zijie Lei"
  - literal: "Muyan Weng"
  - literal: "Jiao Sun"
  - literal: "Yan Liu"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26487"

# Custom fields
paper_id: "2606.26487"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "embedding"
  - "efficient-transformer"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "tempowave"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:37Z"
created_at: "2026-06-28T08:15:37Z"
---

# Speaking Numbers to LLMs: Multi-Wavelet Number Embeddings for Time Series Forecasting

**Authors**: Defu Cao, Zijie Lei, Muyan Weng, Jiao Sun, Yan Liu
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26487](https://arxiv.org/abs/2606.26487)

## Summary

TempoWave addresses the misalignment between discrete LLM tokenizers and continuous numerical time series data by replacing standard token representations with multi-scale wavelet digit embeddings. This interface maps scalar observations into coefficients that capture both fine-grained local dynamics and macro global structures while maintaining robustness to normalization. Empirical results on five forecasting benchmarks demonstrate that the proposed method significantly improves forecasting reliability and numerical precision compared to standard embedding approaches.

## Key Contributions

- Introduced TempoWave, a multi-wavelet digit embedding interface that preserves local fluctuations and macro global structures in time series data.
- Demonstrated that TempoWave resolves numerical ordering and reliability issues inherent in standard LLM tokenizers.
- Achieved state-of-the-art forecasting performance across five context-enriched benchmarks by outperforming standard numeric tokenization and existing embedding interfaces.

## Open Questions & Future Work

- [[generalizing-wavelet-embeddings-non-contextual-forecasting]]

## Key Concepts

- [[tempowave]]: A plug-and-play temporal wavelet digit interface that maps scalar observations into multi-scale, multi-wavelet digit embeddings for LLMs.

## Archivist Review

I approved TempoWave as a reusable, general-purpose approach for aligning numerical time series data with LLM tokenizers. I also approved a targeted open question regarding the generalizability of this approach to non-contextual forecasting architectures, which addresses a key limitation in the current scope of the research. No datasets were approved as they were not specified in the analysis.

### Approved Concepts
- TempoWave: This interface serves as the core methodological contribution, resolving the misalignment between LLM tokenizers and continuous numerical time series data.

### Approved Open Questions
- Generalizing Wavelet Embeddings: Understanding if this embedding technique is universally beneficial across various types of forecasting architectures, rather than just those already utilizing external context, is critical for establishing it as a general-purpose improvement for numerical LLM interfaces.

## Links

- [Abstract](https://arxiv.org/abs/2606.26487)
- [PDF](https://arxiv.org/pdf/2606.26487)

