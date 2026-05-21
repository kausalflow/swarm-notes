---
created_at: '2026-05-21T08:36:29Z'
source_papers:
- '[[openalex-2509.17625-comparing-data-assimilation-and-likelihood-based-inference-o]]'
title: Robustness of LBI in Asymmetric ABMs
---

**Background:** Agent-based models (ABMs) often exhibit symmetries in their state space, such as invariance to translation or reflection in opinion dynamics models. The ability of inference methods to adapt to parametric mis-specification through state adaptation—where inferred latent states are adjusted to maintain probabilistic consistency—is well-documented in symmetric settings.

**Question / Future Work:** It is currently unknown whether the observed resilience of likelihood-based inference (LBI) to parametric mis-specification, which relies on inherent symmetries in the Bounded-Confidence Model (BCM), extends to more complex ABMs that lack such symmetries, such as those featuring heterogeneous agents or asymmetric interaction rules. Investigating this adaptability is necessary to understand the general applicability of LBI across diverse model architectures.

**Why It Matters:** This is technically important because it determines whether LBI's robustness is a fundamental feature of the inference approach or a byproduct of specific model geometry, influencing its suitability for more realistic, heterogeneous social systems.

**Evidence:** However, this resilience relies on symmetries inherent in the BCM (e.g., invariance around x = 0.5). Whether similar adaptability extends to ABMs lacking such symmetries—such as those with heterogeneous agents or asymmetric interaction rules—remains an open question worth exploring.