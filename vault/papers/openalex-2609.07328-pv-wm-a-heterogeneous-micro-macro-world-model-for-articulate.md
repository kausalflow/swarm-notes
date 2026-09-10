---
# CSL-compatible fields
title: "PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout"
author:
  - literal: "Haozhuang Chi"
  - literal: "Jingsong Liang"
  - literal: "Ziying Song"
  - literal: "Lei Yang"
  - literal: "Shihao Li"
  - literal: "Haoruo Zhang"
  - literal: "Chen Lv"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07328"

# Custom fields
paper_id: "2609.07328"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "robotics"
  - "forecasting"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:32Z"
created_at: "2026-09-10T09:17:32Z"
---

# PV-WM: A Heterogeneous Micro-Macro World Model for Articulated Pedestrian-Vehicle Co-Rollout

**Authors**: Haozhuang Chi, Jingsong Liang, Ziying Song, Lei Yang, Shihao Li, Haoruo Zhang, Chen Lv
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07328](https://arxiv.org/abs/2609.07328)

## Summary

PV-WM is a heterogeneous micro-macro world model that jointly predicts pedestrian root locomotion, 15-joint articulation, and rigid vehicle kinematics through synchronized recurrent rollouts. By operating over structured post-perception tracks and recomputing pedestrian-vehicle geometry after every transition, PV-WM captures multi-scale agent dynamics. Evaluated across Waymo contexts, the framework outperforms modular specialist baselines while substantially reducing parameter count and computational latency.

## Key Contributions

- Introduces PV-WM, a heterogeneous micro-macro world model that unifies pedestrian root motion, 15-joint articulation, and rigid vehicle states into a synchronized recurrent rollout.
- Demonstrates that recurrent execution over chunks reduces Root ADE by 12.7% and MPJPE by 14.8% relative to a matched one-shot complete-state predictor.
- Achieves reductions of 5.2% in Root ADE, 7.6% in MPJPE, 11.9% in P-V distance error, and 5.8% in oriented-box closest-approach error compared to a modular specialist on Waymo contexts while requiring 57.1% fewer parameters and 96.5% lower FLOPs.

## Archivist Review

The paper presents PV-WM for joint pedestrian-vehicle co-rollout, but the techniques and dataset references are domain-specific to autonomous driving robotics and do not introduce canonical reusable concepts or datasets suited for long-term vault inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2609.07328)
- [PDF](https://arxiv.org/pdf/2609.07328)

