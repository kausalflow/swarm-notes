---
# CSL-compatible fields
title: "West-WRF AI 2-km: High-Resolution Prediction of Integrated Vapor Transport and Precipitation"
author:
  - literal: "Nazak Rouzegari"
  - literal: "Vesta Afzali Gorooh"
  - literal: "Agniv Sengupta"
  - literal: "Phu Nguyen"
  - literal: "Kuolin Hsu"
  - literal: "Amir AghaKouchak"
  - literal: "Soroosh Sorooshian"
  - literal: "F. Martin Ralph"
  - literal: "Luca Delle Monache"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25512"

# Custom fields
paper_id: "2609.25512"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-09-25T09:55:15Z"
created_at: "2026-09-25T09:55:15Z"
---

# West-WRF AI 2-km: High-Resolution Prediction of Integrated Vapor Transport and Precipitation

**Authors**: Nazak Rouzegari, Vesta Afzali Gorooh, Agniv Sengupta, Phu Nguyen, Kuolin Hsu, Amir AghaKouchak, Soroosh Sorooshian, F. Martin Ralph, Luca Delle Monache
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25512](https://arxiv.org/abs/2609.25512)

## Summary

The authors introduce West-WRF AI 2-km, a stretched-grid artificial intelligence weather forecasting model featuring a 2-km high resolution over the western U.S. and Northeast Pacific and a 31-km resolution globally. By pretraining on ERA5 and fine-tuning with regional 2-km reanalysis data, the model generates autoregressive 6-hourly forecasts for precipitation and integrated vapor transport. Evaluations over winters 2020-2023 demonstrate that West-WRF AI 2-km successfully captures fine-scale spectral variability, localized extremes, and extreme IVT thresholds compared to traditional numerical weather prediction systems and coarser AI models.

## Key Contributions

- Introduces West-WRF AI 2-km, a stretched-grid artificial intelligence weather forecasting model offering 2-km high-resolution predictions over the western United States and Northeast Pacific.
- Builds upon a global AI model pretrained on the 40-year ERA5 dataset and fine-tuned using the CW3E 2-km regional reanalysis for autoregressive 6-hourly precipitation and integrated vapor transport (IVT) forecasting.
- Demonstrates superior skill over winters 2020-2023 in capturing fine-scale spectral variability, sharp narrow coastal precipitation bands, terrain-sensitive extremes, and extreme IVT thresholds compared to coarser AI models and NWP systems.

## Archivist Review

The paper presents a regional high-resolution fine-tuning application (West-WRF AI 2-km) using a stretched-grid AI weather model, which builds on established global foundation models and regional reanalysis. Since no novel reusable ML methodologies, foundational architectures, or open-ended theoretical questions were introduced that extend beyond domain-specific application, all candidate lists were kept empty in accordance with strict archival standards.

## Links

- [Abstract](https://arxiv.org/abs/2609.25512)
- [PDF](https://arxiv.org/pdf/2609.25512)

