---
created_at: '2026-05-28T08:38:10Z'
source_papers:
- '[[openalex-2605.25633-exponential-mixing-properties-of-nonlinear-functional-autore]]'
title: Exponential mixing and discretization in NFAR
---

**Background:** Nonlinear functional autoregressive (NFAR) models provide a framework for analyzing functional time series, but their statistical properties rely heavily on stringent mixing conditions and idealized continuous observations.

**Question / Future Work:** It is necessary to extend current exponential mixing conditions to broader noise classes (e.g., sub-Gaussian) and to rigorously derive convergence rates for estimators when using discretely sampled functional time series data where the mesh size varies.

**Why It Matters:** These limitations directly impede the application of high-level functional theory to real-world data, which is essentially discrete and rarely Gaussian.

**Evidence:** Extending this assumption to broader classes of noise distributions... appears to be difficult... We should derive bounds on the error induced by discrete observations... characterize how the convergence rate depends on the mesh size.