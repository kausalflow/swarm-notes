---
created_at: '2026-06-14T08:38:44Z'
source_papers:
- '[[openalex-2606.13615-data-driven-subsampling-rates-for-diffusion-parameter-estima]]'
title: Generalizing SDE Noise Assumptions
---

**Background:** Stochastic differential equations (SDEs) are often used in multiscale modeling where the physical behavior is characterized by distinct fast and slow dynamics. Parameter estimation for these systems is typically biased if the data is sampled without regard for the underlying scale separation.

**Question / Future Work:** The analytical foundation of the monotone run indicator and subsampling method relies on SDEs with additive noise; it remains an open question to what extent these results can be generalized to SDEs with state-dependent (non-additive) noise, where the diffusion coefficient varies with the process state.

**Why It Matters:** Generalizing to non-additive noise is crucial for the applicability of this data-driven subsampling method to a wider range of physical and financial systems where diffusion characteristics are state-dependent.

**Evidence:** Only SDE models with additive noise were studied in this paper. It therefore remains an open question to what extent the results on the length of monotone runs on an infinitesimal scale, and thus also our method, can be applied to more general SDEs.