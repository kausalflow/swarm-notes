---
# CSL-compatible fields
title: "AIFS-SUBS: Extending Data-Driven Forecasting to Sub-Seasonal Timescales"
author:
  - literal: "Jakob Schloer"
  - literal: "Steffen Tietsche"
  - literal: "Christopher D. Roberts"
  - literal: "Lorenzo Zampieri"
  - literal: "Simon Lang"
  - literal: "Gert Mertes"
  - literal: "Gareth Jones"
  - literal: "Matthew Chantry"
  - literal: "Frédéric Vitart"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.05100"

# Custom fields
paper_id: "2607.05100"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "forecasting"
  - "time-series"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "era5"
concept_slugs:
  - "aifs-subs"
dataset_slugs:
  - "era5"
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:18:10Z"
created_at: "2026-07-09T08:18:10Z"
---

# AIFS-SUBS: Extending Data-Driven Forecasting to Sub-Seasonal Timescales

**Authors**: Jakob Schloer, Steffen Tietsche, Christopher D. Roberts, Lorenzo Zampieri, Simon Lang, Gert Mertes, Gareth Jones, Matthew Chantry, Frédéric Vitart
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.05100](https://arxiv.org/abs/2607.05100)

## Summary

AIFS-SUBS is a data-driven model developed by ECMWF designed specifically for sub-seasonal weather forecasting. By using a 24-hour autoregressive step and incorporating stratospheric predictors, the model mitigates error accumulation typically seen in long-horizon rollouts. Evaluation on ERA5 demonstrates competitive performance against the operational Integrated Forecasting System (IFS) across probabilistic metrics, MJO indices, and stratospheric events, all while drastically lowering computational energy demands.

## Key Contributions

- AIFS-SUBS extends data-driven forecasting to sub-seasonal timescales (weeks 2-6) by employing a 24-hour autoregressive step to mitigate error accumulation.
- The model achieves probabilistic skill comparable to the operational Integrated Forecasting System (IFS) while significantly reducing energy consumption by approximately 200x.
- AIFS-SUBS provides superior forecasting for MJO convective components and captures sudden stratospheric warming (SSW) frequencies and surface impacts more effectively than traditional IFS.

## Open Questions & Future Work

- [[coupling-earth-system-components-subseasonal]]
- [[stabilizing-high-resolution-autoregressive-rollouts]]

## Key Concepts

- [[aifs-subs]]: An autoregressive data-driven model for sub-seasonal weather forecasting that utilizes a 24-hour step and expanded atmospheric predictors.

## Archivist Review

Approved AIFS-SUBS as a representative mechanism for addressing autoregressive error accumulation in long-range weather forecasting. Approved ERA5 as a foundational weather dataset frequently used as a baseline. Approved two open questions regarding Earth-system coupling and rollout stabilization, as these represent significant, persistent bottlenecks in meteorological AI forecasting.

### Approved Concepts
- AIFS-SUBS: First ECMWF machine learning model specifically optimized for sub-seasonal forecasting, addressing long-term autoregressive drift.

### Approved Open Questions
- Coupling Earth-system components for subseasonal forecasting: Atmospheric coupling is a critical bottleneck for sub-seasonal skill, as surface variables depend heavily on long-memory components of the climate system which are currently treated only as boundary conditions.
- Stabilizing high-resolution autoregressive rollouts: Improving temporal resolution is vital for accurately resolving the diurnal cycle and reducing discretization errors in numerical forecasting.

## Datasets

- [[era5]]

## Links

- [Abstract](https://arxiv.org/abs/2607.05100)
- [PDF](https://arxiv.org/pdf/2607.05100)

