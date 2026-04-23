---
created_at: '2026-04-23T06:56:54Z'
source_papers:
- '[[openalex-2511.07385-samsara-a-continuous-time-markov-chain-monte-carlo-sampler-f]]'
title: Convergence Diagnostics for Trans-Dimensional MCMC
---

**Background:** In Continuous-Time Markov Chain Monte Carlo (CTMCMC) samplers, the autocorrelation length is often monitored to assess the statistical independence of samples, but the trans-dimensional nature of the parameter space complicates this calculation as expectation values are not well-defined for variable-dimensional states.

**Question / Future Work:** There is a need to develop more robust and standard diagnostic methods for assessing the convergence and autocorrelation length of MCMC chains operating in trans-dimensional spaces where the dimensionality is not fixed. The currently proposed scalar functions, such as the log-posterior or distances to reference points, are ad-hoc proxies that may not fully capture the complexity of the trans-dimensional exploration process.

**Why It Matters:** Reliable convergence diagnostics are essential for interpreting Bayesian inference results; without them, it is difficult to determine if a trans-dimensional sampler has adequately explored the full parameter space, particularly in high-dimensional or multimodal settings.