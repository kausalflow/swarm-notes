---
created_at: '2026-10-09T11:35:13Z'
source_papers:
- '[[openalex-2610.08322-structure-aware-graph-abstention-for-reliable-selective-fore]]'
title: Joint Instance and Relational Selective Forecasting
---

**Background:** Selective forecasting adds an abstention layer on top of point predictions to withhold high-risk forecasts under a retained-coverage budget. Most selective rules score forecasts as a whole, but multivariate trajectories can look plausible individually while violating cross-variable dependencies.

**Question / Future Work:** Investigate how to jointly model instance-level plausibility and relational consistency to improve selective forecasting reliability in multivariate time series.

**Why It Matters:** Unifying instance-level plausibility and relational consistency is critical for advancing reliable uncertainty estimation and risk-aware decision-making in multivariate structured forecasting.

**Evidence:** Selective forecasting for structured outputs therefore faces two questions: is the forecast plausible, and is it relationally consistent across variables? Instance-level plausibility and relational consistency are distinct notions of reliability