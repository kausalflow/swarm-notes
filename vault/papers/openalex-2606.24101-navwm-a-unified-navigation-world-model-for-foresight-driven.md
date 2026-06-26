---
# CSL-compatible fields
title: "NavWM: A Unified Navigation World Model for Foresight-Driven Planning"
author:
  - literal: "Y. Mei"
  - literal: "Longteng Guo"
  - literal: "YU Ming-ming"
  - literal: "Guiyu Zhao"
  - literal: "X He"
  - literal: "Jing Liu"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24101"

# Custom fields
paper_id: "2606.24101"
paper_source: "openalex"
domain: "robotics"
tags:
  - "world-model"
  - "multimodal"
  - "navigation"
  - "robotics"
  - "planning"
  - "trajectory-forecasting"
  - "autonomous-agent"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "navwm-framework"
  - "anchor-based-multimodal-trajectory-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:26:22Z"
created_at: "2026-06-26T08:26:22Z"
---

# NavWM: A Unified Navigation World Model for Foresight-Driven Planning

**Authors**: Y. Mei, Longteng Guo, YU Ming-ming, Guiyu Zhao, X He, Jing Liu
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24101](https://arxiv.org/abs/2606.24101)

## Summary

NavWM is a unified navigation world model that bridges the gap between perception, generation, and control by jointly modeling spatio-temporal dynamics. The model uses latent world tokens to capture geometric and semantic priors, which are then used to inform an anchor-based trajectory forecasting framework. By generating a diverse multimodal action space, NavWM functions as a closed-loop planner that uses visual foresight to select optimal navigation paths. The approach consistently outperforms previous navigation methods in success rates and future state fidelity.

## Key Contributions

- Introduces NavWM, a unified world model that integrates latent world reasoning, multimodal action prediction, and visual generation.
- Proposes an anchor-based multimodal trajectory forecasting framework to produce diverse action spaces and mitigate mode collapse in navigation.
- Demonstrates state-of-the-art performance in high-fidelity future state generation and zero-shot navigation success across robotics benchmarks.

## Open Questions & Future Work

- [[scaling-world-models-to-open-world-navigation]]

## Key Concepts

- [[navwm-framework]]: A unified navigation world model that integrates latent world reasoning, multimodal action prediction, and controllable visual generation for robotic planning.
- [[anchor-based-multimodal-trajectory-forecasting]]: A trajectory forecasting approach utilizing anchor trajectories to generate a diverse action space and mitigate mode collapse in navigation tasks.

## Archivist Review

NavWM is approved as a representative framework for integrating perception, generation, and control, and the anchor-based trajectory forecasting method is approved as a reusable technique to mitigate mode collapse in planning tasks. The open question regarding open-world scaling is approved as it addresses a critical, non-trivial limitation in embodied world model generalization. Other candidates were not submitted.

### Approved Concepts
- NavWM: Serves as a comprehensive architectural pattern for unified navigation and world modeling.
- Anchor-based Multimodal Trajectory Forecasting: Provides a specific mechanism to induce diversity in trajectory generation for planning agents.

### Approved Open Questions
- Scaling World Models to Open-World: Generalization is a fundamental bottleneck for embodied agents, limiting their deployment in non-controlled, real-world settings.

## Links

- [Abstract](https://arxiv.org/abs/2606.24101)
- [PDF](https://arxiv.org/pdf/2606.24101)

