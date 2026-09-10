---
created_at: '2026-09-10T09:17:06Z'
source_papers:
- '[[openalex-2609.07257-bayesian-generalized-network-autoregressive-model-with-struc]]'
title: Extensions to BGNAR Framework
---

**Background:** Bayesian generalized network autoregressive (BGNAR) models assume a fixed and known network structure while utilizing structured shrinkage and persistence priors for multivariate time series analysis.

**Question / Future Work:** Future research should investigate extending the framework to accommodate time-varying network structures or network uncertainty, relaxing the diagonal error covariance assumption to capture structured contemporaneous cross-node dependence, and developing scalable posterior computation algorithms for high-dimensional network time series.

**Why It Matters:** Addressing time-varying networks, non-diagonal error covariances, and computational scalability is vital for expanding network autoregressive models to handle complex, large-scale real-world multivariate time series systems.

**Evidence:** The current formulation assumes a fixed and known network, and future work could accommodate time-varying network structures or uncertainty in the network itself.