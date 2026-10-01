---
created_at: '2026-10-01T11:14:22Z'
source_papers:
- '[[openalex-2609.36966-judgecast-time-series-forecasting-with-experience-informed-c]]'
title: Mitigating Adjustment Failure Modes
---

**Background:** Time series forecasting with covariates requires assessing how individual exogenous variables affect targets across shifting temporal contexts without parameter updates.

**Question / Future Work:** Develop robust mechanisms or architectures to mitigate common failure modes in experience-informed judgmental adjustments for time series forecasting, such as incorrect adjustment directions, unnecessary adjustments on near-accurate base forecasts, and missed within-horizon reversals.

**Why It Matters:** Understanding and resolving failure modes in non-parametric, experience-guided adjustment frameworks is crucial for deploying reliable LLM-based time series forecasting systems in high-stakes real-world domains.

**Evidence:** We analyze failure cases of JudgeCast on PJM and identify three major failure modes in its forecast-time judgmental adjustment... Incorrect Adjustment Direction... Unnecessary Adjustment... Missed Within-Horizon Reversal.