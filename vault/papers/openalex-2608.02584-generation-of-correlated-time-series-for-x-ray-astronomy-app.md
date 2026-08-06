---
# CSL-compatible fields
title: "Generation of Correlated Time Series for X-ray Astronomy Applications"
author:
  - literal: "S. Larner"
  - literal: "Michael A. Nowak"
  - literal: "Jörn Wilms"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02584"

# Custom fields
paper_id: "2608.02584"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:18Z"
created_at: "2026-08-06T07:31:18Z"
---

# Generation of Correlated Time Series for X-ray Astronomy Applications

**Authors**: S. Larner, Michael A. Nowak, Jörn Wilms
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02584](https://arxiv.org/abs/2608.02584)

## Summary

This paper presents an algorithm for generating pairs of correlated time series with arbitrary power spectra, coherence functions, and phase lag profiles tailored for X-ray astronomy applications. The method decomposes dependent time series into coherent and incoherent components using a complex transfer function applied to a reference series, ensuring precise preservation of target spectral shapes and cross-spectral properties. Additionally, the authors derive approximate analytic expressions for the variance and covariance of coherence and phase lag estimators to enable proper likelihood incorporation during joint model fitting. Evaluation on a two-Lorentzian model demonstrates close alignment between input models and generated time series properties across four decades in frequency.

## Key Contributions

- Presents an algorithm for generating correlated pairs of time series with arbitrary target power spectra, coherence functions, and phase lag profiles.
- Extends existing methods by decomposing the dependent time series into coherent and incoherent components using a complex transfer function applied to a reference series.
- Derives approximate analytic expressions for the variance of coherence and phase lag estimators and their covariance matrix for joint likelihood fitting.
- Demonstrates close agreement between input models and generated power spectra, coherence, and phase lag profiles across four decades in frequency using a two-Lorentzian model.

## Archivist Review

No novel architectural components or distinct reusable algorithmic primitives requiring permanent vault notes were identified. Standard domain-specific simulation technique for X-ray astronomy time series.

## Links

- [Abstract](https://arxiv.org/abs/2608.02584)
- [PDF](https://arxiv.org/pdf/2608.02584)

