---
created_at: '2026-10-08T11:41:09Z'
source_papers:
- '[[openalex-2610.06210-mocar-motion-code-coordinate-aware-autoregression-for-contin]]'
title: Generalizing Motion Codes Across Sampling Rates and Embodiments
---

**Background:** Continuous trajectory forecasting models for autonomous driving often rely on task-specific decoding pipelines or trajectory-space re-tokenization, raising the question of how alternative latent representation designs and cross-dataset adaptation can be unified.

**Question / Future Work:** Explore how endpoint-normalized continuous motion codes and decoder-only autoregressive latent rollouts can be further generalized across diverse temporal sampling rates, different sensor horizons, and non-driving robotics domains without requiring extensive task-specific re-engineering.

**Why It Matters:** Understanding how latent motion codes generalize across different sampling frequencies and embodiments is critical for expanding autoregressive trajectory forecasting beyond autonomous driving.

**Evidence:** Other rates require temporal resampling or adaptation of the code duration... may extend beyond road-agent forecasting, since many robotic, aerial, and embodied systems also require continuous rollout under evolving local coordinate frames.