---
# CSL-compatible fields
title: "Hybrid Kolmogorov-Arnold Network and XGBoost Framework for Week-Ahead Price Forecasting in Australia's National Electricity Market"
author:
  - literal: "Houxuan Zhou"
  - literal: "Sriram Prasad"
  - literal: "Chenghao Huang"
  - literal: "Jiajie Feng"
  - literal: "Hao Wang"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22387"

# Custom fields
paper_id: "2605.22387"
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
  - "kan-xgboost-hybrid-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:41Z"
created_at: "2026-05-24T07:46:41Z"
---

# Hybrid Kolmogorov-Arnold Network and XGBoost Framework for Week-Ahead Price Forecasting in Australia's National Electricity Market

**Authors**: Houxuan Zhou, Sriram Prasad, Chenghao Huang, Jiajie Feng, Hao Wang
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22387](https://arxiv.org/abs/2605.22387)

## Summary

This paper presents a hybrid forecasting framework that integrates Kolmogorov-Arnold Networks (KAN) with XGBoost to address the challenges of high volatility and nonlinear dynamics in electricity price forecasting. By combining KAN's global representation capacity with XGBoost's local robustness, the model effectively captures both long-term trends and short-term price spikes. Experimental results on Australian National Electricity Market (NEM) data demonstrate superior performance compared to traditional statistical models and standard neural networks.

## Key Contributions

- Introduces a KAN+XGBoost hybrid model for week-ahead electricity price forecasting, combining global nonlinear representation with local robustness.
- Evaluated on real-world Australian National Electricity Market (NEM) data using an expanding window strategy.
- Outperforms SARIMAX, LSTM, and standalone baselines, achieving a 12% MAE reduction over XGBoost.

## Open Questions & Future Work

- [[extreme-price-spike-prediction-bottlenecks]]

## Key Concepts

- [[kan-xgboost-hybrid-framework]]: A hybrid architecture integrating Kolmogorov-Arnold Networks for nonlinear global dependencies and XGBoost for local price fluctuation robustness.

## Archivist Review

The hybrid model concept is approved as it addresses the growing interest in combining KANs with traditional ensemble methods for time-series forecasting. The open question regarding extreme price spike prediction is approved because it identifies a critical limitation in current forecasting loss functions that extends beyond this specific paper. Other datasets were rejected as they are domain-specific regional market snapshots rather than generalized benchmark datasets.

### Approved Concepts
- KAN+XGBoost Hybrid Framework: Combines the strengths of neural-based global nonlinear representation with tree-based local robustness for electricity price forecasting.

### Approved Open Questions
- Predicting Extreme Price Spikes: Improving the prediction of extreme price spikes is crucial for market participants to manage financial risks effectively, as these events significantly impact operational planning and profitability.

## Links

- [Abstract](https://arxiv.org/abs/2605.22387)
- [PDF](https://arxiv.org/pdf/2605.22387)

