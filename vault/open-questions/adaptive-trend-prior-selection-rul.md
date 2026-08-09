---
created_at: '2026-08-09T05:41:06Z'
source_papers:
- '[[openalex-2608.05925-local-global-feature-mixer-and-trend-guided-consistent-learn]]'
title: Adaptive Trend Prior Selection
---

**Background:** Remaining useful life (RUL) prediction of rotating machinery using degradation-process (DP) modeling often suffers from error accumulation and failure to preserve irreversible degradation trends over long horizons during recursive health indicator (HI) extrapolation.

**Question / Future Work:** Investigate whether an adaptive procedure can be developed to automatically select or estimate the trend function family (e.g., linear, polynomial, exponential, or mixtures thereof) directly from the observed HI prefix or validation data, thereby eliminating reliance on manually prescribed functional priors while avoiding data leakage from unobserved future observations.

**Why It Matters:** Manual specification of trend priors limits the generalizability of trend-guided consistent learning across diverse mechanical degradation regimes, making an adaptive or learnable trend-family selection method crucial for robust autonomous RUL prognostics.