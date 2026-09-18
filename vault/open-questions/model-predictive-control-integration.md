---
created_at: '2026-09-18T09:17:14Z'
source_papers:
- '[[openalex-2609.18588-peak-aware-short-term-load-forecasting-across-distribution-g]]'
title: Uncertainty-Aware Model Predictive Control
---

**Background:** Short-term load forecasting models in distribution grids are typically evaluated on average accuracy across all timestamps, overlooking operationally critical high-demand intervals where forecast errors can trigger severe grid congestion and voltage violations.

**Question / Future Work:** Integrate peak-aware probabilistic load forecasts (such as those from time-series foundation models) directly into model predictive control frameworks to enable uncertainty-aware demand management and optimize grid stability under real-time operational constraints.

**Why It Matters:** Bridging the gap between peak-aware forecasting and active downstream grid control (such as MPC) is crucial for transforming offline forecast improvements into tangible operational reliability and congestion mitigation for distribution system operators.

**Evidence:** Future work will integrate Chronos-2 forecasts into model predictive control to enable uncertainty-aware demand management and grid-stability optimization under real-time operational constraints.