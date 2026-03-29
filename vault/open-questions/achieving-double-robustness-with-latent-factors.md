---
created_at: '2026-03-29T06:06:47Z'
source_papers:
- '[[openalex-2603.25010-bayesian-propensity-score-augmented-latent-factor-models-for]]'
title: Achieving double-robustness extension
---

**Background:** The proposed Bayesian propensity score-augmented latent factor model (PS-LFM) does not fully satisfy the classical double-robustness property because the estimation of latent factors (from the outcome model) influences the treatment assignment model.

**Question / Future Work:** Future research could aim to develop extensions to the PS-LFM that reintroduce or approximate the double-robustness property, ensuring consistent estimation of treatment effects if either the outcome model or the treatment assignment model is correctly specified, which is a major goal in robust causal inference.

**Why It Matters:** Achieving double robustness in the presence of unobserved confounding modeled via latent factors remains a significant, unresolved challenge in causal inference methodology.

**Evidence:** Second, because latent factor loadings are estimated from the outcome model and subsequently incorporated into the treatment assignment model, the proposed approach does not fully satisfy the classical double-robustness property: correct specification of either the treatment or outcome model alone is insufficient for consistent estimation.