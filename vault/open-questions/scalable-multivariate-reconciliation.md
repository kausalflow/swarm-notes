---
created_at: '2026-05-21T08:28:21Z'
source_papers:
- '[[openalex-2605.17920-multivariate-reconciliation-for-hierarchical-time-series]]'
title: Scalable multivariate reconciliation estimation
---

**Background:** Multivariate forecast reconciliation requires the estimation of a covariance matrix of base forecast errors, the size of which scales with the number of variables and the number of nodes in the hierarchy.

**Question / Future Work:** As the number of variables and the number of hierarchy nodes increase, the covariance matrix grows rapidly, creating a bottleneck for computational scalability. Future research is needed to develop more efficient, scalable estimation techniques, such as factor models or sparse estimators, to make the approach practical for large-scale hierarchical systems.

**Why It Matters:** The current approach suffers from the curse of dimensionality as the size of the hierarchy and the number of variables increase, limiting its applicability to massive real-world datasets.

**Evidence:** the covariance matrix Wh grows rapidly with m and n, making scalable estimation an important direction for future work.