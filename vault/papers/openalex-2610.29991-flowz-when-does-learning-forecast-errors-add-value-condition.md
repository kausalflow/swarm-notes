---
# CSL-compatible fields
title: "Flowz: When Does Learning Forecast Errors Add Value? Conditional Flow Matching for Financial Price Forecasts"
author:
  - literal: "Giancarlo Vercellino"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29991"

# Custom fields
paper_id: "2610.29991"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "probabilistic-forecast"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "flowz"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:11:58Z"
created_at: "2026-10-24T09:11:58Z"
---

# Flowz: When Does Learning Forecast Errors Add Value? Conditional Flow Matching for Financial Price Forecasts

**Authors**: Giancarlo Vercellino
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29991](https://arxiv.org/abs/2610.29991)

## Summary

This paper introduces Flowz, a conditional flow model of direct multi-step price-level residuals fitted using random features and ridge regression to improve forecasting models. Evaluated across 24 US stocks, multiple horizons, and standard baselines including EWMA and ARIMA, Flowz reduces mean CRPS by up to 30.7% at farther horizons when paired with drifting specifications like EWMA, whereas stationary baselines degrade.

## Key Contributions

- Introduces Flowz, a conditional flow model for learning direct multi-step price-level residuals using random features and ridge regression.
- Demonstrates that Flowz reduces mean CRPS by 30.7% against EWMA and 24.0% against Gaussian residual controls at farther horizons across 24 US stocks.
- Reveals that conditional residual learning improves drifting specifications like EWMA at longer horizons while worsening stationary statistical baselines like ARIMA and ARFIMA.

## Limitations

ARIMA, ARFIMA, and structural extensions worsen when combined with conditional residual learning compared to baseline comparators.

## Open Questions & Future Work

- [[adapting-conditional-flow-matching-to-parametric-baselines]]

## Key Concepts

- [[flowz]]: A conditional flow model of direct multi-step price-level residuals fitted using random features and ridge regression.

## Archivist Review

Approved the central 'Flowz' concept as a reusable conditional flow residual modeling method and the explicit open question regarding adapting flow matching to stationary/parametric baselines. Followed strict scarcity principles and applied all domain-specific review standards.

### Approved Concepts
- Flowz: Flowz is the central generative residual modeling approach proposed to conditionalize and improve forecasting errors across multiple horizons.

### Approved Open Questions
- Adapting Flow Matching to Parametric Baselines: Understanding why residual flow matching fails on certain linear and structural baselines while succeeding on EWMA is critical for generalizing probabilistic residual learning across time-series forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2610.29991)
- [PDF](https://arxiv.org/pdf/2610.29991)

