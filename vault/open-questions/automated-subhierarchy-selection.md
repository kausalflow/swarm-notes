---
created_at: '2026-06-28T08:15:46Z'
source_papers:
- '[[openalex-2606.26774-end-to-end-probabilistic-hierarchical-forecasting-of-large-h]]'
title: Automated subhierarchy selection criteria
---

**Background:** The selection of time series in hierarchical forecasting systems currently relies on manual choices for which aggregate series should be forecasted to propagate predictions downwards. Principled criteria to automate this selection process while balancing computational budget and forecast accuracy remain absent.

**Question / Future Work:** Developing data-driven, principled criteria for selecting the optimal sub-hierarchy of time series to forecast is essential. Such an automated approach should incorporate metrics related to forecastability, computational constraints, and the trade-off between the accuracy of aggregated models versus the information loss from excluding bottom-level series.

**Why It Matters:** This is a critical bottleneck for deploying hierarchical forecasting models at scale, as the choice of sub-hierarchy directly dictates both the computational cost and the upper bound of achievable accuracy.