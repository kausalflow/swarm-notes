---
# CSL-compatible fields
title: "Forecasting Motion in the Wild"
author:
  - literal: "Neerja Thakkar"
  - literal: "Shiry Ginosar"
  - literal: "Jacob Walker"
  - literal: "Jitendra Malik"
  - literal: "Joao Carreira"
  - literal: "Carl Doersch"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.01015"

# Custom fields
paper_id: "2604.01015"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "transformer"
  - "multimodal"
  - "computer-vision"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "dense-point-trajectories"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:49:16Z"
created_at: "2026-04-04T05:49:16Z"
---

# Forecasting Motion in the Wild

**Authors**: Neerja Thakkar, Shiry Ginosar, Jacob Walker, Jitendra Malik, Joao Carreira, Carl Doersch
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.01015](https://arxiv.org/abs/2604.01015)

## Summary

This paper addresses the challenge of predictive visual intelligence by introducing dense point trajectories as a structured mid-level representation that disentangles motion from appearance. The authors propose a diffusion transformer that models these trajectories as visual tokens, allowing the system to reason about occlusion and forecast complex motion patterns of diverse, non-rigid agents. To support this approach, they provide a 300-hour, in-the-wild video dataset and demonstrate that their method achieves category-agnostic, data-efficient predictions that outperform existing state-of-the-art baselines.

## Key Contributions

- Introduces dense point trajectories as a mid-level representation to disentangle motion from appearance in complex, non-rigid agents.
- Develops a diffusion transformer architecture capable of modeling unordered trajectory sets while explicitly reasoning about occlusion for coherent motion forecasting.
- Curates a large-scale, 300-hour in-the-wild animal video dataset with integrated shot detection and camera-motion compensation.

## Open Questions & Future Work

- [[generalizing-behavior-forecasting]]

## Key Concepts

- [[dense-point-trajectories]]: A mid-level visual representation that uses dense point trajectories to disentangle motion from appearance across diverse, non-rigid agents.

## Archivist Review

I approved the core representation (Dense point trajectories) as it provides a reusable abstraction for category-agnostic motion modeling, and the open question regarding generalizable behavior forecasting as it highlights a substantial bottleneck in transitioning from specific to foundational models of motion. I rejected no candidates because only one concept and one open question were provided and both met the criteria for inclusion in the vault. No datasets were approved as none were specifically named in the provided input.

### Approved Concepts
- Dense point trajectories: It serves as the core representation for disentangling motion from appearance to enable category-agnostic behavior forecasting.

### Approved Open Questions
- Generalizing Behavior Forecasting Representations: Establishing a category-agnostic behavior forecasting framework is essential for moving beyond narrow, domain-specific models towards true predictive visual intelligence. Understanding the limits and extensions of this trajectory-token approach is crucial for scaling motion understanding in unconstrained, real-world settings.

## Links

- [Abstract](https://arxiv.org/abs/2604.01015)
- [PDF](https://arxiv.org/pdf/2604.01015)

