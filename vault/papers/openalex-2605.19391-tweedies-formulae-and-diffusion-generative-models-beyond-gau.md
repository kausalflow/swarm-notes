---
# CSL-compatible fields
title: "Tweedie's Formulae and Diffusion Generative Models Beyond Gaussian"
author:
  - literal: "Wenpin Tang"
  - literal: "Nizar Touzi"
  - literal: "Zikun Zhang"
  - literal: "Xun Yu Zhou"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19391"

# Custom fields
paper_id: "2605.19391"
paper_source: "openalex"
domain: "nlp"
tags:
  - "diffusion-model"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "non-gaussian-diffusion-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:35Z"
created_at: "2026-05-22T08:17:35Z"
---

# Tweedie's Formulae and Diffusion Generative Models Beyond Gaussian

**Authors**: Wenpin Tang, Nizar Touzi, Zikun Zhang, Xun Yu Zhou
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19391](https://arxiv.org/abs/2605.19391)

## Summary

This paper extends the scope of stochastic differential equation-based diffusion models by deriving Tweedie's formulae for non-Gaussian processes, including geometric Brownian motion, squared Bessel, and Cox-Ingersoll-Ross processes. By incorporating state-dependent diffusion coefficients, the authors formulate new denoising score-matching objectives that relax the reliance on Gaussian noise perturbations. Experimental results across image synthesis, financial time series generation, and empirical Bayes estimation confirm the practical utility and flexibility of these non-Gaussian diffusion frameworks.

## Key Contributions

- Generalizes Tweedie's formula for denoising score matching to non-Gaussian diffusion processes, specifically GBM, BESQ, and CIR processes.
- Provides novel denoising score-matching objectives derived from state-dependent diffusion coefficients, enabling flexible noise modeling beyond standard Gaussian assumptions.
- Demonstrates the effectiveness of non-Gaussian diffusion models on image generation, financial time series forecasting, and empirical Bayes estimation tasks.

## Open Questions & Future Work

- [[non-gaussian-diffusion-stability]]

## Key Concepts

- [[non-gaussian-diffusion-processes]]: A framework for diffusion generative models using state-dependent diffusion coefficients and generalized Tweedie's formulae instead of standard Gaussian perturbations.

## Archivist Review

I approved 'Non-Gaussian Diffusion Processes' as the core methodological contribution of the paper, as it formalizes the extension of Tweedie's formula to state-dependent diffusion. I also approved 'Non-Gaussian Diffusion Stability' as an open question, as it identifies the critical bottleneck preventing the scaling of these models. Other generic terms were rejected to keep the vault focused on distinct research advances.

### Approved Concepts
- Non-Gaussian Diffusion Processes: This is the core theoretical contribution, providing a formal bridge between classical stochastic calculus and modern score-based generative modeling for non-Gaussian regimes.

### Approved Open Questions
- Non-Gaussian Diffusion Stability: Numerical instability is the primary barrier to the widespread adoption of non-Gaussian diffusion models in practical applications like financial modeling and generative tasks on constrained manifolds.

## Links

- [Abstract](https://arxiv.org/abs/2605.19391)
- [PDF](https://arxiv.org/pdf/2605.19391)

