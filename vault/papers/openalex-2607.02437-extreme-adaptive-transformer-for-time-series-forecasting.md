---
# CSL-compatible fields
title: "Extreme Adaptive Transformer for Time Series Forecasting"
author:
  - literal: "S. Shrestha"
  - literal: "Hui Liu"
  - literal: "Yifan Zhang"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.02437"

# Custom fields
paper_id: "2607.02437"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "extreme-adaptive-transformer-exformer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:51:28Z"
created_at: "2026-07-05T07:51:28Z"
---

# Extreme Adaptive Transformer for Time Series Forecasting

**Authors**: S. Shrestha, Hui Liu, Yifan Zhang
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.02437](https://arxiv.org/abs/2607.02437)

## Summary

The Extreme-Adaptive Transformer (Exformer) addresses the challenge of forecasting rare, critical extreme events in skewed time series, such as hydrologic streamflow. Standard Transformer models often neglect these patterns by treating all time points uniformly, leading to poor performance during extreme peaks. Exformer incorporates a novel attention mechanism consisting of Local, Stride, and Extreme components, which selectively model short-term, periodic, and extreme dependencies. The framework significantly outperforms state-of-the-art forecasting models across four streamflow datasets by explicitly focusing on event-aware relationships.

## Key Contributions

- Introduces the Extreme-Adaptive Transformer (Exformer), which decomposes attention into Local, Stride, and Extreme components to explicitly model rare event dependencies.
- Demonstrates improved 3-day forecasting accuracy on four real-world hydrologic streamflow datasets compared to state-of-the-art baselines.
- Provides a mechanism for Transformer-based models to handle highly skewed, imbalanced time series data without treating all time points uniformly.

## Open Questions & Future Work

- [[adaptive-extreme-event-thresholding]]

## Key Concepts

- [[extreme-adaptive-transformer-exformer]]: A transformer-based forecasting framework featuring a three-component sparse attention mechanism (Local, Stride, and Extreme) to model dependencies for rare extreme events.

## Archivist Review

I approved the Extreme-Adaptive Transformer (Exformer) as a distinct modular attention mechanism for imbalanced forecasting, and the open question regarding adaptive thresholding, as it identifies a clear bottleneck in event-aware sequence modeling. I applied a strict filter to reject sub-components (Local/Stride attention) as they are standard sparse attention patterns already represented by the broader Exformer concept. No new datasets were approved as the hydrologic datasets used were generic or not provided in a specific, named, and reusable format.

### Approved Concepts
- Extreme-Adaptive Transformer (Exformer): The paper's core novelty is a specialized attention mechanism for imbalanced time series forecasting that separates attention into local, stride, and extreme components to prevent the underrepresentation of rare events.

### Approved Open Questions
- Adaptive extreme event thresholding: Current methods rely on pre-determined thresholds to classify extremes, which limits robustness in real-world scenarios where extreme events are non-stationary and thresholds are difficult to define. Improving the adaptability of extreme-aware attention is essential for generalizable, mission-critical forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2607.02437)
- [PDF](https://arxiv.org/pdf/2607.02437)

