---
# CSL-compatible fields
title: "State estimation in homogeneous isotropic turbulence using super-resolution with a 4DVar training algorithm"
author:
  - literal: "Mark Weyrauch"
  - literal: "Moritz Linkmann"
  - literal: "Jacob Page"
issued:
  date-parts:
    - [2026, 4, 9]
url: "https://arxiv.org/abs/2510.16904"

# Custom fields
paper_id: "2510.16904"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "cnn"
  - "super-resolution"
  - "physics-informed-machine-learning"
  - "fluid-dynamics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "4dvar-super-resolution-training"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-12T06:20:48Z"
created_at: "2026-04-12T06:20:48Z"
---

# State estimation in homogeneous isotropic turbulence using super-resolution with a 4DVar training algorithm

**Authors**: Mark Weyrauch, Moritz Linkmann, Jacob Page
**Date**: 2026-04-09
**Paper ID**: [openalex:2510.16904](https://arxiv.org/abs/2510.16904)

## Summary

This paper introduces a novel training framework that uses the 4DVar data assimilation algorithm to train super-resolution neural networks for 3D isotropic turbulence without requiring high-resolution ground truth. By adapting a pseudo-spectral JAX-CFD solver to 3D, the authors incorporate entire physical trajectories into the training loss. The resulting model outperforms standard 4DVar at initial time steps and serves as an effective hybrid initialization for robust 4DVar-based estimation.

## Key Contributions

- Demonstrates that 4DVar data assimilation can train neural networks for 3D isotropic turbulence super-resolution without high-resolution ground truth.
- Adapts a pseudo-spectral JAX-CFD solver for 3D flows, enabling the inclusion of entire trajectories in the loss function for gradient-based optimization.
- Develops a hybrid initialization strategy where neural networks initialize 4DVar, achieving more than twice the accuracy of standalone state estimation methods.

## Key Concepts

- [[4dvar-super-resolution-training]]: A training paradigm that integrates 4DVar data assimilation into the loss function of super-resolution neural networks, eliminating the dependency on high-resolution reference datasets.

## Archivist Review

I have approved the 4DVar Super-Resolution Training concept as it provides a distinct, reusable methodology for training neural operators or SR models in physics-constrained regimes where high-resolution ground truth is absent. No other candidates were provided, and no further concepts or datasets were identified that meet the high bar for inclusion.

### Approved Concepts
- 4DVar Super-Resolution Training: Enables neural network training for super-resolution in physical fluid dynamics contexts where high-resolution ground truth data is unavailable by leveraging physical solvers.

## Links

- [Abstract](https://arxiv.org/abs/2510.16904)
- [PDF](https://arxiv.org/pdf/2510.16904)

