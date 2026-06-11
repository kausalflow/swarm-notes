---
# CSL-compatible fields
title: "Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data"
author:
  - literal: "Xinyue Fang"
  - literal: "Robert Ślepaczuk"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09478"

# Custom fields
paper_id: "2606.09478"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "machine-learning"
  - "finance"
architectures:
  []
datasets:
  - "csi-300-index"
concept_slugs:
  - "regime-augmented-harq"
dataset_slugs:
  - "csi-300-index"
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:50Z"
created_at: "2026-06-11T09:07:50Z"
---

# Volatility Forecasting and Return Prediction under Market Regimes: Evidence from High-Frequency Chinese Equity Data

**Authors**: Xinyue Fang, Robert Ślepaczuk
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09478](https://arxiv.org/abs/2606.09478)

## Summary

This paper develops a two-stage financial forecasting framework that combines econometric volatility modeling with machine-learning return prediction. By incorporating Markov-switching GJR-GARCH filtering into HARQ specifications, the authors effectively capture long-memory and regime-dependent volatility dynamics. Empirical analysis using CSI 300 high-frequency data reveals that while unconditional return prediction remains weak, integrating regime-aware volatility forecasts into defensive trading strategies significantly improves economic performance after accounting for transaction costs.

## Key Contributions

- Introduces a sequential two-stage framework that integrates regime-aware volatility modeling (HARQ-MSGARCH) with machine-learning return prediction (XGBoost).
- Demonstrates that regime-aware volatility forecasting consistently outperforms baseline HARQ models using high-frequency Chinese equity data.
- Shows that return predictability is state-dependent and concentrated in low-volatility regimes, emphasizing the importance of turnover controls and volatility scaling for economic viability.

## Open Questions & Future Work

- [[bridging-statistical-predictability-economic-value]]

## Key Concepts

- [[regime-augmented-harq]]: A volatility modeling specification that integrates HARQ with Markov-switching mechanisms to capture market structural changes and long-memory dependencies.

## Archivist Review

I approved the Regime-augmented HARQ concept for its methodological contribution to capturing regime-dependent long-memory volatility and the open question regarding the predictability-to-economic-value gap, as it identifies a fundamental, non-trivial research challenge in financial time series. I approved the CSI 300 Index dataset as it is the central, high-frequency empirical testbed for the paper's framework. All items were evaluated against the requirement for cross-domain and long-term research utility.

### Approved Concepts
- Regime-augmented HARQ: It serves as the core econometrically grounded feature engineering for the first stage of the proposed framework, enabling the capture of complex financial time series dynamics.

### Approved Open Questions
- Bridging Predictability and Economic Value: This question is critical because it addresses the persistent gap between statistical predictive success and economic utility, which is the primary challenge in applying machine learning to real-world asset management.

## Datasets

- [[csi-300-index]]

## Links

- [Abstract](https://arxiv.org/abs/2606.09478)
- [PDF](https://arxiv.org/pdf/2606.09478)

