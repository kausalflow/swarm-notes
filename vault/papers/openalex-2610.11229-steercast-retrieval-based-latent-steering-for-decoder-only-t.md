---
# CSL-compatible fields
title: "SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting"
author:
  - literal: "Van Dai Do"
  - literal: "Huu Giang Nguyen"
  - literal: "Minh Hoang Nguyen"
  - literal: "Hung Le"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11229"

# Custom fields
paper_id: "2610.11229"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "autoregressive"
  - "long-context"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:51:51Z"
created_at: "2026-10-10T10:51:51Z"
---

# SteerCast: Retrieval-Based Latent Steering for Decoder-Only Time Series Forecasting

**Authors**: Van Dai Do, Huu Giang Nguyen, Minh Hoang Nguyen, Hung Le
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11229](https://arxiv.org/abs/2610.11229)

## Summary

SteerCast is a retrieval-based latent steering method designed to improve decoder-only time series forecasters at inference time without requiring model parameter updates. It builds a database of historical representations and corresponding steering vectors—computed as the difference between ground-truth and predicted representations—from the training set. During autoregressive generation, it retrieves nearest neighbors for a query history and injects their aggregated steering vectors into the model's hidden states, guiding predictions toward reliable trajectories. Experiments across diverse multivariate benchmarks and multiple horizons demonstrate that SteerCast outperforms fine-tuned backbones and retrieval baselines.

## Key Contributions

- Proposes SteerCast, a retrieval-based latent steering method for decoder-only time series forecasting that operates entirely at inference time without modifying model parameters.
- Constructs an offline database of training history representations paired with latent steering vectors defined as the difference between ground-truth and predicted continuation states.
- Injects aggregated nearest-neighbor steering vectors into the forecaster's hidden states during autoregressive generation to guide trajectories toward patterns seen in similar training cases.
- Demonstrates consistent improvements in forecasting accuracy across diverse multivariate time series benchmarks and multiple horizons compared to fine-tuned backbones and retrieval-based baselines.

## Open Questions & Future Work

- [[extending-latent-steering-to-encoder-based-forecasters-in-time-series-forecasting]]

## Archivist Review

Approved one open question regarding extending latent steering to encoder-based architectures while keeping rejections scarce and aligned with the strict review policy.

### Approved Open Questions
- Latent Steering for Encoder-Based Forecasters: Extending latent steering beyond decoder-only architectures broadens the applicability of test-time representation interventions to a wider class of time series models.

### Rejected Candidates
- [open_question] Learned Attention Neighbor Aggregation (`learned-attention-neighbor-aggregation-for-retrieval-based-latent-steering`) - low_impact: Proposes a minor extension regarding weighting schemes for nearest neighbors rather than a fundamental unresolved bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.11229)
- [PDF](https://arxiv.org/pdf/2610.11229)

