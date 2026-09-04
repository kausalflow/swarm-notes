---
# CSL-compatible fields
title: "Poisson-Gamma Dynamical Systems with Time-varying Transition Dynamics"
author:
  - literal: "Jiahao Wang"
  - literal: "Yijun Wang"
  - literal: "Nan Fang"
  - literal: "Sikun Yang"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.00896"

# Custom fields
paper_id: "2609.00896"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-models"
  - "bayesian"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tv-pgds"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:11:19Z"
created_at: "2026-09-04T09:11:19Z"
---

# Poisson-Gamma Dynamical Systems with Time-varying Transition Dynamics

**Authors**: Jiahao Wang, Yijun Wang, Nan Fang, Sikun Yang
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.00896](https://arxiv.org/abs/2609.00896)

## Summary

Bayesian Poisson-Gamma Dynamical Systems (PGDSs) are effective for modeling count-valued time series, but existing models struggle with evolving transition dynamics. To address this, the authors propose TV-PGDS, which allows underlying transition matrices to evolve over time via three specially-designed Dirichlet Markov chains. They also develop a fully-conjugate and efficient Gibbs sampler using Dirichlet-Multinomial-Beta data augmentation. Experiments demonstrate that TV-PGDS achieves superior predictive performance by effectively capturing time-varying dependencies.

## Key Contributions

- Proposes TV-PGDS, a Poisson-Gamma Dynamical System extension that allows underlying transition matrices to evolve over time for count-valued time series.
- Constructs three specialized Dirichlet Markov chains (Dir-Dir, Dir-Gam-Dir, PR-Gam-Dir) to capture heterogeneous structural mutations in transition dependencies.
- Develops a fully-conjugate and efficient Gibbs sampler using Dirichlet-Multinomial-Beta data augmentation for posterior simulation.

## Open Questions & Future Work

- [[change-point-detection-tv-pgds]]

## Key Concepts

- [[tv-pgds]]: A Poisson-Gamma Dynamical System extension featuring time-varying transition kernels and specialized Dirichlet Markov chains to model evolving count time series dependencies.

## Archivist Review

Approved the core TV-PGDS concept for modeling time-varying transition dynamics in count-valued time series, along with the explicitly posed open question regarding adaptive change-point detection. Adhered to strict scarcity limits.

### Approved Concepts
- Poisson-Gamma Dynamical Systems with Time-varying Transition Dynamics (TV-PGDS): Introduces a novel time-varying transition kernel framework for Poisson-Gamma dynamical systems to model evolving dependency structures in count time series.

### Approved Open Questions
- Change-Point Detection for TV-PGDS: Overcomes the manual hyperparameter tuning of sub-interval lengths and enables data-driven, non-stationary temporal modeling for count time series.

## Links

- [Abstract](https://arxiv.org/abs/2609.00896)
- [PDF](https://arxiv.org/pdf/2609.00896)

