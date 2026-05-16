---
created_at: '2026-05-16T07:09:26Z'
source_papers:
- '[[openalex-2605.13150-generative-modeling-of-approximately-periodic-time-series-by]]'
title: Scalable inference for posterior-modulated kernels
---

**Background:** Gaussian process-based generative models for approximately periodic time series rely on covariance structures that often complicate the evaluation of the likelihood and its determinant when scaled to numerous repetitions.

**Question / Future Work:** The development of scalable inference techniques, such as sparse Gaussian process approximations, is required to bypass the computational cubic complexity associated with the likelihood evaluation of posterior-modulated kernels in large-scale approximately periodic systems.

**Why It Matters:** Scalability is a critical requirement for deploying generative models in industrial systems where the number of process repetitions is large, making the computational efficiency of these models a significant bottleneck.