---
# CSL-compatible fields
title: "Analysis of Uncertain GARCH Model with the application of crude oil future prices"
author:
  - literal: "Zhihong Yin"
  - literal: "Zhiming Li"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37071"

# Custom fields
paper_id: "2610.37071"
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
processed_at: "2026-10-30T11:04:58Z"
created_at: "2026-10-30T11:04:58Z"
---

# Analysis of Uncertain GARCH Model with the application of crude oil future prices

**Authors**: Zhihong Yin, Zhiming Li
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37071](https://arxiv.org/abs/2610.37071)

## Summary

This paper introduces the uncertain generalized autoregressive conditional heteroskedasticity (UGARCH) model to capture time-varying volatility, persistence, and variance dynamics in uncertain time series environments. The authors prove mean stationarity conditions for the variance process, develop recursive constrained least squares estimation alongside cross-validation order selection, and formulate uncertain hypothesis tests. Through numerical simulations and an empirical study on West Texas Intermediate crude oil futures prices, the proposed UGARCH model demonstrates superior conditional-variance fitting and robust point and interval forecasting capabilities compared to traditional UARCH baselines.

## Key Contributions

- Develops an uncertain generalized autoregressive conditional heteroskedasticity (UGARCH) model incorporating lagged conditional variance terms under uncertain measures.
- Proves sufficient conditions for the mean stationarity of the variance process and proposes recursive constrained least squares for parameter estimation.
- Introduces uncertain hypothesis tests for model effect detection and goodness-of-fit assessment, supported by both numerical simulations and empirical evaluation on West Texas Intermediate crude oil futures prices.

## Open Questions & Future Work

- [[asymmetric-ugarch-model-extensions]]

## Archivist Review

The paper introduces the uncertain GARCH (UGARCH) model for volatility estimation under uncertainty theory. While the UGARCH framework itself is specific to uncertainty theory and lacks broad machine learning reusability outside of specialized econometric modeling, the open question regarding asymmetric extensions of volatility models under uncertainty captures a valuable structural research direction.

### Approved Open Questions
- Asymmetric UGARCH Model Extensions: Capturing leverage and asymmetry effects is crucial for financial volatility forecasting and risk management under uncertainty theory, mirroring the historical evolution of classical GARCH models into EGARCH and GJR-GARCH.

## Links

- [Abstract](https://arxiv.org/abs/2610.37071)
- [PDF](https://arxiv.org/pdf/2610.37071)

