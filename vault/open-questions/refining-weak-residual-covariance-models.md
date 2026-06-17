---
created_at: '2026-06-17T09:27:15Z'
source_papers:
- '[[openalex-2606.15690-multi-fidelity-sindy-sparse-discovery-of-nonlinear-dynamical]]'
title: Refining Weak Residual Covariance Models
---

**Background:** In the identification of dynamical systems from noisy measurements, weak formulations involve integrating governing equations against localized test functions to avoid explicit numerical differentiation. The performance of these methods, especially in multi-fidelity contexts, depends on a leading-order approximation that assumes noise primarily propagates through the weak left-hand side.

**Question / Future Work:** Future research needs to develop more refined covariance models that explicitly incorporate the perturbation induced in the weak feature matrix, which is currently neglected at leading order. This is particularly important for more challenging partial differential equation (PDE) identification settings or when measurement noise levels are high, as the current approximation may be insufficient.

**Why It Matters:** Improving the covariance approximation is crucial for ensuring the robustness and accuracy of the generalized least-squares weighting in the weak-SINDy framework, especially for complex PDEs where feature-matrix perturbations cannot be ignored.

**Evidence:** The covariance model is derived at leading order and neglects the perturbation induced in the weak feature matrix, which may become important in more challenging PDE settings or at higher noise levels.