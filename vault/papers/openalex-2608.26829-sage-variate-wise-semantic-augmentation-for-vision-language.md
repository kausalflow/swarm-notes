---
# CSL-compatible fields
title: "SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting"
author:
  - literal: "Haizhao Fan"
  - literal: "Xinyi Le"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26829"

# Custom fields
paper_id: "2608.26829"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "clip"
  - "vision-language-model"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sage-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:19Z"
created_at: "2026-08-30T10:10:19Z"
---

# SAGE: Variate-Wise Semantic Augmentation for Vision-Language Time Series Forecasting

**Authors**: Haizhao Fan, Xinyi Le
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26829](https://arxiv.org/abs/2608.26829)

## Summary

Time series forecasting models often lack semantic knowledge of individual variables, while existing LLM-based or uniform prompt approaches suffer from high computational costs or neglect heterogeneous variate semantics. To address this, the authors propose SAGE, an end-to-end CLIP-based framework that leverages variate-wise textual descriptions and rendered visual series aligned through training-only contrastive objectives. SAGE achieves state-of-the-art accuracy across eight long-term benchmarks and M4 without placing an LLM in the inference loop.

## Key Contributions

- Proposes SAGE, an end-to-end CLIP-based framework that jointly models temporal, cross-variable, textual, and visual information for time series forecasting.
- Employs a CLIP text encoder with gated residual paths to inject variable-specific descriptions and statistical descriptors alongside a frozen CLIP vision encoder aligned via a training-only contrastive objective.
- Achieves state-of-the-art accuracy across eight long-term benchmarks and the M4 dataset without requiring an LLM in the forecasting inference loop.

## Open Questions & Future Work

- [[end-to-end-text-composition-for-time-series]]

## Key Concepts

- [[sage-framework]]: An end-to-end CLIP-based framework for time series forecasting that jointly models temporal, cross-variable, textual, and visual information.

## Archivist Review

Approved the central SAGE framework concept and the unique open question concerning end-to-end text composition for multimodal forecasting. Rejected the hierarchical text representation question due to redundancy with existing hierarchical adaptation entries.

### Approved Concepts
- SAGE Framework: Introduces a novel end-to-end CLIP-based framework for time series forecasting that combines variate-wise textual descriptions and visual alignments without inference-time LLMs.

### Approved Open Questions
- End-to-End Text Composition: Automating text generation removes the dependency on manual prompt engineering and allows dynamic adaptation to diverse temporal domains.

### Rejected Candidates
- [open_question] Hierarchical Text Representation for Multivariate Time Series (`hierarchical-text-representation-for-multivariate-time-series`) - duplicate_existing: Substantially overlaps with existing architectural scaling and hierarchical conditioning questions in the knowledge vault.

## Links

- [Abstract](https://arxiv.org/abs/2608.26829)
- [PDF](https://arxiv.org/pdf/2608.26829)

