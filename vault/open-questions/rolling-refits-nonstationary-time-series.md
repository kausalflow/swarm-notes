---
created_at: '2026-09-30T10:49:28Z'
source_papers:
- '[[openalex-2609.33866-valid-and-efficient-split-conformal-regression-for-time-seri]]'
title: Rolling Refits and Nonstationary Series
---

**Background:** Split conformal regression intervals are constructed by fitting a model on a training block and calibrating nonconformity scores on an adjacent block of a time series.

**Question / Future Work:** Extend the current non-asymptotic coverage and length guarantees for split conformal regression on time series from stationary processes to rolling refits and nonstationary settings.

**Why It Matters:** Extending split conformal methods to rolling refits and nonstationary processes is critical for practical deployment in streaming financial, energy, and sensor time-series forecasting.

**Evidence:** The theory has two limitations. First, the coverage guarantees are marginal and concern one split of a stationary series; they extend to any fixed forecast horizon, but rolling refits and nonstationary series are not covered.