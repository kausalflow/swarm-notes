---
# CSL-compatible fields
title: "Forecasting Multiple Observables with SCROLL: Score-Trained Uncertainty for Stochastic Dynamics"
author:
  - literal: "Pavel Prochazka"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25898"

# Custom fields
paper_id: "2608.25898"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-estimation"
  - "probabilistic-forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "scroll"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:47Z"
created_at: "2026-08-28T16:59:47Z"
---

# Forecasting Multiple Observables with SCROLL: Score-Trained Uncertainty for Stochastic Dynamics

**Authors**: Pavel Prochazka
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25898](https://arxiv.org/abs/2608.25898)

## Summary

The paper introduces SCROLL, a score-trained uncertainty framework for forecasting multiple observables of stochastic dynamical systems by composing per-task free-routed last-layer beliefs on a shared backbone. This approach eliminates the need for manual multi-task loss balancing by absorbing unit-dependent scaling into jointly learned likelihood parameters. Evaluated on both synthetic stochastic systems and real-world air-quality data, SCROLL accurately recovers analytic predictive kernels and outperforms tuned baselines in negative log-likelihood and calibration at a fraction of the computational cost.

## Key Contributions

- Introduces SCROLL, a score-trained uncertainty framework that composes observables' likelihoods in per-task free-routed last-layer beliefs on a shared backbone.
- Absorbs unit-dependent loss scaling into likelihood parameters learned in a single gradient pass without manual loss balancing.
- Recovers the analytic kernel on the well-specified homoscedastic Ornstein–Uhlenbeck process.
- Achieves superior negative log-likelihood (NLL) and calibration on heteroscedastic systems like stochastic Lorenz-63 and real air-quality data at a fraction of tuned grid costs.

## Key Concepts

- [[scroll]]: Score-trained uncertainty framework for forecasting multiple observables with shared backbones and free-routed last-layer beliefs.

## Archivist Review

Approved SCROLL as the core framework for multi-observable probabilistic forecasting, adhering strictly to the scarcity and novelty constraints. No other concepts, datasets, or open questions met the rigorous threshold for vault permanence.

### Approved Concepts
- SCROLL: SCROLL is the core framework proposed in the paper for multi-task uncertainty forecasting in stochastic dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2608.25898)
- [PDF](https://arxiv.org/pdf/2608.25898)

