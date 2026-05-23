---
created_at: '2026-05-23T07:26:00Z'
source_papers:
- '[[openalex-2605.21108-efficient-learning-of-deep-state-space-models-via-importance]]'
title: Parallel Differentiable Particle Smoothing
---

**Background:** Differentiable particle filters and smoothing methods often rely on sequential forward passes that limit parallelization efficiency on modern hardware. While parallelizable approaches exist, they frequently require repeated resampling or introduce biased gradient estimates.

**Question / Future Work:** The development of differentiable particle smoothers that maintain unbiased gradient updates while enabling efficient parallelization remains an unresolved challenge. Existing approaches often struggle with the trade-off between the sequential nature of traditional resampling and the computational overhead of differentiable relaxations, or lack rigorous guarantees regarding the correspondence between their output marginals and the smoothing posterior defined by the underlying generative model.

**Why It Matters:** This is central to enabling scalable training of deep state space models (DSSMs) for supervised and semi-supervised tasks, where high-fidelity latent representations and efficient parallel processing are both required.