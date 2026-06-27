---
created_at: '2026-06-27T07:43:13Z'
source_papers:
- '[[openalex-2606.25292-time-varying-model-averaging-of-multi-layer-network-vector-a]]'
title: Model Averaging Inference Limits
---

**Background:** Model averaging methods often rely on the assumption of a correctly specified candidate model or a local asymptotic framework where misspecification vanishes as sample size increases.

**Question / Future Work:** Developing robust inference methods and prediction intervals for model averaging, specifically those that do not rely on local misspecification assumptions or fixed model dimensions, remains a significant challenge for time-varying, high-dimensional forecasting. Extending non-asymptotic methods like conformal prediction to these settings while preserving coverage guarantees under non-stationary and network-structured dependencies requires further theoretical and empirical exploration.

**Why It Matters:** It addresses the fundamental tension between achieving optimal model combination and providing reliable uncertainty quantification in high-dimensional, non-stationary forecasting environments.

**Evidence:** construction of prediction intervals using model averaging estimators remain under-explored... [these results] are restricted to the setting where both the number of candidate models and the number of predictors remain fixed.