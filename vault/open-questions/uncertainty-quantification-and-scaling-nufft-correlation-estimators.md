---
created_at: '2026-09-06T09:01:03Z'
source_papers:
- '[[openalex-2609.03866-nufftcf-fast-auto-and-cross-correlation-function-estimation]]'
title: Uncertainty Quantification and Scaling for NUFFT Correlation Estimators
---

**Background:** The estimation of auto-correlation and cross-correlation functions for irregularly sampled time series can be accelerated using Non-Uniform Fast Fourier Transforms (NUFFT), yet the impact of finite-sample selection bias and uncertainty quantification under heterogeneous sampling remains underexplored.

**Question / Future Work:** Future work should focus on extending uncertainty quantification for NUFFT-based correlation estimators beyond deterministic effective pair counts, potentially by adapting resampling or bootstrap techniques akin to existing slotting methods, and exploring alternative weighting kernels or GPU-accelerated backends for massive time series datasets.

**Why It Matters:** Uncertainty quantification and scalability to massive irregularly sampled datasets are crucial bottlenecks for adopting Fourier-domain correlation estimators in operational survey pipelines and environmental monitoring.

**Evidence:** Future work may include extending nufftcf uncertainty quantification beyond the deterministic effective pair count b following pyZDCF own approach, exploring additional weighting kernels within the same NUFFT reformulation.