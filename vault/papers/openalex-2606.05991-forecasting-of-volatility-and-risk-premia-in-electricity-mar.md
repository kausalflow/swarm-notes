---
# CSL-compatible fields
title: "Forecasting of volatility and risk premia in electricity markets"
author:
  - literal: "Thomas K. Kloster"
  - literal: "Fred Espen Benth"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.05991"

# Custom fields
paper_id: "2606.05991"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "parsimonious-matrix-har-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:19:04Z"
created_at: "2026-06-07T08:19:04Z"
---

# Forecasting of volatility and risk premia in electricity markets

**Authors**: Thomas K. Kloster, Fred Espen Benth
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.05991](https://arxiv.org/abs/2606.05991)

## Summary

This paper addresses the challenge of forecasting realized covariation in electricity markets by modeling it as a matrix-valued representation of a latent infinite-dimensional covariance operator. The authors introduce a parsimonious matrix-HAR model and demonstrate that utilizing information from renewable generation and extended time horizons enhances predictive accuracy. Furthermore, empirical results indicate that these volatility forecasts significantly outperform standard backward-looking methods in the prediction of electricity forward market risk premia.

## Key Contributions

- Constructed a parsimonious matrix-HAR model to forecast latent infinite-dimensional realized covariation in electricity markets.
- Demonstrated that incorporating longer time horizons and renewable generation data significantly improves one-week ahead volatility forecasts.
- Showed that the proposed variance forecasts yield superior performance in predicting spread risk premia in forward electricity markets compared to backward-looking statistical benchmarks.

## Open Questions & Future Work

- [[electricity-volatility-skewness-limitations]]

## Key Concepts

- [[parsimonious-matrix-har-model]]: A matrix-valued HAR (Heterogeneous Autoregressive) variant for forecasting latent infinite-dimensional covariance operators in electricity markets.

## Archivist Review

I approved the Matrix-HAR model as it represents a meaningful extension of classical time-series techniques to matrix-valued latent operators. The open question was renamed for clarity and adherence to standard nomenclature. Other candidates were rejected to maintain the high selective threshold of the vault.

### Approved Concepts
- Parsimonious Matrix-HAR Model: It provides a tractable, matrix-valued approach to capturing latent covariance structures, extending standard univariate HAR frameworks.

### Approved Open Questions
- Electricity Volatility Skewness Limitations: Addressing this limitation is crucial for improving tail-risk estimation and risk premia forecasting in highly volatile markets.

### Rejected Candidates
- [open_question] Modeling Skewness in Electricity Volatility (`volatility-skewness-modeling-crisis`) - duplicate_existing: Renamed to electricity-volatility-skewness-limitations for better conciseness and alignment with existing vault naming standards.

## Links

- [Abstract](https://arxiv.org/abs/2606.05991)
- [PDF](https://arxiv.org/pdf/2606.05991)

