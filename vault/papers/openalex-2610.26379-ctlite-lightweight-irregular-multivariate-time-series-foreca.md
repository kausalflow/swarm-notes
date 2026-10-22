---
# CSL-compatible fields
title: "CTLite: Lightweight Irregular Multivariate Time Series Forecasting with Reusable Continuous-Time Summaries"
author:
  - literal: "Shusen Ma"
  - literal: "Xudong Zuo"
  - literal: "Yangchun Xie"
  - literal: "Yun-Bo Zhao"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26379"

# Custom fields
paper_id: "2610.26379"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:14Z"
created_at: "2026-10-22T09:43:14Z"
---

# CTLite: Lightweight Irregular Multivariate Time Series Forecasting with Reusable Continuous-Time Summaries

**Authors**: Shusen Ma, Xudong Zuo, Yangchun Xie, Yun-Bo Zhao
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26379](https://arxiv.org/abs/2610.26379)

## Summary

Irregular multivariate time series forecasting often suffers from redundant computation and tightly coupled historical representations. CTLite addresses this by decoupling historical summarization via a parameter-free continuous-time moment encoder from a compact learned readout mechanism. This design allows historical summaries to be computed once and reused across multiple optimization steps or repeated forecast calls without altering predictions or gradients, significantly improving computational efficiency and reducing latency.

## Key Contributions

- Proposes CTLite, a lightweight irregular multivariate time series forecasting framework that decouples historical summarization from learned prediction.
- Introduces a parameter-free continuous-time moment encoder that summarizes local levels and trends across multiple temporal scales while suppressing poorly supported slope estimates.
- Employs a compact readout with damped local extrapolation and low-rank cross-variable correction accounting for observation freshness, target availability, and forecast horizon.
- Achieves top-tier mean MSE and MAE performance on four real-world benchmarks using only 88-2,537 trainable parameters, while reducing inference latency by 18.6-87.3%.

## Archivist Review

No new concepts or datasets met the strict reusability and explicit naming criteria for standalone archival.

## Links

- [Abstract](https://arxiv.org/abs/2610.26379)
- [PDF](https://arxiv.org/pdf/2610.26379)

