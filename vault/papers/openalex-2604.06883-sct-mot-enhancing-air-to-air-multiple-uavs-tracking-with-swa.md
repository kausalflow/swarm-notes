---
# CSL-compatible fields
title: "SCT-MOT: Enhancing Air-to-Air Multiple UAVs Tracking with Swarm-Coupled Motion and Trajectory Guidance"
author:
  - literal: "Zhaochen Chu"
  - literal: "Tao Song"
  - literal: "Ren Jin"
  - literal: "Shaoming He"
  - literal: "Defu Lin"
  - literal: "Siqing Cheng"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.06883"

# Custom fields
paper_id: "2604.06883"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multi-agent"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:55:35Z"
created_at: "2026-04-11T05:55:35Z"
---

# SCT-MOT: Enhancing Air-to-Air Multiple UAVs Tracking with Swarm-Coupled Motion and Trajectory Guidance

**Authors**: Zhaochen Chu, Tao Song, Ren Jin, Shaoming He, Defu Lin, Siqing Cheng
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.06883](https://arxiv.org/abs/2604.06883)

## Summary

SCT-MOT is a novel framework for tracking multiple UAVs in air-to-air swarm environments, addressing challenges such as nonlinear group motion and poor visual cues for small objects. The framework employs a Swarm Motion-Aware Trajectory Prediction (SMTP) module to capture swarm-level dependencies and a Trajectory-Guided Spatio-Temporal Feature Fusion (TG-STFF) module to align motion priors with visual features. Extensive validation on the AIRMOT, MOT-FLY, and UAVSwarm datasets demonstrates improved trajectory forecasting accuracy and overall tracking robustness compared to current state-of-the-art methods.

## Key Contributions

- Introduces SCT-MOT, a multi-object tracking framework specifically designed for air-to-air UAV swarm scenarios.
- Develops the SMTP module, which improves nonlinear group motion forecasting by modeling dependencies across a swarm.
- Proposes the TG-STFF module to enhance temporal consistency and spatial discriminability for small, visually ambiguous objects.
- Demonstrates superior performance on three public datasets (AIRMOT, MOT-FLY, UAVSwarm) compared to existing state-of-the-art trackers.

## Open Questions & Future Work

- [[adaptive-trajectory-prediction-window-for-multi-agent-tracking]]

## Archivist Review

I rejected the proposed modules as they are highly paper-specific implementation details rather than broadly applicable forecasting or tracking concepts. I approved one open question focused on the limitation of fixed-length lookback windows in multi-agent dynamics, as this is a known, non-trivial problem in the field. I did not approve the datasets as they are domain-specific benchmarks rather than foundational resources.

### Approved Open Questions
- Adaptive Multi-Agent Trajectory Windows: Fixed window sizes are often suboptimal for heterogeneous swarm maneuvers, making adaptive windowing a critical research direction for tracking robustness.

### Rejected Candidates
- [concept] Swarm Motion-Aware Trajectory Prediction (SMTP) (`swarm-motion-aware-trajectory-prediction-smtp`) - paper_local: This is a paper-specific module implementation rather than a general, reusable tracking concept.
- [concept] Trajectory-Guided Spatio-Temporal Feature Fusion (TG-STFF) (`trajectory-guided-spatio-temporal-feature-fusion-tg-stff`) - paper_local: This is a paper-specific fusion module implementation that does not establish a generalizable method beyond this specific framework.

## Links

- [Abstract](https://arxiv.org/abs/2604.06883)
- [PDF](https://arxiv.org/pdf/2604.06883)

