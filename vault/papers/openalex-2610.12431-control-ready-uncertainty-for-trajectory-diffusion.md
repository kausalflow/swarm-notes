---
# CSL-compatible fields
title: "Control-Ready Uncertainty for Trajectory Diffusion"
author:
  - literal: "Zhiwei Xue"
  - literal: "Jia Yue Kam"
  - literal: "Jinhang Qiu"
  - literal: "Yifeng Cheng"
  - literal: "Ege Gursoy"
  - literal: "Jiaming Wang"
  - literal: "Vincent Bonnet"
  - literal: "Harold Soh"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12431"

# Custom fields
paper_id: "2610.12431"
paper_source: "openalex"
domain: "robotics"
tags:
  - "diffusion-model"
  - "robotics"
  - "uncertainty"
  - "forecasting"
  - "generative-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "scope"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:05:37Z"
created_at: "2026-10-11T11:05:37Z"
---

# Control-Ready Uncertainty for Trajectory Diffusion

**Authors**: Zhiwei Xue, Jia Yue Kam, Jinhang Qiu, Yifeng Cheng, Ege Gursoy, Jiaming Wang, Vincent Bonnet, Harold Soh
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12431](https://arxiv.org/abs/2610.12431)

## Summary

Diffusion models excel at representing multimodal trajectory distributions, but extracting uncertainty usually demands costly Monte Carlo sampling, hindering real-time control. To resolve this, the paper introduces Score-Curvature for Online Precision Estimation (SCOPE), a lightweight module that appends control-ready uncertainty to diffusion trajectory models. SCOPE distills score-curvature information to learn structured precision matrices around nominal trajectories, generating calibrated Gaussian tubes with minimal overhead. Experiments across pedestrian forecasting, crowd navigation, Maze2D control, and real-world robot manipulation show that SCOPE enables fast uncertainty estimation and enhances closed-loop performance.

## Key Contributions

- Introduces SCOPE, a lightweight module that augments diffusion trajectory models with control-ready uncertainty without Monte Carlo sampling.
- Learns a structured precision matrix around nominal trajectories by distilling score-curvature information to produce calibrated Gaussian tubes.
- Demonstrates improved closed-loop performance in pedestrian forecasting, crowd navigation, Maze2D control, and real-world robotic manipulation.

## Open Questions & Future Work

- [[visual-observation-trajectory-diffusion-uncertainty]]

## Key Concepts

- [[scope]]: A lightweight module that augments diffusion trajectory models with control-ready uncertainty by distilling score-curvature information into calibrated Gaussian tubes.

## Archivist Review

Approved SCOPE as a valuable, reusable module for fast uncertainty extraction from diffusion trajectory models, along with its corresponding future work on extending score-curvature estimation to high-dimensional visual observations.

### Approved Concepts
- Score-Curvature for Online Precision Estimation (SCOPE): Introduces a lightweight module for extracting calibrated covariance estimates from diffusion models without expensive Monte Carlo sampling.

### Approved Open Questions
- Visual Observation Trajectory Diffusion Uncertainty: Enables uncertainty-aware trajectory diffusion and planning directly from high-dimensional sensor streams without requiring explicit lower-dimensional state tracking.

## Links

- [Abstract](https://arxiv.org/abs/2610.12431)
- [PDF](https://arxiv.org/pdf/2610.12431)

