---
# CSL-compatible fields
title: "Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Time Series Forecasting"
author:
  - literal: "Kiran Madhusudhanan"
  - literal: "Christian Klötergens"
  - literal: "Lars Schmidt-Thieme"
  - literal: "Vijaya Krishna Yalavarthi"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.11114"

# Custom fields
paper_id: "2608.11114"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
  - "uncertainty-estimation"
  - "generative-model"
  - "normalizing-flow"
architectures:
  []
datasets:
  []
concept_slugs:
  - "two-stage-odd-residual-flows-torf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:08Z"
created_at: "2026-08-14T06:07:08Z"
---

# Two-stage Odd Residual Flows for Mean-Preserving Probabilistic Time Series Forecasting

**Authors**: Kiran Madhusudhanan, Christian Klötergens, Lars Schmidt-Thieme, Vijaya Krishna Yalavarthi
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.11114](https://arxiv.org/abs/2608.11114)

## Summary

Probabilistic time series forecasting often forces a trade-off between point accuracy and distributional flexibility. To resolve this, the authors propose Two-stage Odd Residual Flows (TORF), which decouples mean forecasting from uncertainty estimation by using a pre-trained deterministic model followed by a Restricted Normalizing Flow with strictly odd functions. This design guarantees mean preservation from the first stage without requiring costly Monte Carlo sampling, yielding state-of-the-art results in both deterministic accuracy (NMAE) and density estimation (CRPS) across various horizons.

## Key Contributions

- Proposes Two-stage Odd Residual Flows (TORF), a framework that decouples deterministic point forecasting from probabilistic uncertainty estimation.
- Utilizes a Restricted Normalizing Flow with strictly odd functions in the second stage to model residual distributions around point forecasts while strictly preserving the expected mean.
- Achieves state-of-the-art deterministic accuracy (NMAE) and strong density estimation performance (CRPS) across short and long-horizon forecasting tasks without requiring costly Monte Carlo sampling.

## Open Questions & Future Work

- [[multivariate-mean-preserving-residual-flows]]

## Key Concepts

- [[two-stage-odd-residual-flows-torf]]: A two-stage probabilistic forecasting framework using restricted normalizing flows with strictly odd functions to decouple mean prediction from uncertainty estimation and guarantee mean preservation without sampling.

## Archivist Review

Approved the core conceptual contribution of Two-stage Odd Residual Flows (TORF) and the open question regarding multivariate extensions, keeping strictly to the guidelines and maintaining high selectivity.

### Approved Concepts
- Two-stage Odd Residual Flows (TORF): Introduces a novel framework that decouples mean forecasting from uncertainty estimation using restricted normalizing flows with strictly odd functions to guarantee mean preservation.

### Approved Open Questions
- Multivariate Mean-Preserving Residual Flows: Crucial for capturing joint dependencies across multiple channels and time steps without sacrificing the analytical mean-preservation property.

## Links

- [Abstract](https://arxiv.org/abs/2608.11114)
- [PDF](https://arxiv.org/pdf/2608.11114)

