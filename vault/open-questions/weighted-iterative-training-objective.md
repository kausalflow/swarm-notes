---
created_at: '2026-03-27T09:10:32Z'
source_papers:
- '[[2603.25370-a-distribution-to-distribution-neural-probabilistic-forecast]]'
title: Weighted Iterative Training
---

**Background:** The ability of a forecasting model to generate predictions across arbitrary lead times is crucial for operational use.

**Question / Future Work:** The iterative strategy allows a single model to generate forecasts for arbitrary lead times ($k\Delta t$) without retraining, unlike the direct strategy which requires a separately trained model for each lead time of interest. The authors suggest that more generally, the contributions from different forecast steps in the iterative objective could be weighted differently to balance the trade-off between short-term performance and learning overall dynamical consistency, though the current study uses uniform weighting.