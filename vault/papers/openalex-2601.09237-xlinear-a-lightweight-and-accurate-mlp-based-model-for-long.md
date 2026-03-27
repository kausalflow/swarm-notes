---
# CSL-compatible fields
title: "XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs"
author:
  - literal: "Xinyang Chen"
  - literal: "Huidong Jin"
  - literal: "yu huang"
  - literal: "Zaiwen Feng"
issued:
  date-parts:
    - [2026, 3, 14]
url: "https://arxiv.org/abs/2601.09237"

# Custom fields
paper_id: "2601.09237"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "efficient-transformer"
architectures:
  []
datasets:
  - "ETTh1"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:30Z"
created_at: "2026-03-27T14:09:30Z"
---

# XLinear: A Lightweight and Accurate MLP-Based Model for Long-Term Time Series Forecasting with Exogenous Inputs

**Authors**: Xinyang Chen, Huidong Jin, yu huang, Zaiwen Feng
**Date**: 2026-03-14
**Paper ID**: [openalex:2601.09237](https://arxiv.org/abs/2601.09237)

## Summary

The paper introduces XLinear, a lightweight Multi-Layer Perceptron (MLP) based model tailored for long-term time series forecasting, specifically designed to incorporate informative exogenous variables efficiently. XLinear employs a global token, derived from the primary endogenous variable, to serve as a central hub for interacting with and weighting the influence of external inputs. The model utilizes MLPs with sigmoid activation to effectively disentangle and model both temporal autocorrelation and cross-variate dependencies introduced by exogenous features. Evaluation across seven standard and five real-world datasets demonstrates that XLinear achieves superior accuracy and computational efficiency compared to existing state-of-the-art forecasting methods when exogenous data is available.

## Key Contributions

- Proposed XLinear, a lightweight MLP-based model designed to efficiently exploit informative signals from both temporal dynamics and relevant exogenous variables for long-term forecasting.
- Introduced a global token derived from the endogenous variable acting as a pivotal hub to selectively extract and integrate relevant information from associated exogenous variables.
- Achieved superior accuracy and efficiency compared to state-of-the-art models across seven standard benchmarks and five real-world datasets featuring exogenous inputs.
- Demonstrated the effectiveness of using MLPs with sigmoid activation to explicitly model both temporal patterns and variate-wise dependencies in the presence of cost-effective exogenous data.

## Limitations

The paper primarily focuses on leveraging exogenous inputs and its performance against modern Transformer or State Space Model baselines without exogenous inputs for purely endogenous long-term forecasting is not explicitly detailed in the abstract.

## Open Questions & Future Work

- [[reducing-vgm-dimensionality-in-high-dimensional-forecasting]]
- [[optimizing-lookback-windows-and-bolstering-reliability]]

## Key Concepts

- [XLinear](../concepts/xlinear-mlp-forecasting.md): A lightweight, MLP-based time series forecasting model that uses a global token derived from the endogenous variable to selectively interact with exogenous variables.

## Datasets

- [ETTh1](../datasets/etth1.md)

## Limitations

The paper primarily focuses on leveraging exogenous inputs and its performance against modern Transformer or State Space Model baselines without exogenous inputs for purely endogenous long-term forecasting is not explicitly detailed in the abstract.

## Links

- [Abstract](https://arxiv.org/abs/2601.09237)
- [PDF](https://arxiv.org/pdf/2601.09237)

