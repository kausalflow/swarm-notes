---
created_at: '2026-09-03T09:17:24Z'
source_papers:
- '[[openalex-2608.30795-uncertainty-aware-end-to-end-ai-weather-forecasting-disentan]]'
title: Decoder Stochastic Branch for Downscaling
---

**Background:** End-to-end weather forecasting systems predict atmospheric states directly from raw Earth observations by combining assimilation encoders, forecasting processors, and station decoders into a single trainable pipeline.

**Question / Future Work:** Investigate the integration of a dedicated stochastic branch at the decoder stage to properly account for downscaling, representativeness, and observation errors that currently contribute to station-level under-dispersion in probabilistic end-to-end weather forecasting models.

**Why It Matters:** Addressing station-level under-dispersion and downscaling uncertainty is crucial for operational decision-making, local extreme weather risk assessment, and closing the calibration gap between gridded and station forecasts.

**Evidence:** The decoder is deterministic, so no uncertainty is added at the downscaling stage; the station-level under-dispersion, concentrated exactly where representativeness and observation error enter, points to a third stochastic branch at the decoder.