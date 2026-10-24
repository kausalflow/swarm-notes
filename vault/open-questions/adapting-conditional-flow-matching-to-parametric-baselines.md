---
created_at: '2026-10-24T09:11:58Z'
source_papers:
- '[[openalex-2610.29991-flowz-when-does-learning-forecast-errors-add-value-condition]]'
title: Adapting Flow Matching to Parametric Baselines
---

**Background:** Financial probabilistic forecasting relies on conditional flow matching and residual learning frameworks to enhance predictive distributions across multiple horizons.

**Question / Future Work:** Investigate how conditional flow matching and residual learning models can be adapted and tuned for parametric baselines such as ARIMA, ARFIMA, and structural state-space models that failed to improve under default configurations.

**Why It Matters:** Understanding why residual flow matching fails on certain linear and structural baselines while succeeding on EWMA is critical for generalizing probabilistic residual learning across time-series forecasting models.

**Evidence:** The second is to adapt the conditional flow to the ARIMA, ARFIMA, and structural baselines that did not improve in this experiment.