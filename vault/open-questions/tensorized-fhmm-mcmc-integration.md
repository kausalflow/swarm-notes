---
created_at: '2026-07-11T07:05:53Z'
source_papers:
- '[[openalex-2607.07008-tensorized-algorithms-and-scalable-filtering-methods-for-hid]]'
title: Scalable MCMC for fHMMs
---

**Background:** Factorial hidden Markov models (fHMMs) are often used to model complex systems influenced by multiple independent latent factors, but they are typically characterized by non-conjugate priors that render standard Gibbs sampling methods inefficient.

**Question / Future Work:** The development of scalable inference procedures for fHMMs under non-conjugate modeling assumptions remains an open challenge, specifically regarding how to integrate efficient tensorized likelihood evaluations into general-purpose MCMC pipelines for scenarios with physical constraints or nonlinear mappings.

**Why It Matters:** Integrating tensorized filtering with MCMC is critical for extending fHMMs to realistic scientific applications where conjugate priors are unavailable.