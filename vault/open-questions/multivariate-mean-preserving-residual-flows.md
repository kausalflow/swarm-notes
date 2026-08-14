---
created_at: '2026-08-14T06:07:08Z'
source_papers:
- '[[openalex-2608.11114-two-stage-odd-residual-flows-for-mean-preserving-probabilist]]'
title: Multivariate Mean-Preserving Residual Flows
---

**Background:** Probabilistic time series forecasting typically forces a compromise between accurate deterministic point predictions and flexible generative uncertainty estimation, where joint negative log-likelihood training or lack of analytical moments creates performance bottlenecks.

**Question / Future Work:** Investigate extending the proposed odd-constrained residual flow and mixture frameworks from univariate marginals to fully multivariate joint distributions with cross-dimensional dependence, while avoiding high computational costs or breaking the exact sampling-free mean preservation guarantee.

**Why It Matters:** Crucial for capturing joint dependencies across multiple channels and time steps without sacrificing the analytical mean-preservation property.

**Evidence:** TORF assumes independent, symmetric residuals, which is sufficient here, but limiting when residuals are asymmetric or cross-dimensionally dependent.