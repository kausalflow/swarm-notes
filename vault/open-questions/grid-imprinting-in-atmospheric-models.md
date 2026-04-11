---
created_at: '2026-04-11T05:56:58Z'
source_papers:
- '[[openalex-2604.07103-a-new-high-order-finite-volume-advection-scheme-on-spherical]]'
title: Grid imprinting in atmospheric models
---

**Background:** Numerical discretization of the shallow-water equations in atmospheric modeling often exhibits grid imprinting and consistency limitations when applied to non-orthogonal or unstructured spherical grids.

**Question / Future Work:** There is a need to develop higher-order shallow-water solvers that allow for tighter coupling between tracer transport and the dynamical core to mitigate grid imprinting and ensure better physical consistency. Specifically, incorporating advection fluxes directly into momentum equations is a potential path toward achieving this integration.

**Why It Matters:** Grid imprinting in tracer transport significantly affects the accuracy of numerical weather prediction models, and determining the division of responsibility between advection schemes and the underlying dynamical core is critical for improving model fidelity.

**Evidence:** This indicates that advances in the shallow-water dynamical discretization itself are still needed, in addition to more accurate tracer transport... A natural extension of this work would be to incorporate the proposed advection fluxes into the momentum equations.