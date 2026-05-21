---
# CSL-compatible fields
title: "Sequential Structure in Intraday Futures Data: LSTM vs Gradient Boosting on MNQ"
author:
  - literal: "Mathias Mesfin"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17724"

# Custom fields
paper_id: "2605.17724"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:40:23Z"
created_at: "2026-05-21T08:40:23Z"
---

# Sequential Structure in Intraday Futures Data: LSTM vs Gradient Boosting on MNQ

**Authors**: Mathias Mesfin
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17724](https://arxiv.org/abs/2605.17724)

## Summary

This paper investigates the predictability of intraday directional movements in Micro E-Mini Nasdaq 100 (MNQ) futures using OHLCV data. By comparing LSTM and gradient boosting architectures through expanding-window walk-forward validation, the study assesses whether sequential structures are exploitable at this scale. The findings reveal that none of the models significantly outperform the base rate, suggesting that four years of single-instrument data are insufficient for reliable sequential forecasting. This work serves as an important empirical study on the limitations of applying modern sequence models to constrained financial datasets.

## Key Contributions

- Provides a rigorous empirical evaluation of LSTM and Gradient Boosting for intraday directional prediction on MNQ futures using 944 days of OHLCV data.
- Demonstrates that neither LSTM nor gradient boosting achieves statistically significant out-of-sample predictive edge over the base rate, indicating noise fitting rather than stable structural signal capture.
- Establishes an empirical lower bound on data scale requirements for applying sequential foundation models to single-instrument financial time series.

## Links

- [Abstract](https://arxiv.org/abs/2605.17724)
- [PDF](https://arxiv.org/pdf/2605.17724)

