---
# CSL-compatible fields
title: "KiT: A Foundation Model for Financial Time-Series Forecasting using DiffusionTransformers"
author:
  - literal: "Boyu Zhang"
  - literal: "Haorui Li"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34507"

# Custom fields
paper_id: "2609.34507"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "generative-adversarial-network"
  - "foundation-model"
  - "transformer"
  - "multimodal"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:29Z"
created_at: "2026-09-30T10:48:29Z"
---

# KiT: A Foundation Model for Financial Time-Series Forecasting using DiffusionTransformers

**Authors**: Boyu Zhang, Haorui Li
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34507](https://arxiv.org/abs/2609.34507)

## Summary

The authors propose KiT, a K-line Diffusion Transformer foundation model that reformulates financial candlestick forecasting as conditional path generation using flow matching rather than traditional auto-regressive decoding. Pre-trained on billions of candlestick bars across multiple markets and resolutions, KiT bypasses error accumulation during inference and outperforms existing task-specific financial models and general time-series foundation models, achieving robust performance on return and volatility RankIC metrics.

## Key Contributions

- Introduces KiT, a K-line Diffusion Transformer foundation model that reformulates future candlestick prediction as conditional path generation via flow matching.
- Pre-trained at multiple parameter scales on billions of candlestick bars spanning diverse markets and timescales.
- Achieves a mean return RankIC of 0.057 and a mean volatility RankIC of 0.66 across three markets and seven resolutions, outperforming task-specific financial forecasters and general time-series foundation models.

## Limitations

The abstract does not discuss computational overhead during inference for flow matching generation or handling of extreme black-swan events.

## Archivist Review

Enforced strict scarcity and novelty standards. The proposed concept 'KiT' is the paper-specific name for their particular model architecture, and the open question regarding order book integration represents standard future work. Therefore, no new vault entries are warranted for this paper.

### Rejected Candidates
- [concept] KiT (`kit`) - paper_local: Paper-specific system name and instantiation of existing diffusion/flow-matching architectures rather than a distinct, reusable methodology.
- [open_question] High-Dimensional Order Book Integration (`high-dimensional-order-book-integration`) - low_impact: Standard future work exploring the incorporation of additional data modalities (Level-3 order books) into financial foundation models.

## Links

- [Abstract](https://arxiv.org/abs/2609.34507)
- [PDF](https://arxiv.org/pdf/2609.34507)

