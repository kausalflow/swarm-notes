---
created_at: '2026-09-25T09:54:06Z'
source_papers:
- '[[openalex-2609.25980-interweaving-marginals-into-multivariate-sample-paths-traini]]'
title: Richer Post-Hoc Dependence Models
---

**Background:** Probabilistic time series foundation models output independent marginal distributions, leaving the reconstruction of multivariate sample paths and joint dependency structures as a post-processing challenge.

**Question / Future Work:** Investigate whether richer or more complex post-hoc dependence models beyond simple separable Gaussian copulas or historical rank templates can yield further gains in multivariate forecast sample path generation.

**Why It Matters:** It highlights an explicit methodological limitation in current separable copula formulations and outlines a concrete direction for improving training-free dependence construction in time series foundation models.

**Evidence:** These findings support dependence reconstruction as a distinct post-processing problem for frozen probabilistic TSFMs and motivate investigating whether richer post-hoc dependence models can yield further gains.