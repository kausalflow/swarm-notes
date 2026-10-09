---
created_at: '2026-10-09T11:33:47Z'
source_papers:
- '[[openalex-2610.09096-are-we-really-benchmarking-forecasting-models-the-impact-of]]'
title: Multivariate and Long-Term Preprocessing Benchmarks
---

**Background:** Time series forecasting benchmarks often apply uniform, minimal preprocessing pipelines across heterogeneous datasets, potentially introducing structural preprocessing bias that disproportionately penalizes models without built-in transformations.

**Question / Future Work:** Future research should expand preprocessing-aware benchmarking frameworks to multivariate time series forecasting tasks and long-term prediction settings to determine whether structural preprocessing bias and model sensitivity to transformations remain stable when cross-channel dependencies and exogenous variables are introduced.

**Why It Matters:** Crucial for understanding if findings on univariate benchmarks generalize to complex multivariate real-world settings where cross-series dynamics interact with preprocessing.

**Evidence:** Future work should therefore extend the benchmark to multivariate forecasting tasks and examine whether the conclusions about structural preprocessing bias remain stable when models can use covariates or multiple target-related signals. A similar extension would be valuable for long-term forecasting settings, where preprocessing choices may affect error accumulation and temporal representation in different ways.