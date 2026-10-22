---
# CSL-compatible fields
title: "Almost Uniform Bias Correction for Persistent Panel Local Projections"
author:
  - literal: "Geert Dhaene"
  - literal: "Artūras Juodis"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26427"

# Custom fields
paper_id: "2610.26427"
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
processed_at: "2026-10-22T09:45:05Z"
created_at: "2026-10-22T09:45:05Z"
---

# Almost Uniform Bias Correction for Persistent Panel Local Projections

**Authors**: Geert Dhaene, Artūras Juodis
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26427](https://arxiv.org/abs/2610.26427)

## Summary

This paper investigates the properties of fixed-effect estimators and bias-correction methods in panel local projections for policy analysis, specifically in settings with autoregressive control variables and persistent series. The authors analyze estimator bias and variance, showing that the half-panel jackknife provides robust bias-reduction beyond stationarity. They recommend using bias-correction-adjusted standard errors to properly account for sampling uncertainty from the half-panel jackknife estimator across various time-series dimensions.

## Key Contributions

- Analyzes the bias and variance of fixed-effect estimators and bias-correction methods in panel local projections with autoregressive control variables and persistent series.
- Demonstrates that the half-panel jackknife possesses desirable bias-reducing properties beyond standard stationary settings.
- Recommends bias-correction-adjusted standard errors to account for sampling uncertainty associated with the half-panel jackknife estimator regardless of the time-series dimension.

## Open Questions & Future Work

- [[generalizing-panel-lp-bias-correction]]

## Archivist Review

Applied strict selectivity standards. No core forecasting mechanisms or reusable time-series concepts were proposed that warrant permanent vault notes, and no datasets were provided. One open question on generalizing panel local projection bias correction was approved as it targets a specific methodological gap in econometric panel data models.

### Approved Open Questions
- Generalizing Panel LP Bias Correction: Extending bias correction and valid inference methods to richer, more realistic panel local projection specifications is crucial for empirical macroeconomics where structural shocks are unobserved or estimated via panel VARs.

## Links

- [Abstract](https://arxiv.org/abs/2610.26427)
- [PDF](https://arxiv.org/pdf/2610.26427)

