---
created_at: '2026-07-16T07:14:33Z'
source_papers:
- '[[openalex-2607.11470-climate-invariant-conformal-prediction-intervals-for-multi-h]]'
title: Valid Conformal Prediction for Non-Exchangeable Series
---

**Background:** Conformal prediction typically assumes that data points are exchangeable, an assumption that is frequently violated in time-series forecasting due to temporal dependence and non-stationarity.

**Question / Future Work:** There is a need for robust, adaptive conformal prediction techniques for time series that provide rigorous validity guarantees despite temporal dependence and distribution drift, moving beyond current empirical mitigation strategies.

**Why It Matters:** Standard conformal prediction lacks formal validity guarantees for non-exchangeable time series, making this a critical theoretical and practical challenge for deploying reliable uncertainty quantification in real-world systems.

**Evidence:** The conformal guarantee is finite-sample under exchangeability, which temporal dependence and seasonal shift violate; the heteroscedastic and group-conditional mechanisms mitigate this empirically rather than restoring an exact guarantee.