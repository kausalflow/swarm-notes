---
# CSL-compatible fields
title: "GazeFS: Target-Centered Gaze-Trajectory Forecasting and Stabilization from Gaze-Head History"
author:
  - literal: "夏要争"
  - literal: "Zaiping Zhu"
  - literal: "Bo Pang"
  - literal: "Minghao Xie"
  - literal: "Hui Li"
  - literal: "Shaorong Wang"
  - literal: "Sheng Li"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03868"

# Custom fields
paper_id: "2609.03868"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "trajectory-prediction"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gazefs"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-06T09:01:13Z"
created_at: "2026-09-06T09:01:13Z"
---

# GazeFS: Target-Centered Gaze-Trajectory Forecasting and Stabilization from Gaze-Head History

**Authors**: 夏要争, Zaiping Zhu, Bo Pang, Minghao Xie, Hui Li, Shaorong Wang, Sheng Li
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03868](https://arxiv.org/abs/2609.03868)

## Summary

This paper introduces GazeFS, an online framework for target-centered gaze-trajectory forecasting and stabilization that maps variable-length gaze-head history to target-center directions and Search/Focus phases without requiring target information at inference. Evaluated across 7,960 acquisition episodes from 30 participants, GazeFS significantly reduces target error, bias, and dispersion compared to raw holds while maintaining robust phase estimation performance.

## Key Contributions

- Formulates gaze correction as online target-centered gaze-trajectory forecasting and stabilization.
- Introduces GazeFS, mapping variable-length gaze-head history to target-center directions and Search/Focus estimates without target information at inference.
- Demonstrates significant reductions in Focus episode bias (0.182 deg), within-episode dispersion (0.257 deg), and P90 target error (0.400 deg) across 7,960 acquisition episodes from 30 participants.

## Open Questions & Future Work

- [[temporal-smoothness-gaze-stabilization]]

## Key Concepts

- [[gazefs]]: An online target-centered gaze-trajectory forecasting and stabilization framework that maps gaze-head history to target-center directions and search-focus estimates without target information at inference.

## Archivist Review

Approved the core GazeFS framework concept and the open question regarding the trade-off between spatial target centering and temporal smoothness in gaze stabilization, adhering to strict scarcity guidelines.

### Approved Concepts
- GazeFS: GazeFS is the central framework introduced in the paper for target-centered gaze-trajectory forecasting and stabilization.

### Approved Open Questions
- Temporal Smoothness in Gaze Stabilization: Crucial for bridging the gap between spatial gaze correction and perceptual jitter reduction in real-time extended reality (XR) interaction systems.

## Links

- [Abstract](https://arxiv.org/abs/2609.03868)
- [PDF](https://arxiv.org/pdf/2609.03868)

