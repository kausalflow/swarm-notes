---
# CSL-compatible fields
title: "Hedging Memory Horizons for Non-Stationary Prediction via Online Aggregation"
author:
  - literal: "Yutong Wang"
  - literal: "Yannig Goude"
  - literal: "Qiwei Yao"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06541"

# Custom fields
paper_id: "2605.06541"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "online-learning"
  - "adaptation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "melo-memory-hedged-ewls-online-aggregation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:22:27Z"
created_at: "2026-05-10T07:22:27Z"
---

# Hedging Memory Horizons for Non-Stationary Prediction via Online Aggregation

**Authors**: Yutong Wang, Yannig Goude, Qiwei Yao
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06541](https://arxiv.org/abs/2605.06541)

## Summary

The paper introduces MELO, an online aggregation method designed to address distribution shifts in chronological forecasting without needing explicit regime indicators. By wrapping a pool of predictors with exponentially weighted least-squares (EWLS) experts operating at different forgetting factors, MELO dynamically adapts to varying memory horizons. The method is theoretically grounded with oracle inequalities and demonstrates superior empirical performance on electricity-load forecasting, effectively handling abrupt non-stationary events like COVID-19 lockdowns.

## Key Contributions

- Introduced MELO, a model-agnostic aggregation framework that dynamically balances stability and adaptation for non-stationary time-series forecasting.
- Established theoretical deterministic oracle inequalities showing MELO competes with optimal time-varying affine combinations of base predictors.
- Achieved a 34.7% reduction in RMSE compared to standard MLpol on French electricity-load forecasting, outperforming models explicitly tuned for exogenous COVID-19 covariates.

## Open Questions & Future Work

- [[multi-scale-adaptation-limits]]

## Key Concepts

- [[melo-memory-hedged-ewls-online-aggregation]]: A model-agnostic online aggregation framework that dynamically weights base predictors across multiple adaptation scales using exponentially weighted least-squares experts.

## Archivist Review

The paper introduces a well-defined and reusable model-agnostic aggregation framework, MELO, which is approved as a concept for the vault due to its clear utility in addressing non-stationarity in time-series forecasting. The proposed open question regarding the theoretical and practical limits of multi-scale adaptation is also approved as it articulates a substantial, unresolved challenge in online learning and forecasting. No datasets were approved as the paper utilizes standard industry data without contributing a novel benchmark.

### Approved Concepts
- Memory-hedged Exponentially Weighted Least-Squares Online aggregation (MELO): The core innovation of the paper, providing a model-agnostic framework for online prediction under distribution shift by hedging across multiple adaptation memories.

### Approved Open Questions
- Limits of multi-scale adaptation: Defining precise preconditions for the effectiveness of multi-scale adaptation layers is critical for their reliable application across heterogeneous industrial domains.

## Links

- [Abstract](https://arxiv.org/abs/2605.06541)
- [PDF](https://arxiv.org/pdf/2605.06541)

