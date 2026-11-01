---
# CSL-compatible fields
title: "Don't Risk It!: Trajectory-Conditioned Distributional Risk for LiDAR-Only Crowd Navigation"
author:
  - literal: "Mathai Mathew Pulicken"
  - literal: "Laksh Nanwani"
  - literal: "Basant Sharma"
  - literal: "Phani Teja Singamaneni"
  - literal: "Arun Kumar Singh"
  - literal: "K. Madhava Krishna"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.40050"

# Custom fields
paper_id: "2610.40050"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "reinforcement-learning"
  - "robustness"
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
processed_at: "2026-11-01T11:34:07Z"
created_at: "2026-11-01T11:34:07Z"
---

# Don't Risk It!: Trajectory-Conditioned Distributional Risk for LiDAR-Only Crowd Navigation

**Authors**: Mathai Mathew Pulicken, Laksh Nanwani, Basant Sharma, Phani Teja Singamaneni, Arun Kumar Singh, K. Madhava Krishna
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.40050](https://arxiv.org/abs/2610.40050)

## Summary

This paper introduces the Don't Risk It Planner (DRIP), an end-to-end LiDAR-only planning framework for crowd navigation that predicts collision-free space without relying on fragile object tracking. Operating directly on LiDAR occupancy grid histories, DRIP evaluates collision risk by predicting a distribution over minimum robot-obstacle clearance for candidate control sequences. The framework is trained using a risk cost that grounds predictive uncertainty in empirical collision outcomes. Closed-loop experiments with up to 45 pedestrians demonstrate superior success rates, fewer collisions, and reduced freezing behavior compared to state-of-the-art baselines.

## Key Contributions

- Proposes the Don't Risk It Planner (DRIP), an end-to-end LiDAR-only planning framework for crowd navigation that avoids fragile object tracking.
- Couples occupancy forecasting with trajectory-conditioned clearance and uncertainty estimation operating on LiDAR-derived occupancy grid histories.
- Introduces a risk cost that grounds predictive uncertainty directly in empirical collision outcomes rather than geometric regression alone.
- Demonstrates in closed-loop experiments with up to 45 pedestrians higher success rates, fewer collisions, and reduced freezing behavior compared to baselines.

## Archivist Review

Applied strict evaluation standards to ensure only highly reusable, foundational concepts and open questions are added to the vault. Since no candidate concepts were provided and the single open question was highly paper-local, all candidates were rejected.

### Rejected Candidates
- [open_question] Continuous Generative Priors for MMD Risk (`continuous-generative-trajectory-priors-mmd-risk`) - paper_local: Future work direction focuses on combining discrete primitives with MMD risk metrics, which is too paper-local and specific to this crowd navigation architecture.

## Links

- [Abstract](https://arxiv.org/abs/2610.40050)
- [PDF](https://arxiv.org/pdf/2610.40050)

