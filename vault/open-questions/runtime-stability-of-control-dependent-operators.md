---
created_at: '2026-05-09T07:03:33Z'
source_papers:
- '[[openalex-2605.04793-bilinear-mamba-koopman-neural-mpc-for-varying-dynamics]]'
title: Runtime Stability of Operators
---

**Background:** Neural MPC models often use spectral penalties during training to promote stability of the learned dynamics operator.

**Question / Future Work:** Formalizing runtime stability guarantees for control-dependent operators, specifically proving that the spectral radius remains bounded within the unit disk for all valid control inputs, remains an open problem in learning-based MPC.

**Why It Matters:** Formal stability is a necessary precursor to using these models in safety-critical autonomous systems.

**Evidence:** ...those mechanisms do not by themselves constitute a formal proof that ρ(Aeff(u)) < 1 uniformly for all u ∈ U.