---
# CSL-compatible fields
title: "Conformal prediction for functional time series: Application to age-specific mortality rates"
author:
  - literal: "Han Lin Shang"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29296"

# Custom fields
paper_id: "2605.29296"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "conformal-prediction"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "conformal-prediction-for-functional-time-series"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:08:45Z"
created_at: "2026-05-31T08:08:45Z"
---

# Conformal prediction for functional time series: Application to age-specific mortality rates

**Authors**: Han Lin Shang
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29296](https://arxiv.org/abs/2605.29296)

## Summary

This paper addresses the limitations of model-based uncertainty quantification in demographic forecasting by applying conformal prediction to functional time series. The author proposes both split and sequential conformal prediction methods, which provide model-agnostic and distribution-free prediction intervals. By validating these approaches using Australian age- and sex-specific mortality rates, the study shows that these procedures improve interval forecast accuracy and ensure finite-sample validity.

## Key Contributions

- Introduces a model-agnostic conformal prediction framework for generating finite-sample valid prediction intervals in functional time series.
- Develops both split conformal prediction and sequential conformal prediction methods for demographic forecasting.
- Demonstrates that conformal prediction effectively calibrates empirical coverage probabilities for Australian age- and sex-specific mortality rates.

## Open Questions & Future Work

- [[conformal-prediction-structural-breaks]]

## Key Concepts

- [[conformal-prediction-for-functional-time-series]]: A model-agnostic, distribution-free framework for generating finite-sample valid prediction intervals for functional time series.

## Archivist Review

The concept of conformal prediction for functional data provides a useful extension of traditional conformal methods to high-dimensional objects. The open question regarding performance under structural breaks identifies a fundamental limitation in applying these exchangeability-based methods to non-stationary real-world processes.

### Approved Concepts
- Conformal prediction for functional time series: It provides a model-agnostic and distribution-free approach to uncertainty quantification in functional data, which is increasingly relevant in time-series analysis.

### Approved Open Questions
- Conformal prediction under non-stationarity: Reliable uncertainty quantification is essential for high-stakes forecasting, and quantifying the degradation of conformal coverage under non-stationarity is a critical open challenge.

## Links

- [Abstract](https://arxiv.org/abs/2605.29296)
- [PDF](https://arxiv.org/pdf/2605.29296)

