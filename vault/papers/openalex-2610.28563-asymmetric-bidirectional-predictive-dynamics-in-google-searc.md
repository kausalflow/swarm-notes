---
# CSL-compatible fields
title: "Asymmetric Bidirectional Predictive Dynamics in Google Search and COVID-19 Time Series: A Multi-Horizon Forecast-Error Analysis"
author:
  - literal: "Andrei Velichko"
  - literal: "Imen Mahmoud"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28563"

# Custom fields
paper_id: "2610.28563"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forecast-error-distribution-entropy"
  - "directional-predictive-response-strength"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:39:41Z"
created_at: "2026-10-23T09:39:41Z"
---

# Asymmetric Bidirectional Predictive Dynamics in Google Search and COVID-19 Time Series: A Multi-Horizon Forecast-Error Analysis

**Authors**: Andrei Velichko, Imen Mahmoud
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28563](https://arxiv.org/abs/2610.28563)

## Summary

This paper investigates asymmetric bidirectional predictive dynamics between Google Trends and COVID-19 time series using rolling LightGBM forecasts across 1-14 day horizons. By combining log-RMSE gain with forecast-error distribution entropy (FEDE) and introducing a persistence-weighted directional predictive response strength (DPRS) score, the authors demonstrate that predictive relationships are frequently asymmetric, metric-dependent, and horizon-sensitive. The findings highlight that forecast accuracy and error-distribution dynamics provide complementary insights into digital trace analysis without implying direct causality.

## Key Contributions

- Examines eight pre-specified Google Trends and COVID-19 time series pairs using LightGBM across rolling 400-day windows and 1-14 day horizons.
- Combines log-RMSE gain with forecast-error distribution entropy (FEDE) to capture horizon-dependent changes in signed error distributions.
- Introduces Directional Predictive Response Strength (DPRS), a relative persistence-weighted score on a 0-100 scale for screening candidate predictive directions.
- Demonstrates that predictive effects are highly asymmetric, direction- and metric-dependent, and vary across forecasting horizons.

## Limitations

Aggregated regime-level patterns should not be extrapolated to individual time points or interpreted as direct evidence of causality.

## Open Questions & Future Work

- [[surrogate-null-models-epidemiological-search]]

## Key Concepts

- [[forecast-error-distribution-entropy]]: A metric capturing horizon-dependent changes in signed forecast-error distributions for multi-horizon time series analysis.
- [[directional-predictive-response-strength]]: A persistence-weighted scoring mechanism on a 0-100 scale for ranking directional predictive relationships across horizons.

## Archivist Review

The selected concepts (Forecast-Error Distribution Entropy and Directional Predictive Response Strength) introduce reusable, rigorous metrics for evaluating directional multi-horizon predictive dynamics beyond standard point errors. The open question targets an important validation bottleneck in observational time series analysis regarding surrogate-based null models. No external named datasets qualify for permanent vault insertion.

### Approved Concepts
- Forecast-Error Distribution Entropy: Introduces a novel metric capturing horizon-dependent changes in signed error distributions for multi-horizon time series analysis.
- Directional Predictive Response Strength: Provides a persistence-weighted scoring mechanism to rank directional predictive relationships across multiple horizons.

### Approved Open Questions
- Surrogate Null Models for Search Dynamics: Important for separating genuine information signals from spurious temporal correlations driven by seasonality or shared external confounding in digital epidemiology and time-series analysis.

## Links

- [Abstract](https://arxiv.org/abs/2610.28563)
- [PDF](https://arxiv.org/pdf/2610.28563)

