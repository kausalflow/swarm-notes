---
# CSL-compatible fields
title: "Modelling Time Series of Counts with Hysteresis"
author:
  - literal: "Xuanye Ma"
  - literal: "Dong Li"
  - literal: "Howell Tong"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2509.15508"

# Custom fields
paper_id: "2509.15508"
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
  - "hysteretic-poisson-autoregressive-hpart-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:12Z"
created_at: "2026-04-16T06:28:12Z"
---

# Modelling Time Series of Counts with Hysteresis

**Authors**: Xuanye Ma, Dong Li, Howell Tong
**Date**: 2026-04-13
**Paper ID**: [openalex:2509.15508](https://arxiv.org/abs/2509.15508)

## Summary

This paper introduces the Hysteretic Poisson Autoregressive (HPART) model to address the limitations of linear Poisson autoregressive models when capturing complex regime-switching dynamics. Unlike existing approaches, the HPART model explicitly incorporates a controlling factor to model genuine hysteresis, providing deeper insights into underlying temporal dynamics. The authors establish a unified inferential framework for parameter estimation and propose hypothesis tests to discriminate between HPART and the related BPART model, demonstrating superior predictive performance on empirical count datasets.

## Key Contributions

- Introduced the Hysteretic Poisson Autoregressive (HPART) model, a nonlinear extension of linear Poisson autoregressive frameworks that captures genuine hysteresis in count time series.
- Provided a unified theoretical framework for the maximum likelihood estimation and asymptotic properties of both HPART and buffered Poisson autoregressive (BPART) models.
- Developed a statistical test to distinguish between non-nested HPART and BPART models, supported by Monte Carlo simulations and empirical validation on real-world datasets.

## Open Questions & Future Work

- [[intercept-variance-to-mean-ratio-in-count-models]]

## Key Concepts

- [[hysteretic-poisson-autoregressive-hpart-model]]: A nonlinear Poisson autoregressive model incorporating a controlling factor to model hysteretic regime switching in count time series.

## Archivist Review

I have approved the HPART model for its novel approach to explicitly modeling hysteresis in count time series, as this is a reusable conceptual framework for non-linear dynamics. I have also approved the open question regarding the intercept variance-to-mean ratio, as the authors identified it as a consistent, unresolved empirical observation spanning multiple established model classes in time series analysis. No datasets were approved as none were provided in the input.

### Approved Concepts
- Hysteretic Poisson Autoregressive (HPART) Model: It introduces a novel nonlinear extension of Poisson autoregressive models that explicitly accounts for hysteresis effects in count data.

### Approved Open Questions
- Intercept Variance-to-Mean Ratio: Understanding this persistent variance-to-mean ratio issue is crucial for improving the robustness and interpretability of parameter estimation in widely used integer-valued time series models.

## Links

- [Abstract](https://arxiv.org/abs/2509.15508)
- [PDF](https://arxiv.org/pdf/2509.15508)

