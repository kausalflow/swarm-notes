---
# CSL-compatible fields
title: "DPAnet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting"
author:
  - literal: "Qianyang Li"
  - literal: "Xingjun Zhang"
  - literal: "Shaoxun Wang"
  - literal: "Jia Wei"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.14868"

# Custom fields
paper_id: "2509.14868"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "multi-head-attention"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dpanet-dual-pyramid-attention-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:58:19Z"
created_at: "2026-04-24T06:58:19Z"
---

# DPAnet: Dual Pyramid Attention Network for Multivariate Time Series Forecasting

**Authors**: Qianyang Li, Xingjun Zhang, Shaoxun Wang, Jia Wei
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.14868](https://arxiv.org/abs/2509.14868)

## Summary

DPANet is a novel architecture designed for long-term multivariate time series forecasting by explicitly decoupling and concurrently modeling temporal and frequency domain dependencies. The model utilizes two parallel pyramids: a Temporal Pyramid based on progressive downsampling and a Frequency Pyramid based on band-pass filtering. These pyramids are integrated through a Cross-Pyramid Fusion Block, which uses cross-attention to facilitate coarse-to-fine information exchange for improved representation learning. The approach demonstrates state-of-the-art results across standard forecasting benchmarks.

## Key Contributions

- Proposes DPANet, a novel architecture that decouples and concurrently models temporal multi-scale dynamics and spectral multi-resolution periodicities.
- Introduces the Cross-Pyramid Fusion Block to facilitate coarse-to-fine hierarchical interactive information exchange via cross-attention.
- Achieves state-of-the-art performance on public long-term time series forecasting benchmarks compared to existing Transformer and MLP-based models.

## Open Questions & Future Work

- [[adaptive-hierarchical-decomposition]]

## Key Concepts

- [[dpanet-dual-pyramid-attention-network]]: A dual-pyramid neural network architecture for long-term multivariate time series forecasting that decouples and concurrently models multi-scale temporal dynamics and spectral periodicities.

## Archivist Review

Approved the core architecture, as its approach to combining multi-scale temporal modeling with multi-resolution spectral filtering is a notable trend in time-series forecasting. Also approved the open question regarding adaptive decomposition, as it addresses a fundamental limitation in existing fixed-transform architectural designs for time-series. Applied a strict filtering policy to exclude internal helper modules and generic benchmarks.

### Approved Concepts
- Dual Pyramid Attention Network (DPANet): The model introduces a dual-pyramid structure to handle both temporal and frequency domains simultaneously, which is the core innovation of the paper.

### Approved Open Questions
- Adaptive Hierarchical Time-Frequency Decomposition: Fixed decomposition approaches may fail to capture irregular or evolving periodicities present in non-stationary time series, limiting the model's flexibility and potential performance on diverse datasets.

## Links

- [Abstract](https://arxiv.org/abs/2509.14868)
- [PDF](https://arxiv.org/pdf/2509.14868)

