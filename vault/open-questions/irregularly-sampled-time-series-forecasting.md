---
created_at: '2026-10-17T08:54:27Z'
source_papers:
- '[[openalex-2610.19831-ctia-ode-continuous-time-inter-variable-attention-for-long-t]]'
title: Irregularly Sampled Time Series Forecasting
---

**Background:** Continuous-time time series forecasting frameworks typically rely on regularly sampled historical observations and face difficulties processing irregularly sampled sequences with missing values.

**Question / Future Work:** Investigate and adapt the continuous-time forecasting architecture to handle irregularly sampled multivariate time series and event-driven forecasting scenarios by replacing fixed-step encoders with continuous-time variants such as ODE-RNNs or neural flow models.

**Why It Matters:** Extending continuous-time attention models to irregular sampling is crucial for real-world domains like healthcare and finance where data is frequently asynchronous and missing.

**Evidence:** Future work will explore the extension of the CTIA mechanism to irregularly sampled multivariate time series and event-driven forecasting scenarios.