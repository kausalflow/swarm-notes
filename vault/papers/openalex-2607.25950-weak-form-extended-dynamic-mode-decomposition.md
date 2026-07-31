---
# CSL-compatible fields
title: "Weak-form Extended Dynamic Mode Decomposition"
author:
  - literal: "Christopher W. Curtis"
  - literal: "David M. Bortz"
issued:
  date-parts:
    - [2026, 7, 28]
url: "https://arxiv.org/abs/2607.25950"

# Custom fields
paper_id: "2607.25950"
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
  - "weak-form-extended-dynamic-mode-decomposition"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-31T07:44:27Z"
created_at: "2026-07-31T07:44:27Z"
---

# Weak-form Extended Dynamic Mode Decomposition

**Authors**: Christopher W. Curtis, David M. Bortz
**Date**: 2026-07-28
**Paper ID**: [openalex:2607.25950](https://arxiv.org/abs/2607.25950)

## Summary

This paper introduces Weak-form Extended Dynamic Mode Decomposition (WEDMD), a novel formulation designed to address the challenges of noise in dynamical systems. The authors establish key analytic results showing that WEDMD effectively mitigates noise impacts in linear stochastic differential equations and accurately approximates Koopman modes for nonlinear systems without relying on sparsity-promoting methods. Consequently, the approach provides robust forecasting capabilities even when working with noisy data.

## Key Contributions

- Developed Weak-form Extended Dynamic Mode Decomposition (WEDMD) to mitigate noise impacts in linear stochastic differential equations.
- Established analytic results demonstrating that WEDMD generates accurate Koopman mode approximations in nonlinear systems without requiring sparsity-promoting regularization.
- Showed that the excellent approximation property of WEDMD enables meaningful forecasting in the presence of noisy data.

## Open Questions & Future Work

- [[stochastic-koopman-frameworks-wedmd]]

## Key Concepts

- [[weak-form-extended-dynamic-mode-decomposition]]: A weak-form formulation of Extended Dynamic Mode Decomposition designed to mitigate noise impacts and approximate Koopman modes effectively.

## Archivist Review

Approved the core operator-theoretic method (WEDMD) and its explicit open question concerning stochastic Koopman extensions under process noise, adhering strictly to scarcity and novelty criteria.

### Approved Concepts
- Weak-form Extended Dynamic Mode Decomposition: It introduces the core methodological framework of WEDMD, which mitigates noise impacts in linear stochastic differential equations and approximates Koopman modes without sparsity promotion.

### Approved Open Questions
- Stochastic Koopman Frameworks and Process Noise: Extending weak-form Koopman frameworks to rigorously handle stochastic process noise is critical for data-driven modeling in systems where stochastic perturbations significantly alter the generator dynamics rather than acting purely as additive measurement noise.

## Links

- [Abstract](https://arxiv.org/abs/2607.25950)
- [PDF](https://arxiv.org/pdf/2607.25950)

