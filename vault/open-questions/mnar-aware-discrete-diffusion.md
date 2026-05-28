---
created_at: '2026-05-28T08:38:23Z'
source_papers:
- '[[openalex-2605.25439-missing-pattern-recognized-diffusion-imputation-model-for-mi]]'
title: MNAR-aware Discrete Diffusion Imputation
---

**Background:** Discrete state-space diffusion models are increasingly used for multi-modal data imputation, but integrating mechanisms to explicitly account for non-random missingness remains a complex challenge.

**Question / Future Work:** The development of MNAR-aware diffusion frameworks for discrete state-space data remains largely unexplored, requiring new formulations to handle the interaction between the missing pattern recognizer and the discrete diffusion process.

**Why It Matters:** Many real-world datasets contain a mixture of continuous and discrete features, and current continuous-only diffusion methods are insufficient for comprehensive multi-modal imputation.

**Evidence:** Nevertheless, introducing a pattern recognizer under MNAR settings within a discrete diffusion framework entails non-trivial formulation challenges as well as practical considerations.