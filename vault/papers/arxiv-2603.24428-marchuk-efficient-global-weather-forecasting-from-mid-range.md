---
# CSL-compatible fields
title: "Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching"
author:
  - literal: "Arsen Kuzhamuratov"
  - literal: "Mikhail Zhirnov"
  - literal: "Andrey Kuznetsov"
  - literal: "Ivan Oseledets"
  - literal: "Konstantin Sobolev"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24428"

# Custom fields
paper_id: "2603.24428"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "autoregressive"
  - "llm"
  - "positional-encoding"
  - "emergent-abilities"
architectures:
  - "decoder-only"
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-26T07:10:59Z"
created_at: "2026-03-26T07:10:59Z"
---

# Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching

**Authors**: Arsen Kuzhamuratov, Mikhail Zhirnov, Andrey Kuznetsov, Ivan Oseledets, Konstantin Sobolev
**Date**: 2026-03-25
**Paper ID**: [arxiv:2603.24428](https://arxiv.org/abs/2603.24428)

## Summary

The paper introduces Marchuk, a novel generative latent flow-matching model specifically engineered for global weather forecasting across the challenging mid-range (up to 15 days) to subseasonal (up to 30 days) horizons. Marchuk operates autoregressively within a learned latent space, conditioning on current weather maps to predict future states, and utilizes trainable positional embeddings instead of RoPE to better capture long-range temporal dynamics. The model demonstrates strong predictive performance competitive with significantly larger models like LaDCast, achieving this efficiency with only 276 million parameters. This combination of extended temporal reach and high computational efficiency marks a significant advancement in global weather prediction models.

## Key Contributions

- Introduction of Marchuk, a generative latent flow-matching model capable of global weather forecasting up to a 30-day horizon, effectively addressing subseasonal prediction challenges.
- Demonstration of high computational efficiency, achieving performance comparable to the much larger LaDCast (276M vs 1.6B parameters) while maintaining faster inference.
- Enhancement of temporal dependency modeling by replacing Rotary Positional Embeddings (RoPE) with trainable positional embeddings and extending the context window.
- Autoregressive prediction of subsequent days' weather maps within a compact, learned latent space conditioned on the current-day state.

## Limitations

The abstract does not explicitly detail limitations, but a generative model's reliance on learned latent space could imply potential issues with extreme or unseen atmospheric conditions.

## Open Questions & Future Work

- [[model-skill-limitations-latent-compression-resolution]]
- [[operational-deployment-data-assimilation]]
- [[physics-informed-loss-functions]]
- [[assimilate-live-observations]]

## Key Concepts

- [Marchuk Model](../concepts/marchuk-weather-forecasting.md): A generative latent flow-matching model designed for global weather forecasting spanning mid-range to subseasonal timescales.

## Limitations

The abstract does not explicitly detail limitations, but a generative model's reliance on learned latent space could imply potential issues with extreme or unseen atmospheric conditions.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.24428)
- [PDF](https://arxiv.org/pdf/2603.24428)

