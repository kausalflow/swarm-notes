---
# CSL-compatible fields
title: "A distributional modelling approach with application to electricity price forecasting"
author:
  - literal: "Aitor Ciarreta"
  - literal: "Peru Muniain"
  - literal: "Ainhoa Zarraga"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01465"

# Custom fields
paper_id: "2610.01465"
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
processed_at: "2026-10-04T10:49:08Z"
created_at: "2026-10-04T10:49:08Z"
---

# A distributional modelling approach with application to electricity price forecasting

**Authors**: Aitor Ciarreta, Peru Muniain, Ainhoa Zarraga
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01465](https://arxiv.org/abs/2610.01465)

## Summary

This paper investigates distributional modeling for electricity price forecasting by applying the Generalised Additive Models for Location, Scale and Shape (GAMLSS) framework to Spanish day-ahead market data from 2020 to 2024. The authors evaluate Normal, Johnson's SU (JSU), and Sinh-Arcsinh (SHASH) specifications where all distributional parameters vary dynamically with market fundamentals like demand, renewables, and risk factors. Using rolling-window evaluations, pinball loss, and Diebold-Mariano tests, they show that flexible specifications such as JSU significantly improve both point and probabilistic forecasting performance, especially in the distributional tails.

## Key Contributions

- Applied the GAMLSS framework to forecast Spanish day-ahead electricity prices using hourly data from 2020 to 2024, incorporating market fundamentals across location, scale, and shape parameters.
- Evaluated alternative distributional specifications (Normal, Johnson's SU, and Sinh-Arcsinh) using rolling-window evaluations, MAE, pinball loss, and Diebold-Mariano tests.
- Demonstrated that the JSU specification with all four parameters driven by covariates achieves superior probabilistic forecasting performance, particularly in the distribution tails.

## Links

- [Abstract](https://arxiv.org/abs/2610.01465)
- [PDF](https://arxiv.org/pdf/2610.01465)

