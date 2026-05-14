---
# CSL-compatible fields
title: "Heteroscedastic Diffusion for Multi-Agent Trajectory Modeling"
author:
  - literal: "Guillem Capellera"
  - literal: "Antonio Rubio"
  - literal: "Luis Ferraz"
  - literal: "Antonio Agudo"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10717"

# Custom fields
paper_id: "2605.10717"
paper_source: "openalex"
domain: "robotics"
tags:
  - "diffusion-model"
  - "multimodal"
  - "trajectory-modeling"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "u2diffine"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:39:02Z"
created_at: "2026-05-14T07:39:02Z"
---

# Heteroscedastic Diffusion for Multi-Agent Trajectory Modeling

**Authors**: Guillem Capellera, Antonio Rubio, Luis Ferraz, Antonio Agudo
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10717](https://arxiv.org/abs/2605.10717)

## Summary

U2Diffine is a unified diffusion-based approach designed to address both trajectory completion and forecasting, two tasks often treated separately in multi-agent modeling. Unlike conventional models, it estimates heteroscedastic state-wise uncertainty by augmenting the denoising process with negative log-likelihood and a first-order Taylor approximation. Additionally, the framework incorporates a Rank Neural Network (RankNN) to assign error probabilities to generated modes, facilitating reliable selection among multi-modal predictions. Experimental results on four sports-related datasets demonstrate superior performance in both accuracy and uncertainty quantification compared to existing trajectory modeling baselines.

## Key Contributions

- Introduces U2Diffine, a unified diffusion framework capable of joint trajectory completion and forecasting with state-wise heteroscedastic uncertainty estimates.
- Proposes a first-order Taylor approximation technique to propagate latent space uncertainty into real state space for trajectory modeling.
- Integrates a Rank Neural Network (RankNN) to estimate error probabilities for individual generated trajectory modes, outperforming existing state-of-the-art methods on NBA and sports-based trajectory benchmarks.

## Open Questions & Future Work

- [[stable-heteroscedastic-uncertainty-propagation-diffusion-models]]

## Key Concepts

- [[u2diffine]]: A unified diffusion framework for joint trajectory completion and forecasting that integrates state-wise heteroscedastic uncertainty estimation via first-order Taylor approximation.

## Archivist Review

I approved the U2Diffine framework for its unified approach to completion and forecasting, and the open question regarding stable uncertainty propagation in diffusion models, as it captures a fundamental limitation in current generative trajectory modeling. I rejected the RankNN concept as it is a standard implementation detail for post-processing multi-modal samples rather than a distinct or novel methodological contribution. I avoided approving the sports datasets provided, as they are domain-specific and not central to universal forecasting knowledge.

### Approved Concepts
- U2Diffine: Provides a unified framework for joint trajectory completion and forecasting with latent-to-state uncertainty propagation via Taylor approximation.

### Approved Open Questions
- Stable uncertainty propagation in diffusion: Calibrated uncertainty is essential for the reliability of generative models in safety-critical robotics and decision-making applications.

### Rejected Candidates
- [concept] Rank Neural Network (RankNN) (`rank-neural-network-ranknn`) - not_novel: Post-processing ranking modules for generative model outputs are common design patterns and this specific implementation does not introduce a novel, reusable architecture or principle.

## Links

- [Abstract](https://arxiv.org/abs/2605.10717)
- [PDF](https://arxiv.org/pdf/2605.10717)

