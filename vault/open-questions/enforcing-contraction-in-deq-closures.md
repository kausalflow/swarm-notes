---
created_at: '2026-11-05T12:52:32Z'
source_papers:
- '[[openalex-2611.02458-learning-the-entropic-relaxation-stable-coarse-grid-emulatio]]'
title: Enforcing Contraction in DEQ Closures
---

**Background:** Deep equilibrium models rely on strict operator-level contraction conditions to guarantee unique fixed points, yet practical neural implementations lack such guarantees.

**Question / Future Work:** Investigate whether practical deep equilibrium network implementations can be modified or constrained to strictly satisfy the contraction condition (e.g., via monotone operator theory or specialized parameterizations) while maintaining expressive power for physical closures.

**Why It Matters:** Bridging the gap between theoretical contraction assumptions and unconstrained neural network layers is essential for rigorous reliability in physics emulation.

**Evidence:** L_v < 1 remains an assumption in our DEQ formulation (Bai et al., 2019), whereas monDEQ (Winston and Kolter, 2020) guarantees a unique equilibrium by construction.