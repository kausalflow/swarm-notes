---
created_at: '2026-06-25T08:19:52Z'
source_papers:
- '[[openalex-2606.22969-topological-out-of-domain-generalization-in-dynamical-system]]'
title: Nonlinear scaling in DSR
---

**Background:** Dynamical systems reconstruction (DSR) using hierarchical models often relies on an affine parameterization of the system, where parameters depend linearly on latent features. This structural assumption may not fully capture the inherently nonlinear ways in which parameters impact the flow map of physical dynamical systems, particularly when mapping from continuous-time to discrete-time representations.

**Question / Future Work:** The authors identify that discrete-time DSR models inherently induce a nonlinear parameter dependence on the flow map that cannot be fully captured by an affine feature mapping, leading to a structural truncation error. It remains unresolved whether more expressive parameterizations can resolve this geometric mismatch without inducing overfitting or loss of interpretability, or if this requires a fundamental shift in how time-discretization is handled within DSR foundation models.

**Why It Matters:** This identifies a fundamental mathematical limit of current state-of-the-art DSR models for long-term forecasting and provides a clear theoretical barrier for future model architectures.

**Evidence:** While this structural omission can be masked during in-domain interpolation because standard ERM only optimizes for local training loss, extrapolating outside the training domain inevitably amplifies the spatial mismatch caused by this missing quadratic curvature, placing a strict bound on the model’s structural fidelity.