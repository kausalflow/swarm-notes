---
# CSL-compatible fields
title: "CTIA-ODE: Continuous-Time Inter-Variable Attention for Long-Term Time Series Forecasting"
author:
  - literal: "Chengyi Pan"
  - literal: "Huangqimei Zheng"
  - literal: "Hao Xue"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.19831"

# Custom fields
paper_id: "2610.19831"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  - "continuous-time-inter-variable-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:27Z"
created_at: "2026-10-17T08:54:27Z"
---

# CTIA-ODE: Continuous-Time Inter-Variable Attention for Long-Term Time Series Forecasting

**Authors**: Chengyi Pan, Huangqimei Zheng, Hao Xue
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.19831](https://arxiv.org/abs/2610.19831)

## Summary

The paper introduces CTIA-ODE, a continuous-time forecasting framework designed to incorporate exogenous variables in multivariate time series without requiring rigid temporal alignment. By embedding a Continuous-Time Inter-Variable Attention (CTIA) mechanism inside an ordinary differential equation (ODE) solver, endogenous trajectories dynamically query static exogenous context along the integration path. Additionally, a dual-stabilization strategy combining a Linear Residual Augmentation module and an Outlier-Robust Hybrid Loss improves continuous latent stability and robustness to heavy-tailed anomalies. Experiments across eight real-world benchmarks show that CTIA-ODE achieves state-of-the-art performance with strong computational efficiency, especially in long-term forecasting.

## Key Contributions

- Introduces CTIA-ODE, a continuous-time multivariate forecasting framework that replaces rigid temporal alignment with Continuous-Time Inter-Variable Attention embedded in an ODE solver.
- Proposes a dual-stabilization strategy featuring a Linear Residual Augmentation (LRA) module for trend anchoring and an Outlier-Robust Hybrid Loss (ORHL) for heavy-tailed anomaly handling.
- Achieves state-of-the-art forecasting performance across eight real-world datasets with favorable accuracy-efficiency trade-offs and low long-horizon inference latency.

## Open Questions & Future Work

- [[irregularly-sampled-time-series-forecasting]]

## Key Concepts

- [[continuous-time-inter-variable-attention]]: A continuous-time attention mechanism embedded within an ODE solver that enables endogenous trajectories to dynamically query exogenous context along the integration path.

## Archivist Review

Approved the core continuous-time attention concept and the associated open question on irregular time series forecasting, adhering strictly to scarcity constraints and filtering out local helper modules like LRA and ORHL.

### Approved Concepts
- Continuous-Time Inter-Variable Attention: It forms the core methodological contribution for handling exogenous variables across continuous time without rigid alignment.

### Approved Open Questions
- Irregularly Sampled Time Series Forecasting: Extending continuous-time attention models to irregular sampling is crucial for real-world domains like healthcare and finance where data is frequently asynchronous and missing.

## Links

- [Abstract](https://arxiv.org/abs/2610.19831)
- [PDF](https://arxiv.org/pdf/2610.19831)

