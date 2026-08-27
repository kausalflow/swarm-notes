---
# CSL-compatible fields
title: "A Library of Mirrors: Deep Neural Nets in Low Dimensions Are Convex Lasso Models with Reflection Features"
author:
  - literal: "Emi Zeger"
  - literal: "Yifei Wang"
  - literal: "Aaron Mishkin"
  - literal: "Tolga Ergen"
  - literal: "Emmanuel J. Candès"
  - literal: "Mert Pilancı"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2403.01046"

# Custom fields
paper_id: "2403.01046"
paper_source: "openalex"
domain: "time-series"
tags:
  - "deep-learning"
  - "optimization"
  - "convex-optimization"
  - "time-series"
  - "autoregressive"
  - "theory"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:54Z"
created_at: "2026-08-27T15:58:54Z"
---

# A Library of Mirrors: Deep Neural Nets in Low Dimensions Are Convex Lasso Models with Reflection Features

**Authors**: Emi Zeger, Yifei Wang, Aaron Mishkin, Tolga Ergen, Emmanuel J. Candès, Mert Pilancı
**Date**: 2026-08-25
**Paper ID**: [openalex:2403.01046](https://arxiv.org/abs/2403.01046)

## Summary

This paper proves that training deep neural networks with piecewise linear activations on 1-D data is equivalent to solving convex Lasso problems with discrete dictionary matrices. The authors show that while 2-layer networks use a dictionary of ramp functions, deeper architectures recursively generate reflection features corresponding to the training data. This convex formulation provides exact insights into global solution landscapes, enables closed-form solutions for minimal regularization, and applies directly to autoregressive time-series models.

## Key Contributions

- Proves that training neural networks on 1-D data is equivalent to convex Lasso problems with discrete, explicitly defined dictionary matrices.
- Demonstrates that 2-layer piecewise linear networks correspond to Lasso with a discrete dictionary of ramp functions, while deeper layers recursively generate reflection features.
- Provides theoretical insights into global optimality, solution landscapes, and closed-form solutions under minimal regularization.
- Illustrates the theory using autoregressive time-series models and shows reflection phenomena in standard nonconvex training.

## Archivist Review

No concepts or datasets met the strict reusability and impact criteria for standalone notes in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2403.01046)
- [PDF](https://arxiv.org/pdf/2403.01046)

