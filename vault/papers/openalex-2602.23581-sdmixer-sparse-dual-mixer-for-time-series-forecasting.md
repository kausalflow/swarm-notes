---
# CSL-compatible fields
title: "SDMixer: Sparse Dual-Mixer for Time Series Forecasting"
author:
  - literal: "Xiang Ao"
issued:
  date-parts:
    - [2026, 2, 27]
url: "https://arxiv.org/abs/2602.23581"

# Custom fields
paper_id: "2602.23581"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "efficient-transformer"
architectures:
  []
datasets:
  - "ETTh1"
  - "Traffic"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:43Z"
created_at: "2026-03-27T14:08:43Z"
---

# SDMixer: Sparse Dual-Mixer for Time Series Forecasting

**Authors**: Xiang Ao
**Date**: 2026-02-27
**Paper ID**: [openalex:2602.23581](https://arxiv.org/abs/2602.23581)

## Summary

The SDMixer model addresses challenges in multivariate time series forecasting, such as multi-scale characteristics and weak correlations, by employing a dual-stream framework. One stream operates in the frequency domain to capture global trends, while the other operates in the time domain to capture local dynamic features. A core component is a sparsity mechanism designed to aggressively filter noise and invalid information, thereby strengthening the accurate modeling of cross-variable dependencies. Experimental validation across several real-world datasets demonstrates that SDMixer sets a new state-of-the-art performance level.

## Key Contributions

- Proposed the Sparse Dual-Mixer (SDMixer) framework, featuring dual streams for frequency and time domain feature extraction.
- Introduced a sparsity mechanism within the Mixer architecture to filter invalid information and enhance cross-variable dependency modeling.
- Achieved leading performance compared to existing models on multiple real-world time series forecasting benchmarks.

## Limitations

The paper does not explicitly detail limitations, but a potential area for future work is investigating the optimal sparsity level determination.

## Open Questions & Future Work

- [[dynamic-sparsity-in-time-frequency-decoupling]]

## Datasets

- [ETTh1](../datasets/etth1.md)
- [Traffic](../datasets/traffic.md)

## Limitations

The paper does not explicitly detail limitations, but a potential area for future work is investigating the optimal sparsity level determination.

## Links

- [Abstract](https://arxiv.org/abs/2602.23581)
- [PDF](https://arxiv.org/pdf/2602.23581)

