---
created_at: '2026-04-17T06:29:42Z'
source_papers:
- '[[openalex-2604.12304-beyond-weather-correlation-a-comparative-study-of-static-and]]'
title: Hybrid Weather-Sequence Load Forecasting
---

**Background:** Residential electricity consumption forecasting at sub-hourly resolution requires balancing stochastic occupant behavior with exogenous drivers like weather. While historical consumption sequences provide strong predictive signals, the optimal integration of meteorological features at fine-grained temporal scales remains a challenge.

**Question / Future Work:** Research is needed to develop and evaluate hybrid forecasting models that combine high-resolution historical consumption data with exogenous weather covariates to optimize performance, especially during extreme weather events.

**Why It Matters:** Establishing whether exogenous features provide marginal or significant gains in hybrid architectures is critical for optimizing smart grid management and demand response strategies.

**Evidence:** The study compares a weather-only MLP against a sequence-only LSTM, leaving the hybrid model untested.