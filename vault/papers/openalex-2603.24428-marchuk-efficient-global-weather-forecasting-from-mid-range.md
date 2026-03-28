---
# CSL-compatible fields
title: "Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching"
author:
  - literal: "A. Kuzhamuratov"
  - literal: "Mikhail Zhirnov"
  - literal: "A. V. Kuznetsov"
  - literal: "Ivan Oseledets"
  - literal: "Konstantin Sobolev"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24428"

# Custom fields
paper_id: "2603.24428"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "state-space-model"
  - "flow-matching"
  - "long-context"
  - "positional-encoding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "marchuk-weather-forecasting"
  - "generative-latent-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:16Z"
created_at: "2026-03-28T05:29:16Z"
---

# Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching

**Authors**: A. Kuzhamuratov, Mikhail Zhirnov, A. V. Kuznetsov, Ivan Oseledets, Konstantin Sobolev
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24428](https://arxiv.org/abs/2603.24428)

## Summary

The paper introduces Marchuk, a novel generative latent flow-matching model for global weather forecasting that targets medium-range (15-day) up to sub-seasonal (30-day) horizons. Marchuk operates by autoregressively predicting subsequent weather maps within a compact learned latent space, conditioned on the current day's conditions. The architecture employs trainable positional embeddings instead of RoPE and an extended temporal context window to improve the modeling of long-range dependencies. Despite having only 276 million parameters, Marchuk achieves performance parity with the 1.6 billion parameter LaDCast model while being significantly faster during inference.

## Key Contributions

- Introduced Marchuk, a generative latent flow-matching model capable of accurate global weather forecasting up to 30-day horizons (sub-seasonal scales).
- Achieved performance comparable to the significantly larger LaDCast model (276M vs 1.6B parameters) while offering substantially higher inference speeds due to architectural efficiency.
- Replaced Rotary Positional Embeddings (RoPE) with trainable positional embeddings and extended the temporal context window to better capture long-range atmospheric dependencies.
- The model conditions on current-day weather maps and autoregressively predicts subsequent maps within a learned latent space.

## Limitations

The abstract does not explicitly state limitations, but the inherent chaotic nature of the atmosphere still imposes a hard limit on predictive skill beyond the sub-seasonal range.

## Key Concepts

- [[marchuk-weather-forecasting]]: A generative latent flow-matching model designed for global weather forecasting across mid-range to sub-seasonal timescales.
- [[generative-latent-flow-matching]]: A generative modeling technique that uses continuous normalizing flows guided by a learned trajectory between data distributions for forecasting.

## Archivist Review

Approved two core concepts: the novel model architecture 'Marchuk' itself, and the underlying methodology 'Generative Latent Flow Matching' it employs. These are central to the paper's contribution to sub-seasonal weather forecasting. Rejected architectural tweaks like replacing RoPE or extending context windows as they are common model engineering practices, not novel, reusable mechanisms.

### Approved Concepts
- Marchuk: Marchuk is the proposed novel generative model architecture specifically designed for medium to sub-seasonal weather forecasting.
- Generative Latent Flow Matching: It is the core methodology for building the generative forecasting model, combining flow matching with a latent predictive structure.

### Rejected Candidates
- [concept] Trainable Positional Embeddings over RoPE (`trainable-positional-embeddings`) - subcomponent_of_broader_mechanism: While an architectural choice, it is a common component replacement rather than a central novel concept for a vault entry.
- [concept] Temporal Context Window Extension (`long-range-temporal-dependency-enhancement`) - not_novel: This is a standard technique for improving long-context modeling, not a novel contribution warranting its own entry separate from the overall model.

## Links

- [Abstract](https://arxiv.org/abs/2603.24428)
- [PDF](https://arxiv.org/pdf/2603.24428)

