---
# CSL-compatible fields
title: "Hybrid Machine Learning Framework for Herd-Level Cattle Growth Pattern and Weight Gain Forecasting in Grazing-Based Production Systems"
author:
  - literal: "Muhammad Riaz Hasib Hossain"
  - literal: "Rafiqul Islam"
  - literal: "Shawn McGrath"
  - literal: "Md Zahidul Islam"
  - literal: "David W. Lamb"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.06001"

# Custom fields
paper_id: "2608.06001"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "lstm"
  - "gru"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:44Z"
created_at: "2026-08-09T05:40:44Z"
---

# Hybrid Machine Learning Framework for Herd-Level Cattle Growth Pattern and Weight Gain Forecasting in Grazing-Based Production Systems

**Authors**: Muhammad Riaz Hasib Hossain, Rafiqul Islam, Shawn McGrath, Md Zahidul Islam, David W. Lamb
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.06001](https://arxiv.org/abs/2608.06001)

## Summary

This paper develops a hybrid machine learning framework for herd-level cattle weight and growth pattern forecasting in commercial grazing systems using automated sensing data collected in southeastern Australia. The study evaluates residual, stacked, cascade, and ensemble-assisted hybrid architectures against traditional statistical and recurrent baselines like ARIMA, LSTM, and GRU. Results show that a cascade gradient boosting, random forest, and neural network (GB-RF-NN) architecture achieves the best predictive performance while maintaining robustness under sparse observation conditions. Feature importance analysis reveals that animal age, rainfall, and temperature are dominant drivers of herd-level weight gain.

## Key Contributions

- Developed a hybrid machine learning framework combining automated sensing observations, demographic variables, and lagged environmental predictors to forecast herd-level cattle growth and weight gain in grazing systems.
- Evaluated four hybrid architecture families (residual, stacked, cascade, and ensemble-assisted frameworks) against ARIMA, LSTM, and GRU baselines.
- Demonstrated that the cascade GB-RF-NN architecture achieves superior predictive performance with a test R^2 of 0.889, RMSE of 21.319 kg, and MAE of 15.462 kg.
- Identified that hybrid architectures maintain greater robustness than recurrent sequential models under sparse observation conditions, with animal age, rainfall, and temperature recognized as dominant predictors.

## Limitations

Forecasting error increased progressively across extended prediction horizons under irregular and sparse livestock observation conditions.

## Archivist Review

No novel or reusable machine learning architectural concepts or distinct framework names proposed; standard hybrid machine learning methodologies and architectures are used in an agricultural application.

## Links

- [Abstract](https://arxiv.org/abs/2608.06001)
- [PDF](https://arxiv.org/pdf/2608.06001)

