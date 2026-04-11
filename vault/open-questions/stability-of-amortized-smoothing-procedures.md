---
created_at: '2026-04-11T05:56:39Z'
source_papers:
- '[[openalex-2604.07169-amortized-filtering-and-smoothing-with-conditional-normalizi]]'
title: Stability of amortized smoothing
---

**Background:** The design of amortized Bayesian filtering and smoothing frameworks involves balancing statistical accuracy with computational efficiency, particularly in high-dimensional settings where posterior distributions may be complex and non-Gaussian.

**Question / Future Work:** The iterative structure of the smoothing procedure, specifically the repeated backward propagation through the learned backward flow, can lead to the accumulation of approximation errors in higher-dimensional settings. Further work is required to establish rigorous theoretical guarantees for the convergence and stability of these amortized smoothing procedures and to explore how their performance scales with the dimension of the state space.

**Why It Matters:** Understanding the stability and error propagation of amortized smoothing is critical for the reliable deployment of these models in high-dimensional scientific and engineering applications, where smoothing is often essential for posterior analysis.

**Evidence:** This deterioration is mainly due to the iterative structure of the smoothing procedure in Algorithm 3. In particular, sampling from p_smoothing requires repeated backward propagation through the learned backward flow, so approximation errors may accumulate along the reverse trajectory and eventually reduce the smoothing accuracy in higher-dimensional settings.