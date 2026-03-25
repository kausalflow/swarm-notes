---
created_at: '2026-03-25T21:18:14Z'
source_papers:
- '[[2603.23465-statistical-efficiency-of-single-and-multi-step-models-for-f]]'
title: Well-Specified Control Cost Decay
---

**Background:** Controllers derived from data-driven predictors are evaluated based on the infinite-horizon LQR cost of the resulting closed-loop system. In a well-specified setting, the faster decay of prediction error for the single-step predictor should translate to better control performance decay.

**Question / Future Work:** Compare the rate of decay of the infinite-horizon LQR cost for controllers trained using single-step vs. intermediate predictors, especially analyzing the dependency on the prediction horizon $H$ and whether the single-step predictor's superior prediction error decay rate translates to a faster decay in closed-loop control performance.