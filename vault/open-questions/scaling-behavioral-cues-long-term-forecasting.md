---
created_at: '2026-07-04T07:36:53Z'
source_papers:
- '[[openalex-2607.00296-learning-when-to-listen-gated-affect-fusion-for-human-motion]]'
title: Scaling Behavioral Cues for Forecasting
---

**Background:** Auxiliary behavioral cues are often noisy and vary in predictive utility, often leading to performance degradation in long-term forecasting when naively fused with kinematic trajectories.

**Question / Future Work:** There is a fundamental challenge in effectively integrating auxiliary multimodal behavioral signals (e.g., affect, speech, text) into motion forecasting without introducing noise that overwhelms long-term kinematic priors. Future work must resolve how to scale these cues beyond short-to-medium horizons and move toward causal world models that jointly learn the interaction between contextual behavioral signals and physical movement.

**Why It Matters:** This question defines the boundary between immediate reactive motion (affect-driven) and long-term behavioral planning, which is a core bottleneck in human-centric forecasting.

**Evidence:** empirical results indicate that facial affect features provide bounded, horizon-dependent predictive cues strictly within short-to-medium windows ... whereas long-term trajectories remain predominantly governed by intrinsic kinematic continuity.