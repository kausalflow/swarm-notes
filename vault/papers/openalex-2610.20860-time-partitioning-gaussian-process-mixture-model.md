---
# CSL-compatible fields
title: "Time-partitioning Gaussian Process Mixture Model"
author:
  - literal: "Guilherme Piantino"
  - literal: "Hedibert Freitas Lopes"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.20860"

# Custom fields
paper_id: "2610.20860"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "gaussian-process"
  - "bayesian"
  - "nonstationary"
  - "change-point-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-partitioning-gaussian-process-mixture-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:56Z"
created_at: "2026-10-22T09:44:56Z"
---

# Time-partitioning Gaussian Process Mixture Model

**Authors**: Guilherme Piantino, Hedibert Freitas Lopes
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.20860](https://arxiv.org/abs/2610.20860)

## Summary

The authors propose the Time-partitioning Gaussian Process Mixture Model (TPGPMM), a Bayesian nonparametric framework for identifying regimes and making nonstationary predictions in financial and macroeconomic time series without relying on Markovian assumptions. TPGPMM uses an adaptive Pitman-Yor process prior over ordered compositions with contiguity enforcement to model block lengths, paired with regime-specific Gaussian processes. Inference is performed via a split-merge Metropolis-within-Gibbs sampler with exact Gibbs updates of regime boundaries, enabling joint estimation of change points and hyperparameters. Evaluations on simulated data, the CBOE Volatility Index, and US Treasury yields show that TPGPMM accurately flags persistent structural shifts and achieves competitive fitting and forecasting performance against change-point and stationary baselines.

## Key Contributions

- Proposes the Time-partitioning Gaussian Process Mixture Model (TPGPMM), a non-Markovian Bayesian nonparametric framework combining an adaptive Pitman-Yor process prior on ordered compositions with regime-specific Gaussian processes.
- Introduces a split-merge Metropolis-within-Gibbs sampler with exact Gibbs updates of regime boundaries to jointly learn change points and hyperparameters.
- Demonstrates robust empirical recovery of true regimes on simulated data and identifies documented market and monetary-policy events on the CBOE Volatility Index and 10-year US Treasury yield.
- Shows that variants estimating noise levels outperform change-point baselines in fit and forecast, and outperform fitted stationary Gaussian processes in RMSE across most horizons.

## Open Questions & Future Work

- [[scalable-bayesian-nonparametric-time-series-partitioning]]

## Key Concepts

- [[time-partitioning-gaussian-process-mixture-model]]: A Bayesian nonparametric framework for regime identification and nonstationary time series prediction without Markovian assumptions.

## Archivist Review

Approved the core methodological concept (TPGPMM) and the explicit open question concerning the scalability of Bayesian nonparametric time-series partitioning. Rejected paper-local evaluation datasets and routine mentions as per vault standards.

### Approved Concepts
- Time-partitioning Gaussian Process Mixture Model: It is the core methodological contribution of the paper, providing a non-Markovian Bayesian nonparametric framework for regime identification and nonstationary time series prediction.

### Approved Open Questions
- Scalable Bayesian Nonparametric Time-Series Partitioning: Computational complexity currently scales cubically with block lengths, bottlenecking application to massive macro-financial datasets or multivariate systems.

## Links

- [Abstract](https://arxiv.org/abs/2610.20860)
- [PDF](https://arxiv.org/pdf/2610.20860)

