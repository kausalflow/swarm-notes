---
# CSL-compatible fields
title: "nufftcf: Fast Auto- and Cross-Correlation Function Estimation for Irregularly-Sampled Time Series via the Non-Uniform FFT"
author:
  - literal: "Jean-Eric Campagne"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03866"

# Custom fields
paper_id: "2609.03866"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nufftcf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-06T09:01:03Z"
created_at: "2026-09-06T09:01:03Z"
---

# nufftcf: Fast Auto- and Cross-Correlation Function Estimation for Irregularly-Sampled Time Series via the Non-Uniform FFT

**Authors**: Jean-Eric Campagne
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03866](https://arxiv.org/abs/2609.03866)

## Summary

The paper presents nufftcf, a fast algorithm for estimating auto- and cross-correlation functions in irregularly-sampled time series by evaluating the Wiener-Khinchin theorem via the Non-Uniform Fast Fourier Transform (NUFFT). By pairing NUFFT with an O(n) two-pointer scan for lag-bin normalization, nufftcf achieves an O(n log n) asymptotic scaling instead of the traditional O(n^2) cost. Validated against established libraries like pastas and pyZDCF, nufftcf provides substantial speedups and low overhead for moderate to long time series across fields such as astronomy and environmental sciences.

## Key Contributions

- Introduces nufftcf, an estimator for auto- and cross-correlation functions of irregularly-sampled time series that scales in O(n log n) time using the Non-Uniform Fast Fourier Transform.
- Replaces the naive O(n^2) pair-count normalization with an O(n) two-pointer scan.
- Demonstrates consistency with established estimators like pastas and pyZDCF, outperforming them on moderate to long series.

## Open Questions & Future Work

- [[uncertainty-quantification-and-scaling-nufft-correlation-estimators]]

## Key Concepts

- [[nufftcf]]: A fast auto- and cross-correlation function estimator for irregularly-sampled time series based on the Non-Uniform Fast Fourier Transform.

## Archivist Review

Approved the core algorithmic concept 'nufftcf' for O(n log n) irregularly-sampled time series correlation estimation via NUFFT, alongside its prominent open question on uncertainty quantification and GPU scalability. No datasets met the strict novelty or standalone requirements.

### Approved Concepts
- nufftcf: It is the core algorithm introduced by the paper to compute auto- and cross-correlation functions for irregularly-sampled time series in O(n log n) time.

### Approved Open Questions
- Uncertainty Quantification and Scaling for NUFFT Correlation Estimators: Uncertainty quantification and scalability to massive irregularly sampled datasets are crucial bottlenecks for adopting Fourier-domain correlation estimators in operational survey pipelines and environmental monitoring.

## Links

- [Abstract](https://arxiv.org/abs/2609.03866)
- [PDF](https://arxiv.org/pdf/2609.03866)

