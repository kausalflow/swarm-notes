---
# CSL-compatible fields
title: "Multiple cyclicity and Wavelet Decomposition with Channel Correlation for Long-term Time Series Forecasting"
author:
  - literal: "Bin Wang"
  - literal: "Heming Yang"
  - literal: "Jinfang Sheng"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17996"

# Custom fields
paper_id: "2606.17996"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mcwc-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:09Z"
created_at: "2026-06-19T09:24:09Z"
---

# Multiple cyclicity and Wavelet Decomposition with Channel Correlation for Long-term Time Series Forecasting

**Authors**: Bin Wang, Heming Yang, Jinfang Sheng
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17996](https://arxiv.org/abs/2606.17996)

## Summary

The McWC model is proposed for long-term time series forecasting, addressing the limitations of existing methods in modeling complex inter-channel correlations and computational efficiency. The architecture decouples cyclical, trend, and inter-channel features through a multi-layer cyclicity construction module and an MLP-based correlation extractor. Additionally, a multi-level wavelet decomposition module fuses frequency-aware information, while a frequency-domain loss function explicitly handles intra-channel autocorrelations. Experimental results demonstrate that the approach provides superior predictive accuracy and efficient historical information extraction.

## Key Contributions

- Introduces McWC, a framework that separately models cyclicity, trend, and inter-channel correlations to improve forecasting accuracy.
- Utilizes a multi-level wavelet decomposition module to integrate high-frequency and low-frequency signal information.
- Achieves state-of-the-art performance across six real-world time series datasets while maintaining higher computational efficiency than complex baseline models.

## Open Questions & Future Work

- [[adaptive-periodic-pattern-learning]]

## Key Concepts

- [[mcwc-model]]: A modular time series forecasting framework that separately models cyclicity, trend, and inter-channel correlations via wavelet decomposition and MLP-based routing.

## Archivist Review

I approved the McWC model as a representative architectural approach for multi-component decomposition and the open question regarding adaptive periodicity. Other candidates were not deemed sufficiently novel or central to merit vault entry according to the guidelines.

### Approved Concepts
- McWC Model: The framework proposes a modular decomposition of time series into cyclic, trend, and inter-channel correlation components, which is a significant and reusable architectural pattern.

### Approved Open Questions
- Adaptive Periodic Pattern Learning: Automating the discovery of multiple cyclical periods is critical for scaling long-term forecasting models to real-world datasets where these structures are unknown or dynamic.

## Links

- [Abstract](https://arxiv.org/abs/2606.17996)
- [PDF](https://arxiv.org/pdf/2606.17996)

