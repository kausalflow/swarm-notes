---
# CSL-compatible fields
title: "When the Fed Speaks: Dynamics and Forecasts of the Volatility Surface"
author:
  - literal: "Lukasz Adamski"
  - literal: "Robert Slepaczuk"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10693"

# Custom fields
paper_id: "2608.10693"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "convolutional-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:27Z"
created_at: "2026-08-14T06:07:27Z"
---

# When the Fed Speaks: Dynamics and Forecasts of the Volatility Surface

**Authors**: Lukasz Adamski, Robert Slepaczuk
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10693](https://arxiv.org/abs/2608.10693)

## Summary

This paper investigates the evolution and forecasting of implied volatility (IV) surfaces around scheduled Federal Open Market Committee (FOMC) meetings. The authors examine whether IV increases prior to announcements, observing stronger effects for short-dated, out-of-the-money options in high-volatility regimes. To capture these dynamics without dimensionality reduction, they employ a convolutional two-dimensional LSTM augmented with exogenous meeting date features. The results indicate that while noise in the IV surface limits the margin over random walk benchmarks, machine learning models remain effective at forecasting volatility during abnormal market conditions.

## Key Contributions

- Quantitatively analyzes the pre-announcement effect of FOMC scheduled meetings on implied volatility (IV) surfaces across moneyness and maturity.
- Demonstrates a machine learning framework incorporating FOMC exogenous date features to forecast IV surfaces directly without dimensionality reduction.
- Applies a convolutional two-dimensional LSTM architecture to learn spatio-temporal signals directly from volatility surfaces.
- Evaluates the forecasting performance of the ML framework against a random walk benchmark, showing robustness during abnormal high-uncertainty days.

## Limitations

The edge of the ML framework can be limited due to the inherent noisy characteristics of the implied volatility surface.

## Archivist Review

Strictly applied the selectivity policy, rejecting both the paper-specific model combination concept and the routine feature-expansion open question to keep the knowledge vault focused on high-impact, broadly reusable insights.

### Rejected Candidates
- [concept] Convolutional 2D LSTM for Volatility Surface Forecasting (`convolutional-2d-lstm-volatility-surface`) - not_reusable: A convolutional 2D LSTM applied to financial surfaces is a specific architecture combination rather than a widely reusable standalone vault concept.
- [open_question] Broadening Macroeconomic Exogenous Features (`macro-exogenous-features-iv-surface`) - low_impact: The open question essentially suggests adding more exogenous variables and attention mechanisms, which is a routine model expansion direction rather than a foundational unresolved bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.10693)
- [PDF](https://arxiv.org/pdf/2608.10693)

