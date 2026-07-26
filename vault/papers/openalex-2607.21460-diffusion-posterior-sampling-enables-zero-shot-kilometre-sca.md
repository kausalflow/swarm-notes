---
# CSL-compatible fields
title: "Diffusion posterior sampling enables zero shot kilometre scale wind forecasting over complex terrain"
author:
  - literal: "Yujiang Cai"
  - literal: "Ya Wang"
  - literal: "Shuanglei Feng"
  - literal: "Bo Wang"
  - literal: "Yiming Liu"
  - literal: "Hui Yuan"
  - literal: "Xinyi Sun"
  - literal: "Haijie Li"
  - literal: "Shenming Fu"
issued:
  date-parts:
    - [2026, 7, 23]
url: "https://arxiv.org/abs/2607.21460"

# Custom fields
paper_id: "2607.21460"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "kilogen"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:29:47Z"
created_at: "2026-07-26T07:29:47Z"
---

# Diffusion posterior sampling enables zero shot kilometre scale wind forecasting over complex terrain

**Authors**: Yujiang Cai, Ya Wang, Shuanglei Feng, Bo Wang, Yiming Liu, Hui Yuan, Xinyi Sun, Haijie Li, Shenming Fu
**Date**: 2026-07-23
**Paper ID**: [openalex:2607.21460](https://arxiv.org/abs/2607.21460)

## Summary

This paper introduces KiloGen, a diffusion posterior sampling framework designed for kilometre-scale near-surface wind forecast enhancement over complex terrain. By learning a high-resolution vector wind prior from WRF simulations and conditioning it on coarse ECMWF forecasts at inference time, KiloGen bypasses the need for explicitly paired training data or learned mapping functions. Evaluated over the mountainous Shanxi region in China, KiloGen successfully restores local wind variability and terrain-driven structures, achieving superior wind speed RMSE compared to baseline ECMWF operational products, especially during strong wind conditions.

## Key Contributions

- Introduces KiloGen, a diffusion posterior sampling framework for kilometre-scale wind forecast enhancement that avoids the need for paired coarse-to-fine training samples.
- Learns a high-resolution vector wind prior from WRF simulations and constrains posterior sampling with coarse operational forecasts from ECMWF at inference time.
- Achieves the lowest overall wind speed RMSE over Shanxi, China, reducing RMSE by approximately 10% for observed winds above 20 m/s and outperforming both 0.25-degree and 0.1-degree ECMWF forecasts.

## Key Concepts

- [[kilogen]]: A diffusion posterior sampling framework for kilometre-scale wind forecast enhancement over complex terrain.

## Archivist Review

Approved the core framework 'KiloGen' as a distinct concept representing diffusion posterior sampling for atmospheric downscaling without paired training data. No open questions or datasets met the strict novelty and naming criteria.

### Approved Concepts
- KiloGen: It introduces a novel diffusion posterior sampling framework for high-resolution wind forecasting without requiring paired training data between coarse and fine scales.

## Links

- [Abstract](https://arxiv.org/abs/2607.21460)
- [PDF](https://arxiv.org/pdf/2607.21460)

