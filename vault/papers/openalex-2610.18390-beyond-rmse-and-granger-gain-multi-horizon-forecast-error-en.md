---
# CSL-compatible fields
title: "Beyond RMSE and Granger Gain: Multi-Horizon Forecast-Error Entropy for Nonlinear Predictive Coupling"
author:
  - literal: "Andrei Velichko"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.18390"

# Custom fields
paper_id: "2610.18390"
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
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:23:37Z"
created_at: "2026-10-16T09:23:37Z"
---

# Beyond RMSE and Granger Gain: Multi-Horizon Forecast-Error Entropy for Nonlinear Predictive Coupling

**Authors**: Andrei Velichko
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.18390](https://arxiv.org/abs/2610.18390)

## Summary

This paper introduces the forecast-error distribution entropy (FEDE) predictive-causality framework to determine whether an auxiliary time series provides predictive information about a target beyond its own history. By quantifying how the full signed forecast-error distribution changes across horizons, FEDE robustly identifies nonlinear dependencies where standard log-RMSE gains and conventional Granger methods fail or show model-form dependence. Experiments across multiple nonlinearities, noise levels, and window configurations demonstrate that FEDE consistently captures predictive coupling under unknown interaction forms.

## Key Contributions

- Introduced the forecast-error distribution entropy (FEDE) predictive-causality framework to quantify signed forecast-error distribution changes across horizons.
- Demonstrated that LightGBM successfully recovers hidden nonlinear source-target channels while Ridge fails.
- Showed that FEDE remains positively aligned across all 108 tested hyperparameter combinations of window length, history length, and maximum forecast horizon.
- Established FEDE as a sensitive, horizon-resolved tool outperforming conventional log-RMSE gains under unknown nonlinear interaction forms.

## Limitations

Evaluated on controlled nonlinear benchmarks and synthetic/stochastic setups; broader empirical verification on massive real-world corpora remains future work.

## Open Questions & Future Work

- [[observational-data-validation-fede]]

## Key Concepts

- [[forecast-error-distribution-entropy]]: A predictive-causality framework that quantifies how the full signed forecast-error distribution changes across prediction horizons to capture nonlinear auxiliary information.

## Archivist Review

Approved the core forecast-error distribution entropy (FEDE) concept and its associated observational validation open question as they directly capture the paper's principal methodological contribution and explicitly defined future work. No datasets or additional subcomponents met the high bar for permanent vault storage.

### Approved Concepts
- Forecast-Error Distribution Entropy: Central methodological contribution quantifying signed forecast-error distribution changes across horizons for predictive causality.

### Approved Open Questions
- Observational Data Validation of FEDE: Crucial for establishing the practical utility and limitations of new machine learning forecasting diagnostics in real-world domains beyond synthetic benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2610.18390)
- [PDF](https://arxiv.org/pdf/2610.18390)

