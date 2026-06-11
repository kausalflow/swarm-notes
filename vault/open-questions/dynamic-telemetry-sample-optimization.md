---
created_at: '2026-06-11T09:07:07Z'
source_papers:
- '[[openalex-2606.09787-zero-touch-predictive-orchestration-automating-time-series-m]]'
title: Dynamic Telemetry Sample Optimization
---

**Background:** Time-series forecasting models in the Cloud-Edge Continuum often face a cold-start problem due to the scarcity of localized historical data on newly discovered nodes. Determining the minimum required local telemetry samples to guarantee specific model accuracy remains an unsolved optimization challenge.

**Question / Future Work:** There is a need to develop a mechanism that dynamically calculates the optimal volume of local telemetry samples required to meet predefined Service Level Agreement (SLA) accuracy targets for a predictive model, rather than relying on a static sample size. This involves balancing data collection overhead with the predictive precision needed for the model to effectively handle system volatility.

**Why It Matters:** This is critical for balancing the trade-off between the operational overhead of data collection on constrained edge devices and the need for sufficient training data to ensure reliable model performance.

**Evidence:** the current framework lacks a mechanism to dynamically calculate the optimal number of telemetry samples required to achieve a predefined target accuracy within a strict time constraint.