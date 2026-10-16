---
# CSL-compatible fields
title: "Physics-Aware Object-Centric SE(3) Forecasting for Real-Time Proactive Dynamic Grasping"
author:
  - literal: "Yirui Zhou"
  - literal: "Hongli Xu"
  - literal: "Ying Zheng"
  - literal: "Yi Wang"
  - literal: "Lap‐Pui Chau"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17843"

# Custom fields
paper_id: "2610.17843"
paper_source: "openalex"
domain: "robotics"
tags:
  - "forecasting"
  - "robotics"
  - "autonomous-agent"
  - "planning"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:23:47Z"
created_at: "2026-10-16T09:23:47Z"
---

# Physics-Aware Object-Centric SE(3) Forecasting for Real-Time Proactive Dynamic Grasping

**Authors**: Yirui Zhou, Hongli Xu, Ying Zheng, Yi Wang, Lap‐Pui Chau
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17843](https://arxiv.org/abs/2610.17843)

## Summary

This paper introduces a physics-aware, object-centric forecasting framework for proactive dynamic grasping that predicts future contact-relevant rigid-body states in SE(3) rather than full visual scenes. By combining a lightweight forecaster trained in randomized physics simulation with a reachability-aware interception selector, the method achieves real-time execution (15 ms) and substantially outperforms reactive baselines across simulation and real-world catching, conveyor, and turntable scenarios.

## Key Contributions

- Proposes a lightweight object-centric forecast-then-select framework that predicts contact-relevant rigid-body trajectories in SE(3) from short pose histories for proactive dynamic grasping.
- Integrates a reachability-aware interception selector to choose feasible contact states under kinematic and timing constraints.
- Improves the average grasping success rate from 24.5% to 62.0% in simulation, and from 15.3% to 67.3% in real-world catching, conveyor, and turntable interception tasks.
- Achieves a fast forecasting runtime of 15 ms, enabling real-time contact decision-making without dense visual future prediction.

## Archivist Review

After rigorous review, no concepts or open questions met the strict vault standards for universal reusability and impact. The single candidate open question on deformable contact dynamics is highly specific to robotic grasping rather than general time-series methodology.

### Rejected Candidates
- [open_question] Deformable and Contact-Aware Dynamics Forecasting (`deformable-and-contact-aware-dynamics-forecasting`) - low_impact: Too specialized to robotics grasping and physics simulation rather than general time-series forecasting methodology or foundational ML bottlenecks.

## Links

- [Abstract](https://arxiv.org/abs/2610.17843)
- [PDF](https://arxiv.org/pdf/2610.17843)

