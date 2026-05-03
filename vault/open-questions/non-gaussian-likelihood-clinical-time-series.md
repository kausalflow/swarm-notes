---
created_at: '2026-05-03T07:13:52Z'
source_papers:
- '[[openalex-2604.27967-differentiable-latent-structure-discovery-for-interpretable]]'
title: Non-Gaussian clinical likelihoods
---

**Background:** Clinical time series often exhibit heterogeneous measurement distributions, discrete states, and indicators that deviate from standard Gaussian assumptions.

**Question / Future Work:** Developing model formulations that accommodate non-Gaussian likelihoods within structural Gaussian processes is essential for capturing discrete clinical events, censored data, and non-linear physiological thresholds.

**Why It Matters:** Most real-world clinical variables (e.g., categorical medications, mortality events) violate Gaussian assumptions, making this a critical extension for model utility.

**Evidence:** The main limitation of the current implementation is that, since this study focused on developing the model’s structural assumptions, we restricted our experiments to Gaussian likelihoods. ... more flexible likelihood formulations ... would be necessary to capture the heterogeneity of clinical time series and to jointly model discrete patient states.