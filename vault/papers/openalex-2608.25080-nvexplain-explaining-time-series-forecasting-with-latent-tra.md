---
# CSL-compatible fields
title: "NVExplain: Explaining Time Series Forecasting with Latent Trajectory Analysis and Structure-Preserving Surrogates"
author:
  - literal: "Muyan Li"
  - literal: "Manikandan Ravikiran"
  - literal: "Aditi Gautam"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.25080"

# Custom fields
paper_id: "2608.25080"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "explainability"
  - "interpretability"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nvexplain"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:58:56Z"
created_at: "2026-08-28T16:58:56Z"
---

# NVExplain: Explaining Time Series Forecasting with Latent Trajectory Analysis and Structure-Preserving Surrogates

**Authors**: Muyan Li, Manikandan Ravikiran, Aditi Gautam
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.25080](https://arxiv.org/abs/2608.25080)

## Summary

The paper introduces NVExplain, a model-agnostic explainability framework for time series forecasting that constructs horizon-resolved temporal influence matrices via latent trajectory analysis and semantic flow. By utilizing structure-preserving perturbations and sparse local surrogates, NVExplain generates human-readable and temporally coherent explanations that attribute forecast horizons to historical lags. Empirical evaluations using faithfulness and stability diagnostics across multiple benchmark datasets demonstrate superior or competitive performance compared to standard baselines alongside high computational efficiency.

## Key Contributions

- Proposes NVExplain, a model-agnostic explainability framework for time series forecasting that attributes each forecast horizon to temporally relevant historical lags.
- Introduces semantic flow to quantify how information evolves across time within the model's internal representations, constructing a horizon-resolved temporal influence matrix.
- Employs structure-preserving perturbations and sparse local surrogate models to produce human-readable, temporally coherent explanations.
- Demonstrates through faithfulness and stability diagnostics that the semantic-flow approach achieves superior or competitive faithfulness compared to standard baselines while maintaining higher computational efficiency.

## Open Questions & Future Work

- [[multivariate-forecasting-feature-level-attributions]]

## Key Concepts

- [[nvexplain]]: A model-agnostic explainability framework for time series forecasting that attributes forecast horizons to historical lags using latent trajectory analysis and structure-preserving surrogates.

## Archivist Review

Approved the core framework concept (NVExplain) and the open question regarding multivariate feature-level attribution extension, as both meet the rigorous criteria for permanence and reusability without duplicating existing vault entries.

### Approved Concepts
- NVExplain: Introduces a complete explainability framework for time series forecasting based on latent trajectory analysis and structure-preserving surrogates.

### Approved Open Questions
- Multivariate and Feature-Level Forecasting Explanations: Real-world industrial and financial forecasting tasks are predominantly multivariate, requiring explanations that jointly resolve both when past events matter (lags) and which variables matter (features).

## Links

- [Abstract](https://arxiv.org/abs/2608.25080)
- [PDF](https://arxiv.org/pdf/2608.25080)

