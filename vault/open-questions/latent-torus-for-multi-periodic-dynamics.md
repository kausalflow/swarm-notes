---
created_at: '2026-06-20T08:17:00Z'
source_papers:
- '[[openalex-2606.18898-anomaly-detection-for-sparse-and-irregular-multivariate-time]]'
title: Latent Torus for Multi-Periodic Dynamics
---

**Background:** Many real-world dynamical systems generate time series characterized by multiple overlapping periods, such as industrial processes or robotic motion. Standard Euclidean latent spaces in generative models often struggle to capture these multi-periodic structures effectively, especially when the data is sparse or irregularly sampled.

**Question / Future Work:** Explore the use of an n-dimensional torus (T^n) as the latent manifold in SDE-based generative models to better represent multi-periodic dynamics with incommensurate periods. This approach targets the fundamental challenge of modeling non-linear, multi-scale cyclical behavior in the latent space.

**Why It Matters:** This addresses a fundamental limitation in representing complex, multi-period cyclical dynamics common in industrial monitoring which currently lack effective inductive bias in standard SDE frameworks.

**Evidence:** the framework could be extended to support an n-dimensional torus T^n = S^1 x ... x S^1 as the latent manifold, which may be particularly well-suited for modeling strictly periodic (n=1) or quasi-periodic (n>1) data