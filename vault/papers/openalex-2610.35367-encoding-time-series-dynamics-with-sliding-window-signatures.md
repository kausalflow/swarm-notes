---
# CSL-compatible fields
title: "Encoding Time Series Dynamics with Sliding-Window Signatures for Online Forecasting"
author:
  - literal: "Nina Drobac"
  - literal: "Margaux Brégère"
  - literal: "Joseph de Vilmarest"
  - literal: "Olivier Wintenberger"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35367"

# Custom fields
paper_id: "2610.35367"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "online-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:02Z"
created_at: "2026-10-29T11:10:02Z"
---

# Encoding Time Series Dynamics with Sliding-Window Signatures for Online Forecasting

**Authors**: Nina Drobac, Margaux Brégère, Joseph de Vilmarest, Olivier Wintenberger
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35367](https://arxiv.org/abs/2610.35367)

## Summary

This paper introduces an online forecasting framework designed for non-stationary time series with evolving relationships between targets and exogenous variables. The approach first encodes input path dynamics using sliding-window signatures to capture nonlinear, path-dependent effects. Next, a regularized linear model is updated online via a Kalman filter to track dynamic coefficients. Finally, multi-scale temporal dependencies are captured by combining forecasters of varying window lengths through online aggregation, achieving superior performance on French national electricity load forecasting and competitive results across benchmark datasets.

## Key Contributions

- Proposes encoding input path dynamics over sliding windows using signatures to capture nonlinear, path-dependent effects in non-stationary time series.
- Employs a regularized linear regression updated online via a Kalman filter to track evolving dynamic relationships.
- Combines forecasters built on multi-scale window lengths through online aggregation to capture dependencies at several time scales.
- Outperforms state-of-the-art approaches on French national electricity load forecasting and remains competitive across several benchmark datasets with exogenous variables.

## Archivist Review

No candidate concepts, datasets, or open questions were provided in the paper analysis payload. Therefore, all lists are empty and no notes are added to the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.35367)
- [PDF](https://arxiv.org/pdf/2610.35367)

