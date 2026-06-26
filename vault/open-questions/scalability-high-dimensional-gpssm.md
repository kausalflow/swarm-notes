---
created_at: '2026-06-26T08:26:41Z'
source_papers:
- '[[openalex-2606.24691-learning-nonlinear-dynamics-improving-the-estimation-efficie]]'
title: Scalability of high-dimensional GP-SSMs
---

**Background:** Gaussian process state-space models (GP-SSMs) often suffer from the curse of dimensionality, where computational costs for approximate inference methods scale exponentially with the number of state variables.

**Question / Future Work:** A major open challenge is the development of scalable estimation methods for high-dimensional GP-SSMs that balance interaction terms with computational efficiency and flexible prior structures.

**Why It Matters:** Scalability is the primary barrier preventing the adoption of GP-SSMs for complex, high-dimensional real-world dynamic systems.

**Evidence:** The number of basis functions to grow exponentially with the number of state variables... This can quickly lead to impractical computation times... To our knowledge, there is currently no Bayesian estimator for the HSGP-SSM that allows for state specific GP priors and a fully unrestricted dynamic error covariance matrix.