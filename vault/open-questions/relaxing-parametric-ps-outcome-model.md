---
created_at: '2026-03-29T06:06:47Z'
source_papers:
- '[[openalex-2603.25010-bayesian-propensity-score-augmented-latent-factor-models-for]]'
title: Relaxing parametric PS-outcome model
---

**Background:** Causal inference methods based on propensity scores (PS) that incorporate latent factors can suffer from model feedback when parameters relevant to both the treatment assignment model (for PS estimation) and the outcome model are estimated jointly. The authors address this by adopting an approximate Bayesian analysis that breaks the feedback loop.

**Question / Future Work:** Addressing the parametric reliance of the proposed method, future work could investigate methods to relax the reliance on prespecified functional forms for how the propensity score enters the outcome model (e.g., for stratification thresholds) while maintaining identification and mitigating bias from mis-specification.

**Why It Matters:** The parametric specification limits the flexibility of the propensity score augmentation, and developing semiparametric or non-parametric ways to incorporate the PS into the outcome model without losing identification is a key extension.

**Evidence:** First, although the propensity score–augmented specification allows for heterogeneous effects across propensity score strata, it still relies on parametric assumptions for both the treatment assignment and outcome models. In particular, because the effect of the propensity score in the outcome model is assumed to follow a prespecified parametric functional form, mis-specification, such as incorrect thresholds used for propensity score stratification, may lead to biased treatment effect estimates.