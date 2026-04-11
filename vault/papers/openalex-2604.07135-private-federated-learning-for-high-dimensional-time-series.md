---
# CSL-compatible fields
title: "Private Federated Learning for High-dimensional Time Series"
author:
  - literal: "Kejun Chen"
  - literal: "Qianqian Zhu"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07135"

# Custom fields
paper_id: "2604.07135"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "federated-learning"
  - "differential-privacy"
  - "forecasting"
  - "multitask-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:54:15Z"
created_at: "2026-04-11T05:54:15Z"
---

# Private Federated Learning for High-dimensional Time Series

**Authors**: Kejun Chen, Qianqian Zhu
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07135](https://arxiv.org/abs/2604.07135)

## Summary

This paper introduces a privacy-preserving federated learning framework designed for high-dimensional vector autoregressive models in data-constrained settings. By utilizing a two-stage estimation approach, the method effectively isolates common low-rank dynamics from sparse, client-specific deviations while adhering to differential privacy constraints. Theoretical analysis establishes non-asymptotic error bounds and consistency properties, while empirical evaluations on macroeconomic and energy-economy datasets demonstrate significant improvements over single-client forecasting benchmarks.

## Key Contributions

- Develops a privacy-preserving federated learning framework for high-dimensional vector autoregressive models using differential privacy.
- Introduces a two-stage estimation procedure that decomposes dynamics into a shared low-rank component and sparse client-specific deviations.
- Establishes non-asymptotic error bounds characterizing the privacy-utility trade-off and proves consistency for a ridge-type rank selection criterion.

## Links

- [Abstract](https://arxiv.org/abs/2604.07135)
- [PDF](https://arxiv.org/pdf/2604.07135)

