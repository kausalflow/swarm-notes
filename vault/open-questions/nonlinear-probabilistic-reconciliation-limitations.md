---
created_at: '2026-05-02T06:56:19Z'
source_papers:
- '[[openalex-2604.26668-nonlinear-probabilistic-forecast-reconciliation]]'
title: Nonlinear Probabilistic Reconciliation Limitations
---

**Background:** Probabilistic forecast reconciliation involves adjusting base forecasts to satisfy specific constraints, historically focused on linear relationships. Recent work has extended these methods to handle nonlinear constraints via projection and sampling-based conditioning.

**Question / Future Work:** The current reliance on Gaussian assumptions and Euclidean distances limits the applicability of these methods to complex, non-Gaussian, or discrete-type time series. Research is required to develop robust reconciliation approaches that handle non-Gaussian distributions, leverage geodesic-distance-based scoring rules on nonlinear manifolds, and scale effectively without reliance on UKF-style Gaussian assumptions.

**Why It Matters:** The current reliance on Gaussian assumptions and Euclidean distances limits the applicability of these reconciliation methods to a wide range of real-world datasets that do not adhere to these properties.