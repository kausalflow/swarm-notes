---
created_at: '2026-03-25T21:18:14Z'
source_papers:
- '[[2603.23465-statistical-efficiency-of-single-and-multi-step-models-for-f]]'
title: Predictor Statistical Efficiency Tradeoff
---

**Background:** In learning-based control, compounding prediction errors from recursively applied single-step models pose a challenge for long-horizon forecasting and controller design. Direct multi-step predictors mitigate this by learning a single model for the entire horizon, but this increases model complexity and data requirements.

**Question / Future Work:** Analyze the trade-off between statistical efficiency (sample size needed for convergence) and predictive accuracy when comparing single-step models rolled out autoregressively against directly trained multi-step models, especially under system misspecification due to partial observability.