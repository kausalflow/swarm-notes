---
# CSL-compatible fields
title: "Physics-guided spatiotemporal neural models for fuel density prediction"
author:
  - literal: "Tolga Çağlar"
  - literal: "Jaynil Jaiswal"
  - literal: "Saqib Azim"
  - literal: "Yudhir Gala"
  - literal: "Mai Nguyen"
  - literal: "İlkay Altıntaş"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.06999"

# Custom fields
paper_id: "2607.06999"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "physics-informed-neural-networks"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:06:05Z"
created_at: "2026-07-11T07:06:05Z"
---

# Physics-guided spatiotemporal neural models for fuel density prediction

**Authors**: Tolga Çağlar, Jaynil Jaiswal, Saqib Azim, Yudhir Gala, Mai Nguyen, İlkay Altıntaş
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.06999](https://arxiv.org/abs/2607.06999)

## Summary

This paper introduces a physics-guided machine learning framework to improve the prediction of spatiotemporal fuel density evolution for fire management. By incorporating differentiable, mass-conserving fuel transport terms and rate-of-spread constraints into the loss functions of ConvLSTM, AFNONet, and ViViT models, the approach ensures physically plausible forecasts. The framework significantly enhances model stability and predictive accuracy compared to standard data-driven baselines, providing an effective tool for prescribed burn management.

## Key Contributions

- Introduces a physics-guided machine learning (PGML) framework for fuel density forecasting, integrating mass-conserving transport constraints.
- Enhances ConvLSTM, AFNONet, and ViViT architectures with differentiable physics-informed loss terms for improved model stability.
- Demonstrates that the proposed PGML approach consistently outperforms purely data-driven baselines in both forecasting accuracy and physical consistency.

## Open Questions & Future Work

- [[generalization-of-physics-guided-wildfire-models]]

## Archivist Review

I have approved the open question regarding the generalization of physics-guided wildfire models, as it addresses a core limitation in translating physics-informed machine learning to complex, real-world environments. No new concepts or datasets were approved as the paper applies existing physics-informed neural network techniques to a specific domain without introducing novel, reusable methodological innovations.

### Approved Open Questions
- Generalization of PGML Wildfire Models: Validating these models on diverse landscapes is critical for transitioning from simulated environments to practical, real-world fire management applications where constraints may interact differently with environmental complexity.

## Links

- [Abstract](https://arxiv.org/abs/2607.06999)
- [PDF](https://arxiv.org/pdf/2607.06999)

