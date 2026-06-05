---
created_at: '2026-06-05T08:39:19Z'
source_papers:
- '[[openalex-2606.03475-surrogate-modeling-of-interconnector-flows-a-machine-learnin]]'
title: Surrogate Modeling Power System Feasibility
---

**Background:** Power system expansion planning often faces computational trade-offs between spatial granularity and model tractability, necessitating the use of surrogates or reduced-order models to represent cross-border interactions. Current surrogate frameworks for interconnector flows are primarily evaluated in deterministic settings with limited consideration of structural system changes or long-term feasibility.

**Question / Future Work:** Future work should extend interconnector-flow surrogate frameworks to complex settings with explicit high-voltage grid representations (e.g., DC/AC-OPF) and incorporate probabilistic outputs to propagate uncertainty into planning decisions. Developing adaptive feasibility-aware training methods that minimize surrogate-induced system infeasibilities without introducing systematic economic biases remains an open challenge.

**Why It Matters:** As power systems integrate higher shares of renewables, the structural patterns of interconnector flows become increasingly volatile and difficult to capture with simple scaling, making robust surrogates critical for computationally tractable long-term planning.