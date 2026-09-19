---
# CSL-compatible fields
title: "Conditional Independence Testing in Time Series"
author:
  - literal: "Jieru Shi"
  - literal: "Rajen D. Shah"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20772"

# Custom fields
paper_id: "2609.20772"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-discovery"
  - "statistical-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "generalised-temporal-covariance-measure-gtcm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:03:24Z"
created_at: "2026-09-19T09:03:24Z"
---

# Conditional Independence Testing in Time Series

**Authors**: Jieru Shi, Rajen D. Shah
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20772](https://arxiv.org/abs/2609.20772)

## Summary

The paper addresses the problem of testing Granger causality in time series through model-free conditional independence testing. It introduces the Generalised Temporal Covariance Measure (GTCM), a test statistic calculated from the sample covariance of residuals after nonlinearly regressing outcomes and exposures on conditioning histories. By incorporating variance weights, polynomial lag expansions, and leveraging regression stability and weak dependence, the method achieves robust type I error control and high statistical power without data splitting.

## Key Contributions

- Proposes a model-free conditional independence testing framework for time series to test Granger causality without relying on restrictive linear vector autoregressive assumptions.
- Introduces the Generalised Temporal Covariance Measure (GTCM) test statistic based on the sample covariance of residuals from nonlinear regressions of outcomes and exposures on joint histories.
- Incorporates variance weights and data-adaptive polynomial lag expansions to handle heteroscedasticity and improve statistical power against local alternatives.
- Establishes valid type I error control under weak nonparametric convergence conditions and utilizes the entire dataset without time-series data splitting via stability and weak dependence assumptions.

## Open Questions & Future Work

- [[conditional-independence-testing-time-series-extensions]]

## Key Concepts

- [[generalised-temporal-covariance-measure-gtcm]]: A test statistic based on the sample covariance of residuals from nonlinear regressions for testing Granger causality in time series.

## Archivist Review

Approved the core Generalised Temporal Covariance Measure (GTCM) concept and its associated open question regarding extensions to nonstationary and high-dimensional settings. Rejected no other items as no extra candidates were provided.

### Approved Concepts
- Generalised Temporal Covariance Measure (GTCM): Central test statistic proposed in the paper for model-free conditional independence testing in time series.

### Approved Open Questions
- Extensions of Time Series Conditional Independence Testing: Extending conditional independence testing beyond current stationarity and low-dimensional conditioning constraints is critical for broad applicability in real-world complex systems like climate science and macroeconomics.

## Links

- [Abstract](https://arxiv.org/abs/2609.20772)
- [PDF](https://arxiv.org/pdf/2609.20772)

