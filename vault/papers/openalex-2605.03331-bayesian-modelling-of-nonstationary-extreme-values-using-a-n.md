---
# CSL-compatible fields
title: "Bayesian Modelling of Nonstationary Extreme Values Using a Nonparametric Hawkes Process"
author:
  - literal: "Gordon J. Ross"
  - literal: "Dean Markwick"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03331"

# Custom fields
paper_id: "2605.03331"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:28:28Z"
created_at: "2026-05-08T06:28:28Z"
---

# Bayesian Modelling of Nonstationary Extreme Values Using a Nonparametric Hawkes Process

**Authors**: Gordon J. Ross, Dean Markwick
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03331](https://arxiv.org/abs/2605.03331)

## Summary

This paper addresses the challenge of forecasting nonstationary extreme events by proposing a Bayesian point process framework that combines a self-exciting Hawkes process with hierarchical modeling. The model uses a Dirichlet process to nonparametrically learn the rate of event clusters and a Generalised Pareto Distribution (GPD) to characterize event magnitudes, allowing for partial pooling across clusters. The resulting hierarchical model is estimated via an MCMC algorithm, demonstrating improved predictive accuracy in simulations and across diverse empirical datasets.

## Key Contributions

- Introduces a Bayesian nonparametric point process model that integrates a self-exciting Hawkes process for occurrence rates with a hierarchical Generalised Pareto Distribution (GPD) for event magnitudes.
- Employs a Dirichlet process to enable flexible learning of temporal excitation patterns in nonstationary event sequences.
- Demonstrates through empirical evaluation on four real-world datasets that the proposed model provides superior predictive performance for extreme events compared to standard model variants.

## Open Questions & Future Work

- [[extensions-for-nonstationary-extreme-modelling]]

## Archivist Review

I approved the open question regarding extensions for nonstationary extreme modelling as it highlights a high-level architectural limitation (exogenous non-stationarity and multivariate dependency) in extreme value processes that is relevant across domains. I did not find any distinct concepts that were not already well-covered by existing frameworks in the vault or that would serve as a standalone reusable concept beyond this specific model configuration.

### Approved Open Questions
- Extensions for Nonstationary Extreme Modelling: These extensions address the limitations of the current model in handling exogenous non-stationarity and multivariate dependencies, which are critical for real-world risk management scenarios such as financial contagion or multi-hazard natural disasters.

## Links

- [Abstract](https://arxiv.org/abs/2605.03331)
- [PDF](https://arxiv.org/pdf/2605.03331)

