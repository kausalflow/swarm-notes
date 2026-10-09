---
# CSL-compatible fields
title: "Towards Calibrated Probabilistic Forecasts for Events of Interest via Outcome-Conditional Recalibration"
author:
  - literal: "Jakob Benjamin Wessel"
  - literal: "Sam Allen"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10076"

# Custom fields
paper_id: "2610.10076"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "outcome-conditional-recalibration"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:50Z"
created_at: "2026-10-09T11:35:50Z"
---

# Towards Calibrated Probabilistic Forecasts for Events of Interest via Outcome-Conditional Recalibration

**Authors**: Jakob Benjamin Wessel, Sam Allen
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10076](https://arxiv.org/abs/2610.10076)

## Summary

This paper introduces outcome-conditional recalibration, a post-hoc method designed to calibrate probabilistic predictions on user-defined regions of the outcome space, addressing the limitation that standard methods conceal miscalibration in critical regions such as extreme events. The approach combines quantile recalibration for conditional distributions with rescaling to match empirical occurrence frequencies. Experiments on regression benchmarks and day-ahead electricity price forecasting demonstrate superior calibration for events like negative prices without sacrificing overall forecast accuracy.

## Key Contributions

- Introduces outcome-conditional recalibration, a post-hoc method enabling valid and continuous probabilistic predictions calibrated on user-defined regions of the outcome space.
- Demonstrates that existing unconditional and conditional recalibration schemes fail to ensure calibration on specific subsets of outcomes like extremes.
- Shows improved outcome-conditional calibration across regression benchmarks while retaining competitive overall calibration.
- Applies the approach to day-ahead electricity price forecasting, substantially improving calibration for negative prices with negligible loss in accuracy.

## Open Questions & Future Work

- [[outcome-conditional-vs-auto-calibration]]

## Key Concepts

- [[outcome-conditional-recalibration]]: A post-hoc recalibration method designed to generate calibrated probabilistic predictions on user-defined regions of the outcome space.

## Archivist Review

We approved the core methodological concept 'Outcome-Conditional Recalibration' as it provides a reusable, post-hoc technique for targeting specific subsets or extreme events in probabilistic forecasting. We also approved the corresponding open question concerning its theoretical relationship with auto-calibration. No datasets were approved because none were explicitly named or introduced as core reusable benchmarks.

### Approved Concepts
- Outcome-Conditional Recalibration: It is the core methodological contribution of the paper, enabling post-hoc calibration on user-defined regions of interest such as extreme events.

### Approved Open Questions
- Connections Between Outcome-Conditional and Auto-Calibration: Clarifying these theoretical relationships bridges disparate hierarchies of calibration concepts in regression and helps determine whether general conditional calibration frameworks can automatically guarantee reliable tail and event-of-interest forecasting without specialized localized recalibration.

## Links

- [Abstract](https://arxiv.org/abs/2610.10076)
- [PDF](https://arxiv.org/pdf/2610.10076)

