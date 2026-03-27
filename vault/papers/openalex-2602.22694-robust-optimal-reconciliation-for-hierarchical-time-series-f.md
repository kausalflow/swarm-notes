---
# CSL-compatible fields
title: "Robust optimal reconciliation for hierarchical time series forecasting with M-estimation"
author:
  - literal: "Zhichao Wang"
  - literal: "Shanshan Wang"
  - literal: "Wei Cao"
  - literal: "Fei Yang"
issued:
  date-parts:
    - [2026, 2, 26]
url: "https://arxiv.org/abs/2602.22694"

# Custom fields
paper_id: "2602.22694"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:29Z"
created_at: "2026-03-27T14:08:29Z"
---

# Robust optimal reconciliation for hierarchical time series forecasting with M-estimation

**Authors**: Zhichao Wang, Shanshan Wang, Wei Cao, Fei Yang
**Date**: 2026-02-26
**Paper ID**: [openalex:2602.22694](https://arxiv.org/abs/2602.22694)

## Summary

This paper addresses the challenge of producing coherent forecasts for Hierarchical Time Series (HTS) that are robust to anomalous or irregular base forecasts. The authors introduce a robust reconciliation framework based on M-estimation, which minimizes a robust loss function subject to the necessary aggregation constraints. The core of the methodology involves an efficient minimization procedure implemented via a modified Newton-Raphson algorithm utilizing local quadratic approximation. Experimental results confirm that this robust approach effectively handles series with non-normal errors and maintains high efficiency in clean datasets, as validated on Australian domestic tourism data.

## Key Contributions

- Proposes a robust reconciliation method for Hierarchical Time Series (HTS) forecasting by incorporating M-estimation to minimize a robust loss function.
- Develops a minimization procedure for the robust reconciliation problem using a modified Newton-Raphson algorithm based on local quadratic approximation.
- Demonstrates superior performance in handling abnormal time series cases (e.g., series with non-normal errors) compared to standard reconciliation methods.
- Shows that the robust method maintains excellent efficiency even when no outliers are present in the HTS structure.

## Limitations

The paper focuses primarily on robustness against abnormal cases and does not detail comparisons against a wide range of statistical baselines (like ARIMA or Prophet) specifically within the context of M-estimation reconciliation.

## Open Questions & Future Work

- [[compute-burden-cross-sectional-hts]]
- [[hts-non-stationary-components]]
- [[optimal-loss-function-selection]]
- [[probabilistic-reconciliation-uncertainty]]
- [[extending-rome-complex-hierarchies]]
- [[rome-general-reconciliation-framework]]
- [[covariance-design-robust-loss]]

## Limitations

The paper focuses primarily on robustness against abnormal cases and does not detail comparisons against a wide range of statistical baselines (like ARIMA or Prophet) specifically within the context of M-estimation reconciliation.

## Links

- [Abstract](https://arxiv.org/abs/2602.22694)
- [PDF](https://arxiv.org/pdf/2602.22694)

