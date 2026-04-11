---
created_at: '2026-04-11T05:55:05Z'
source_papers:
- '[[openalex-2604.07292-graph-neural-ode-digital-twins-for-control-oriented-reactor]]'
title: Noise Mitigation for ODE Surrogates
---

**Background:** Continuous-time neural models like Neural ODEs are inherently sensitive to input noise when applied to real-time sensor streams. Robust performance in digital twin applications necessitates managing this sensitivity to prevent divergence during online operation.

**Question / Future Work:** The development of robust noise-mitigation pipelines, such as recursive smoothing or adaptive signal filtering, is required to prevent sensor noise from destabilizing the learned continuous-time dynamics in online forecasting environments.

**Why It Matters:** This is a critical bottleneck for the practical deployment of Neural ODE-based surrogates in noisy, real-world operational environments.

**Evidence:** Additionally, deploying the surrogate for continual online adaptation will require robust noise-mitigation pipelines (e.g., recursive smoothing and signal filtering) to prevent sensor noise from destabilizing the continuous-time dynamics during retraining.