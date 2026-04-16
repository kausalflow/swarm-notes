---
created_at: '2026-04-16T06:29:10Z'
source_papers:
- '[[openalex-2604.11624-prediction-of-chaotic-dynamics-from-data-an-introduction]]'
title: Stability metrics for finite perturbations
---

**Background:** Chaotic dynamical systems are characterized by extreme sensitivity to initial conditions, with Lyapunov exponents traditionally defined for infinitesimal perturbations. Applying these stability analysis concepts to data-driven surrogate models requires addressing the discrepancies between linear theory and finite-amplitude, discrete-time dynamics.

**Question / Future Work:** Investigating the extension of Lyapunov-based stability analysis to finite-amplitude perturbations and finite-time fluctuations is necessary to accurately characterize the local predictability of machine learning models trained on chaotic time series.

**Why It Matters:** This is a fundamental limitation in validating the reliability of neural network surrogates for chaotic dynamical systems, which often operate in finite-amplitude regimes rather than the infinitesimal linear limit.