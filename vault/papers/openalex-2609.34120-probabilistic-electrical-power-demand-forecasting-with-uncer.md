---
# CSL-compatible fields
title: "Probabilistic electrical power demand forecasting with uncertainty quantification"
author:
  - literal: "Mahesh Neupane"
  - literal: "Pragya Dhungana"
  - literal: "Pradip Khatri"
  - literal: "Swechhya Baskota"
  - literal: "Hariom Dhungana"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34120"

# Custom fields
paper_id: "2609.34120"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
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
processed_at: "2026-09-30T10:50:39Z"
created_at: "2026-09-30T10:50:39Z"
---

# Probabilistic electrical power demand forecasting with uncertainty quantification

**Authors**: Mahesh Neupane, Pragya Dhungana, Pradip Khatri, Swechhya Baskota, Hariom Dhungana
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34120](https://arxiv.org/abs/2609.34120)

## Summary

This study presents an empirical evaluation of four contemporary probabilistic forecasting models—NGBoost, Bayesian, Monte Carlo Dropout, and Gaussian Process Regression—for electrical power demand forecasting. By addressing the uncertainty introduced by renewable energy sources, the authors find that NGBoost consistently achieves superior performance in terms of MAE, RMSE, and well-calibrated uncertainty estimation across real-world power consumption datasets. The findings highlight NGBoost as a robust framework for reliable smart grid planning and operation.

## Key Contributions

- Demonstrates that NGBoost outperforms Bayesian, Monte Carlo Dropout, and Gaussian Process Regression models in probabilistic electricity consumption forecasting.
- Achieves lower MAE and RMSE while producing well-calibrated uncertainty estimates with high prediction-interval coverage and narrow intervals.
- Provides an empirical comparison of four contemporary probabilistic forecasting methods on real-world power systems datasets to address increased variability from renewable energy sources.

## Limitations

Evaluated specifically on electricity consumption data; broader generalizability across other non-energy time-series domains remains unexplored.

## Archivist Review

The paper provides an empirical comparison of existing probabilistic forecasting models on electrical power demand. Since no novel architectural mechanism or standalone reusable framework was introduced, and the open question is standard future-work boilerplate for evaluation comparisons, no permanent vault notes are approved.

### Rejected Candidates
- [open_question] Probabilistic Forecasting Trade-offs and Calibration (`probabilistic-forecasting-tradeoffs-and-calibration`) - low_impact: Too broad and standard for empirical comparison papers in energy forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.34120)
- [PDF](https://arxiv.org/pdf/2609.34120)

