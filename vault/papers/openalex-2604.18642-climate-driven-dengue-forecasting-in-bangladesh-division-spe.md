---
# CSL-compatible fields
title: "Climate-driven dengue forecasting in Bangladesh: division-specific feature-set design and lag structure"
author:
  - literal: "Faizunnesa Khondaker"
  - literal: "Md. Kamrujjaman"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2604.18642"

# Custom fields
paper_id: "2604.18642"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:41Z"
created_at: "2026-10-02T10:47:41Z"
---

# Climate-driven dengue forecasting in Bangladesh: division-specific feature-set design and lag structure

**Authors**: Faizunnesa Khondaker, Md. Kamrujjaman
**Date**: 2026-09-30
**Paper ID**: [openalex:2604.18642](https://arxiv.org/abs/2604.18642)

## Summary

This paper investigates climate-driven dengue forecasting in Bangladesh by comparing division-specific feature-set designs and lag structures for Dhaka and Barishal. Using meteorological and monthly dengue incidence data from 2022 to 2025, the authors evaluate four feature sets varying wetness and sunshine indicators across 0-4 month lags. Benchmarking multivariate Poisson regression, ANNs, XGBoost, and SARIMAX demonstrates that optimal model architecture and feature configuration vary significantly by geographic division.

## Key Contributions

- Contrasts climate-driven dengue incidence forecasting across high-burden Dhaka and rising-burden Barishal using monthly data from 2022 to 2025.
- Evaluates four distinct climate feature sets varying wetness and sunshine representations combined with 0 to 4-month lag structures.
- Compares multivariate Poisson regression, artificial neural networks, XGBoost, and SARIMAX, finding ANN-1 optimal for Dhaka (RMSE = 2176.70) and SARIMAX optimal for Barishal (RMSE = 817.56).

## Archivist Review

Applied epidemiological forecasting papers that evaluate standard regression and neural network architectures on regional disease datasets do not introduce sufficiently novel, reusable theoretical mechanisms or architectural concepts to merit permanent vault notes. The single proposed open question was rejected because it represents routine domain-specific future work rather than an architectural or methodological bottleneck.

### Rejected Candidates
- [open_question] Extended Drivers for Dengue Forecasting (`extended-drivers-long-history-dengue-forecasting`) - low_impact: This is a standard application-specific future work direction proposing more features and longer history for a specific regional disease model, lacking broader foundational methodological novelty.

## Links

- [Abstract](https://arxiv.org/abs/2604.18642)
- [PDF](https://arxiv.org/pdf/2604.18642)

