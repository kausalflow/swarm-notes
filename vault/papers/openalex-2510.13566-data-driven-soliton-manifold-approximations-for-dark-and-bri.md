---
# CSL-compatible fields
title: "Data-driven soliton manifold approximations for dark and bright waves: Some prototypical 1D case examples"
author:
  - literal: "Yang Su"
  - literal: "Shaoxuan Chen"
  - literal: "Wei Zhu"
  - literal: "P. G. Kevrekidis"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2510.13566"

# Custom fields
paper_id: "2510.13566"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sparse-identification-of-nonlinear-dynamics-sindy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:37:18Z"
created_at: "2026-07-04T07:37:18Z"
---

# Data-driven soliton manifold approximations for dark and bright waves: Some prototypical 1D case examples

**Authors**: Yang Su, Shaoxuan Chen, Wei Zhu, P. G. Kevrekidis
**Date**: 2026-07-01
**Paper ID**: [openalex:2510.13566](https://arxiv.org/abs/2510.13566)

## Summary

This paper investigates the use of data-driven sparse identification of nonlinear dynamics (SINDy) to reconstruct approximate ODE systems governing soliton interactions in the nonlinear Schrödinger model. By utilizing time-series waveform diagnostics generated from numerical PDE simulations, the authors recover effective dynamical equations without relying on traditional expert-derived variational methods. The results confirm that this methodology accurately captures the underlying physical dynamics of bright and dark waves, offering a robust, data-centric alternative to theoretical model construction.

## Key Contributions

- Demonstrates the ability of sparse identification of nonlinear dynamics (SINDy) to reconstruct reduced-order ODE approximations for soliton interactions without prior physical knowledge.
- Provides a comparative analysis between expert-derived theoretical ODEs and data-driven approximations for both bright and dark soliton interactions in nonlinear Schrödinger models.
- Validates the robustness of data-driven manifold approximations in the presence and absence of external trapping potentials.

## Open Questions & Future Work

- [[limitations-of-sindy-for-complex-soliton-interactions]]

## Key Concepts

- [[sparse-identification-of-nonlinear-dynamics-sindy]]: A data-driven method for discovering governing ordinary differential equations from time-series observations of dynamical systems using sparse regression.

## Archivist Review

The paper demonstrates the application of SINDy to soliton dynamics. I approved the SINDy concept as it is a foundational, reusable method for scientific model discovery. I also approved the open question regarding its limitations in complex multi-body interactions, as this highlights a key research bottleneck in physics-informed machine learning. No datasets were approved as the paper utilizes standard mathematical models rather than a specific, novel empirical dataset.

### Approved Concepts
- Sparse Identification of Nonlinear Dynamics (SINDy): Central framework for identifying reduced-order ODE approximations from complex PDE data.

### Approved Open Questions
- SINDy for Complex Soliton Interactions: Addresses the fundamental limitations of using sparse regression for discovering governing physics in complex, high-dimensional nonlinear wave systems.

## Links

- [Abstract](https://arxiv.org/abs/2510.13566)
- [PDF](https://arxiv.org/pdf/2510.13566)

