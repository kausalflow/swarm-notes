---
# CSL-compatible fields
title: "RankFormer: Rethinking Time Series Transformers through Representation Capacity Analysis and Progressive Decoding"
author:
  - literal: "Peiwang Tang"
  - literal: "Cheng HE"
  - literal: "Xijie Liang"
  - literal: "Defu Lian"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36703"

# Custom fields
paper_id: "2610.36703"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:04:35Z"
created_at: "2026-10-30T11:04:35Z"
---

# RankFormer: Rethinking Time Series Transformers through Representation Capacity Analysis and Progressive Decoding

**Authors**: Peiwang Tang, Cheng HE, Xijie Liang, Defu Lian
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36703](https://arxiv.org/abs/2610.36703)

## Summary

This paper investigates the expressive representation capacity of time series Transformers through a novel rank-based analysis framework and proposes RankFormer, an encoder-decoder architecture for multivariate time series forecasting. The analysis shows that patchification expands potential capacity, which is then managed by downstream encoding structures. Guided by these insights, the authors introduce a rank-enhancing encoder with Hourglass Attention and an Interactive Progressive Decoder (IPD) for progressive, cross-channel trajectory refinement. Extensive experiments validate that RankFormer achieves competitive performance against state-of-the-art baselines on long-term forecasting benchmarks.

## Key Contributions

- Proposes a rank-based analysis framework to investigate the representation capacity of time series Transformers across tokenization, embedding, and attention designs.
- Develops a rank-enhancing encoder with Hourglass Attention to stabilize and maximize representation capacity during temporal and cross-token interaction.
- Introduces the Interactive Progressive Decoder (IPD) to model complex multivariate dynamics via global-guided cross-channel interaction and progressive refinement.
- Demonstrates competitive performance on real-world long-term time series forecasting benchmarks.

## Archivist Review

No novel standalone concepts or critical benchmark dataset names are explicitly specified in the abstract that justify new vault entries.

## Links

- [Abstract](https://arxiv.org/abs/2610.36703)
- [PDF](https://arxiv.org/pdf/2610.36703)

