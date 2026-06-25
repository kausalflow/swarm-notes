---
created_at: '2026-06-25T08:16:40Z'
source_papers:
- '[[openalex-2606.23619-thermodynamic-inference-from-noisy-single-molecule-time-seri]]'
title: Robust Model Selection for Thermodynamic Inference
---

**Background:** In single-molecule experiments, entropy production inference is often limited by finite temporal resolution and experimental measurement noise, which can mask the true microscopic dynamics. Current methods for estimating entropy production frequently rely on models that may not accurately capture the non-Markovian dynamics induced by these coarse-grained observations.

**Question / Future Work:** It is unclear how to reliably select an appropriate underlying kinetic model (such as a Hidden Markov Model) for thermodynamic inference without introducing significant bias or overfitting. Future research is required to develop robust, model-agnostic, or non-parametric Bayesian techniques that provide rigorous lower bounds on entropy production without the computational expense or model-dependence of current methods.

**Why It Matters:** This is a fundamental bottleneck in the field of stochastic thermodynamics. If inference results depend strongly on the chosen model, the resulting thermodynamic conclusions may not be objectively grounded in the data. Developing model-robust inference is essential for the reliability of applying stochastic thermodynamics to complex biological systems.