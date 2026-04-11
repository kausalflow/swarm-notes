---
# CSL-compatible fields
title: "A new high-order finite-volume advection scheme on spherical Voronoi grids and a comparative study in a mimetic finite-volume moist shallow-water model"
author:
  - literal: "Luan F. Santos"
  - literal: "Jeferson Brambatti Granjeiro"
  - literal: "Pedro S. Peixoto"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07103"

# Custom fields
paper_id: "2604.07103"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:56:58Z"
created_at: "2026-04-11T05:56:58Z"
---

# A new high-order finite-volume advection scheme on spherical Voronoi grids and a comparative study in a mimetic finite-volume moist shallow-water model

**Authors**: Luan F. Santos, Jeferson Brambatti Granjeiro, Pedro S. Peixoto
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07103](https://arxiv.org/abs/2604.07103)

## Summary

This paper addresses the challenge of numerical diffusion in atmospheric modeling on irregular spherical grids by introducing a high-order advection scheme based on k-exact reconstruction. By extending this technique from planar to spherical centroidal Voronoi tessellations, the authors enable improved tracer transport simulation while maintaining grid flexibility. Evaluation on classical advection test cases and a moist shallow-water model demonstrates the scheme's high-order accuracy and robustness against grid distortion, showing it is a viable alternative to existing methods in systems like MPAS.

## Key Contributions

- Introduces a class of high-order advection schemes for spherical centroidal Voronoi tessellations (SCVTs) using k-exact reconstruction.
- Demonstrates that the proposed schemes reduce numerical diffusion and maintain high-order accuracy on irregular, locally refined grids.
- Conducts a comparative performance analysis against existing MPAS advection schemes within a mimetic finite-volume moist shallow-water model.

## Open Questions & Future Work

- [[grid-imprinting-in-atmospheric-models]]

## Archivist Review

The paper focuses on specialized numerical methods for atmospheric modeling rather than generalizable machine learning algorithms. I have rejected the proposed k-exact reconstruction concept as it pertains to classical numerical analysis rather than learning-based temporal modeling. I approved the open question regarding grid imprinting, as it touches on a significant, unresolved structural bottleneck in spatiotemporal modeling that is relevant to weather and climate forecasting research.

### Approved Open Questions
- Grid imprinting in atmospheric models: Grid imprinting in tracer transport significantly affects the accuracy of numerical weather prediction models, and determining the division of responsibility between advection schemes and the underlying dynamical core is critical for improving model fidelity.

### Rejected Candidates
- [concept] k-exact reconstruction on spherical Voronoi grids (`k-exact-reconstruction-on-spherical-voronoi-grids`) - paper_local: This is a domain-specific numerical analysis technique that, while elegant, does not constitute a generalizable machine learning concept for the current vault.

## Links

- [Abstract](https://arxiv.org/abs/2604.07103)
- [PDF](https://arxiv.org/pdf/2604.07103)

