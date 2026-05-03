---
created_at: '2026-05-03T07:14:20Z'
source_papers:
- '[[openalex-2604.28163-sequential-inference-for-gaussian-processes-a-signal-process]]'
title: Scalability of Spatiotemporal Markovian GPs
---

**Background:** Markovian Gaussian processes allow exact inference in linear time via linear time-invariant stochastic differential equations, but they often scale cubically with the number of spatial locations.

**Question / Future Work:** Research is needed to develop scalable inference methods for spatiotemporal Markovian Gaussian processes that bypass the O(N_s^3) complexity in the number of spatial locations without relying solely on standard sparse inducing-point approximations.

**Why It Matters:** This complexity bottleneck restricts the use of Markovian GPs in high-dimensional spatiotemporal monitoring and climate modeling tasks.

**Evidence:** Although Markovian formulations avoid the cubic scaling in time typical of standard GPs, they still exhibit \mathcal{O}(N_s^3) complexity in the number of spatial locations, which can become prohibitive.