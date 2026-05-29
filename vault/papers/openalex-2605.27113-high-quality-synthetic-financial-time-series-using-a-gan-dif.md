---
# CSL-compatible fields
title: "High-Quality Synthetic Financial Time-Series using a GAN-Diffusion Framework"
author:
  - literal: "Giuseppe Masi"
  - literal: "Andrea Coletta"
  - literal: "Novella Bartolini"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27113"

# Custom fields
paper_id: "2605.27113"
paper_source: "openalex"
domain: "finance"
tags:
  - "gan"
  - "diffusion-model"
  - "time-series"
  - "generative-adversarial-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "comets-gan"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:37:29Z"
created_at: "2026-05-29T08:37:29Z"
---

# High-Quality Synthetic Financial Time-Series using a GAN-Diffusion Framework

**Authors**: Giuseppe Masi, Andrea Coletta, Novella Bartolini
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27113](https://arxiv.org/abs/2605.27113)

## Summary

This paper addresses the difficulty of generating realistic synthetic financial data that captures complex market stylized facts and inter-asset correlations. The authors propose a hybrid framework that integrates a custom Conditional GAN, CoMeTS-GAN, with a diffusion model. By using the GAN's Critic as a guide for the diffusion process, the framework effectively enforces learned correlation structures, providing a high-fidelity solution for counterfactual market simulation.

## Key Contributions

- Introduces CoMeTS-GAN, a conditional generative adversarial network for the joint simulation of mid-price and volume for multiple correlated financial assets.
- Proposes a hybrid GAN-Diffusion framework where the GAN's Critic acts as a guiding module to enforce complex inter-asset correlation structures during the diffusion generation process.
- Demonstrates that the integrated architecture outperforms state-of-the-art baselines in capturing financial stylized facts and modeling realistic cross-asset correlations.

## Open Questions & Future Work

- [[robust-multivariate-financial-generation]]

## Key Concepts

- [[comets-gan]]: A conditional GAN architecture designed to jointly model correlated multivariate financial time-series like mid-price and volume.

## Archivist Review

I have approved the core generative concept (CoMeTS-GAN) and the corresponding open question regarding multivariate financial dependency modeling. These additions are narrow enough to maintain the quality of the vault while addressing the paper's specific contribution to synthetic financial time-series generation. All other candidates were rejected as they were either too generic or local implementation details.

### Approved Concepts
- CoMeTS-GAN: It provides a modular approach to jointly modeling heterogeneous financial time-series (price and volume) while enforcing correlation, which is a common requirement in financial simulation.

### Approved Open Questions
- Robust multivariate financial generation: Correlation dynamics are fundamental to portfolio risk management; failing to accurately model them limits the utility of synthetic data for counterfactual analysis and stress testing.

## Links

- [Abstract](https://arxiv.org/abs/2605.27113)
- [PDF](https://arxiv.org/pdf/2605.27113)

