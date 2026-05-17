---
created_at: '2026-05-17T07:31:22Z'
source_papers:
- '[[openalex-2605.14976-multi-regime-markov-switching-models-with-time-varying-trans]]'
title: GAS model identifiability issues
---

**Background:** Generalized Autoregressive Score (GAS) models define transition probabilities in Markov-switching frameworks using the score of the conditional log-likelihood. These models often exhibit non-identifiability when the score-driven updates are coupled with variance parameters in the likelihood surface.

**Question / Future Work:** Further research is required to resolve the statistical non-identifiability and numerical instability observed when estimating the GAS score coefficient in multi-regime Markov-switching models, particularly regarding the flat likelihood ridges that often cause convergence failure.

**Why It Matters:** The identifiability issue limits the practical application of GAS-based time-varying transition probability models, as current estimation methods frequently fail to converge or provide reliable parameter estimates for the dynamic components.

**Evidence:** Another finding from our paper is that the GAS score coefficient appears to be statistically non-identifiable, due to a ridge in the joint likelihood surface.