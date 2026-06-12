---
created_at: '2026-06-12T08:53:43Z'
source_papers:
- '[[openalex-2606.11162-cogent-continuous-graph-emulators-with-neural-ordinary-diffe]]'
title: Arbitrary Continuous-Time Query Fidelity
---

**Background:** Physical simulation emulators using graph neural networks typically rely on fixed sequences of discrete time-step transitions or predefined forecast horizons to predict future states.

**Question / Future Work:** Investigate the viability and precision of querying latent neural ODE models at non-discrete time steps to support arbitrary-time state interpolation in physics emulators. Current evaluations are largely restricted to fixed horizons, failing to demonstrate the potential for true continuous-time query capability.

**Why It Matters:** This addresses the core claim of continuous-time emulation, which remains theoretically supported by the model design but practically unverified in existing benchmarks.