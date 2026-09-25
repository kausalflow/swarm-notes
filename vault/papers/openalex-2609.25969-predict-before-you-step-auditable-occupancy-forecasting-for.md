---
# CSL-compatible fields
title: "Predict Before You Step: Auditable Occupancy Forecasting for Dynamic Obstacle Avoidance under Sparse Guidance"
author:
  - literal: "Yuhui Mao"
  - literal: "Fen Liu"
  - literal: "Shenghai Yuan"
  - literal: "Tianxin Hu"
  - literal: "Ruimeng Liu"
  - literal: "Rong Su"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25969"

# Custom fields
paper_id: "2609.25969"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-recurrent-occupancy-rollout-policy-loop"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:54:56Z"
created_at: "2026-09-25T09:54:56Z"
---

# Predict Before You Step: Auditable Occupancy Forecasting for Dynamic Obstacle Avoidance under Sparse Guidance

**Authors**: Yuhui Mao, Fen Liu, Shenghai Yuan, Tianxin Hu, Ruimeng Liu, Rong Su
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25969](https://arxiv.org/abs/2609.25969)

## Summary

This paper introduces LOOP (Latent-recurrent Occupancy rollOut Policy), an auditable local avoidance policy for legged robots that connects sparse waypoint guidance to a frozen locomotion controller using future occupancy rollouts. By warping current maps with learned flow and visibility gates over a 1 s horizon, LOOP enables robust velocity selection through geometric risk estimates and map-derived features. Evaluations in Isaac Lab and real-world trials on a Unitree Go2 demonstrate superior collision avoidance against reactive baselines and reliable onboard execution.

## Key Contributions

- Proposed LOOP (Latent-recurrent Occupancy rollOut Policy), connecting sparse waypoint guidance to a frozen locomotion controller at 50 Hz for legged robot obstacle avoidance.
- Developed a recurrent predictor forecasting future occupancy over a 1 s horizon by warping the current map with learned flow and visibility gates.
- Achieved 57.1% head-on success at obstacle speeds of 2.5-3.2 m/s in Isaac Lab evaluations, surpassing a retrained reactive baseline by 8.2 percentage points.
- Demonstrated real-world deployment feasibility on a Unitree Go2 running onboard in 14.5 ms per step with zero collisions across 16 crossing trials.

## Open Questions & Future Work

- [[disentangling-explicit-future-information]]

## Key Concepts

- [[latent-recurrent-occupancy-rollout-policy-loop]]: A local avoidance policy connecting sparse waypoint guidance to a frozen locomotion controller using recurrent occupancy rollouts.

## Archivist Review

Approved the core policy architecture concept (LOOP) as a distinctive approach to auditable occupancy forecasting and dynamic obstacle avoidance under sparse guidance, along with the foundational open question concerning the disentanglement of explicit future information from model capacity. All constraints were strictly followed.

### Approved Concepts
- Latent-recurrent Occupancy rollOut Policy (LOOP): LOOP provides an auditable occupancy rollout mechanism combining sparse waypoint guidance and explicit future map warping for dynamic obstacle avoidance in robotics.

### Approved Open Questions
- Disentangling Explicit Future Information: Crucial for understanding whether predictive representations genuinely improve decision-making or merely act as regularizers or capacity expansions.

## Links

- [Abstract](https://arxiv.org/abs/2609.25969)
- [PDF](https://arxiv.org/pdf/2609.25969)

