---
created_at: '2026-06-07T08:19:32Z'
source_papers:
- '[[openalex-2606.05560-wasserstein-exponential-smoothing]]'
title: Multivariate Wasserstein Exponential Smoothing
---

**Background:** Wasserstein exponential smoothing (WES) utilizes optimal transport to extend exponential smoothing to probability distributions on the real line. The methodology relies on the one-dimensional isometry between the Wasserstein distance and the L2-distance of quantile functions to achieve computational tractability.

**Question / Future Work:** The extension of the WES framework to multivariate probability distributions (distributions on ℝᵈ where d > 1) remains a significant open challenge. The current reliance on the exact isometry between the Wasserstein distance and the L2-distance of quantile functions is specific to one-dimensional domains and does not generalize directly to higher dimensions. Future work is required to develop computationally efficient, regularized approximations of multidimensional Wasserstein geometry that can sustain recursive interpolation without losing the structural simplicity characteristic of the current model.

**Why It Matters:** This is critical because many real-world distributional time series, such as multivariate financial assets or multi-dimensional biosensor readings, naturally reside in higher-dimensional spaces. Without this extension, the applicability of the WES framework remains fundamentally limited.