---
created_at: '2026-04-04T05:49:27Z'
source_papers:
- '[[openalex-2604.00897-super-resolving-coarse-resolution-weather-forecasts-with-flo]]'
title: Integrated Super-Resolution Forecasting Feedback
---

**Background:** Autoregressive weather forecasting models often operate at coarse spatial resolutions to remain computationally tractable, potentially missing small-scale features that impact local accuracy. Generative super-resolution offers a potential pathway to inject these details as a post-processing step, but its integration back into iterative forecasting loops remains underexplored.

**Question / Future Work:** Determine the optimal approach for integrating generative super-resolution models into autoregressive forecasting pipelines, specifically assessing whether reinjecting super-resolved states can improve or hinder forecast skill at long lead times compared to standard post-processing.

**Why It Matters:** Understanding the interaction between downscaling and autoregressive forecasting is essential for developing computationally efficient, high-resolution global weather prediction systems.

**Evidence:** We also investigated an alternative way of applying super-resolution within the forecasting workflow... The motivation is to assess whether a more realistic representation of subgrid-scale variability, once re-aggregated to the coarse grid, may mitigate systematic biases and influence forecast evolution at longer lead times.