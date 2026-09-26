---
# CSL-compatible fields
title: "Bayesian inference, on-line forecasting and model choice for large VAR models with Cholesky stochastic volatility"
author:
  - literal: "Nicolas Chopin"
  - literal: "András Fülöp"
  - literal: "Yuedan Huo"
  - literal: "Anna De Simoni"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27431"

# Custom fields
paper_id: "2609.27431"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "bayesian"
  - "monte-carlo"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cholesky-stochastic-volatility-bvar"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:48Z"
created_at: "2026-09-26T09:37:48Z"
---

# Bayesian inference, on-line forecasting and model choice for large VAR models with Cholesky stochastic volatility

**Authors**: Nicolas Chopin, András Fülöp, Yuedan Huo, Anna De Simoni
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27431](https://arxiv.org/abs/2609.27431)

## Summary

This paper develops scalable Bayesian inference, on-line forecasting, and model choice techniques for large vector autoregressions (BVARs) with Cholesky stochastic volatility. The authors introduce a novel MCMC kernel combining a conditionally independent reparametrisation with Particle Gibbs, as well as a Sequential Monte Carlo squared (SMC^2) framework. Applied to US macroeconomic data, these methods substantially improve mixing efficiency and enable exact on-line marginal likelihood estimation for non-conjugate BVARs.

## Key Contributions

- Introduces a novel Markov chain Monte Carlo (MCMC) kernel based on reparametrisation and Particle Gibbs that mixes significantly better than existing samplers for high-dimensional Cholesky stochastic volatility BVARs.
- Develops a Sequential Monte Carlo squared (SMC^2) sampler utilizing the proposed MCMC kernel to deliver sequential one-step-ahead predictive densities and marginal likelihoods.
- Demonstrates superior mixing performance on a 15-dimensional VAR system, achieving a major speedup in effective sample size per second compared to benchmark samplers.

## Open Questions & Future Work

- [[high-dimensional-particle-degeneracy-in-smc]]

## Key Concepts

- [[cholesky-stochastic-volatility-bvar]]: A Bayesian vector autoregression model incorporating Cholesky stochastic volatility for capturing time-varying macroeconomic uncertainty.

## Archivist Review

Strictly evaluated candidates against vault criteria. The concept of Cholesky Stochastic Volatility BVAR represents an important specialized econometric model class, and the open question on particle degeneracy highlights a fundamental scalability bottleneck in sequential Monte Carlo methods for multivariate time series. No named external dataset was suitable for permanent archiving.

### Approved Concepts
- Cholesky Stochastic Volatility BVAR: Presents a scalable MCMC and SMC framework for large BVARs with Cholesky stochastic volatility that overcomes traditional posterior simulation bottlenecks.

### Approved Open Questions
- High-Dimensional Particle Degeneracy in SMC: Overcoming particle degeneracy in high-dimensional sequential Monte Carlo is critical for enabling real-time forecasting and model choice in large-scale macroeconomic systems.

## Links

- [Abstract](https://arxiv.org/abs/2609.27431)
- [PDF](https://arxiv.org/pdf/2609.27431)

