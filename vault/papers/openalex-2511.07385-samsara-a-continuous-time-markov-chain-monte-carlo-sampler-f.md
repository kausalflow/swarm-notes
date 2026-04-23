---
# CSL-compatible fields
title: "samsara: a continuous-time Markov chain Monte Carlo sampler for trans-dimensional Bayesian analysis"
author:
  - literal: "Gabriele Astorino"
  - literal: "Lorenzo Valbusa Dall'Armi"
  - literal: "R. Buscicchio"
  - literal: "Joachim Pomper"
  - literal: "Angelo Ricciardone"
  - literal: "W. Del Pozzo"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2511.07385"

# Custom fields
paper_id: "2511.07385"
paper_source: "openalex"
domain: "nlp"
tags:
  - "reinforcement-learning"
  - "bayesian-inference"
  - "markov-chain-monte-carlo"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "samsara-ctmcmc-sampler"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:56:54Z"
created_at: "2026-04-23T06:56:54Z"
---

# samsara: a continuous-time Markov chain Monte Carlo sampler for trans-dimensional Bayesian analysis

**Authors**: Gabriele Astorino, Lorenzo Valbusa Dall'Armi, R. Buscicchio, Joachim Pomper, Angelo Ricciardone, W. Del Pozzo
**Date**: 2026-04-20
**Paper ID**: [openalex:2511.07385](https://arxiv.org/abs/2511.07385)

## Summary

This paper introduces Samsara, a continuous-time Markov chain Monte Carlo (CTMCMC) framework designed for Bayesian inference in scenarios with large and unknown parameter dimensionality. Unlike traditional reversible-jump MCMC (RJMCMC) methods, Samsara models parameter evolution through Poisson-driven birth, death, and mutation processes, utilizing adaptive rate definitions to achieve automatic acceptance of trans-dimensional moves. The approach is validated on various benchmarks, including Gaussian mixture models and time-series signal inference, where it demonstrates competitive efficiency and accuracy compared to standard nested sampling methods.

## Key Contributions

- Introduces Samsara, a continuous-time MCMC framework that facilitates trans-dimensional Bayesian inference by modeling evolution via Poisson-driven birth, death, and mutation processes.
- Achieves automatic acceptance of trans-dimensional moves through adaptive rate definitions that satisfy detailed balance, improving sampling efficiency over RJMCMC.
- Demonstrates high-accuracy performance on benchmarks including Gaussian mixture models and signal inference in noisy time series, showing agreement with nested sampling baselines.

## Open Questions & Future Work

- [[diagnostics-trans-dimensional-mcmc]]
- [[ctmcmc-hamiltonian-dynamics-integration]]

## Key Concepts

- [[samsara-ctmcmc-sampler]]: A continuous-time Markov chain Monte Carlo (CTMCMC) framework that models parameter evolution through Poisson-driven birth, death, and mutation processes for trans-dimensional Bayesian analysis.

## Archivist Review

The paper introduces a structured approach to trans-dimensional Bayesian inference via continuous-time MCMC. The core concept is approved for its methodological shift away from RJMCMC, and the open questions are approved as they address fundamental limitations (convergence diagnostics and gradient integration) in stochastic trans-dimensional sampling that are broadly applicable to the field.

### Approved Concepts
- Samsara: Samsara introduces a novel CTMCMC framework specifically for trans-dimensional Bayesian inference, offering an efficient alternative to traditional RJMCMC methods.

### Approved Open Questions
- Convergence Diagnostics for Trans-Dimensional MCMC: Reliable convergence diagnostics are essential for interpreting Bayesian inference results; without them, it is difficult to determine if a trans-dimensional sampler has adequately explored the full parameter space, particularly in high-dimensional or multimodal settings.
- Integrating Deterministic Drift into CTMCMC: Integrating deterministic drift could significantly improve the mixing and efficiency of samplers in large parameter spaces, potentially bridging the performance gap between CTMCMC and other high-efficiency sampling techniques like NUTS or HMC.

## Links

- [Abstract](https://arxiv.org/abs/2511.07385)
- [PDF](https://arxiv.org/pdf/2511.07385)

