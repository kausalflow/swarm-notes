---
# CSL-compatible fields
title: "A Neural Operator Emulator for Coastal and Riverine Shallow Water Dynamics"
author:
  - literal: "Peter Rivera-Casillas"
  - literal: "Sourav Dutta"
  - literal: "Shukai Cai"
  - literal: "Mark Loveland"
  - literal: "Kamaljyoti Nath"
  - literal: "Khemraj Shukla"
  - literal: "Corey J. Trahan"
  - literal: "Jonghyun Lee"
  - literal: "Matthew W. Farthing"
  - literal: "Clint Dawson"
issued:
  date-parts:
    - [2026, 5, 29]
url: "https://arxiv.org/abs/2502.14782"

# Custom fields
paper_id: "2502.14782"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "neural-operator"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mitonet"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-01T10:10:23Z"
created_at: "2026-06-01T10:10:23Z"
---

# A Neural Operator Emulator for Coastal and Riverine Shallow Water Dynamics

**Authors**: Peter Rivera-Casillas, Sourav Dutta, Shukai Cai, Mark Loveland, Kamaljyoti Nath, Khemraj Shukla, Corey J. Trahan, Jonghyun Lee, Matthew W. Farthing, Clint Dawson
**Date**: 2026-05-29
**Paper ID**: [openalex:2502.14782](https://arxiv.org/abs/2502.14782)

## Summary

This paper presents the Multiple-Input Temporal Operator Network (MITONet), an autoregressive neural emulator designed to approximate high-fidelity numerical solvers for hydrodynamic processes governed by time-dependent, parameterized partial differential equations. By leveraging latent-space operator learning, the model efficiently handles complex geometries, time-varying boundary conditions, and varying domain parameters like bottom friction. MITONet demonstrates robust generalization and significant computational speedups when forecasting tide-driven and riverine flow dynamics, maintaining high accuracy over extended 175-day rollouts.

## Key Contributions

- Introduced MITONet, an autoregressive neural emulator that utilizes latent-space operator learning for efficient PDE approximation.
- Demonstrated high predictive skill (anomaly correlation > 0.9, NRMSE < 0.011) in modeling 2D shallow-water dynamics for coastal and riverine environments.
- Achieved substantial computational speedups and generalization to unseen parameter values and long-duration autoregressive rollouts of up to 175 days.

## Open Questions & Future Work

- [[spatial-interpolation-latent-neural-operators]]

## Key Concepts

- [[mitonet]]: An autoregressive neural emulator that utilizes latent-space operator learning to approximate the dynamics of complex, time-dependent, parameterized partial differential equations.

## Archivist Review

I have approved the MITONet architecture as a representative latent-space neural operator emulator for complex physical systems. I also approved the open question regarding spatial interpolation, as it highlights a fundamental architectural tradeoff between latent dimensionality reduction and discretization-invariant physical querying. No datasets were approved, as the ones discussed are routine domain-specific test cases rather than central, reusable benchmarking resources.

### Approved Concepts
- Multiple-Input Temporal Operator Network (MITONet): It is the primary proposed framework for neural emulation of parameterized hydrodynamic PDEs.

### Approved Open Questions
- Spatial interpolation in latent operators: Bridging the gap between the efficiency of latent-space methods and the flexibility of grid-agnostic solvers is essential for high-fidelity physical simulation.

## Links

- [Abstract](https://arxiv.org/abs/2502.14782)
- [PDF](https://arxiv.org/pdf/2502.14782)

