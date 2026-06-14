---
created_at: '2026-06-14T08:36:50Z'
source_papers:
- '[[openalex-2502.12370-positional-encoding-in-transformer-based-time-series-models]]'
title: PE for Forecasting Horizons
---

**Background:** Time series forecasting using transformer architectures requires maintaining temporal coherence across the input observation window and the generated future forecast horizon.

**Question / Future Work:** Explore positional encoding techniques that maintain continuity across the boundary between historical observations and predicted future values, specifically aiming to enable variable-length forecasting without necessitating model retraining for each horizon.

**Why It Matters:** Developing positional encodings that generalize across forecast horizons is essential for creating versatile, scalable time series forecasting models.

**Evidence:** Third, our encoder-only classification focus limits generalizability to forecasting... Encoder-decoder architectures raise questions about whether encoders and decoders should use identical PE methods, and whether continuous PE could enable variable-length forecasting without retraining.