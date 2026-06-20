---
# CSL-compatible fields
title: "CNN-based Surface Temperature Forecasts with Ensemble Numerical Weather Prediction"
author:
  - literal: "Takuya Inoue"
  - literal: "Takuya Kawabata"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2507.18937"

# Custom fields
paper_id: "2507.18937"
paper_source: "openalex"
domain: "time-series"
tags:
  - "cnn-based-surface-temperature-forecasts-with-ensemble-numerical-weather-prediction"
  - "forecasting"
  - "time-series"
architectures:
  - "cnn-based-surface-temperature-forecasts-with-ensemble-numerical-weather-prediction"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:49Z"
created_at: "2026-06-20T08:17:49Z"
---

# CNN-based Surface Temperature Forecasts with Ensemble Numerical Weather Prediction

**Authors**: Takuya Inoue, Takuya Kawabata
**Date**: 2026-06-17
**Paper ID**: [openalex:2507.18937](https://arxiv.org/abs/2507.18937)

## Summary

This paper presents a CNN-based post-processing framework to enhance medium-range surface temperature forecasts from low-resolution ensemble numerical weather prediction (NWP) systems. By applying a CNN member-wise to the ensemble, the method achieves spatial downscaling from 40-km to 5-km while simultaneously correcting systematic biases. The approach improves both deterministic accuracy and probabilistic reliability for forecasts extending up to 5.5 days, offering a computationally efficient alternative for operational weather centers. Unlike traditional ensemble averaging, which smooths spatial fields, this member-wise correction preserves forecast information while reducing noise-driven errors.

## Key Contributions

- Proposes a CNN-based post-processing method for ensemble NWP models that simultaneously performs bias correction and spatial downscaling.
- Achieves high-resolution (5-km) temperature forecasts from low-resolution (40-km) ensemble inputs with lead times up to 132 hours.
- Demonstrates that member-wise CNN correction improves probabilistic reliability and the spread–skill ratio compared to traditional ensemble averaging.

## Links

- [Abstract](https://arxiv.org/abs/2507.18937)
- [PDF](https://arxiv.org/pdf/2507.18937)

