---
# CSL-compatible fields
title: "GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting"
author:
  - literal: "Joseph Ross Ungar Natter"
  - literal: "Long Vu"
  - literal: "Yifan Zhang"
  - literal: "Bobin Deng"
  - literal: "Kun Suo"
  - literal: "Rui Wu"
  - literal: "Kun Suo"
  - literal: "Rui Wu"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37598"

# Custom fields
paper_id: "2610.37598"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "in-context-learning"
  - "graph-neural-network"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:05:17Z"
created_at: "2026-10-30T11:05:17Z"
---

# GAS-PFN: Graph-Aware Spatiotemporal Prior-Data Fitted Networks for Zero-Shot Traffic Forecasting

**Authors**: Joseph Ross Ungar Natter, Long Vu, Yifan Zhang, Bobin Deng, Kun Suo, Rui Wu, Kun Suo, Rui Wu
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37598](https://arxiv.org/abs/2610.37598)

## Summary

The authors propose GAS-PFN, a graph-aware spatiotemporal Prior-Data Fitted Network (PFN) designed for zero-shot traffic forecasting. By incorporating sampled road topology into synthetic task priors through random-walk diffusion and utilizing a dual-pass mask-conditioned Transformer architecture, GAS-PFN effectively captures both sensor-specific temporal dynamics and spatial interactions without requiring parameter updates. Evaluated across six benchmarks at a 90-minute horizon, GAS-PFN outperforms TimePFN and other general-purpose zero-shot forecasters by significant margins in MSE.

## Key Contributions

- Introduces GAS-PFN, a graph-aware spatiotemporal prior-data fitted network for zero-shot traffic forecasting.
- Incorporates sampled road topology into synthetic task priors via random-walk diffusion to learn graph-coupled dynamics during pretraining.
- Employs a co-designed inference architecture with two mask-conditioned passes through a shared Transformer backbone to separately model temporal dynamics and spatiotemporal interactions.
- Achieves a 34.0% average MSE reduction compared to TimePFN across six benchmarks at the 90-minute horizon.

## Links

- [Abstract](https://arxiv.org/abs/2610.37598)
- [PDF](https://arxiv.org/pdf/2610.37598)

