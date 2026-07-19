---
# CSL-compatible fields
title: "GAttNHP: Group Attention Neural Hawkes Process for Extrapolation Reasoning in Temporal Knowledge Graphs"
author:
  - literal: "Xiangni Tian"
  - literal: "Kaixian Yu"
  - literal: "Runpeng Dai"
  - literal: "Niansheng Tang"
  - literal: "Hao Zhu"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14733"

# Custom fields
paper_id: "2607.14733"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "attention-mechanism"
  - "self-attention"
  - "knowledge-graph"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gattnhp"
  - "non-crossing-quantile-regression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:25:12Z"
created_at: "2026-07-19T07:25:12Z"
---

# GAttNHP: Group Attention Neural Hawkes Process for Extrapolation Reasoning in Temporal Knowledge Graphs

**Authors**: Xiangni Tian, Kaixian Yu, Runpeng Dai, Niansheng Tang, Hao Zhu
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14733](https://arxiv.org/abs/2607.14733)

## Summary

GAttNHP is a unified framework for temporal knowledge graph (TKG) event forecasting that addresses long-range dependencies, inter-chain dynamics, and heavy-tailed inter-arrival times. The approach models subject-relation chains as continuous-time point processes using a self-attention encoder and uses a semantic soft-grouping module to share excitation patterns efficiently across chains. Time prediction is handled by a novel non-crossing quantile regression head, which provides stable and calibrated estimates despite data sparsity. Experiments across six benchmarks show significant improvements in both entity and time prediction, especially for rare, long-tail events.

## Key Contributions

- Introduces GAttNHP, a continuous-time framework for TKG event forecasting using self-attention to encode long-range temporal dependencies.
- Proposes a semantic soft-grouping module that facilitates excitation pattern sharing across event chains via latent group memberships.
- Employs a Non-Crossing Quantile regression head to provide stable, calibrated time predictions for heavy-tailed inter-arrival distributions.
- Demonstrates consistent state-of-the-art performance on six TKG benchmarks, particularly in long-tail event chain prediction.

## Open Questions & Future Work

- [[adaptive-group-multihop-tkg]]

## Key Concepts

- [[gattnhp]]: A continuous-time point process framework for TKG event forecasting that uses self-attention and latent semantic group memberships to handle long-range dependencies and inter-chain excitation.
- [[non-crossing-quantile-regression]]: A regression head for time prediction that enforces monotonic ordering on quantile estimates to ensure stability under heavy-tailed temporal distributions.

## Archivist Review

The approved items focus on the core methodological contributions of GAttNHP: a continuous-time framework for TKG forecasting and an NCQ regression mechanism for robust time prediction. These methods are distinct, reusable, and address core challenges in TKG forecasting that the existing vault lacks. The open question was approved for its focus on the architectural evolution of TKG reasoning components.

### Approved Concepts
- Group Attention Neural Hawkes Process (GAttNHP): It is the central framework introduced to integrate TKG event forecasting with neural Hawkes processes and semantic grouping.
- Non-Crossing Quantile (NCQ) Regression: It addresses the instability of mean-based time prediction in heavy-tailed inter-arrival distributions.

### Approved Open Questions
- Adaptive Grouping and Multi-hop Reasoning: These directions address the limitations of static group assignments and the challenges of complex, multi-hop relationship evolution in dynamic graphs, which are critical for advancing TKG extrapolation capabilities.

## Links

- [Abstract](https://arxiv.org/abs/2607.14733)
- [PDF](https://arxiv.org/pdf/2607.14733)

