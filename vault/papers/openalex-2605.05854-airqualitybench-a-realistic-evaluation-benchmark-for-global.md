---
# CSL-compatible fields
title: "AirQualityBench: A Realistic Evaluation Benchmark for Global Air Quality Forecasting"
author:
  - literal: "Xing Xu"
  - literal: "Xu Wang"
  - literal: "Yudong Zhang"
  - literal: "Huilin Zhao"
  - literal: "Zhengyang Zhou"
  - literal: "Yang Wang"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05854"

# Custom fields
paper_id: "2605.05854"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "airqualitybench"
concept_slugs:
  - "airqualitybench"
dataset_slugs:
  - "airqualitybench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:38Z"
created_at: "2026-05-10T07:21:38Z"
---

# AirQualityBench: A Realistic Evaluation Benchmark for Global Air Quality Forecasting

**Authors**: Xing Xu, Xu Wang, Yudong Zhang, Huilin Zhao, Zhengyang Zhou, Yang Wang
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05854](https://arxiv.org/abs/2605.05854)

## Summary

AirQualityBench is a new, realistic benchmark for global air quality forecasting that addresses common flaws in existing evaluation protocols such as artificial data imputation and over-simplification. The dataset comprises hourly observations from 3,720 global stations, explicitly preserving native missingness to better simulate real-world monitoring network constraints. By shifting the evaluation focus to error calculation on valid future observations without reliance on dense data tensors, the study reveals significant gaps between performance on sanitized benchmarks and real-world deployment scenarios.

## Key Contributions

- Introduced AirQualityBench, a large-scale global multi-pollutant dataset consisting of 3,720 stations with realistic, native observation masks.
- Established a unified evaluation protocol that treats structured missingness as a first-class forecasting task rather than using simplified, imputed data.
- Demonstrated that existing state-of-the-art models often fail to generalize when evaluated under realistic conditions compared to sanitized benchmarks.

## Open Questions & Future Work

- [[standardizing-global-air-quality-units]]
- [[region-stratified-forecasting-robustness]]

## Key Concepts

- [[airqualitybench]]: A comprehensive global multi-pollutant forecasting benchmark that preserves native missingness and physical concentration scales.

## Archivist Review

The paper introduces a significant benchmark that moves the field away from overly sanitized datasets towards realistic, mask-aware forecasting evaluation. The approved items capture the essence of this new benchmark and the specific research gaps it highlights regarding regional robustness and physical unit standardization. I have adhered to the scarcity constraints and kept the terminology aligned with the domain.

### Approved Concepts
- AirQualityBench: Provides a standardized, realistic evaluation framework that accounts for real-world monitoring network challenges like structured missingness and heterogeneous pollutant scales.

### Approved Open Questions
- Harmonizing Global Pollutant Units: This is crucial for moving the field toward physically interpretable evaluation, ensuring that forecasting metrics are meaningful and comparable across different global monitoring networks and pollutant types.
- Region-Stratified Forecasting Evaluation: Region-stratified evaluation is essential for environmental equity and ensuring that air quality forecasting technologies remain reliable and useful in developing regions where they are often most needed but least supported by infrastructure.

## Datasets

- [[airqualitybench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.05854)
- [PDF](https://arxiv.org/pdf/2605.05854)

