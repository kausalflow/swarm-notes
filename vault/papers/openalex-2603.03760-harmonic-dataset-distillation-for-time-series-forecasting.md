---
# CSL-compatible fields
title: "Harmonic Dataset Distillation for Time Series Forecasting"
author:
  - literal: "Seungha Hong"
  - literal: "Sanghwan Jang"
  - literal: "Wonbin Kweon"
  - literal: "Suyeon Kim"
  - literal: "Gyuseok Lee"
  - literal: "Hwanjo Yu"
issued:
  date-parts:
    - [2026, 3, 4]
url: "https://arxiv.org/abs/2603.03760"

# Custom fields
paper_id: "2603.03760"
paper_source: "openalex"
domain: "time-series"
tags:
  - "dataset"
  - "time-series"
  - "forecasting"
  - "frequency-domain-analysis"
  - "model_distillation"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:13Z"
created_at: "2026-03-27T14:08:13Z"
---

# Harmonic Dataset Distillation for Time Series Forecasting

**Authors**: Seungha Hong, Sanghwan Jang, Wonbin Kweon, Suyeon Kim, Gyuseok Lee, Hwanjo Yu
**Date**: 2026-03-04
**Paper ID**: [openalex:2603.03760](https://arxiv.org/abs/2603.03760)

## Summary

The paper addresses the computational challenges of large-scale Time Series Forecasting (TSF) by proposing Harmonic Dataset Distillation (HDT), a novel data distillation technique tailored for time series. HDT operates in the frequency domain by decomposing the time series into its sinusoidal basis using the Fast Fourier Transform (FFT) and performing Harmonic Matching. This frequency-domain approach ensures that distillation updates are applied globally, effectively capturing the core periodic structure without disrupting crucial temporal dependencies. Extensive experiments confirm that HDT offers superior cross-architecture generalization and scalability compared to conventional methods, validating its utility for practical, large-scale TSF applications.

## Key Contributions

- Introduction of Harmonic Dataset Distillation for Time Series Forecasting (HDT), which synthesizes a compact dataset mimicking the performance of the original large dataset.
- Proposal of Harmonic Matching in the frequency domain, achieved by decomposing the time series using FFT, ensuring global updates that preserve temporal dependencies.
- Demonstration of HDT's strong cross-architecture generalization and scalability, making it practical for large-scale time series applications.

## Limitations

The abstract primarily focuses on the benefits of the frequency-domain approach for distillation, but the specific impact on forecasting horizon performance and comparison to statistical baselines are not explicitly detailed.

## Open Questions & Future Work

- [[harmonic-matching-psd-smoothness-assumptions]]
- [[improving-tsf-dd-cross-architecture-robustness]]
- [[optimal-harmonic-selection-dd-tsf]]
- [[multivariate-harmonic-dd-tsf]]

## Key Concepts

- [Harmonic Dataset Distillation](../concepts/harmonic-dataset-distillation.md): A dataset distillation technique for time series forecasting that decomposes time series into sinusoidal bases via FFT and aligns the periodic structure through Harmonic Matching in the frequency domain.

## Limitations

The abstract primarily focuses on the benefits of the frequency-domain approach for distillation, but the specific impact on forecasting horizon performance and comparison to statistical baselines are not explicitly detailed.

## Links

- [Abstract](https://arxiv.org/abs/2603.03760)
- [PDF](https://arxiv.org/pdf/2603.03760)

