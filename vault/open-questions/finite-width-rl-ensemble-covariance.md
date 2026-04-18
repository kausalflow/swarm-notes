---
created_at: '2026-04-18T06:07:03Z'
source_papers:
- '[[openalex-2604.13414-minimax-optimality-and-spectral-routing-for-majority-vote-en]]'
title: Finite-width RL Ensemble Covariance
---

**Background:** Majority-vote ensembles rely on the assumption of approximately independent base learners, which degrades in the presence of Markovian dependence common in time-series and reinforcement learning. The theoretical characterization of this degradation is currently limited to simplified infinite-width regimes, leaving the behavior of practical finite-width models poorly understood.

**Question / Future Work:** There is a need to formalize the covariance limits for ensembles composed of finite-width neural networks with non-stationary, dynamically moving targets, as current theoretical treatments often rely on Neural Tangent Kernel (NTK) simplifications. This would bridge the gap between idealized minimax theory and real-world ensemble performance in deep reinforcement learning.

**Why It Matters:** Deep RL models operate in the finite-width regime with non-stationary targets, making this a critical bottleneck for understanding ensemble stability in practical applications.

**Evidence:** Formalizing the covariance limits for finite-width networks with dynamically moving targets, without NTK simplifications, remains open.