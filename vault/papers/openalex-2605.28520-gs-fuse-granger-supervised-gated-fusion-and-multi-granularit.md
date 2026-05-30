---
# CSL-compatible fields
title: "GS-FUSE: Granger-Supervised Gated Fusion and Multi-Granularity Alignment for Event-Driven Financial Forecasting"
author:
  - literal: "Yang Zhang"
  - literal: "En Chun"
  - literal: "Ziyun Mao"
  - literal: "Yulu Wu"
  - literal: "Jun Wang"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28520"

# Custom fields
paper_id: "2605.28520"
paper_source: "openalex"
domain: "finance"
tags:
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "language-model"
  - "llm"
  - "adapter"
architectures:
  []
datasets:
  []
concept_slugs:
  - "granger-supervised-gated-fusion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:35:28Z"
created_at: "2026-05-30T07:35:28Z"
---

# GS-FUSE: Granger-Supervised Gated Fusion and Multi-Granularity Alignment for Event-Driven Financial Forecasting

**Authors**: Yang Zhang, En Chun, Ziyun Mao, Yulu Wu, Jun Wang
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28520](https://arxiv.org/abs/2605.28520)

## Summary

GS-Fuse is a multimodal event-based forecasting framework that improves market prediction by explicitly modeling the causal relationship between financial events and price trajectories. Unlike symmetric fusion approaches, it uses a Granger-supervised gated fusion module to selectively incorporate textual signals only when they provide incremental value over historical price trends. Additionally, a multi-granularity alignment mechanism ensures that both high-level event summaries and fine-grained textual cues are effectively aligned with future market movements. The framework operates as a plug-and-play adapter compatible with existing LLM and time-series backbones.

## Key Contributions

- Introduced GS-Fuse, a flexible, plug-and-play adapter framework for multimodal financial forecasting that integrates textual and price signals.
- Developed a Granger-supervised gated fusion module that ensures event text is utilized only when it provides incremental predictive value beyond historical price data.
- Proposed a multi-granularity alignment mechanism to bridge high-level events and fine-grained textual cues with market outcomes, achieving consistent SOTA performance across multiple asset classes and horizons.

## Open Questions & Future Work

- [[structural-causal-modeling-financial-regimes]]

## Key Concepts

- [[granger-supervised-gated-fusion]]: A multimodal fusion mechanism that selectively utilizes auxiliary data based on its Granger-causal predictive utility relative to time-series history.

## Archivist Review

I approved the Granger-supervised gated fusion mechanism as it offers a specific, reusable causal-aware gating logic for multimodal forecasting. I rejected the multi-granularity alignment concept because it is a generic objective frequently used in multimodal literature without a distinct or unique implementation strategy described here. The open question was approved for its focus on the fundamental limitations of using Granger-causality as a proxy for structural causal discovery in financial forecasting.

### Approved Concepts
- Granger-supervised gated fusion: It provides a novel, causal-aware method to selectively fuse multimodal data by learning the incremental predictive value of one modality relative to another, addressing the common problem of redundant or noisy multimodal inputs.

### Approved Open Questions
- Structural Causal Financial Modeling: Bridging the gap between statistical predictive utility and structural causal discovery is a fundamental bottleneck for deploying event-driven models in complex, non-stationary financial environments.

### Rejected Candidates
- [concept] Multi-granularity alignment (`multi-granularity-alignment`) - generic: This is a common, generic architectural objective in multimodal learning that lacks a sufficiently unique or reusable technical definition to warrant a standalone vault note.

## Links

- [Abstract](https://arxiv.org/abs/2605.28520)
- [PDF](https://arxiv.org/pdf/2605.28520)

