---
# CSL-compatible fields
title: "Neural Network-Based Estimation of Time-Dependent Parameters in AR(p) Processes"
author:
  - literal: "Agnieszka Kopeć"
  - literal: "Paweł Przybyłowicz"
  - literal: "Martyna Wiącek"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00470"

# Custom fields
paper_id: "2607.00470"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:59Z"
created_at: "2026-07-04T07:36:59Z"
---

# Neural Network-Based Estimation of Time-Dependent Parameters in AR(p) Processes

**Authors**: Agnieszka Kopeć, Paweł Przybyłowicz, Martyna Wiącek
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00470](https://arxiv.org/abs/2607.00470)

## Summary

This paper introduces a forecasting framework that combines the interpretability of discrete-time autoregressive processes with the expressive power of neural networks to estimate time-varying parameters. By modeling coefficients as functions of time, the approach captures nonstationary patterns while maintaining a transparent parametric structure. The authors analyze the model under both Gaussian and Laplace noise assumptions, providing a rigorous derivation for prediction intervals and demonstrating the model's flexibility in handling diverse time-series dynamics.

## Key Contributions

- Formulates a framework for estimating time-dependent coefficients in TVAR(p) models using deep learning for improved flexibility.
- Extends parameter estimation to accommodate both Gaussian and Laplace-distributed noise for robustness against heavy-tailed dynamics.
- Provides analytical derivations for predictive uncertainty quantification and construction of prediction intervals within the TVAR(1) specification.

## Open Questions & Future Work

- [[multivariate-tvar-and-generalized-noise-modeling]]

## Archivist Review

The paper proposes a specific application of neural networks for parameter estimation in TVAR models. While practical, this approach does not introduce a sufficiently distinct new concept to justify a standalone entry. The identified open question regarding the extension to multivariate processes and broader noise distributions is tracked as it represents a significant research direction for combining statistical parametric models with deep learning.

### Approved Open Questions
- Multivariate TVAR and Generalized Noise Modeling: This is a foundational gap in bridging parametric statistical models with neural network-based forecasting for non-stationary, multivariate phenomena.

### Rejected Candidates
- [concept] TVAR Parameter Estimation Framework (`tvar-parameter-estimation-framework`) - not_novel: The proposed framework is a classic TVAR implementation using neural networks, which is a specific application rather than a distinct, reusable methodology distinct from existing state-space or neural-ODE approaches.

## Links

- [Abstract](https://arxiv.org/abs/2607.00470)
- [PDF](https://arxiv.org/pdf/2607.00470)

