---
# CSL-compatible fields
title: "LAMP: Lane-Aligned Motion Primitives for Feasible Trajectory Prediction"
author:
  - literal: "Sangjin Han"
  - literal: "Hoseong Jung"
  - literal: "Jeongtae Her"
  - literal: "Changhyun Choi"
  - literal: "H. Jin Kim"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26661"

# Custom fields
paper_id: "2606.26661"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "vae"
  - "multimodal"
architectures:
  []
datasets:
  - "argoverse-2"
concept_slugs:
  - "lane-aligned-motion-primitives-lamp"
dataset_slugs:
  - "argoverse-2"
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:48Z"
created_at: "2026-06-28T08:16:48Z"
---

# LAMP: Lane-Aligned Motion Primitives for Feasible Trajectory Prediction

**Authors**: Sangjin Han, Hoseong Jung, Jeongtae Her, Changhyun Choi, H. Jin Kim
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26661](https://arxiv.org/abs/2606.26661)

## Summary

This paper introduces LAMP, a motion forecasting framework designed to improve the feasibility and logical consistency of predicted trajectories in autonomous driving. By utilizing a VQ-VAE, the model learns discrete, shape-aware motion primitives that better capture spatiotemporal patterns compared to traditional endpoint-based methods. A feasibility-aware intention selector further refines these predictions by applying lane-topology priors, ensuring that the model prioritizes paths that adhere to road geometry. Experiments on the Argoverse 2 dataset show that LAMP effectively balances prediction accuracy with physical and logical feasibility.

## Key Contributions

- Proposes LAMP, a topology-aware forecasting framework that anchors multimodal predictions to lane-aligned motion primitives.
- Uses a VQ-VAE to capture complex spatiotemporal patterns as discrete intention queries, improving over standard endpoint-based representations.
- Introduces a feasibility-aware intention selector with a lane-topology prior to filter unreachable trajectories while maintaining multimodal diversity.
- Achieves state-of-the-art performance on Argoverse 2 regarding trajectory feasibility and diversity while maintaining competitive prediction accuracy.

## Open Questions & Future Work

- [[diversity-preserving-scene-adaptation]]

## Key Concepts

- [[lane-aligned-motion-primitives-lamp]]: A motion forecasting framework that anchors multimodal trajectory predictions to discrete, lane-topology-aware motion primitives learned via VQ-VAE.

## Archivist Review

I approved the core framework LAMP and the identified open question regarding the feasibility-diversity trade-off in trajectory prediction, as these address significant limitations in robotic motion forecasting. Argoverse 2 is approved as a canonical dataset for this domain. I rejected other candidates as they were either subcomponents or encompassed by these core concepts.

### Approved Concepts
- Lane-Aligned Motion Primitives (LAMP): This is the core methodology of the paper, enabling topology-aware motion forecasting that enforces feasibility in trajectory prediction.

### Approved Open Questions
- Diversity-Preserving Scene Adaptation: Achieving both diversity and feasibility is critical for autonomous driving; systems that either produce infeasible trajectories or lack the necessary behavioral variety fail to support safe, robust downstream planning.

## Datasets

- [[argoverse-2]]

## Links

- [Abstract](https://arxiv.org/abs/2606.26661)
- [PDF](https://arxiv.org/pdf/2606.26661)

