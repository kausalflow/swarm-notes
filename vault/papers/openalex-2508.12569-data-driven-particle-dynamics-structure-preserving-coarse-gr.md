---
# CSL-compatible fields
title: "Data-driven particle dynamics: Structure-preserving coarse-graining for emergent behavior in nonequilibrium systems"
author:
  - literal: "Quercus Hernández"
  - literal: "Max Win"
  - literal: "Thomas C. O’Connor"
  - literal: "Paulo E. Arratia"
  - literal: "Nathaniel Trask"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2508.12569"

# Custom fields
paper_id: "2508.12569"
paper_source: "openalex"
domain: "biology"
tags:
  - "self-supervised-learning"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "metriplectic-bracket-coarse-graining"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:10:39Z"
created_at: "2026-05-16T07:10:39Z"
---

# Data-driven particle dynamics: Structure-preserving coarse-graining for emergent behavior in nonequilibrium systems

**Authors**: Quercus Hernández, Max Win, Thomas C. O’Connor, Paulo E. Arratia, Nathaniel Trask
**Date**: 2026-05-13
**Paper ID**: [openalex:2508.12569](https://arxiv.org/abs/2508.12569)

## Summary

This paper presents a physics-informed machine learning framework for coarse-graining high-dimensional dynamical systems into low-dimensional models. By utilizing the metriplectic bracket formalism, the method guarantees that learned models adhere to fundamental thermodynamic laws, conservation of momentum, and fluctuation-dissipation balance. The approach also incorporates a self-supervised learning technique to infer emergent structural variables, making it applicable to systems where such variables are not explicitly known. The utility of this approach is validated through its success in capturing emergent stochastic dynamics in complex physical systems like colloidal suspensions and star polymers.

## Key Contributions

- Introduced a machine learning framework for coarse-grained dynamics using the metriplectic bracket formalism to enforce thermodynamic consistency.
- Developed a self-supervised learning strategy to identify emergent structural variables from time-series trajectory data without labeled entropic state variables.
- Demonstrated the framework's ability to preserve nonequilibrium statistics in star polymer coarse-graining and colloidal suspension modeling from video.

## Key Concepts

- [[metriplectic-bracket-coarse-graining]]: A physics-informed machine learning framework that uses metriplectic structures to ensure thermodynamic consistency and conservation laws in learned coarse-grained dynamical models.

## Archivist Review

I approved the Metriplectic Bracket Formalism as it represents a significant, reusable physics-informed inductive bias for ensuring thermodynamic consistency in dynamical systems modeling. No other candidates were provided or identified as warranting standalone notes based on the criteria.

### Approved Concepts
- Metriplectic Bracket Formalism for Coarse-Graining: It provides a physics-informed inductive bias that guarantees thermodynamic consistency and fluctuation-dissipation balance in learned dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2508.12569)
- [PDF](https://arxiv.org/pdf/2508.12569)

