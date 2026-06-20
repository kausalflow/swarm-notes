---
created_at: '2026-06-20T08:18:46Z'
source_papers:
- '[[openalex-2606.19093-aifs-dop-end-to-end-medium-range-weather-prediction-from-obs]]'
title: Probabilistic Training for DOP Smoothing
---

**Background:** Machine-learned models trained directly on sparse observational data often suffer from output smoothing, which obscures small-scale physical features at longer lead times.

**Question / Future Work:** There is a need to develop probabilistic objective functions for direct observation prediction to better capture atmospheric variability and mitigate the over-smoothing associated with deterministic mean-squared error optimization. This shift is crucial for verifying whether probabilistic models can maintain structural fidelity in medium-range forecasts.

**Why It Matters:** Mitigating the smoothing effect is a primary bottleneck in transitioning observation-driven AI models into high-reliability operational weather forecasting.

**Evidence:** In future applications, we will investigate training AIFS-DOP against a probabilistic loss... to better understand the potential of ensemble forecasting directly from observations.