---
created_at: '2026-05-14T07:38:18Z'
source_papers:
- '[[openalex-2605.10154-stable-long-horizon-pde-forecasting-via-latent-structured-sp]]'
title: Long-Horizon PDE Extrapolation Stability
---

**Background:** Neural surrogates for complex physical systems often struggle to maintain physical consistency when iteratively applied beyond the temporal horizons observed during training.

**Question / Future Work:** Identifying architectural inductive biases that enable stable and physically consistent extrapolation for long-horizon rollouts—beyond simple data-fitting—remains a core challenge in scientific machine learning. Research is required to understand how propagators can be constrained to remain on the manifold of valid physical solutions during recursive inference.

**Why It Matters:** The ability to perform reliable, long-horizon extrapolation is essential for moving beyond short-term mimicry to actionable physical forecasting.

**Evidence:** In this recursive regime, even tiny one-step approximation errors can be nonlinearly amplified, causing the model to drift away from the manifold of physical solutions.