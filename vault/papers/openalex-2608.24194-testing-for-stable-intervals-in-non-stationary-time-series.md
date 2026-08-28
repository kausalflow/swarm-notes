---
# CSL-compatible fields
title: "Testing for Stable Intervals in Non-Stationary Time Series"
author:
  - literal: "Florian Heinrichs"
issued:
  date-parts:
    - [2026, 8, 25]
url: "https://arxiv.org/abs/2608.24194"

# Custom fields
paper_id: "2608.24194"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:15Z"
created_at: "2026-08-28T16:59:15Z"
---

# Testing for Stable Intervals in Non-Stationary Time Series

**Authors**: Florian Heinrichs
**Date**: 2026-08-25
**Paper ID**: [openalex:2608.24194](https://arxiv.org/abs/2608.24194)

## Summary

This paper introduces an econometric and statistical testing framework for identifying stable intervals within non-stationary time series under dependent, locally stationary errors. By formulating stability over duration delta using a supremum-infimum functional on signals derived from local linear regression, the author constructs plug-in tests whose asymptotic distribution is driven by near-extremal windows. The resulting methodology handles time-varying long-run variance and derivative-based hypotheses, providing consistent tests with valid level control for physiological and engineering applications.

## Key Contributions

- Formulates an existence test for stable intervals of duration delta within non-stationary regression models with dependent locally stationary errors.
- Employs local linear regression to estimate the signal functional and derives Gaussian and extreme value approximations for kernel estimators over shrinking index sets with time-varying long-run variance.
- Demonstrates asymptotic consistency, asymptotic level control, and applicability to physiological and engineering time series.

## Archivist Review

Reviewed the candidate open question and rejected it because it targets paper-specific theoretical extensions under smoothness assumptions rather than a high-impact, reusable ML research bottleneck. No concepts or datasets were proposed.

### Rejected Candidates
- [open_question] Piecewise Smooth Stable Interval Testing (`piecewise-smooth-stable-interval-testing`) - low_impact: The proposed question addresses an incremental theoretical extension (piecewise smooth functions and variance structures) that is standard future work for asymptotic testing frameworks and does not represent a foundational cross-cutting bottleneck for machine learning time series architectures.

## Links

- [Abstract](https://arxiv.org/abs/2608.24194)
- [PDF](https://arxiv.org/pdf/2608.24194)

