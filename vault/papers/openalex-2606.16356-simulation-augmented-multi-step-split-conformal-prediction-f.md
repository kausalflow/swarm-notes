---
# CSL-compatible fields
title: "Simulation-Augmented Multi-Step Split Conformal Prediction for Aggregated Forecasts"
author:
  - literal: "Andro Sabashvili"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16356"

# Custom fields
paper_id: "2606.16356"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "simulation-augmented-multi-step-split-conformal-prediction-sa-mscp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:37Z"
created_at: "2026-06-17T09:25:37Z"
---

# Simulation-Augmented Multi-Step Split Conformal Prediction for Aggregated Forecasts

**Authors**: Andro Sabashvili
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16356](https://arxiv.org/abs/2606.16356)

## Summary

This paper introduces SA-MSCP, a novel framework for uncertainty quantification in aggregated time-series forecasting, such as annual totals and growth rates. The approach improves upon standard baselines by generating future trajectories from cross-validated residuals using a block bootstrap, followed by constructing prediction intervals from empirical quantiles. Empirical results indicate that this simulation-augmented conformal method provides superior coverage for complex, aggregated forecasting objectives.

## Key Contributions

- Proposes SA-MSCP, a simulation-augmented conformal method that improves empirical coverage for aggregated forecasting targets such as annual totals and year-over-year growth.
- Demonstrates that combining cross-validated residuals with block bootstrap sampling significantly enhances calibration compared to standard simulated-path baselines.
- Establishes simulation-enhanced conformal calibration as a general, effective framework for uncertainty quantification in multi-step aggregated time-series tasks.

## Open Questions & Future Work

- [[principled-temporal-calibration]]

## Key Concepts

- [[simulation-augmented-multi-step-split-conformal-prediction-sa-mscp]]: A multi-step conformal prediction method that improves coverage for aggregated forecasts by generating future paths from cross-validated residuals via block bootstrap.

## Archivist Review

The paper introduces a specific methodology for uncertainty quantification in aggregated forecasting, which is a common but challenging task in time-series analysis. The SA-MSCP method is approved for its general applicability as a calibration framework, and the open question regarding the theoretical foundations of temporal dependence in conformal prediction is approved as it addresses a core limitation in the field. Other items were deemed either too narrow or not central enough to justify inclusion in the knowledge vault.

### Approved Concepts
- Simulation-Augmented Multi-Step Split Conformal Prediction (SA-MSCP): Provides a new framework for valid uncertainty quantification in aggregated time-series forecasting tasks like annual totals and growth rates.

### Approved Open Questions
- Principled Calibration for Temporal Dependence: Current methods rely on heuristic aggregation and lack formal coverage guarantees for non-stationary or dependent data, making them insufficient for safety-critical applications in finance or supply chain management.

## Links

- [Abstract](https://arxiv.org/abs/2606.16356)
- [PDF](https://arxiv.org/pdf/2606.16356)

