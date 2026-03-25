---
source_papers:
- '[[2603.23465-statistical-efficiency-of-single-and-multi-step-models-for-f]]'
title: Compare control performance LQR
---

**Background:** Research on learning-based control and forecasting often involves comparing single-step autoregressive models against direct multi-step predictors. Compounding error from recursive single-step models is a key challenge, while multi-step models require learning more parameters.

**Question / Future Work:** The paper analyzed the prediction error trade-off between single-step and multi-step predictors in the well-specified linear system setting, concluding that the single-step predictor is statistically more efficient asymptotically. A comparison with the multi-step predictor is left for future work in the closed-loop control performance analysis.