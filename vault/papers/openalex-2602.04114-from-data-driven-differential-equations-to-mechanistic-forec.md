---
# CSL-compatible fields
title: "From data-driven differential equations to mechanistic forecasting with machine learning"
author:
  - literal: "Amit K. Chakraborty"
  - literal: "Hao Wang"
  - literal: "Pouria Ramazi"
issued:
  date-parts:
    - [2026, 11, 4]
url: "https://arxiv.org/abs/2602.04114"

# Custom fields
paper_id: "2602.04114"
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
processed_at: "2026-11-05T12:52:02Z"
created_at: "2026-11-05T12:52:02Z"
---

# From data-driven differential equations to mechanistic forecasting with machine learning

**Authors**: Amit K. Chakraborty, Hao Wang, Pouria Ramazi
**Date**: 2026-11-04
**Paper ID**: [openalex:2602.04114](https://arxiv.org/abs/2602.04114)

## Summary

This paper introduces a data-driven differential equation discovery method that relaxes the standard time-invariant coefficient assumption by learning the temporal evolution of time-varying parameters directly from time-series data. By predicting future values of these time-varying parameters and substituting them into the learned equations, the framework achieves robust mechanistic forecasting. Evaluated on simulated epidemiological and ecological systems as well as real-world greenhouse gas and cyanobacteria datasets, the proposed approach outperforms conventional deep learning and machine learning baselines such as CNN-LSTM and gradient boosting.

## Key Contributions

- Proposes a data-driven discovery framework for differential equations that incorporates both constant and time-varying parameters to capture evolving system dynamics.
- Transforms the discovered equations into a forecasting model by predicting time-varying parameters and substituting them into the learned differential equations.
- Demonstrates superior forecasting performance compared to CNN-LSTM and gradient boosting machines, achieving a mean absolute error below 3% for learning and below 6% for forecasting up to a month ahead.

## Archivist Review

Reviewed the proposed open questions from the paper on data-driven differential equations and mechanistic forecasting. Both open questions represent standard future work extensions (exploring ensembles and validation objectives) rather than foundational, unique open research problems, so both were rejected under high-selectivity standards.

### Rejected Candidates
- [open_question] Ensemble Parameter Predictors for Forecasting (`ensemble-parameter-predictors-forecasting`) - low_impact: Standard future work proposal suggesting multi-baseline or ensemble parameter predictors without addressing a deep structural bottleneck distinct from existing open questions on parameter drift.
- [open_question] Forecast-Aware Validation Objectives (`forecast-aware-validation-objectives`) - low_impact: Routine exploration of validation objectives and model selection criteria that applies generally to machine learning models rather than a specific fundamental limitation.

## Links

- [Abstract](https://arxiv.org/abs/2602.04114)
- [PDF](https://arxiv.org/pdf/2602.04114)

