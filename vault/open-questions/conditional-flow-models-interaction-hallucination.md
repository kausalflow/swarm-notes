---
created_at: '2026-10-17T08:55:55Z'
source_papers:
- '[[openalex-2610.20288-predicting-unseen-scientific-interactions-conditional-flow-m]]'
title: Interaction Hallucination in Conditional Flow Models
---

**Background:** Conditional generative models such as flow matching and diffusion models are widely applied to predict complex scientific responses and interactions across physical and biological domains. However, aggregate fidelity metrics often conceal whether these models successfully learn and extrapolate interaction effects versus hallucinating non-additive structures.

**Question / Future Work:** Investigate whether conditional generative models systematically learn true interaction dynamics or merely produce plausible non-additive hallucinations due to inherent architectural and training inductive biases, and determine general conditions under which interaction extrapolation succeeds or fails across different data representations and identifiability regimes.

**Why It Matters:** Understanding how generative models extrapolate interaction effects is critical for high-stakes scientific discovery, as models can appear accurate overall while incorrectly predicting the combinatorial or synergistic effects that motivate experiments.

**Evidence:** It remains unclear how these models learn interactions and when these successfully extrapolate to unseen conditions.