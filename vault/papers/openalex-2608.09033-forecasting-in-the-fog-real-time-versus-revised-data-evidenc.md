---
# CSL-compatible fields
title: "Forecasting in the Fog: Real-Time versus Revised-Data Evidence on Machine Learning's Edge over the Phillips Curve"
author:
  - literal: "Louis Agyekum"
  - literal: "Obed Obese"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09033"

# Custom fields
paper_id: "2608.09033"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:30Z"
created_at: "2026-08-13T06:09:30Z"
---

# Forecasting in the Fog: Real-Time versus Revised-Data Evidence on Machine Learning's Edge over the Phillips Curve

**Authors**: Louis Agyekum, Obed Obese
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09033](https://arxiv.org/abs/2608.09033)

## Summary

This paper investigates whether machine learning's predictive edge over the Phillips curve in inflation forecasting survives when models are trained and evaluated on real-time data vintages rather than fully revised series, and whether SHAP feature importances are artifacts of in-sample estimation. Using 2000-2026 U.S. data, the authors find that real-time and revised accuracy differences are largely negligible, but out-of-sample SHAP analysis reveals massive shifts in feature importance—such as PCE inflation dominance disappearing in real-time data—showing that retrospective fits heavily bias feature attribution.

## Key Contributions

- Evaluates whether machine learning inflation forecasting advantages over the Phillips curve persist under real-time (ALFRED) data vintages versus fully revised series across 3-, 6-, and 12-month horizons.
- Demonstrates that real-time and revised accuracy differences are generally small and statistically indistinguishable under Diebold-Mariano tests, with Gradient Boosting showing consistent positive skill only at longer horizons.
- Reveals a dramatic discrepancy in walk-forward out-of-sample SHAP feature importance between revised and real-time data, exposing PCE inflation dominance as a hindsight artifact.
- Introduces a Relative Skill Index (RSI) to summarize accuracy gaps across models and horizons for auditing machine learning inflation forecasts.

## Limitations

Limited to U.S. macroeconomic series (unemployment, CPI, PCE, payrolls, real GDP, Treasury spread) and specific traditional versus machine learning models evaluated over 2000-2026.

## Links

- [Abstract](https://arxiv.org/abs/2608.09033)
- [PDF](https://arxiv.org/pdf/2608.09033)

