---
created_at: '2026-07-09T08:18:54Z'
source_papers:
- '[[openalex-2607.04955-causticflow-an-efficient-machine-learning-framework-combinin]]'
title: Incorporating Higher-Order Microlensing Effects
---

**Background:** Machine learning models for gravitational microlensing inference are often trained on simulations that overlook real-world complexities and higher-order physical effects.

**Question / Future Work:** There is a need to develop training procedures that incorporate higher-order physical perturbations (such as lens orbital motion and parallax) and non-Gaussian observational noise to improve the generalizability of surrogate models to real-world astronomical light curves. Current gaps in realism hinder the deployment of these models in large-scale survey analysis.

**Why It Matters:** This bottleneck is central to transitioning deep-learning-based astronomical inference from simulated ideal conditions to robust real-world survey operations.

**Evidence:** Although our tests on the real events show that CausticFlow is able to make reasonably good predictions for some events that show higher-order effects, the model fails when the higher-order effects become so prominent... incorporating such higher-order effects into the model training procedure is expected to enhance predictive performance.