---
# CSL-compatible fields
title: "RONOM: Reduced-Order Neural Operator Modeling"
author:
  - literal: "Sven Dummer"
  - literal: "Dongwei Ye"
  - literal: "Christoph Brüne"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2507.12814"

# Custom fields
paper_id: "2507.12814"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "reduced-order-neural-operator-modeling-ronom"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:29:14Z"
created_at: "2026-06-26T08:29:14Z"
---

# RONOM: Reduced-Order Neural Operator Modeling

**Authors**: Sven Dummer, Dongwei Ye, Christoph Brüne
**Date**: 2026-06-23
**Paper ID**: [openalex:2507.12814](https://arxiv.org/abs/2507.12814)

## Summary

RONOM addresses the computational inefficiency of solving time-dependent partial differential equations (PDEs) by combining reduced-order modeling with neural operator learning. While traditional ROM is restricted to fixed meshes, RONOM enables infinite-dimensional mapping while providing rigorous discretization error bounds. The framework achieves superior performance in spatial super-resolution, discretization robustness, and offers new insights into temporal super-resolution tasks.

## Key Contributions

- Introduces RONOM, a framework that integrates reduced-order modeling (ROM) error bounds into neural operator learning for time-dependent PDEs.
- Establishes discretization error bounds, convergence, and robustness guarantees for neural operator learning.
- Demonstrates superior spatial super-resolution and discretization robustness in numerical PDE benchmarks compared to standard neural operators.

## Open Questions & Future Work

- [[error-analysis-variable-basis-operators]]

## Key Concepts

- [[reduced-order-neural-operator-modeling-ronom]]: A hybrid framework for solving PDEs that combines neural operator learning with the rigorous discretization error bounds typical of reduced-order modeling.

## Archivist Review

The paper successfully proposes a methodology to synthesize numerical ROM error bounds with operator learning. I approved the framework as a concept because it represents a clear architectural paradigm shift in how one might constrain neural operators. The open question regarding discretization error for adaptive/variable-basis operators is a significant, fundamental theoretical hurdle that deserves tracking as the field moves beyond simple uniform-grid neural operators.

### Approved Concepts
- Reduced-Order Neural Operator Modeling (RONOM): It provides a principled way to bridge numerical ROM techniques (rigorous error bounds) with operator learning (discretization invariance).

### Approved Open Questions
- Discretization error for adaptive neural operators: Addressing this gap is necessary to ensure that resolution-invariant models provide reliable convergence properties in critical PDE solving applications.

## Links

- [Abstract](https://arxiv.org/abs/2507.12814)
- [PDF](https://arxiv.org/pdf/2507.12814)

