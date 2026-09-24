---
# CSL-compatible fields
title: "Spectral divide-and-conquer MCMC for long stationary time series"
author:
  - literal: "Zixuan Wang"
  - literal: "Matias Quiroz"
  - literal: "Feng Li"
  - literal: "Mattias Villani"
  - literal: "Robert Kohn"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.23985"

# Custom fields
paper_id: "2609.23985"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "bayesian-inference"
  - "mcmc"
  - "distributed-training"
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
processed_at: "2026-09-24T09:38:27Z"
created_at: "2026-09-24T09:38:27Z"
---

# Spectral divide-and-conquer MCMC for long stationary time series

**Authors**: Zixuan Wang, Matias Quiroz, Feng Li, Mattias Villani, Robert Kohn
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.23985](https://arxiv.org/abs/2609.23985)

## Summary

This paper introduces a spectral divide-and-conquer Markov chain Monte Carlo (MCMC) framework for scalable Bayesian inference on long stationary time series. By exploiting the asymptotic independence of the frequency-domain Whittle likelihood, the method integrates a distributed fast Fourier transform with parallel MCMC algorithms. Theoretical guarantees demonstrate that the posterior approximation error converges in probability to the exact time-domain posterior, outperforming existing time-domain divide-and-conquer baselines especially on persistent processes.

## Key Contributions

- Proposes a frequency-domain framework for scalable Bayesian inference in stationary time series using the Whittle likelihood to bypass time-domain temporal dependence challenges.
- Develops a distributed fast Fourier transform integrated with embarrassingly parallel MCMC algorithms in a cluster-computing framework to handle time series exceeding single-node memory.
- Establishes that the spectral divide-and-conquer MCMC posterior approximation converges in probability to the exact time-domain posterior within a shrinking neighbourhood of the full-data Whittle posterior mode, deriving its convergence rate.
- Demonstrates superior performance over state-of-the-art time-domain divide-and-conquer approaches, particularly on highly persistent processes, and illustrates applicability on a semi-long range meteorological time series.

## Open Questions & Future Work

- [[weaker-regularity-conditions-for-local-approximation]]
- [[spectral-divide-and-conquer-for-multivariate-time-series]]
- [[extension-to-locally-stationary-processes]]

## Archivist Review

Approved three explicit future work directions that address theoretical regularity, multivariate extensions, and local stationarity in spectral MCMC. No concepts or datasets qualified under strict vault criteria.

### Approved Open Questions
- Weaker Regularity Conditions for Local Approximation: Removing strong assumptions enhances the general applicability and mathematical rigor of approximation error bounds in spectral and distributed MCMC methods.
- Spectral Divide-and-Conquer for Multivariate Time Series: Multivariate time series modeling is common in macroeconomics and environmental monitoring, and scaling these models remains a major computational challenge.
- Extension to Locally Stationary Processes: Real-world data like financial and climate time series are frequently non-stationary, making extensions to local stationarity critical for practical utility.

## Links

- [Abstract](https://arxiv.org/abs/2609.23985)
- [PDF](https://arxiv.org/pdf/2609.23985)

