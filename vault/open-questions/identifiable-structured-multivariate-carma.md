---
created_at: '2026-09-26T09:37:24Z'
source_papers:
- '[[openalex-2609.28419-multivariate-continuous-time-autoregressive-moving-average-p]]'
title: Identifiable Structured Multivariate CARMA
---

**Background:** Multivariate continuous-time autoregressive moving average (MCARMA) processes model irregularly sampled multi-band time series with correlated stochastic drivers, but unrestricted parameterizations face severe computational and identifiability bottlenecks.

**Question / Future Work:** Determine structured matrix parameterizations and off-diagonal dynamic terms in multivariate continuous-time moving average models that can remain identifiable under irregular and partially observed sampling designs, while avoiding the massive parameter proliferation of unrestricted formulations.

**Why It Matters:** Crucial for extending continuous-time multivariate stochastic models beyond frequency-independent coherence while maintaining statistical identifiability and computational tractability under realistic astronomical observation constraints.

**Evidence:** Allowing selected off-diagonal dynamic terms, alternative latent driving structures, or other structured matrix parameterizations could accommodate frequency-dependent cross-spectral behavior while avoiding the large number of parameters in an unrestricted MCARMA model. Determining which such structures remain identifiable under irregular and partially observed sampling is an important statistical problem in its own right.