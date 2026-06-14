---
created_at: '2026-06-14T08:38:37Z'
source_papers:
- '[[openalex-2606.13063-a-quadratic-order-reduction-gaussian-process-ordinary-differ]]'
title: Non-equispaced derivative estimation in GP-ODE
---

**Background:** Standard finite-difference schemes for time-derivative estimation in Gaussian Process Ordinary Differential Equations (GP-ODE) typically require equispaced temporal data.

**Question / Future Work:** There is a need for robust and computationally efficient derivative approximation schemes for non-equispaced temporal data that maintain sufficient regularity for convergence in GP-ODE frameworks. The current kernel-based optimization techniques for non-uniform discretizations lack the computational efficiency of standard equispaced schemes.

**Why It Matters:** This is a fundamental bottleneck for applying GP-ODE models to real-world, irregular observational data, impacting both model accuracy and computational feasibility.

**Evidence:** In the case of non-uniform temporal discretisation, the construction of \\Psi becomes highly nontrivial, since it must depend solely on x and, in addition, possess sufficient regularity to lie in the space H^{(m+5)/2}(U, \\mathbb{R}^m).