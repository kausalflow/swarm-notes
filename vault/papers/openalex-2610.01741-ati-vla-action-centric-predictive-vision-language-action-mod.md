---
# CSL-compatible fields
title: "ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection"
author:
  - literal: "Yijie Zhu"
  - literal: "Rui Shao"
  - literal: "Jie He"
  - literal: "Wei Li"
  - literal: "Bo Zhao"
  - literal: "Yelin Wang"
  - literal: "Xiaochen Yuan"
  - literal: "Tao Tan"
  - literal: "Miao Zhang"
  - literal: "Xiaojiang Peng"
  - literal: "Zitong Yu"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01741"

# Custom fields
paper_id: "2610.01741"
paper_source: "openalex"
domain: "robotics"
tags:
  - "vision-language-model"
  - "multimodal"
  - "agent"
  - "autonomous-agent"
  - "action"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:49:39Z"
created_at: "2026-10-04T10:49:39Z"
---

# ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection

**Authors**: Yijie Zhu, Rui Shao, Jie He, Wei Li, Bo Zhao, Yelin Wang, Xiaochen Yuan, Tao Tan, Miao Zhang, Xiaojiang Peng, Zitong Yu
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01741](https://arxiv.org/abs/2610.01741)

## Summary

Predictive Vision-Language-Action (VLA) models often underperform direct action prediction due to observation-action modality misalignment and conflicting joint optimization objectives. To resolve this, the authors propose ATI-VLA, a framework featuring actionable representation alignment via a shared codebook and action-centric adaptive injection of predictive latents through a lightweight side-path. Experiments on simulation and real-world robotic tasks demonstrate that ATI-VLA achieves state-of-the-art performance and faster training convergence.

## Key Contributions

- Introduces ATI-VLA, an action-centric predictive VLA framework designed to address modality misalignment and joint optimization conflicts in robotic manipulation.
- Proposes Actionable Representation Alignment via a Shared Codebook to map predictive observations and actions into a unified discrete latent space.
- Implements Action-Centric Adaptive Injection using a lightweight adaptive side-path to inject predictive latents as explicit priors under a single action-centric objective.
- Achieves state-of-the-art performance with faster convergence across simulation and real-world robotic tasks.

## Archivist Review

The proposed candidate is a routine scaling suggestion that does not expose a deep technical bottleneck or reusable time-series/forecasting mechanism. Following strict selectivity, no concepts or open questions are approved.

### Rejected Candidates
- [open_question] Scaling to Heterogeneous Robot Datasets (`scaling-predictive-vla-heterogeneous-datasets`) - low_impact: This is a standard future work suggestion proposing scaling to larger and more heterogeneous datasets without introducing a specific unresolved mechanism or limitation.

## Links

- [Abstract](https://arxiv.org/abs/2610.01741)
- [PDF](https://arxiv.org/pdf/2610.01741)

