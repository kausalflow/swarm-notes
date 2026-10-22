---
created_at: '2026-10-22T09:44:56Z'
source_papers:
- '[[openalex-2610.20860-time-partitioning-gaussian-process-mixture-model]]'
title: Scalable Bayesian Nonparametric Time-Series Partitioning
---

**Background:** Macro-financial time series exhibit complex nonstationarity and regime-specific temporal dependencies that cannot be accurately captured by stationary covariance functions or rigid Markovian assumptions.

**Question / Future Work:** Address the computational scalability of Bayesian nonparametric time-partitioning mixture models to enable efficient joint inference over long observation sequences and higher-dimensional multivariate time series without relying solely on restrictive batch sampling approximations.

**Why It Matters:** Computational complexity currently scales cubically with block lengths, bottlenecking application to massive macro-financial datasets or multivariate systems.

**Evidence:** We deliberately prioritised an accurate approximation of the posterior over scaling to very long series... multivariate extensions and more complex kernels would raise the cost