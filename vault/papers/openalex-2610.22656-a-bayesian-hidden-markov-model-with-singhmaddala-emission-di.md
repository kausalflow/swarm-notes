---
# CSL-compatible fields
title: "A Bayesian Hidden Markov Model with Singh–Maddala Emission Distributions for Heavy-Tailed Regime-Switching Time Series"
author:
  - literal: "Safaa K. Kadhem"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.22656"

# Custom fields
paper_id: "2610.22656"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "bayesian"
  - "hidden-markov-model"
  - "regime-switching"
  - "heavy-tailed"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hidden-markov-model-with-singh-maddala-emission-distributions"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:58Z"
created_at: "2026-10-22T09:43:58Z"
---

# A Bayesian Hidden Markov Model with Singh–Maddala Emission Distributions for Heavy-Tailed Regime-Switching Time Series

**Authors**: Safaa K. Kadhem
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.22656](https://arxiv.org/abs/2610.22656)

## Summary

The paper develops a fully Bayesian Hidden Markov Model with Singh-Maddala (Burr Type XII) emission distributions (HMMSM) to model heavy-tailed, regime-switching time series. It derives the complete Bayesian structure and implements an adaptive Metropolis-within-Gibbs sampler utilizing forward-filtering backward-sampling and conjugate Dirichlet updates. Evaluations on simulated heavy-tailed data show superior model selection and parameter recovery compared to seven competing specifications, while an application to Irish monthly rainfall data highlights the model's empirical utility and uncovers a fundamental weak identifiability of the Singh-Maddala scale parameter.

## Key Contributions

- Develops a fully Bayesian Hidden Markov Model with Singh-Maddala (Burr Type XII) emission distributions (HMMSM) for heavy-tailed regime-switching time series.
- Designs an adaptive Metropolis-within-Gibbs sampler combining forward-filtering backward-sampling, conjugate Dirichlet updates, and adaptive Metropolis steps.
- Demonstrates superior performance over seven competing specifications on heavy-tailed simulations (delta WAIC >= 51.76) and evaluates a 26-year gridded rainfall dataset for Ireland.

## Limitations

Documents weak identifiability of the Singh-Maddala scale parameter in certain empirical applications, recommending inference on identifiable parameters as primary targets.

## Open Questions & Future Work

- [[systematic-simulation-boundary-validation]]

## Key Concepts

- [[hidden-markov-model-with-singh-maddala-emission-distributions]]: A fully Bayesian Hidden Markov Model utilizing Singh-Maddala emission distributions to capture heavy tails and regime switching.

## Archivist Review

Approved the primary HMMSM methodological framework and the open question regarding its performance boundaries across parameter grids. Rejected the emission distribution subcomponent as it is subsumed by the overarching framework note.

### Approved Concepts
- Hidden Markov Model with Singh-Maddala Emission Distributions: Introduces the HMMSM framework combining HMMs with heavy-tailed Singh-Maddala emission distributions for regime-switching time series.

### Approved Open Questions
- Systematic simulation boundary validation: Understanding the precise performance boundaries and regimes where heavy-tailed multi-parameter emissions outperform simpler alternatives is crucial for methodological guidance in applied time series modeling.

### Rejected Candidates
- [concept] Singh-Maddala Emission Distribution (`singh-maddala-emission-distribution`) - subcomponent_of_broader_mechanism: Subcomponent of the broader HMMSM framework.

## Links

- [Abstract](https://arxiv.org/abs/2610.22656)
- [PDF](https://arxiv.org/pdf/2610.22656)

