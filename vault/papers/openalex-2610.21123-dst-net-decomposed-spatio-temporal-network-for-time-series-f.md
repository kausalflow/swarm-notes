---
# CSL-compatible fields
title: "DST-Net: Decomposed Spatio-Temporal Network for Time Series Forecasting"
author:
  - literal: "Yaohua Zha"
  - literal: "Wu Hai"
  - literal: "Shu‐Tao Xia"
  - literal: "DST-Net: Decomposed Spatio-Temporal Network for Time Series Forecasting"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21123"

# Custom fields
paper_id: "2610.21123"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "graph-neural-network"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:12:29Z"
created_at: "2026-10-18T09:12:29Z"
---

# DST-Net: Decomposed Spatio-Temporal Network for Time Series Forecasting

**Authors**: Yaohua Zha, Wu Hai, Shu‐Tao Xia, DST-Net: Decomposed Spatio-Temporal Network for Time Series Forecasting
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21123](https://arxiv.org/abs/2610.21123)

## Summary

The paper proposes DST-Net, a decomposed spatio-temporal network for time series forecasting that addresses the limitations of homogeneous modeling across different sequence components. DST-Net decouples the trend component—which exhibits dominant spatial coupling and temporal redundancy—using a Latent Graph Block to capture global topological dependencies. Meanwhile, it handles the seasonal component—which features local temporal evolution but is prone to attention distraction—using a Gaussian Multi-scale Attention mechanism with learnable Gaussian priors. Extensive experiments on real-world benchmarks demonstrate the effectiveness of this component-tailored disentangled architecture.

## Key Contributions

- Proposes DST-Net, a decomposed spatio-temporal network that applies heterogeneous modeling strategies tailored to trend and seasonal components in time series forecasting.
- Introduces a Latent Graph Block for the trend branch to capture global topological dependencies and system-wide co-movements across channels.
- Introduces a Gaussian Multi-scale Attention mechanism for the seasonal branch to impose structural constraints via learnable Gaussian priors, mitigating attention distraction and filtering global noise.

## Links

- [Abstract](https://arxiv.org/abs/2610.21123)
- [PDF](https://arxiv.org/pdf/2610.21123)

