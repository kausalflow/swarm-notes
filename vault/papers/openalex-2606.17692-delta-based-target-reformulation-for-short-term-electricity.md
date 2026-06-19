---
# CSL-compatible fields
title: "Delta-Based Target Reformulation for Short-Term Electricity Load Forecasting Using LSTM and Transformer Models"
author:
  - literal: "Vansh Bansal"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17692"

# Custom fields
paper_id: "2606.17692"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "lstm"
  - "deep-learning"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  - "delta-based-target-reformulation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:33Z"
created_at: "2026-06-19T09:24:33Z"
---

# Delta-Based Target Reformulation for Short-Term Electricity Load Forecasting Using LSTM and Transformer Models

**Authors**: Vansh Bansal
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17692](https://arxiv.org/abs/2606.17692)

## Summary

This paper proposes a delta-based target reformulation for short-term electricity load forecasting to mitigate the challenges of data non-stationarity. Instead of predicting absolute values, models are trained to predict the change between consecutive time steps, which are then used to reconstruct final forecasts. Evaluations using LSTM, Transformer, and LightGBM models on real-world Indian electricity load data reveal that this technique acts as a potent inductive bias for neural networks, significantly improving accuracy for hour-ahead horizons.

## Key Contributions

- Demonstrates that delta-based target reformulation consistently reduces MAPE by over 50% for hour-ahead electricity load forecasting across LSTM and Transformer models.
- Shows that while delta-based targets act as a powerful inductive bias for deep sequence models, their performance advantage is dependent on the forecasting horizon compared to static models like LightGBM.
- Establishes that reforming absolute load targets as differences between consecutive time steps stabilizes the learning target, significantly enhancing the accuracy of neural networks in non-stationary power load environments.

## Open Questions & Future Work

- [[hybrid-target-formulation-horizon-robustness]]

## Key Concepts

- [[delta-based-target-reformulation]]: A training strategy that reformulates forecasting as the prediction of consecutive time-step deltas to improve learning stability in non-stationary time series.

## Archivist Review

The paper introduces delta-based target reformulation as an inductive bias to improve training for deep learning models in non-stationary time series. I approved the concept for its general applicability and the open question for identifying a specific performance bottleneck related to error accumulation in long-horizon forecasting. I rejected the NASA POWER dataset as it is a generic meteorological data source rather than a specific electricity load benchmark.

### Approved Concepts
- Delta-Based Target Reformulation: Addresses target non-stationarity in deep learning-based time-series forecasting by borrowing from classical differencing methods to stabilize the learning objective.

### Approved Open Questions
- Hybrid Target Formulation Horizon Robustness: This addresses a fundamental trade-off in time-series forecasting where different models and horizons require varying levels of target stationarity, impacting the reliability of production-grade forecasting pipelines.

## Links

- [Abstract](https://arxiv.org/abs/2606.17692)
- [PDF](https://arxiv.org/pdf/2606.17692)

