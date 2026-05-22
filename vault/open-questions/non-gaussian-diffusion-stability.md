---
created_at: '2026-05-22T08:17:35Z'
source_papers:
- '[[openalex-2605.19391-tweedies-formulae-and-diffusion-generative-models-beyond-gau]]'
title: Non-Gaussian Diffusion Stability
---

**Background:** Diffusion generative models typically rely on Gaussian noise injection, but non-Gaussian diffusion models with state-dependent diffusion coefficients offer advantages for constrained data modalities. These non-Gaussian processes are known to be computationally challenging and susceptible to instability in training and sampling.

**Question / Future Work:** Establishing numerically stable reverse-time sampling schemes and robust score-matching objectives for non-Gaussian diffusion processes (e.g., CIR, BESQ) is critical for matching the efficiency and scalability of current Gaussian diffusion frameworks.

**Why It Matters:** Numerical instability is the primary barrier to the widespread adoption of non-Gaussian diffusion models in practical applications like financial modeling and generative tasks on constrained manifolds.

**Evidence:** Improving the training and sampling efficiency and the stability of CIR-based models remains an important direction for future work.