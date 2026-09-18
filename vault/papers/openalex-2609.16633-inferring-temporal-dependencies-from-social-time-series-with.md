---
# CSL-compatible fields
title: "Inferring Temporal Dependencies from Social Time Series with the Cross-Correlogram"
author:
  - literal: "Bridget Smart"
  - literal: "Renaud Lambiotte"
  - literal: "Takaaki Aoki"
  - literal: "Ryota Kobayashi"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16633"

# Custom fields
paper_id: "2609.16633"
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
  - "cross-correlogram-temporal-dependency-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:06Z"
created_at: "2026-09-18T09:17:06Z"
---

# Inferring Temporal Dependencies from Social Time Series with the Cross-Correlogram

**Authors**: Bridget Smart, Renaud Lambiotte, Takaaki Aoki, Ryota Kobayashi
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16633](https://arxiv.org/abs/2609.16633)

## Summary

This paper adapts the cross-correlogram technique to characterize temporal dependencies in social time series by introducing a smooth intensity correction that mitigates biases caused by periodic rhythms and non-stationarity. Through theoretical analysis, simulations, and an application to 3.1 million events on X (Twitter), the authors show that their method accurately uncovers lagged temporal relationships that conventional Granger causality and co-occurrence measures miss.

## Key Contributions

- Proposes an adapted cross-correlogram method incorporating smooth intensity functions to correct for periodic bias in social time series.
- Demonstrates theoretically and via simulation that the proposed estimator outperforms interval-jitter and Granger causality methods in periodic regimes.
- Applies the method to 3.1 million event times from X (Twitter), revealing delayed temporal relationships aligned with broadcast schedules.

## Key Concepts

- [[cross-correlogram-temporal-dependency-estimation]]: An adapted cross-correlogram method that integrates functional behavioral models with temporal response profiling to correct for periodic biases in social time series.

## Archivist Review

Approved the core concept of adapting cross-correlograms for periodic bias correction in social time series. No other concepts or datasets met the strict novelty and reusability standards.

### Approved Concepts
- Cross-Correlogram Temporal Dependency Estimation: Provides a robust alternative to Granger causality for bursty and non-stationary social time series by correcting for periodic biases.

## Links

- [Abstract](https://arxiv.org/abs/2609.16633)
- [PDF](https://arxiv.org/pdf/2609.16633)

