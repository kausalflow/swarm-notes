---
created_at: '2026-03-26T06:26:52Z'
source_papers:
- '[[2603.24474-leveraging-synthetic-and-genetic-data-to-improve-epidemic-fo]]'
title: Extending Context Window for Seasonality
---

**Background:** Forecasting seasonal diseases requires context windows that capture at least one full cycle of the outbreak's seasonality, which can be significantly longer than the typical 20 time steps used in the current model.

**Question / Future Work:** Future work should explore increasing the context window ($C$) to capture seasonality, such as setting $C=52$ or $C=104$ weeks, to ensure the deep learning model has sufficient context for forecasting seasonal diseases.