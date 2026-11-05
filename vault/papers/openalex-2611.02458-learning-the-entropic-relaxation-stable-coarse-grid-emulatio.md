---
# CSL-compatible fields
title: "Learning the Entropic Relaxation: Stable Coarse-Grid Emulation with Neural Discrete Equilibrium"
author:
  - literal: "Jose Antonio Lara Benitez"
  - literal: "Kareem Hegazy"
  - literal: "Anastasis Kratsios"
  - literal: "Ivan Dokmanić"
  - literal: "Maarten V. de Hoop"
  - literal: "Michael W. Mahoney"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02458"

# Custom fields
paper_id: "2611.02458"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:52:32Z"
created_at: "2026-11-05T12:52:32Z"
---

# Learning the Entropic Relaxation: Stable Coarse-Grid Emulation with Neural Discrete Equilibrium

**Authors**: Jose Antonio Lara Benitez, Kareem Hegazy, Anastasis Kratsios, Ivan Dokmanić, Maarten V. de Hoop, Michael W. Mahoney
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02458](https://arxiv.org/abs/2611.02458)

## Summary

This paper explores stable physical system emulation at extremely coarse grids using the Neural Discrete Equilibrium (NeurDE) method, introducing physically-principled control over entropy dynamics to reinforce dissipative mechanisms. By preventing aliasing and unresolved frequency noise, entropically-stabilized NeurDE achieves stable long-time rollouts for thousands of forecasting steps on high Reynolds number turbulent flows (Re=100,000) even at ultra-coarse grids down to 16x16.

## Key Contributions

- Introduces entropically-stabilized Neural Discrete Equilibrium (NeurDE) for stable coarse-grid emulation of complex physical systems
- Demonstrates stable long-time rollouts for thousands of forecasting steps on large Reynolds number turbulent flows (Re=100,000) using extremely coarse grids down to 16x16
- Provides physically-principled control over entropy dynamics that reinforces the physical system's dissipative mechanism to prevent grid-scale noise and aliasing

## Open Questions & Future Work

- [[enforcing-contraction-in-deq-closures]]

## Archivist Review

Applied rigorous selectivity standards, approving only one substantive open question on enforcing contraction in deep equilibrium closures and approving no redundant concepts or routine datasets.

### Approved Open Questions
- Enforcing Contraction in DEQ Closures: Bridging the gap between theoretical contraction assumptions and unconstrained neural network layers is essential for rigorous reliability in physics emulation.

## Links

- [Abstract](https://arxiv.org/abs/2611.02458)
- [PDF](https://arxiv.org/pdf/2611.02458)

