---
created_at: '2026-03-27T09:10:32Z'
source_papers:
- '[[2603.25370-a-distribution-to-distribution-neural-probabilistic-forecast]]'
title: Joint Distributional Forecasting
---

**Background:** Probabilistic forecasting models for dynamical systems benefit from evolving predictive distributions directly rather than reconstructing them via ensemble sampling.

**Question / Future Work:** The current implementation models marginal predictive distributions for each state dimension rather than the full joint distribution over the complete state vector. A future extension is to develop the framework to operate directly on the full joint predictive distribution-to-distribution, which requires finding scalable parameterizations for high-dimensional dependence structures and covariance representations.