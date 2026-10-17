---
# CSL-compatible fields
title: "Resolving Structural Uncertainty in Stochastic Dynamical Systems via Ensemble-Based Bayesian Inference"
author:
  - literal: "Francesco Zambelli"
  - literal: " Valeria d’Andrea"
  - literal: " Manlio De Domenico"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19744"

# Custom fields
paper_id: "2610.19744"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "probabilistic-models"
  - "bayesian"
  - "stochastic-differential-equations"
  - "uncertainty-quantification"
  - "causal-discovery"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:56:11Z"
created_at: "2026-10-17T08:56:11Z"
---

# Resolving Structural Uncertainty in Stochastic Dynamical Systems via Ensemble-Based Bayesian Inference

**Authors**: Francesco Zambelli,  Valeria d’Andrea,  Manlio De Domenico
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19744](https://arxiv.org/abs/2610.19744)

## Summary

This paper proposes a fully Bayesian ensemble-based inference framework to recover the interaction structure of complex stochastic dynamical systems from sparse time-series observations. The approach integrates a continuous-time SDE likelihood formulation based on the Onsager-Machlup quasi-potential with a non-parametric Minimum Description Length structural prior to prevent kinetic overfitting. Using a block-coordinate optimization scheme that combines sub-quadratic MCMC topological sampling and Nelder-Mead optimization, the framework efficiently explores the high-dimensional posterior. Evaluations on macroscopic population dynamics demonstrate that non-stationary transient data are essential for causal resolution, and that propagating structural uncertainty via ensembles significantly improves perturbation prediction robustness compared to MAP estimates.

## Key Contributions

- Proposes a fully Bayesian ensemble-based inference framework using an Onsager-Machlup quasi-potential SDE likelihood combined with a non-parametric Minimum Description Length structural prior to recover interaction structures from sparse time-series.
- Employs a block-coordinate optimization scheme combining sub-quadratic MCMC topological sampling and deterministic Nelder-Mead parameter optimization.
- Demonstrates on non-linear macroscopic population dynamics that inference requires non-stationary transient data to resolve causal information.
- Proves that propagating structural uncertainty via ensemble-based posterior analysis yields more robust and reliable predictions for downstream perturbations than single-point MAP estimates.

## Archivist Review

No new concepts or open questions met the strict criteria for permanent vault inclusion, as the paper combines existing stochastic differential equation likelihoods and Minimum Description Length priors rather than introducing a novel, reusable modeling paradigm.

### Rejected Candidates
- [open_question] Single-Cell Developmental Network Inference (`single-cell-transcriptomic-network-inference`) - low_impact: Future work extension proposing application to another domain without resolving a core theoretical bottleneck in time series modeling.

## Links

- [Abstract](https://arxiv.org/abs/2610.19744)
- [PDF](https://arxiv.org/pdf/2610.19744)

