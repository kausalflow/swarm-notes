---
# CSL-compatible fields
title: "Stable Attention Response for Reliable Precipitation Nowcasting"
author:
  - literal: "Penghui Wen"
  - literal: "Zexin Hu"
  - literal: "Sen Zhang"
  - literal: "Patrick Filippi"
  - literal: "Xiaogang Zhu"
  - literal: "Allen Benter"
  - literal: "Thomas Bishop"
  - literal: "Zhiyong Wang"
  - literal: "Kun Hu"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13181"

# Custom fields
paper_id: "2605.13181"
paper_source: "openalex"
domain: "time-series"
tags:
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "multimodal"
architectures:
  []
datasets:
  - "sevir"
  - "meteonet"
concept_slugs:
  - "attention-response-energy-stability"
dataset_slugs:
  - "sevir"
  - "meteonet"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:09:55Z"
created_at: "2026-05-16T07:09:55Z"
---

# Stable Attention Response for Reliable Precipitation Nowcasting

**Authors**: Penghui Wen, Zexin Hu, Sen Zhang, Patrick Filippi, Xiaogang Zhu, Allen Benter, Thomas Bishop, Zhiyong Wang, Kun Hu
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13181](https://arxiv.org/abs/2605.13181)

## Summary

Precipitation nowcasting models often suffer from unreliable predictions due to the inherent instability of attention-response energy across samples. This paper theoretically demonstrates how this cross-sample variability propagates through self-attention to increase prediction error. The authors propose HARECast, a novel framework that uses group-wise regularization to stabilize head-wise attention energy. Evaluated on the SEVIR and MeteoNet benchmarks, HARECast demonstrates state-of-the-art reliability and forecasting performance.

## Key Contributions

- Identifies cross-sample instability of attention-response energy as a critical, underexplored source of unreliability in precipitation nowcasting.
- Provides a theoretical derivation linking cross-sample attention variability to an enlarged lower bound on prediction error.
- Introduces HARECast, a group-wise regularization framework that stabilizes attention-response energy and achieves state-of-the-art results on SEVIR and MeteoNet benchmarks.

## Open Questions & Future Work

- [[batch-independent-attention-stabilization]]

## Key Concepts

- [[attention-response-energy-stability]]: A paradigm for improving attention-based forecasting by regularizing the cross-sample variance of attention-response energy across model heads.

## Archivist Review

The paper is approved for its novel insight into attention-response energy as a driver of forecasting unreliability. I have abstracted the specific model name (HARECast) into a more generalizable concept of attention-response energy stability and approved two critical open-source benchmarks utilized. The open question regarding batch-independent stabilization addresses a major bottleneck for the real-world deployment of attention-based forecasting models.

### Approved Concepts
- Attention Response Energy Stability: Identifies cross-sample instability in attention mechanisms as a fundamental source of forecasting unreliability, proposing a general regularization framework for stabilization.

### Approved Open Questions
- Batch-Independent Attention Stabilization: This is a key bottleneck for the operationalization of high-performance attention-based time series models in real-world systems.

### Rejected Candidates
- [concept] Head-wise Attention Response Energy-regulated (HARECast) (`harecast-head-wise-attention-response-energy-regulated-framework`) - subcomponent_of_broader_mechanism: This is a paper-specific model implementation; the underlying mechanism of attention response stability is more fundamental and reusable.

## Datasets

- [[sevir]]
- [[meteonet]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13181)
- [PDF](https://arxiv.org/pdf/2605.13181)

