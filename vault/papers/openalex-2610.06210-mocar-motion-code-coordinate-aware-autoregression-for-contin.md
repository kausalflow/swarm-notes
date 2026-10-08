---
# CSL-compatible fields
title: "MoCAR: Motion-code Coordinate-aware AutoRegression for Continuous Trajectory Forecasting"
author:
  - literal: "Yiming Xu"
  - literal: "Hao Cheng"
  - literal: "Monika Sester"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06210"

# Custom fields
paper_id: "2610.06210"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "autoregressive"
  - "multimodal"
  - "planning"
  - "benchmark"
  - "zero-shot-learning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "mocar"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:09Z"
created_at: "2026-10-08T11:41:09Z"
---

# MoCAR: Motion-code Coordinate-aware AutoRegression for Continuous Trajectory Forecasting

**Authors**: Yiming Xu, Hao Cheng, Monika Sester
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06210](https://arxiv.org/abs/2610.06210)

## Summary

MoCAR is a decoder-only framework that casts continuous trajectory forecasting as next-code prediction within a coordinate-aware continuous latent space, avoiding the need for complex proposal-and-refinement pipelines. By learning endpoint-normalized motion codes that jointly capture local trajectory geometry and reference-frame transitions, MoCAR enables stable latent autoregression. Experiments on Argoverse benchmarks demonstrate top-tier performance, robust zero-shot transferability, and strong improvements in turn-heavy scenarios.

## Key Contributions

- Proposes MoCAR, a decoder-only framework that casts continuous trajectory forecasting as next-code prediction in a coordinate-aware latent space.
- Learns a continuous motion-code space from endpoint-normalized trajectory segments capturing local geometry and reference-frame transitions.
- Achieves top-tier performance on Argoverse benchmarks with a single-stage architecture and strong zero-shot transfer capabilities.

## Open Questions & Future Work

- [[generalizing-motion-codes-across-sampling-rates-and-embodiments-1740999511]]

## Key Concepts

- [[mocar]]: A decoder-only framework that casts trajectory forecasting as next-code prediction in a coordinate-aware continuous latent space.

## Archivist Review

Approved the core MoCAR framework note for its novel contribution to continuous trajectory forecasting via coordinate-aware latent autoregression, along with a well-motivated open question on cross-embodiment and sampling rate generalization. Redundant and overly broad benchmark candidates were rejected in accordance with vault standards.

### Approved Concepts
- MoCAR: Introduces a novel coordinate-aware continuous latent space and next-code autoregressive generation framework for trajectory forecasting.

### Approved Open Questions
- Generalizing Motion Codes Across Sampling Rates and Embodiments: Understanding how latent motion codes generalize across different sampling frequencies and embodiments is critical for expanding autoregressive trajectory forecasting beyond autonomous driving.

### Rejected Candidates
- [concept] Motion-code Coordinate-aware AutoRegression (`motion-code-coordinate-aware-autoregression`) - duplicate_existing: Redundant with the MoCAR concept slug.
- [dataset] Argoverse (`argoverse`) - generic: Too broad as a general benchmark suite name without a specific dataset tag unless uniquely formatted.

## Links

- [Abstract](https://arxiv.org/abs/2610.06210)
- [PDF](https://arxiv.org/pdf/2610.06210)

