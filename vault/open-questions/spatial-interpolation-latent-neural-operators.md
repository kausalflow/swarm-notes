---
created_at: '2026-06-01T10:10:23Z'
source_papers:
- '[[openalex-2502.14782-a-neural-operator-emulator-for-coastal-and-riverine-shallow]]'
title: Spatial interpolation in latent operators
---

**Background:** Neural operators often map physical fields through latent spaces to achieve computational efficiency, which frequently conflicts with the ability to query solutions at arbitrary, off-grid spatial locations.

**Question / Future Work:** Researching architectural extensions to latent-space operator networks that retain discretization invariance or enable accurate spatial interpolation to arbitrary coordinates, while maintaining the efficiency of latent representations, is an open challenge.

**Why It Matters:** Bridging the gap between the efficiency of latent-space methods and the flexibility of grid-agnostic solvers is essential for high-fidelity physical simulation.

**Evidence:** the proposed MITONet framework lacks the ability to spatially interpolate/extravolate the solution to any arbitrary spatial points in the domain, due to the introduction of the autoencoder-generated latent space.