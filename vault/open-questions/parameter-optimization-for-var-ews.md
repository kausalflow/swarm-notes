---
created_at: '2026-05-30T07:36:50Z'
source_papers:
- '[[openalex-2605.28260-early-warnings-of-critical-transitions-through-vector-autore]]'
title: VAR parameter optimization for EWS
---

**Background:** The estimation of eigenvalues in multiscale dynamical systems via Vector Autoregression (VAR) is limited by the sensitivity to choice of parameters such as window size, sampling rate, and detrending methods.

**Question / Future Work:** There is a need for robust, universal methods to determine optimal sliding window lengths and sampling rates for VAR-based eigenvalue estimation in non-stationary multiscale systems. Investigating whether Takens-style embeddings or fitting to specific slow-fast normal forms can reliably extract informative eigenvalues for singular Hopf bifurcations remains an open technical challenge.

**Why It Matters:** Addressing these parameters is critical for moving from theoretical models to reliable 'in the wild' forecasting, where data is often sparse, non-stationary, and noise-limited.

**Evidence:** The VAR(k,1) method faces many of the same challenges as AR(1), in particular, choice of detrending method, sampling times and length of the sliding window...