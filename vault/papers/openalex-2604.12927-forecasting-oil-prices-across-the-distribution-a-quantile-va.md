---
# CSL-compatible fields
title: "Forecasting Oil Prices Across the Distribution: A Quantile VAR Approach"
author:
  - literal: "Hilde C. Bjornland"
  - literal: "Nicolás Hardy"
  - literal: "Dimitris Korobilis"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12927"

# Custom fields
paper_id: "2604.12927"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:10Z"
created_at: "2026-04-17T06:29:10Z"
---

# Forecasting Oil Prices Across the Distribution: A Quantile VAR Approach

**Authors**: Hilde C. Bjornland, Nicolás Hardy, Dimitris Korobilis
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12927](https://arxiv.org/abs/2604.12927)

## Summary

This paper introduces a Quantile Bayesian Vector Autoregression (QBVAR) framework to improve oil price forecasting by capturing asymmetric predictor effects across the conditional distribution. By relaxing the assumptions of standard mean-focused models, the approach provides significant gains in point prediction accuracy and superior tail-risk assessment. Empirical results on monthly oil price data spanning 1975 to 2025 demonstrate the model's effectiveness in predicting downside risks during economic crises, although upside risk remains better captured by traditional stochastic volatility models.

## Key Contributions

- Develops a Quantile Bayesian Vector Autoregression (QBVAR) to model conditional distributions of oil prices, allowing predictor effects to vary across quantiles.
- Demonstrates that QBVAR improves median oil price point forecasts by 2-5% compared to standard Bayesian VARs.
- Shows that modeling left-tail (downside) risk with financial condition variables yields 10-25% forecast improvements during crisis episodes.

## Open Questions & Future Work

- [[hybrid-quantile-sv-forecasting]]

## Archivist Review

I approved the open question regarding the hybrid integration of quantile-based models and stochastic volatility because it addresses a fundamental limitation in conditional distribution forecasting for time-series. The proposed model, QBVAR, was rejected as a concept because it represents a specific adaptation of established econometric methods rather than a distinct, reusable architectural innovation. I applied a strict filter to ensure only high-level, research-oriented problems are tracked.

### Approved Open Questions
- Hybrid Quantile-SV Forecasting Frameworks: This addresses the critical bottleneck where quantile VAR models show asymmetric performance, failing to characterize extreme upside price spikes as effectively as downside risk.

### Rejected Candidates
- [concept] Quantile Bayesian Vector Autoregression (QBVAR) (`qbvar`) - not_novel: This is an application-specific extension of existing Bayesian VAR and quantile regression methods, lacking sufficient distinctness as a foundational concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.12927)
- [PDF](https://arxiv.org/pdf/2604.12927)

