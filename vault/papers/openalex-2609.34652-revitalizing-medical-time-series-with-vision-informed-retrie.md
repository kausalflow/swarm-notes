---
# CSL-compatible fields
title: "Revitalizing Medical Time Series with Vision-Informed Retrieval: A Vision-Language Perspective"
author:
  - literal: "Guoqi Yu"
  - literal: "Juncheng Wang"
  - literal: "Shujun Wang"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34652"

# Custom fields
paper_id: "2609.34652"
paper_source: "openalex"
domain: "time-series"
tags:
  - "multimodal"
  - "vision-language-model"
  - "retrieval-augmented-generation"
  - "attention-mechanism"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "vision-informed-retrieval"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:19Z"
created_at: "2026-09-30T10:50:19Z"
---

# Revitalizing Medical Time Series with Vision-Informed Retrieval: A Vision-Language Perspective

**Authors**: Guoqi Yu, Juncheng Wang, Shujun Wang
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34652](https://arxiv.org/abs/2609.34652)

## Summary

This paper introduces Vision-Informed Retrieval (ViRe), a novel framework that bridges medical time series analysis with vision-language models by treating waveform plots as morphology-aware queries. Specifically, ViRe extracts visual queries using pre-trained VLMs and applies an attention-based cross-modal retrieval mechanism to select relevant temporal and channel evidence from raw numerical representations. Evaluated across six public benchmarks against ten established baselines, ViRe demonstrates superior performance, yielding an average 6.42% relative improvement over prior state-of-the-art methods.

## Key Contributions

- Introduces Vision-Informed Retrieval (ViRe), utilizing frozen VLM-derived waveform representations as morphology-aware queries to guide retrieval from raw numerical medical time series features.
- Employs a tailored attention-based cross-modal retrieval mechanism to select morphology-relevant temporal and channel evidence from numerical representations.
- Achieves a 6.42% relative improvement over previous state of the art across six public benchmarks against ten established baselines.

## Open Questions & Future Work

- [[medical-waveform-vlm-adaptations]]

## Key Concepts

- [[vision-informed-retrieval]]: A cross-modal retrieval framework that uses frozen VLM-derived waveform representations as morphology-aware queries to guide retrieval from numerical medical time series.

## Archivist Review

Approved the cross-modal retrieval concept and its corresponding open question on domain-specific waveform VLM adaptations, adhering strictly to the vault's high-selectivity standard. No datasets were approved because the abstract refers only to generic public benchmarks rather than a specific named repository.

### Approved Concepts
- Vision-Informed Retrieval: Provides a novel cross-modal retrieval mechanism that bridges waveform plots and numerical time series for medical classification.

### Approved Open Questions
- Domain-Specific Vision-Language Encoders for Waveform Analysis: Identifying domain-specific encoders and adaptive rendering operators addresses current bottlenecks regarding general-purpose CLIP limitations and rendering hyperparameter sensitivity in medical time-series analysis.

## Links

- [Abstract](https://arxiv.org/abs/2609.34652)
- [PDF](https://arxiv.org/pdf/2609.34652)

