---
# CSL-compatible fields
title: "Attributing Differences Between Forecast Runs to Input Changes, With Applications to CCAR and CECL Exercises"
author:
  - literal: "Xuan Mei"
  - literal: "Junze Lin"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04547"

# Custom fields
paper_id: "2608.04547"
paper_source: "openalex"
domain: "finance"
tags:
  - "forecasting"
  - "interpretability"
  - "explainability"
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
processed_at: "2026-08-08T05:34:46Z"
created_at: "2026-08-08T05:34:46Z"
---

# Attributing Differences Between Forecast Runs to Input Changes, With Applications to CCAR and CECL Exercises

**Authors**: Xuan Mei, Junze Lin
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04547](https://arxiv.org/abs/2608.04547)

## Summary

This paper examines the problem of explaining the differences between consecutive forecast runs in complex financial systems such as CCAR and CECL, which incorporate portfolio data, macroeconomic scenarios, models, and assumptions. By formulating forecast-gap attribution as a cooperative game, the authors evaluate and compare methods including exact Shapley values, hierarchical Shapley values, Integrated Gradients, and various SHAP approximations. Their analysis delivers practical guidelines for choosing attribution methods based on computational cost, interpretability, and regulatory governance needs.

## Key Contributions

- Formulates forecast-gap attribution as a cooperative game to attribute differences between forecasting runs to input changes without depending on an arbitrary sequence of input replacements.
- Compares several attribution approaches including exact Shapley value, hierarchical or nested Shapley values, Integrated Gradients, Gradient SHAP, Permutation SHAP, and Kernel SHAP in production forecasting contexts such as CCAR and CECL exercises.
- Provides a practical framework for selecting attribution methods based on input scale, hybrid run feasibility, interpretability, reproducibility, and governance requirements.

## Archivist Review

No concepts proposed as the paper explores the application and comparison of existing attribution methods (Shapley values, Integrated Gradients, etc.) to forecasting runs rather than introducing a novel reusable architectural component or method.

## Links

- [Abstract](https://arxiv.org/abs/2608.04547)
- [PDF](https://arxiv.org/pdf/2608.04547)

