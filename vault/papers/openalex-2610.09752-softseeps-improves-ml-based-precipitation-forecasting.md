---
# CSL-compatible fields
title: "SoftSEEPS improves ML-based precipitation forecasting"
author:
  - literal: "Jost Arndt"
  - literal: "Utku Isil"
  - literal: "Noelia Otero"
  - literal: "Rodrigo Almeida"
  - literal: "Wojciech Samek"
  - literal: "Jackie Ma"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.09752"

# Custom fields
paper_id: "2610.09752"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "softseeps"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:05Z"
created_at: "2026-10-09T11:35:05Z"
---

# SoftSEEPS improves ML-based precipitation forecasting

**Authors**: Jost Arndt, Utku Isil, Noelia Otero, Rodrigo Almeida, Wojciech Samek, Jackie Ma
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.09752](https://arxiv.org/abs/2610.09752)

## Summary

The authors propose SoftSEEPS, a differentiable approximation of the standard SEEPS meteorological score that enables gradient-based optimization of machine learning models for precipitation forecasting. By combining SoftSEEPS with RMSE in a joint training objective, a decoder trained on the latent space of a pre-trained low-resolution forecasting model achieves effective precipitation forecasting on the IMERG dataset with minimal metric trade-offs.

## Key Contributions

- Developed SoftSEEPS, a differentiable approximation of the standard SEEPS meteorological score for precipitation forecasting.
- Enabled direct end-to-end training of machine learning models to optimize precipitation skill scores.
- Demonstrated precipitation forecasting by training a decoder on the latent space of a pre-trained low-resolution forecasting model using the IMERG dataset.
- Showed that SoftSEEPS can be combined with RMSE in a joint objective with marginal trade-offs in performance metrics.

## Key Concepts

- [[softseeps]]: A differentiable approximation of the SEEPS score designed for training machine learning models on precipitation forecasting.

## Archivist Review

Approved the core methodological concept 'SoftSEEPS' as a reusable differentiable loss function for precipitation forecasting. Rejected the open question as routine scaling future work, and omitted the IMERG dataset since it is a standard pre-existing geospatial satellite product rather than a novel benchmark.

### Approved Concepts
- SoftSEEPS: It introduces a differentiable relaxation of the SEEPS meteorological score, enabling direct end-to-end optimization of machine learning models for precipitation forecasting.

### Rejected Candidates
- [open_question] Scaling SoftSEEPS in Large Weather Models (`scaling-softseeps-large-models`) - low_impact: Too close to routine scaling future work rather than an unresolved theoretical or algorithmic mechanism bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.09752)
- [PDF](https://arxiv.org/pdf/2610.09752)

