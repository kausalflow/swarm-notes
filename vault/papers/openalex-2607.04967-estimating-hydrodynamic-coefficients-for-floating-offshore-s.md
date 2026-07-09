---
# CSL-compatible fields
title: "Estimating Hydrodynamic Coefficients for Floating Offshore Structures from Movement Data Using Physics-Informed Neural Networks"
author:
  - literal: "Anders Schou"
  - literal: "Jens Visbech"
  - literal: "Allan Peter Engsig-Karup"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04967"

# Custom fields
paper_id: "2607.04967"
paper_source: "openalex"
domain: "physics-informed-machine-learning"
tags:
  - "physics-informed-neural-network"
  - "time-series"
  - "parameter-estimation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-informed-neural-networks-for-hydrodynamics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:41Z"
created_at: "2026-07-09T08:18:41Z"
---

# Estimating Hydrodynamic Coefficients for Floating Offshore Structures from Movement Data Using Physics-Informed Neural Networks

**Authors**: Anders Schou, Jens Visbech, Allan Peter Engsig-Karup
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04967](https://arxiv.org/abs/2607.04967)

## Summary

This paper presents a physics-informed neural network (PINN) framework for estimating hydrodynamic coefficients in floating offshore structures by directly incorporating the Cummins equations into the model. The method addresses the inverse problem of recovering physical parameters—such as added mass and damping coefficients—from observed translational and rotational motion data. By formulating the Cummins equations as a first-order system, the approach effectively performs simultaneous state and parameter estimation. The framework is verified using free decay simulations of a sphere and a box, demonstrating accurate parameter recovery.

## Key Contributions

- Introduces a method to estimate hydrodynamic coefficients (added mass, damping, hydrostatic restoring) from motion data using PINNs.
- Formulates the Cummins equations as a first-order system to allow simultaneous state and parameter estimation.
- Validates the framework on the free decay of spheres and boxes, demonstrating robust performance on inverse dynamics tasks.

## Open Questions & Future Work

- [[pinn-hydrodynamic-coefficient-real-data-validation]]

## Key Concepts

- [[physics-informed-neural-networks-for-hydrodynamics]]: A method that uses physics-informed neural networks to solve inverse problems for hydrodynamic coefficients by embedding the Cummins equations into the model structure.

## Archivist Review

I have approved the core concept of using PINNs for hydrodynamic coefficient estimation as it represents a broader scientific machine learning pattern. The open question regarding real-world data validation is also highly pertinent for this domain. Other candidates were deemed redundant or specific to the provided examples.

### Approved Concepts
- Physics-Informed Neural Networks for Hydrodynamics: Enables parameter estimation for complex dynamical systems directly from observational motion data.

### Approved Open Questions
- Validation on Measured Sensor Data: Essential for transitioning from synthetic verification to real-world engineering and structural monitoring deployments.

## Links

- [Abstract](https://arxiv.org/abs/2607.04967)
- [PDF](https://arxiv.org/pdf/2607.04967)

