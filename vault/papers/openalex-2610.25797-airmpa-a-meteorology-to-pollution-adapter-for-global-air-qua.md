---
# CSL-compatible fields
title: "AirMPA: A Meteorology-to-Pollution Adapter for Global Air Quality Forecasting"
author:
  - literal: "Yiheng Wang"
  - literal: "Kai Zheng"
  - literal: "Yuetan Lin"
  - literal: "Fanglu Fan"
  - literal: "Chenliang Tao"
  - literal: "Guochao Chen"
  - literal: "Hongliang Zhang"
  - literal: "Hao Li"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.25797"

# Custom fields
paper_id: "2610.25797"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:32Z"
created_at: "2026-10-22T09:44:32Z"
---

# AirMPA: A Meteorology-to-Pollution Adapter for Global Air Quality Forecasting

**Authors**: Yiheng Wang, Kai Zheng, Yuetan Lin, Fanglu Fan, Chenliang Tao, Guochao Chen, Hongliang Zhang, Hao Li
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.25797](https://arxiv.org/abs/2610.25797)

## Summary

Accurate global air quality forecasting is challenging due to the entanglement of meteorological and pollutant variables in unified deep learning models. To resolve this, the authors propose AirMPA, a decoupled autoregressive framework that forecasts 13 atmospheric pollutants by leveraging meteorological fields, emission priors, and historical pollutant concentrations. Built upon an enhanced Swin-Transformer architecture featuring zonal release attention and dual-branch fusion, AirMPA ingests ERA5 data during training and external forecast fields during inference. Experimental evaluations demonstrate that AirMPA outperforms established baselines such as Aurora and the Copernicus Atmosphere Monitoring Service (CAMS) across a 5-day forecast horizon.

## Key Contributions

- AirMPA introduces a decoupled autoregressive framework for meteorology-to-pollution forecasting, separating meteorological and pollutant variable modeling to enhance pollutant-specific representation learning.
- The model incorporates an improved Swin-Transformer architecture with zonal release attention and dual-branch fusion to model global transport continuity and heterogeneous pollutant dynamics.
- AirMPA achieves stable autoregressive prediction up to 5 days ahead, consistently outperforming Aurora and surpassing the Copernicus Atmosphere Monitoring Service (CAMS) in approximately 90% of pollutant-lead-time evaluation cases.

## Archivist Review

Applied strict reusability and selectivity standards. No new concepts or open questions met the high bar for permanent standalone vault inclusion, as the architectural components and tasks are specific to air quality modeling rather than generalizable forecasting paradigms.

## Links

- [Abstract](https://arxiv.org/abs/2610.25797)
- [PDF](https://arxiv.org/pdf/2610.25797)

