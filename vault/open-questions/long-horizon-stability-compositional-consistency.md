---
created_at: '2026-04-17T06:30:21Z'
source_papers:
- '[[openalex-2604.12794-stable-fine-time-step-long-horizon-turbulence-prediction-wit]]'
title: Long-horizon stability and consistency
---

**Background:** Neural operators used as surrogate models for turbulence forecasting frequently encounter stability issues during long-horizon autoregressive rollouts, especially when using fine temporal resolutions.

**Question / Future Work:** How can multi-step training objectives be designed to enforce compositional consistency across different time strides in neural operators to prevent error accumulation and ensure stable long-horizon simulations in chaotic systems?

**Why It Matters:** This is a fundamental challenge for the deployment of learned surrogates in high-fidelity physics simulations.