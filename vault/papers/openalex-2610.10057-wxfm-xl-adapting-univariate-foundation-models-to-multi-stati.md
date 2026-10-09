---
# CSL-compatible fields
title: "WxFM-XL: Adapting Univariate Foundation Models to Multi-Station Weather Forecasting"
author:
  - literal: "Xiao Wang"
  - literal: "Changjian Chen"
  - literal: "Zhuo Tang"
  - literal: "Rongwen Li"
  - literal: "Hongwu Liu"
  - literal: "Kenli Li"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10057"

# Custom fields
paper_id: "2610.10057"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "foundation-model"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "wxfm-xl"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:34:25Z"
created_at: "2026-10-09T11:34:25Z"
---

# WxFM-XL: Adapting Univariate Foundation Models to Multi-Station Weather Forecasting

**Authors**: Xiao Wang, Changjian Chen, Zhuo Tang, Rongwen Li, Hongwu Liu, Kenli Li
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10057](https://arxiv.org/abs/2610.10057)

## Summary

This paper introduces WxFM-XL, a framework for adapting univariate time series foundation models to multi-station weather forecasting by explicitly modeling spatial information and station-specific error priors. WxFM-XL constructs a cross-station error correlation prior graph to capture error distributions relative to the foundation model, and employs a dynamic fusion mechanism to combine it with a spatial correlation graph. Extensive experiments across multiple benchmarks demonstrate that WxFM-XL outperforms existing state-of-the-art multivariate and foundation model adaptation baselines.

## Key Contributions

- Proposes WxFM-XL to adapt univariate time series foundation models for multi-station weather forecasting.
- Introduces a cross-station error correlation prior graph to capture stationwise error priors relative to the foundation model.
- Develops a dynamic fusion mechanism that adaptively integrates a spatial correlation graph with the error correlation prior graph.
- Demonstrates superior performance over state-of-the-art baselines across multiple weather forecasting datasets.

## Open Questions & Future Work

- [[joint-multivariate-multistation-weather-forecasting]]

## Key Concepts

- [[wxfm-xl]]: A model for adapting univariate time series foundation models to multi-station weather forecasting via cross-station error correlation and dynamic spatial fusion.

## Archivist Review

Approved WxFM-XL as a representative architecture for adapting univariate foundation models via error correlation priors and dynamic fusion. Also approved an open question regarding joint multivariate and multi-station forecasting. No standalone datasets were provided.

### Approved Concepts
- WxFM-XL: Central novel model proposed for adapting univariate time series foundation models to multi-station weather forecasting.

### Approved Open Questions
- Joint Multivariate and Multi-Station Forecasting: Extending station-level spatio-temporal adaptation to fully joint multivariate-station modeling represents an important architectural scaling step for weather forecasting foundation models.

## Links

- [Abstract](https://arxiv.org/abs/2610.10057)
- [PDF](https://arxiv.org/pdf/2610.10057)

