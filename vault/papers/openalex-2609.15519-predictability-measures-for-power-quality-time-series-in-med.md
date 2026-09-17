---
# CSL-compatible fields
title: "Predictability Measures for Power Quality Time Series in Medium-Term Forecasting"
author:
  - literal: "Peter Feistel"
  - literal: "Max Domagk"
  - literal: "Jan Meyer"
  - literal: "Marco Lindner"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15519"

# Custom fields
paper_id: "2609.15519"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:42:58Z"
created_at: "2026-09-17T09:42:58Z"
---

# Predictability Measures for Power Quality Time Series in Medium-Term Forecasting

**Authors**: Peter Feistel, Max Domagk, Jan Meyer, Marco Lindner
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15519](https://arxiv.org/abs/2609.15519)

## Summary

This paper investigates medium-term forecasting of power quality (PQ) parameters over horizons of weeks to a year using 2,807 weekly time series from the German transmission system. After benchmarking eight forecasting models and finding STL-ARIMA to be most effective, the authors evaluate model-free features like SVD entropy and Crest Factor to measure intrinsic predictability. By employing these features in a logistic regression, they successfully estimate forecast reliability beforehand to separate automatable time series from those requiring manual review.

## Key Contributions

- Evaluated 8 forecasting models on 2,807 weekly power quality time series spanning transmission networks, showing STL-ARIMA achieves an average sMAPE of 17.63%.
- Identified model-free features—specifically SVD entropy and Crest Factor—that correlate strongly with realized forecast accuracy across models.
- Developed a logistic regression framework using intrinsic predictability measures to estimate the probability of poor forecasts before model training, enabling automated routing for power grid maintenance.

## Archivist Review

No novel reusable concepts or named datasets meet the strict criteria for standalone archival notes.

## Links

- [Abstract](https://arxiv.org/abs/2609.15519)
- [PDF](https://arxiv.org/pdf/2609.15519)

