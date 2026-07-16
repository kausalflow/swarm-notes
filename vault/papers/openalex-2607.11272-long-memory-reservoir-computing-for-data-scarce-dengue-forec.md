---
# CSL-compatible fields
title: "Long-Memory Reservoir Computing for Data-Scarce Dengue Forecasting"
author:
  - literal: "Rahul Goswami"
  - literal: "Shinjini Paul"
  - literal: "Palash Ghosh"
  - literal: "Tanujit Chakraborty"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11272"

# Custom fields
paper_id: "2607.11272"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "conformal-prediction"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fractional-echo-state-network-fesn"
  - "wavelet-echo-state-network-wesn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:08Z"
created_at: "2026-07-16T07:14:08Z"
---

# Long-Memory Reservoir Computing for Data-Scarce Dengue Forecasting

**Authors**: Rahul Goswami, Shinjini Paul, Palash Ghosh, Tanujit Chakraborty
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11272](https://arxiv.org/abs/2607.11272)

## Summary

This paper addresses the challenge of forecasting dengue incidence, which is characterized by short, non-stationary, and long-memory time series. The authors introduce two reservoir computing variants, Fractional ESN (fESN) and Wavelet ESN (wESN), designed to incorporate explicit long-range temporal dependencies. Theoretical analysis proves these models generate long-memory processes, and empirical results confirm they outperform statistical and deep learning baselines while providing reliable uncertainty intervals through conformal prediction.

## Key Contributions

- Proposes two novel long-memory reservoir computing frameworks, fESN and wESN, to address long-range temporal dependence in short, noisy, and non-stationary data.
- Establishes theoretical guarantees demonstrating that fESN and wESN generate polynomially decaying dependence patterns, unlike the short-memory dynamics of standard ESNs.
- Demonstrates superior forecasting performance over statistical (ARIMA/ARFIMA) and deep learning baselines across multiple dengue incidence datasets.
- Integrates conformal prediction to provide distribution-free, calibrated uncertainty quantification for dengue risk assessment.

## Open Questions & Future Work

- [[multivariate-long-memory-reservoir-computing]]
- [[intrinsic-long-memory-reservoir-states]]

## Key Concepts

- [[fractional-echo-state-network-fesn]]: An ESN variant that integrates fractional-differencing dynamics into the reservoir to explicitly model statistical long memory.
- [[wavelet-echo-state-network-wesn]]: An ESN architecture that utilizes wavelet smoothing to isolate low-frequency components for memory-aware modeling.

## Archivist Review

The paper introduces two reservoir computing variants for long-memory time series. I approved the two proposed architectures as they provide distinct approaches to embedding long-range dependency into recurrent structures. The open questions regarding multivariate extensions and internal state dynamics address core architectural limitations identified by the authors.

### Approved Concepts
- Fractional Echo State Network (fESN): Central architecture variant addressing the limitation of standard ESNs in capturing long-range temporal dependence.
- Wavelet Echo State Network (wESN): Novel approach to improving reservoir robustness in noisy, data-scarce settings by separating frequency components.

### Approved Open Questions
- Multivariate Long-Memory Reservoir Computing: Multivariate forecasting is essential for integrating exogenous drivers (climate, socio-environmental) known to influence infectious disease dynamics, which currently limits the predictive scope of univariate long-memory models.
- Intrinsic Long-Memory Reservoir States: Integrating memory at the state-transition level rather than as an auxiliary input path could provide a more theoretically consistent and expressive way to model long-memory dynamics in high-dimensional state spaces.

## Links

- [Abstract](https://arxiv.org/abs/2607.11272)
- [PDF](https://arxiv.org/pdf/2607.11272)

