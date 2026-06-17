---
created_at: '2026-06-17T09:26:11Z'
source_papers:
- '[[openalex-2606.16677-distributional-forecasting-of-eu-asylum-applications-with-dy]]'
title: Mitigating long-horizon variance accumulation
---

**Background:** The forecasting of asylum application inflows involves nonstationary, count-valued time series characterized by structural volatility and cross-country interdependence. Current state-space models for this purpose often exhibit conservative predictive distributions when extended to medium-run forecast horizons.

**Question / Future Work:** There is a need to develop more robust conditional mean dynamics for multivariate count models to address the observed accumulation of predictive uncertainty at longer horizons, where current random-walk specifications become increasingly conservative. Potential avenues include incorporating covariate-driven, mean-reverting, or logistic processes to better constrain the growth of forecast variance.

**Why It Matters:** This is critical because over-conservative forecasts at longer horizons limit the utility of these models for medium-term resource planning and budgetary allocation, which are common requirements for asylum reception agencies.