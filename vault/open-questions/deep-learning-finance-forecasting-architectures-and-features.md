---
created_at: '2026-05-30T07:36:00Z'
source_papers:
- '[[openalex-2605.27977-deep-learning-forecasting-of-the-us-aggregate-bond-index]]'
title: Optimizing Deep Learning Finance Forecasts
---

**Background:** Financial time series forecasting often involves choosing between raw levels, log returns, or fractionally differenced series to handle non-stationarity and long-memory dependencies. Current research shows predictive performance is highly sensitive to the alignment between data representation and model inductive bias.

**Question / Future Work:** It remains an open question whether the forecasting performance of neural models on persistence-dominated financial series can be substantially improved by incorporating multi-variate features (e.g., cross-asset signals, term-structure variables) or specialized sequence-aware architectures (e.g., Transformers) that effectively reconcile long-memory retention with non-linear predictive capabilities.

**Why It Matters:** Understanding the limits of univariate versus multivariate and static versus sequence-aware architectures is a core bottleneck in advancing financial time-series forecasting.