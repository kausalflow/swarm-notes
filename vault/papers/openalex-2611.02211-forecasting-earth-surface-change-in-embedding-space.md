---
# CSL-compatible fields
title: "Forecasting Earth Surface Change in Embedding Space"
author:
  - literal: "Jingtao Li"
  - literal: "Sadiq Jaffer"
  - literal: "Anil Madhavapeddy"
  - literal: "Pedro Sousa"
  - literal: "Anthony Ortiz"
  - literal: "Kyle Gao"
  - literal: "Zhengpeng Feng"
  - literal: "Yanfei Zhong"
  - literal: "Kevin White"
  - literal: "Srinivasan Keshav"
issued:
  date-parts:
    - [2026, 11, 1]
url: "https://arxiv.org/abs/2611.02211"

# Custom fields
paper_id: "2611.02211"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "transformer"
  - "multimodal"
  - "forecasting"
  - "anomaly-detection"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:02Z"
created_at: "2026-11-04T12:40:02Z"
---

# Forecasting Earth Surface Change in Embedding Space

**Authors**: Jingtao Li, Sadiq Jaffer, Anil Madhavapeddy, Pedro Sousa, Anthony Ortiz, Kyle Gao, Zhengpeng Feng, Yanfei Zhong, Kevin White, Srinivasan Keshav
**Date**: 2026-11-01
**Paper ID**: [openalex:2611.02211](https://arxiv.org/abs/2611.02211)

## Summary

This paper introduces E^2Forecast, a transformer-based model that forecasts Earth surface changes directly in the embedding space of foundation models rather than raw pixel spectral values. The method utilizes a dual-branch architecture—incorporating a Gaussian branch for point estimates and uncertainties and a rectified-flow branch for ensemble generation—to robustly handle irregular histories and noisy observations. Evaluated on Sentinel-1 and Sentinel-2 benchmarks across nine remote sensing foundation models, E^2Forecast significantly improves forecasting accuracy, reduces model overconfidence, and enhances unsupervised anomaly change detection.

## Key Contributions

- Proposes E^2Forecast, a transformer-based forecaster operating in the embedding space of Earth foundation models rather than raw pixel spectral values to circumvent cloud, shadow, and sensor noise issues.
- Implements a dual-branch architecture combining a Gaussian branch for direct mean and variance point forecasting and a rectified-flow branch for generative forecast ensembles.
- Achieves substantial performance gains on Sentinel-1 and Sentinel-2 benchmarks, halving the cosine distance from 0.20 to 0.10 and reducing z-score standard deviation from 2.63 to 1.22.
- Enables label-free anomaly change detection by comparing new observations with forecasts, increasing F_1 score from 41.58 to 48.70 on a global benchmark.

## Open Questions & Future Work

- [[modeling-cross-dimensional-correlations-in-embedding-forecasting]]
- [[incorporating-earth-system-drivers-in-forecasting]]

## Archivist Review

The paper proposes a novel framework for forecasting Earth surface changes in foundation model embedding space rather than pixel space. The core concept represents an application-specific architecture (E2Forecast with a Gaussian and rectified-flow dual branch) which is highly paper-local, so no concept notes were approved. However, the open questions regarding full covariance modeling in high-dimensional embedding spaces and incorporating external Earth system drivers address foundational challenges in temporal modeling and were approved. No distinct new datasets qualify for standalone vault notes.

### Approved Open Questions
- Modeling Cross-Dimensional Correlations: Accounting for full dimensional covariances is crucial for accurate uncertainty estimation and realistic high-dimensional probabilistic forecasting.
- Incorporating Earth System Drivers: Integrating physical environmental drivers is essential for moving from purely statistical time series extrapolation to physically grounded Earth forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2611.02211)
- [PDF](https://arxiv.org/pdf/2611.02211)

