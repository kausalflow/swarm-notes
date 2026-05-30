---
created_at: '2026-05-30T07:37:17Z'
source_papers:
- '[[openalex-2605.28099-a-computationally-tractable-measure-of-global-sensitivity-fo]]'
title: Fisher divergence for multimodal posteriors
---

**Background:** Fisher divergence has been widely used for parameter estimation and generative modeling; however, it has historically performed poorly for multimodal posteriors with well-separated modes.

**Question / Future Work:** Future work is needed to adapt the Fisher divergence-based sensitivity measure for multimodal posteriors, as the current formulation is often blind to disjoint modes. Investigating the use of tempered versions of the reference posterior is a potential approach to mitigate this sensitivity limitation.

**Why It Matters:** Multimodal posteriors are common in complex Bayesian models, and the failure of score-based methods to capture mode-specific sensitivity is a major practical limitation for global sensitivity analysis.

**Evidence:** A first direction would be to address settings involving multimodal posteriors with well-separated modes, a scenario for which score-based divergences are known to perform poorly... One potential remedy is to construct the divergence using a tempered version of the reference posterior, thereby reducing the blindness to disjoint modes.