---
created_at: '2026-05-28T08:37:43Z'
source_papers:
- '[[openalex-2605.26052-quantile-autoregressive-moving-average-models-for-ratio-base]]'
title: Enforcing quantile monotonicity
---

**Background:** Dynamic quantile models often face the crossing problem where independently estimated quantiles violate the fundamental monotonicity constraint.

**Question / Future Work:** Developing techniques to enforce or ensure quantile monotonicity in multi-quantile ULS–ARMA frameworks is essential to maintain coherent conditional distribution estimates.

**Why It Matters:** Monotonicity is a critical property for coherent multi-quantile forecasting; without it, interpretations of the conditional distribution's shape and extremes become invalid.

**Evidence:** As in other quantile-based time series frameworks, if several quantiles are modeled independently, their estimated trajectories might not satisfy the natural monotonicity across τ.