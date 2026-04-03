---
# CSL-compatible fields
title: "Growth-rate distributions at stationarity"
author:
  - literal: "Edgardo Brigatti"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29916"

# Custom fields
paper_id: "2603.29916"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generalized-logistic-growth-rate-null-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:07:31Z"
created_at: "2026-04-03T06:07:31Z"
---

# Growth-rate distributions at stationarity

**Authors**: Edgardo Brigatti
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29916](https://arxiv.org/abs/2603.29916)

## Summary

This paper provides an analytical framework to explain non-normal growth-rate distributions in stationary time-series by relating them to the system's underlying abundance statistics. The author shows that generalized logistic distributions serve as a powerful null model for systems with Gamma or heavy-tailed abundance, effectively capturing both tent-shaped and Gaussian-like distributions. Furthermore, the paper offers a practical heuristic workflow for selecting appropriate stochastic differential equation models to describe macroecological patterns in data-sparse settings.

## Key Contributions

- Establishes that deviations from normality in growth-rate distributions of stationary time-series are a natural consequence of the underlying abundance distribution rather than pathological behavior.
- Demonstrates that stationary Gamma or heavy-tailed systems yield growth-rate distributions accurately modeled by the generalized logistic distribution.
- Introduces a heuristic workflow for selecting between stochastic differential equation models to reproduce observed macroecological growth patterns in data-constrained scenarios.

## Open Questions & Future Work

- [[stationarity-limits-in-non-markovian-systems]]

## Key Concepts

- [[generalized-logistic-growth-rate-null-model]]: A generalized logistic distribution used as a robust null model to describe diverse growth-rate distribution shapes ranging from tent-shaped to nearly normal.

## Archivist Review

The paper provides a refreshing analytical perspective on growth-rate distribution modeling, moving away from simple normality to a generalized logistic null model. I approved the concept as it offers a reusable, theoretically grounded approach for non-normal time-series analysis. The open question was approved to highlight the fundamental limitation of Markovian assumptions in characterizing stationarity for complex, real-world growth processes.

### Approved Concepts
- Generalized Logistic Growth-Rate Null Model: Provides a flexible analytical framework for characterizing growth-rate distribution shapes that outperforms simple normality assumptions for heavy-tailed or stationary Gamma-distributed data.

### Approved Open Questions
- Stationarity limits in non-Markovian systems: Understanding whether these growth-rate distribution patterns hold outside of Markovian constraints is crucial for the broader applicability of the proposed heuristic selection workflow in real-world systems.

## Links

- [Abstract](https://arxiv.org/abs/2603.29916)
- [PDF](https://arxiv.org/pdf/2603.29916)

