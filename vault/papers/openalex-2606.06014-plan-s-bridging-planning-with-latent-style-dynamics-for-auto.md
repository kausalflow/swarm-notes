---
# CSL-compatible fields
title: "PLAN-S: Bridging Planning with Latent Style Dynamics for Autonomous Driving World Models"
author:
  - literal: "Xiaoyun Qiu"
  - literal: "Jingtao He"
  - literal: "Yijie Chen"
  - literal: "Yusong Huang"
  - literal: "Haotian Wang"
  - literal: "Yixuan Wang"
  - literal: "Xinhu Zheng"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06014"

# Custom fields
paper_id: "2606.06014"
paper_source: "openalex"
domain: "robotics"
tags:
  - "llm"
  - "multimodal"
  - "agent"
  - "planning"
architectures:
  []
datasets:
  - "nuScenes"
  - "NAVSIM"
concept_slugs:
  - "plan-s-planner-facing-bridge"
dataset_slugs:
  - "nuscenes"
  - "navsim"
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:21:01Z"
created_at: "2026-06-07T08:21:01Z"
---

# PLAN-S: Bridging Planning with Latent Style Dynamics for Autonomous Driving World Models

**Authors**: Xiaoyun Qiu, Jingtao He, Yijie Chen, Yusong Huang, Haotian Wang, Yixuan Wang, Xinhu Zheng
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06014](https://arxiv.org/abs/2606.06014)

## Summary

PLAN-S addresses the lack of controllability in end-to-end latent world model planners by introducing an intermediate bridge that decodes style-conditioned, four-channel semantic cost maps. This bridge provides explicit control over risk and driving preferences before final trajectory generation, bypassing the limitations of direct latent-to-trajectory mapping. The approach is validated across diverse planner types and driving benchmarks, demonstrating significant safety improvements and scene-consistent style modulation.

## Key Contributions

- Introduces PLAN-S, a style-conditioned semantic cost map bridge between latent world models and downstream trajectory planners.
- Demonstrates modularity and performance gains by successfully integrating with frozen backbones ResWorld (nuScenes) and WoTE (NAVSIM).
- Achieves 42% relative reduction in 3s collision rate on nuScenes and reaches 89.4 PDMS on NAVSIM through improved risk and style-aware trajectory selection.

## Open Questions & Future Work

- [[latent-style-controllability-metrics]]

## Key Concepts

- [[plan-s-planner-facing-bridge]]: A planner-facing bridge architecture that decodes style-conditioned semantic cost maps from latent world model representations to enhance planning controllability.

## Archivist Review

I have approved the core concept 'PLAN-S' as a reusable planner-facing bridge architecture and the open question regarding metrics for latent-space controllability. The datasets nuScenes and NAVSIM were approved as they are central to the evaluation of robotics and autonomous driving models. All other candidates were rejected as they were either too narrow or did not meet the requirement for high-level research impact.

### Approved Concepts
- PLAN-S (Planner-Facing Bridge): Addresses the compactness-controllability dilemma in latent world models for autonomous driving by decoupling latent scene dynamics from trajectory planning via style-conditioned cost maps, providing a modular interface for downstream planners.

### Approved Open Questions
- Metrics for Latent Style Controllability: Without clear, objective metrics for latent-space controllability, it is difficult to guarantee that driving policies adapt to user preferences in safe, predictable ways, which is essential for personalizing autonomous driving systems.

## Datasets

- [[nuscenes]]
- [[navsim]]

## Links

- [Abstract](https://arxiv.org/abs/2606.06014)
- [PDF](https://arxiv.org/pdf/2606.06014)

