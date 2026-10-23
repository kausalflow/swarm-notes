---
# CSL-compatible fields
title: "Practical identifiability and parameter estimation of compartmental epidemiological models"
author:
  - literal: "Q. Y. Chen"
  - literal: "Zoi Rapti"
  - literal: "Yannis Drossinos"
  - literal: "Jesús Cuevas–Maraver"
  - literal: "George A. Kevrekidis"
  - literal: "P. G. Kevrekidis"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2406.17827"

# Custom fields
paper_id: "2406.17827"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:41:00Z"
created_at: "2026-10-23T09:41:00Z"
---

# Practical identifiability and parameter estimation of compartmental epidemiological models

**Authors**: Q. Y. Chen, Zoi Rapti, Yannis Drossinos, Jesús Cuevas–Maraver, George A. Kevrekidis, P. G. Kevrekidis
**Date**: 2026-10-21
**Paper ID**: [openalex:2406.17827](https://arxiv.org/abs/2406.17827)

## Summary

This paper investigates practical parameter identifiability and estimation in ODE-based epidemiological models using simulated data with added noise. The authors compare maximum likelihood and Markov chain Monte Carlo (MCMC) methods, demonstrating that MCMC is more robust and that the benefits of fixing unmeasured initial conditions are model-dependent.

## Key Contributions

- Investigates practical parameter identifiability and parameter estimation in ODE-based epidemiological models using simulated noisy data to avoid unknown data quality issues.
- Compares maximum likelihood and Markov chain Monte Carlo (MCMC) estimation methods, finding MCMC to be overall more robust than point estimators.
- Demonstrates that the impact of fixing versus fitting unmeasured initial conditions on parameter estimate quality is model-dependent across different compartmental models.
- Shows that structural identifiability's value becomes moot in the presence of significantly noisy data.

## Limitations

Evaluated on simulated compartmental models rather than direct real-world epidemiological data streams.

## Open Questions & Future Work

- [[spatial-epidemiological-model-identifiability]]

## Archivist Review

Applied strict review filters, approving only the high-value open question on spatial epidemiological model identifiability while rejecting all other candidates due to lack of distinct methodological novelty or domain-general reusability.

### Approved Open Questions
- Spatially Dependent Model Identifiability: Spatially dependent epidemiological models introduce significant high-dimensionality and complex parameter correlations that make identifiability analysis vastly more difficult, necessitating dedicated methodological advancements.

## Links

- [Abstract](https://arxiv.org/abs/2406.17827)
- [PDF](https://arxiv.org/pdf/2406.17827)

