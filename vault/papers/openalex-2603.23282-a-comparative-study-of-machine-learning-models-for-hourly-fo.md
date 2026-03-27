---
# CSL-compatible fields
title: "A Comparative Study of Machine Learning Models for Hourly Forecasting of Air Temperature and Relative Humidity"
author:
  - literal: "Jiaqi Dong"
issued:
  date-parts:
    - [2026, 3, 24]
url: "https://arxiv.org/abs/2603.23282"

# Custom fields
paper_id: "2603.23282"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "cnn"
  - "machine-learning"
  - "evaluation"
  - "ensemble-learning"
architectures:
  - "cnn"
datasets:
  []
concept_slugs:
  - "xgboost-meteorological-forecasting-comparison"
  - "cnn-lstm-time-series-hybrid"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T15:43:39Z"
created_at: "2026-03-27T15:43:39Z"
---

# A Comparative Study of Machine Learning Models for Hourly Forecasting of Air Temperature and Relative Humidity

**Authors**: Jiaqi Dong
**Date**: 2026-03-24
**Paper ID**: [openalex:2603.23282](https://arxiv.org/abs/2603.23282)

## Summary

This study comparatively evaluates seven machine learning models, including XGBoost, LSTM, and CNN-LSTM, for short-term hourly forecasting of air temperature and relative humidity in the complex urban environment of Chongqing, China. Utilizing a standardized framework incorporating feature engineering and time-series validation, the research found that the eXtreme Gradient Boosting (XGBoost) model yielded the best overall predictive accuracy across both variables. The results highlight the robust effectiveness of tree-based ensemble methods over deep learning models for this specific application of structured meteorological time-series prediction. The superior performance of XGBoost suggests a practical direction for intelligent forecasting systems in geographically challenging areas.

## Key Contributions

- Systematically compared seven machine learning models (including XGBoost, LSTM, and CNN-LSTM) for hourly air temperature and relative humidity forecasting in topographically complex regions.
- Demonstrated that the tree-based ensemble model, XGBoost, achieved superior predictive accuracy (MAE of 0.302 °C for temperature) compared to deep learning models.
- Established a unified framework involving data preprocessing, lag-feature construction, and rolling statistical features for robust time-series evaluation.
- Provided practical guidance confirming the strong effectiveness of tree-based methods for structured meteorological time-series prediction.

## Limitations

The study focuses only on short-term hourly forecasting and does not explore longer horizons or incorporate complex external causal factors beyond the provided time series.

## Key Concepts

- [[xgboost-meteorological-forecasting-comparison]]: eXtreme Gradient Boosting (XGBoost) applied and benchmarked as the top-performing model for hourly air temperature and relative humidity forecasting.
- [[cnn-lstm-time-series-hybrid]]: A hybrid deep learning architecture combining a Convolutional Neural Network (CNN) for feature extraction with a Long Short-Term Memory (LSTM) network for sequence modeling in time-series prediction.

## Archivist Review

The analysis provided only two concepts, both representing models that were evaluated. The primary, reusable finding is the strong empirical performance of the tree-based XGBoost model relative to the deep learning models (LSTM, CNN-LSTM) for this structured meteorological forecasting task. I am approving XGBoost performance as the key reusable concept, while rejecting the CNN-LSTM concept as it is merely one evaluated baseline component rather than a central novel mechanism. No datasets or open questions were provided for review.

### Approved Concepts
- XGBoost for Meteorological Forecasting: The paper specifically highlights XGBoost as the best performer, suggesting its structured comparison against deep learning models for this specific type of time series is a key finding.
- CNN-LSTM Hybrid for Time Series: The CNN-LSTM model represents a specific combination of deep learning architectures used for sequential data comparison against pure statistical/tree methods.

### Rejected Candidates
- [concept] CNN-LSTM Hybrid for Time Series (`cnn-lstm-time-series-hybrid`) - subcomponent_of_broader_mechanism: While CNN-LSTM is a standard architecture, its inclusion here is primarily as one of the evaluated baselines against the primary finding (XGBoost performance), thus the core reusable idea is the performance result itself, not the architecture's novelty.
- [concept] XGBoost for Meteorological Forecasting (`xgboost-meteorological-forecasting-comparison`) - generic: The concept approved here is the strong finding: the empirical demonstration that XGBoost outperforms LSTMs/CNNs for this structured meteorological forecasting task. The slug is kept as it captures this specific empirical finding.

## Links

- [Abstract](https://arxiv.org/abs/2603.23282)
- [PDF](https://arxiv.org/pdf/2603.23282)

