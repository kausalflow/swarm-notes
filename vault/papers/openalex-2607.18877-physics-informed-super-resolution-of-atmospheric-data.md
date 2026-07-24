---
# CSL-compatible fields
title: "Physics-Informed Super-Resolution of Atmospheric Data"
author:
  - literal: "Chang Xu"
  - literal: "Gencer Sumbul"
  - literal: "Hugo Porta"
  - literal: "Manon Bechaz"
  - literal: "Sebastian Schemm"
  - literal: "Devis Tuia"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.18877"

# Custom fields
paper_id: "2607.18877"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "super-resolution"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "era5"
concept_slugs:
  - "physics-informed-super-resolution-pisr"
  - "normalized-physical-consistency-npc"
dataset_slugs:
  - "era5"
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:25:48Z"
created_at: "2026-07-24T07:25:48Z"
---

# Physics-Informed Super-Resolution of Atmospheric Data

**Authors**: Chang Xu, Gencer Sumbul, Hugo Porta, Manon Bechaz, Sebastian Schemm, Devis Tuia
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.18877](https://arxiv.org/abs/2607.18877)

## Summary

This paper addresses the challenge of physical inconsistency in machine-learning-based atmospheric data super-resolution by introducing Physics-Informed Super-Resolution (PISR), which constrains models with multi-scale objectives based on hydrostatic primitive equations. Additionally, the authors propose Normalized Physical Consistency (NPC), a novel evaluation metric derived from these primitive equations to measure physical validity. Experiments on the ERA5, CERRA, and COSMO datasets show that PISR improves reconstruction accuracy, physical consistency, and downstream detection of extreme events like heatwaves and extreme winds.

## Key Contributions

- Proposes Physics-Informed Super-Resolution (PISR), a method incorporating multi-scale objectives based on primitive equations to encode multivariate atmospheric physics.
- Introduces Normalized Physical Consistency (NPC), a metric derived from primitive equations to measure the physical validity of super-resolved data.
- Demonstrates enhanced reconstruction fidelity, physical consistency, and downstream extreme event detection (heatwaves and extreme winds) on ERA5, CERRA, and COSMO datasets.

## Open Questions & Future Work

- [[relaxing-hydrostatic-assumptions-and-unconstrained-variables]]

## Key Concepts

- [[physics-informed-super-resolution-pisr]]: A super-resolution method for atmospheric data that constrains models using multi-scale objectives based on hydrostatic primitive equations.
- [[normalized-physical-consistency-npc]]: A quantitative evaluation metric derived from primitive equations to measure physical consistency in super-resolved atmospheric data.

## Archivist Review

Approved core concepts PISR and NPC as valuable contributions to physics-informed spatial downscaling and evaluation. Added ERA5 as a key reusable dataset. Approved the open question regarding the relaxation of hydrostatic assumptions.

### Approved Concepts
- Physics-Informed Super-Resolution (PISR): Introduces a novel framework for constraining atmospheric data super-resolution models with hydrostatic primitive equations to ensure physical consistency.
- Normalized Physical Consistency (NPC): Provides a principled quantitative metric derived from primitive equations to measure the physical consistency of super-resolved atmospheric data.

### Approved Open Questions
- Relaxing Hydrostatic Assumptions and Unconstrained Variables: Addressing limitations in governing equations and extending physics-informed constraints to unconstrained variables like precipitation is vital for extending climate models to finer scales and broader meteorological phenomena.

## Datasets

- [[era5]]

## Links

- [Abstract](https://arxiv.org/abs/2607.18877)
- [PDF](https://arxiv.org/pdf/2607.18877)

