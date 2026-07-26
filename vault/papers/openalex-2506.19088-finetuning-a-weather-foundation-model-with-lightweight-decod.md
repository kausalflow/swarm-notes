---
# CSL-compatible fields
title: "Fine‐Tuning a Weather Foundation Model With Lightweight Decoders for Unseen Physical Processes"
author:
  - literal: "Fanny Lehmann"
  - literal: "Fırat Özdemir"
  - literal: "Benedikt Soja"
  - literal: "Torsten Hoefler"
  - literal: "Siddhartha Mishra"
  - literal: "Sebastian Schemm"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2506.19088"

# Custom fields
paper_id: "2506.19088"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "pre-training"
  - "fine-tuning"
  - "autoregressive"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:29:44Z"
created_at: "2026-07-26T07:29:44Z"
---

# Fine‐Tuning a Weather Foundation Model With Lightweight Decoders for Unseen Physical Processes

**Authors**: Fanny Lehmann, Fırat Özdemir, Benedikt Soja, Torsten Hoefler, Siddhartha Mishra, Sebastian Schemm
**Date**: 2026-07-23
**Paper ID**: [openalex:2506.19088](https://arxiv.org/abs/2506.19088)

## Summary

This study investigates how to adapt the state-of-the-art Aurora weather foundation model to predict unseen hydrological variables without full fine-tuning. By training lightweight shallow decoders on the model's latent representations, the approach achieves strong predictive accuracy while reducing training time by 43% and memory by 53% compared to full fine-tuning. Furthermore, the results demonstrate that Aurora's latent space encodes meaningful physical relationships, as decoder performance correlates directly with the underlying physical correlation to pretrained variables.

## Key Contributions

- Evaluates the Aurora weather foundation model on predicting unseen hydrological variables not included during pretraining.
- Introduces a lightweight approach using shallow decoders trained on frozen latent representations to predict new physical variables.
- Demonstrates that the decoder-based approach requires 43% less training time and 53% less memory than full fine-tuning while preserving autoregressive stability.
- Shows that decoder accuracy correlates with physical relationships in the foundation model's latent space, outperforming UNet, climatology, and persistence baselines.

## Limitations

Decoder accuracy is dependent on the physical correlation between the newly introduced variables and those encountered during original pretraining.

## Archivist Review

No novel reusable methodology concepts identified that warrant permanent vault notes beyond standard ML techniques.

## Links

- [Abstract](https://arxiv.org/abs/2506.19088)
- [PDF](https://arxiv.org/pdf/2506.19088)

