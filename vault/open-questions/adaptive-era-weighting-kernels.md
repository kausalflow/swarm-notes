---
created_at: '2026-03-26T07:11:08Z'
source_papers:
- '[[2603.24299-mortality-forecasting-as-a-flow-field-in-tucker-decompositio]]'
title: Adaptive kernel weighting
---

**Background:** The current flow-field model's era-weighted speed function uses a fixed, truncated exponential kernel to prioritize contemporary dynamics during training for a specific forecast origin.

**Question / Future Work:** Natural extensions to the forecasting architecture include the development of adaptive kernels that update dynamically as the forecast evolves, potentially allowing the model to adjust the weighting of historical data based on observed changes in the pace of improvement over time.