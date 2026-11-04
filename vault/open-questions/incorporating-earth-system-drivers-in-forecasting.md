---
created_at: '2026-11-04T12:40:02Z'
source_papers:
- '[[openalex-2611.02211-forecasting-earth-surface-change-in-embedding-space]]'
title: Incorporating Earth System Drivers
---

**Background:** Forecasting models operating on satellite time series typically rely solely on past embeddings, location data, and timestamps, omitting external Earth system drivers such as weather and terrain.

**Question / Future Work:** Incorporate exogenous Earth system drivers—such as meteorological variables, hydrological data, and terrain profiles—as additional condition tokens to better constrain physical land surface changes and improve long-term forecasting accuracy.

**Why It Matters:** Integrating physical environmental drivers is essential for moving from purely statistical time series extrapolation to physically grounded Earth forecasting.

**Evidence:** Second, E$^2$Forecast forecasts only from past embeddings, location and date, without accounting for the external factors that drive land surface change, such as weather. which govern vegetation growth, floods and fires, and terrain, which shapes how water and land cover evolve. Adding such Earth system drivers as extra condition tokens is a natural next step that we intend to explore in future work.