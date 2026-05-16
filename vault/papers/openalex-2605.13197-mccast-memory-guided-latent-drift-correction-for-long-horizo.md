---
# CSL-compatible fields
title: "McCast: Memory-Guided Latent Drift Correction for Long-Horizon Precipitation Nowcasting"
author:
  - literal: "Penghui Wen"
  - literal: "Yu Luo"
  - literal: "Lintao Wang"
  - literal: "Mengwei He"
  - literal: "Patrick Filippi"
  - literal: "Thomas Francis Bishop"
  - literal: "Zhiyong Wang"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13197"

# Custom fields
paper_id: "2605.13197"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "autoregressive"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "SEVIR"
  - "MeteoNet"
concept_slugs:
  - "drift-corrective-memory-bank-dcbank"
dataset_slugs:
  - "sevir"
  - "meteonet"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:10:02Z"
created_at: "2026-05-16T07:10:02Z"
---

# McCast: Memory-Guided Latent Drift Correction for Long-Horizon Precipitation Nowcasting

**Authors**: Penghui Wen, Yu Luo, Lintao Wang, Mengwei He, Patrick Filippi, Thomas Francis Bishop, Zhiyong Wang
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13197](https://arxiv.org/abs/2605.13197)

## Summary

McCast is a novel method for precipitation nowcasting that addresses the error accumulation inherent in standard autoregressive models by focusing on global trajectory evolution. It introduces a Drift-Corrective Memory Bank (DCBank) which actively calibrates latent states during rollouts using temporally organized historical information. By shifting the objective from purely step-wise accuracy to long-term temporal coherence, McCast effectively mitigates drift in long-horizon forecasts, outperforming existing baselines on the SEVIR and MeteoNet benchmarks.

## Key Contributions

- Introduced McCast, a memory-guided latent drift correction framework that addresses error accumulation in long-horizon autoregressive precipitation nowcasting.
- Designed the Drift-Corrective Memory Bank (DCBank), which uses historical memory to actively calibrate divergent latent trajectories.
- Achieved state-of-the-art performance on SEVIR and MeteoNet benchmarks, demonstrating superior temporal coherence over long forecasting horizons.

## Open Questions & Future Work

- [[long-horizon-drift-correction-limits]]

## Key Concepts

- [[drift-corrective-memory-bank-dcbank]]: A memory mechanism designed to explicitly estimate and apply temporal corrections to autoregressive latent states to prevent long-horizon forecast drift.

## Archivist Review

I approved the Drift-Corrective Memory Bank concept as it provides a reusable paradigm for mitigating autoregressive error accumulation through active trajectory calibration rather than passive conditioning. I also approved the open question regarding the limits of these drift-correction techniques, as it addresses a fundamental bottleneck in long-horizon time-series forecasting. The SEVIR and MeteoNet datasets were approved as they are recognized, critical benchmarks for nowcasting tasks.

### Approved Concepts
- Drift-Corrective Memory Bank (DCBank): This is the core novelty of the paper, representing a shift from passive memory conditioning to active, trajectory-level correction in autoregressive forecasting.

### Approved Open Questions
- Long-Horizon Drift Correction Limits: Extending the horizon of reliable precipitation forecasts is a primary goal of the field, and determining whether latent memory mechanisms can remain physically and temporally coherent over longer durations is critical for advancing nowcasting reliability.

## Datasets

- [[sevir]]
- [[meteonet]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13197)
- [PDF](https://arxiv.org/pdf/2605.13197)

