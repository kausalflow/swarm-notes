---
created_at: '2026-07-24T07:24:42Z'
source_papers:
- '[[openalex-2106.11043-scalable-bayesian-inference-for-time-series-via-divide-and-c]]'
title: Scalable Bayesian Inference for Nonstationary and Long-Memory Time Series
---

**Background:** Divide-and-conquer Bayesian inference methods for dependent time series partition data into sequential subsequences, compute subset posteriors, and aggregate them under temporal dependence.

**Question / Future Work:** Extend divide-and-conquer Bayesian inference methods and their theoretical guarantees from stationary, short-memory time series to nonstationary time series as well as processes exhibiting long-range dependence.

**Why It Matters:** Extending divide-and-conquer guarantees beyond stationary, fast-mixing processes is critical for broader real-world applicability, as many environmental and financial time series exhibit nonstationarity or long-range memory.

**Evidence:** Our theoretical results rely on assumptions of stationarity and fast mixing. It would be interesting to relax these assumptions and develop scalable posterior inference algorithms for nonstationary time series, as well as for series with long-range dependence.