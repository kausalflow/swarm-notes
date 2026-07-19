---
# CSL-compatible fields
title: "Mixed-Frequency Time Series Forecasting via Depth-Separable Neural Networks"
author:
  - literal: "Yize Wang"
  - literal: "Qianqian Zhu"
  - literal: "Guodong Li"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14771"

# Custom fields
paper_id: "2607.14771"
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
  - "depth-separable-neural-networks-for-mixed-frequency-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:07Z"
created_at: "2026-07-19T07:24:07Z"
---

# Mixed-Frequency Time Series Forecasting via Depth-Separable Neural Networks

**Authors**: Yize Wang, Qianqian Zhu, Guodong Li
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14771](https://arxiv.org/abs/2607.14771)

## Summary

This paper addresses the limitations of linear frequency alignment in mixed-frequency time series forecasting by proposing a depth-separable neural network. The model utilizes a parameter-sharing mechanism to facilitate deep architectures that effectively capture nonlinearity between variables sampled at different frequencies. Theoretical analysis establishes the approximation properties and prediction error bounds for this approach. Empirical results demonstrate significant performance gains over traditional linear mixed-frequency methods in macroeconomic forecasting.

## Key Contributions

- Introduces a depth-separable neural network architecture for nonlinear alignment of mixed-frequency time series data.
- Implements a parameter-sharing mechanism across alignment stages to enable deeper networks for high-frequency predictors.
- Provides theoretical guarantees including approximation theory and non-asymptotic prediction error bounds for the proposed model.
- Demonstrates superior predictive accuracy over linear mixed-frequency methods on U.S. quarterly macroeconomic datasets.

## Open Questions & Future Work

- [[theoretical-estimation-for-neural-mixed-frequency-models]]

## Key Concepts

- [[depth-separable-neural-networks-for-mixed-frequency-forecasting]]: A deep neural network architecture employing parameter-sharing for nonlinear frequency alignment in mixed-frequency time series forecasting.

## Archivist Review

The concept of depth-separable neural networks is approved for its reusable approach to nonlinear frequency alignment, which is a specific, well-defined problem in the time series domain. The open question regarding theoretical foundations for these models is also approved, as it addresses a significant gap in moving from empirical performance to statistical rigor in neural time-series architectures. All other candidates were rejected for being either too narrow, redundant, or boilerplate suggestions that did not meet the archival quality standards.

### Approved Concepts
- Depth-Separable Neural Networks for Mixed-Frequency Forecasting: It provides a reusable architectural framework for replacing linear frequency alignment with learnable nonlinear operations, which is a fundamental problem in mixed-frequency time series analysis.

### Approved Open Questions
- Theoretical Estimation for Mixed-Frequency Networks: Theoretical reliability is required to transition deep learning architectures from empirical experiments to robust tools for complex economic and financial forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2607.14771)
- [PDF](https://arxiv.org/pdf/2607.14771)

