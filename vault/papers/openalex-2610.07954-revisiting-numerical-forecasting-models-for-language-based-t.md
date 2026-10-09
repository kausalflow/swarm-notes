---
# CSL-compatible fields
title: "Revisiting Numerical Forecasting Models for Language-Based Trajectory Prediction"
author:
  - literal: "JunGyu Lee"
  - literal: "Inhwan Bae"
  - literal: "Hae‐Gon Jeon"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.07954"

# Custom fields
paper_id: "2610.07954"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "reinforcement-learning"
  - "trajectory-prediction"
  - "language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mixture-of-reward-experts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:19Z"
created_at: "2026-10-09T11:35:19Z"
---

# Revisiting Numerical Forecasting Models for Language-Based Trajectory Prediction

**Authors**: JunGyu Lee, Inhwan Bae, Hae‐Gon Jeon
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.07954](https://arxiv.org/abs/2610.07954)

## Summary

Language-based trajectory predictors capture behavioral intent and social context by treating coordinates as discrete tokens, but lack direct guidance for continuous coordinate-space dynamics. To address this, the authors introduce MoRE (Mixture of Reward Experts), a reinforcement learning framework that transfers numerical forecasting priors into pretrained language models via an uncertainty-weighted consensus reward. By focusing policy refinement on high-entropy samples using cached expert predictions, MoRE improves trajectory accuracy on benchmarks like ETH-UCY, SDD, and NBA without increasing inference latency or memory.

## Key Contributions

- Introduces MoRE, a reinforcement learning refinement framework that transfers numerical forecasting priors into pretrained language-based trajectory predictors.
- Leverages an uncertainty-weighted consensus of five frozen numerical predictors converted into expert rewards to provide direct coordinate-level guidance.
- Achieves performance improvements on ETH-UCY, reducing ADE from 0.22 to 0.20 m and FDE from 0.32 to 0.29 m, alongside reductions on SDD and NBA datasets.
- Reduces collision rates and aligns pedestrian spacing with ground-truth distributions without increasing inference memory or latency.

## Open Questions & Future Work

- [[deterministic-forecasters-adaptive-expert-weighting]]

## Key Concepts

- [[mixture-of-reward-experts]]: A reinforcement learning refinement framework that transfers numerical forecasting priors into language-based trajectory predictors via uncertainty-weighted consensus rewards.

## Archivist Review

Approved the core methodological framework 'Mixture of Reward Experts' as a reusable concept for transferring continuous numerical priors into language models via reinforcement learning, along with its associated open question on deterministic forecaster improvement and adaptive expert weighting. Standard benchmark datasets (ETH-UCY, SDD, NBA) were rejected in accordance with policy to avoid routine dataset clutter.

### Approved Concepts
- Mixture of Reward Experts: Central mechanism combining numerical forecasting priors with language-based trajectory prediction via reinforcement learning and uncertainty-weighted consensus.

### Approved Open Questions
- Deterministic Forecasters and Adaptive Expert Weighting: Crucial for overcoming current limitations in deterministic trajectory forecasting and improving the robustness of multi-expert consensus rewards in reward-guided language policies.

### Rejected Candidates
- [dataset] ETH-UCY (`eth-ucy`) - not_reusable: Standard benchmark dataset commonly evaluated in trajectory forecasting without introducing distinct conceptual methodology.

## Links

- [Abstract](https://arxiv.org/abs/2610.07954)
- [PDF](https://arxiv.org/pdf/2610.07954)

