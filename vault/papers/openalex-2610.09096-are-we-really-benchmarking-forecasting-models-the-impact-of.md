---
# CSL-compatible fields
title: "Are We Really Benchmarking Forecasting Models? The Impact of Preprocessing on Time Series Performance"
author:
  - literal: "Guilherme Afonso Galindo Padilha"
  - literal: "Paulo S. G. de Mattos Neto"
  - literal: "Rafael M. O. Cruz"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.09096"

# Custom fields
paper_id: "2610.09096"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:33:47Z"
created_at: "2026-10-09T11:33:47Z"
---

# Are We Really Benchmarking Forecasting Models? The Impact of Preprocessing on Time Series Performance

**Authors**: Guilherme Afonso Galindo Padilha, Paulo S. G. de Mattos Neto, Rafael M. O. Cruz
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.09096](https://arxiv.org/abs/2610.09096)

## Summary

This paper investigates the structural preprocessing bias in modern time series forecasting benchmarks, where simple scaling is used while critical transformations like differencing are overlooked. Through a comprehensive evaluation of 11 forecasting models across 16 reversible preprocessing pipelines on 29,000 M4 time series, the authors show that optimizing preprocessing per series yields 27% to 87% performance gains. This allows simpler architectures to rival complex state-of-the-art models, revealing preprocessing as a primary driver of forecasting performance.

## Key Contributions

- Identifies a structural preprocessing bias in modern forecasting benchmarks due to the omission of critical transformations like differencing
- Evaluates 11 forecasting models across 16 reversible preprocessing pipelines on 29,000 M4 time series
- Demonstrates that series-specific preprocessing optimization yields 27% to 87% performance gains, making simpler architectures competitive with complex state-of-the-art models

## Open Questions & Future Work

- [[multivariate-and-long-term-preprocessing-benchmarks]]

## Archivist Review

In accordance with the strict filtering policy, no new architectural concepts or standard benchmark datasets were approved, as the paper's primary contribution is an empirical investigation of structural preprocessing bias. However, the open question regarding the extension of preprocessing-aware benchmarks to multivariate and long-term settings was approved as it targets an important methodological limitation across time series forecasting.

### Approved Open Questions
- Multivariate and Long-Term Preprocessing Benchmarks: Crucial for understanding if findings on univariate benchmarks generalize to complex multivariate real-world settings where cross-series dynamics interact with preprocessing.

## Links

- [Abstract](https://arxiv.org/abs/2610.09096)
- [PDF](https://arxiv.org/pdf/2610.09096)

