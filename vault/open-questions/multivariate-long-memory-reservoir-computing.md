---
created_at: '2026-07-16T07:14:08Z'
source_papers:
- '[[openalex-2607.11272-long-memory-reservoir-computing-for-data-scarce-dengue-forec]]'
title: Multivariate Long-Memory Reservoir Computing
---

**Background:** Epidemic time series, such as dengue incidence, often exhibit long-range dependence, non-stationarity, and nonlinear dynamics, while being limited by small sample sizes. Existing models like ARFIMA are too rigid to capture nonlinear patterns, and deep recurrent neural networks typically fail to encode genuine long-memory dynamics in a statistically rigorous sense.

**Question / Future Work:** Extending reservoir computing frameworks to multivariate forecasting involves developing methods to handle diverse exogenous covariates (e.g., climate data) that may exhibit varying memory strengths, requiring either variable-specific memory parameters or distinct integrated pathways.

**Why It Matters:** Multivariate forecasting is essential for integrating exogenous drivers (climate, socio-environmental) known to influence infectious disease dynamics, which currently limits the predictive scope of univariate long-memory models.

**Evidence:** Extending fESN and wESN to multivariate forecasting is therefore a natural direction for future research. However, such an extension is nontrivial because different covariates may exhibit different memory strengths.