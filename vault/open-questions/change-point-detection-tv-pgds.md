---
created_at: '2026-09-04T09:11:19Z'
source_papers:
- '[[openalex-2609.00896-poisson-gamma-dynamical-systems-with-time-varying-transition]]'
title: Change-Point Detection for TV-PGDS
---

**Background:** Time-invariant transition kernels in Poisson-Gamma Dynamical Systems fail to capture non-stationary real-world shift dynamics, leading to approximation errors in count-valued time series.

**Question / Future Work:** Designing an adaptive change-point detection mechanism that automatically determines and partitions the entire time horizon into irregular sub-intervals based on shifts in transition dynamics, removing the reliance on pre-fixed sub-interval lengths.

**Why It Matters:** Overcomes the manual hyperparameter tuning of sub-interval lengths and enables data-driven, non-stationary temporal modeling for count time series.

**Evidence:** We believe that incorporating a change-point detection mechanism—which adaptively partitions the entire time horizon into irregular sub-intervals based on shifts in transition dynamics—would further enhance the model’s flexibility and accuracy. We leave this as our future work.