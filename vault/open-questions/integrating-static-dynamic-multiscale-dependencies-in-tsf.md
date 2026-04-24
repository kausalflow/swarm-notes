---
created_at: '2026-04-24T06:58:58Z'
source_papers:
- '[[openalex-2509.18135-sdgf-fusing-static-and-multi-scale-dynamic-correlations-for]]'
title: Integrating Static and Dynamic Multiscale Dependencies in TSF
---

**Background:** Multivariate time series forecasting relies on capturing inter-variable dependencies, which often vary in structure and strength across different temporal scales and frequencies. Current graph-based neural networks struggle to fully integrate global static structural relationships with these dynamic, scale-specific dependencies.

**Question / Future Work:** There is a need for more robust frameworks that can simultaneously and effectively model both global, stable relationships and complex, non-stationary inter-series dependencies that evolve across multiple temporal scales without losing fine-grained dependency information.

**Why It Matters:** This is a fundamental bottleneck in multivariate forecasting, as ignoring the interplay between stable long-term relations and transient, scale-dependent dynamics often limits model generalizability in non-stationary environments.