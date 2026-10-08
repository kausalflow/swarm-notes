---
# CSL-compatible fields
title: "Xaurora: Generative Weather Forecasting with Denoising Stochastic Interpolants from a Foundation Model Prior"
author:
  - literal: "Eliot Walt"
  - literal: "Miltiadis Kofinas"
  - literal: "Mücke Nikolaj"
  - literal: "Efstratios Gavves"
  - literal: "Dim Coumou"
  - literal: "Eliot Walt"
  - literal: "Miltiadis Kofinas"
  - literal: "Mücke Nikolaj"
  - literal: "Efstratios Gavves"
  - literal: "Dim Coumou"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06509"

# Custom fields
paper_id: "2610.06509"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "diffusion-model"
  - "generative-adversarial-network"
  - "uncertainty"
architectures:
  []
datasets:
  []
concept_slugs:
  - "denoising-stochastic-interpolants"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:41:15Z"
created_at: "2026-10-08T11:41:15Z"
---

# Xaurora: Generative Weather Forecasting with Denoising Stochastic Interpolants from a Foundation Model Prior

**Authors**: Eliot Walt, Miltiadis Kofinas, Mücke Nikolaj, Efstratios Gavves, Dim Coumou, Eliot Walt, Miltiadis Kofinas, Mücke Nikolaj, Efstratios Gavves, Dim Coumou
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06509](https://arxiv.org/abs/2610.06509)

## Summary

Xaurora is a generative weather forecasting framework that converts deterministic foundation models (specifically Aurora) into probabilistic ensemble predictors using Denoising Stochastic Interpolants and an SDE rollout replay buffer. By finetuning from a pretrained deterministic prior, Xaurora achieves near state-of-the-art performance on global ensemble metrics while remaining highly parameter and sample efficient, producing skillful 15-day forecasts in just 13 minutes.

## Key Contributions

- Introduces Denoising Stochastic Interpolants combined with an SDE rollout replay buffer to turn deterministic foundation models into generative probabilistic models.
- Develops Xaurora, a stochastic weather foundation model finetuned from the small Aurora model, achieving near state-of-the-art performance on global ensemble metrics.
- Demonstrates high parameter and sample efficiency, generating skillful 15-day probabilistic forecasts in 13 minutes.

## Open Questions & Future Work

- [[overcoming-noise-floor-generative-weather]]

## Key Concepts

- [[denoising-stochastic-interpolants]]: A novel generative method combining denoising stochastic interpolants with a replay buffer for stochastic differential equation rollout to enable probabilistic training.

## Archivist Review

Approved the central methodological contribution of Denoising Stochastic Interpolants and the important open question concerning high-frequency spectral noise floors in generative weather emulation. Kept rejections empty as no additional candidates were proposed.

### Approved Concepts
- Denoising Stochastic Interpolants: Central novel generative method proposed to convert a deterministic foundation model into a stochastic ensemble-prediction model via SDE rollouts.

### Approved Open Questions
- Overcoming Noise Floor in Generative Weather Forecasting: The noise floor is a fundamental limitation shared across modern data-driven and generative weather forecasting models, affecting how well small-scale atmospheric turbulence and mesoscale dynamics are represented in ensemble predictions.

## Links

- [Abstract](https://arxiv.org/abs/2610.06509)
- [PDF](https://arxiv.org/pdf/2610.06509)

