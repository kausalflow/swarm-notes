---
created_at: '2026-10-10T10:51:51Z'
source_papers:
- '[[openalex-2610.11229-steercast-retrieval-based-latent-steering-for-decoder-only-t]]'
title: Latent Steering for Encoder-Based Forecasters
---

**Background:** Decoder-only time series foundation models can be enhanced during inference using retrieval-based latent steering, which corrects trajectory errors by injecting learned shifts without modifying underlying model parameters.

**Question / Future Work:** Future work should explore extending the latent-steering retrieval perspective from decoder-only autoregressive time series forecasters to encoder-based and direct-prediction models, which process entire look-back windows into output tokens in a single forward pass without exposing per-step latent trajectories.

**Why It Matters:** Extending latent steering beyond decoder-only architectures broadens the applicability of test-time representation interventions to a wider class of time series models.

**Evidence:** Extending the latent-steering perspective to encoder-based forecasters is an interesting direction for future work.