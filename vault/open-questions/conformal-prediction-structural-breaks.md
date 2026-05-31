---
created_at: '2026-05-31T08:08:45Z'
source_papers:
- '[[openalex-2605.29296-conformal-prediction-for-functional-time-series-application]]'
title: Conformal prediction under non-stationarity
---

**Background:** Conformal prediction frameworks rely on exchangeability assumptions, which are violated in non-stationary time series or those with structural breaks.

**Question / Future Work:** Further research is required to characterize the performance of sequential conformal prediction methods under severe structural shifts and to determine if current update mechanisms sufficiently maintain coverage without excessive interval inflation.

**Why It Matters:** Reliable uncertainty quantification is essential for high-stakes forecasting, and quantifying the degradation of conformal coverage under non-stationarity is a critical open challenge.

**Evidence:** Under temporal dependence, we expect approximate marginal coverage near (1-α) under weak dependence and a reasonably specified quantile regression model, with possibly over or under-coverage under strong dependence or structural breaks.