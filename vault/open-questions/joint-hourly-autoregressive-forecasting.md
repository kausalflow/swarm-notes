---
created_at: '2026-10-04T10:49:29Z'
source_papers:
- '[[openalex-2610.01835-varda-single-10-deterministic-data-driven-weather-forecastin]]'
title: Joint Hourly Autoregressive Forecasting
---

**Background:** Data-driven regional weather prediction models face architectural and temporal limitations when mapping high-resolution kilometre-scale grid inputs into latent spaces due to mismatched spatio-temporal scales and coarse temporal forecasting steps.

**Question / Future Work:** Investigate alternative model designs, such as training a single forecasting model that predicts multiple hourly steps jointly in each autoregressive step, to better exploit kilometre-scale information and overcome the limitations of 6-hourly temporal forecasting steps.

**Why It Matters:** This is technically important because current 6-hourly autoregressive forecasting steps fail to capture fast sub-diurnal convective and local weather dynamics, hindering the full utilization of 1 km regional grids.

**Evidence:** Consequently, other designs are being explored, such as training a single forecasting model predicting multiple hourly steps jointly in each autoregressive step.