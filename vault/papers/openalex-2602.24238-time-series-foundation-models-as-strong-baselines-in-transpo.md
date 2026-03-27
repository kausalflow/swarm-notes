---
# CSL-compatible fields
title: "Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis"
author:
  - literal: "Javier Pulido"
  - literal: "Filipe Rodrigues"
issued:
  date-parts:
    - [2026, 2, 27]
url: "https://arxiv.org/abs/2602.24238"

# Custom fields
paper_id: "2602.24238"
paper_source: "openalex"
domain: "time-series"
tags:
  - "language-model"
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "evaluation"
  - "benchmark"
  - "foundation-model"
architectures:
  []
datasets:
  - "highway traffic volume and flow datasets"
  - "urban traffic speed datasets"
  - "bike-sharing demand datasets"
  - "electric vehicle charging station data datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:50Z"
created_at: "2026-03-27T14:09:50Z"
---

# Time Series Foundation Models as Strong Baselines in Transportation Forecasting: A Large-Scale Benchmark Analysis

**Authors**: Javier Pulido, Filipe Rodrigues
**Date**: 2026-02-27
**Paper ID**: [openalex:2602.24238](https://arxiv.org/abs/2602.24238)

## Summary

This paper investigates the zero-shot effectiveness of the Chronos-2 time-series foundation model as a general-purpose forecaster for transportation dynamics across ten real-world datasets, including traffic volume, speed, and demand. The evaluation protocol rigorously benchmarks Chronos-2 against traditional statistical methods and specialized deep learning architectures without any task-specific training. Results indicate that the foundation model frequently achieves state-of-the-art or competitive accuracy, especially for longer forecasting horizons, confirming its utility as a strong baseline. Furthermore, the model's inherent probabilistic outputs are shown to offer reliable uncertainty quantification through prediction interval coverage and sharpness metrics. This work strongly suggests that large, pre-trained time-series models can significantly simplify the baseline establishment process in specialized forecasting domains like transportation.

## Key Contributions

- Benchmarked the zero-shot performance of the Chronos-2 time-series foundation model across ten diverse transportation forecasting datasets.
- Demonstrated that Chronos-2 achieves state-of-the-art or competitive accuracy compared to specialized deep learning models and statistical baselines without any fine-tuning.
- Showed that Chronos-2's native probabilistic outputs provide useful uncertainty quantification (coverage and sharpness) for transportation forecasting tasks.
- Advocated for the adoption of general-purpose time-series foundation models as strong, standardized baselines in transportation forecasting research.

## Limitations

The evaluation is strictly zero-shot, leaving open the potential gains from lightweight fine-tuning or prompt engineering on these specialized domains.

## Open Questions & Future Work

- [[ts-fm-fine-tuning-transportation-gains]]
- [[homogenization-of-foundation-model-errors]]
- [[ts-fm-new-baseline-standard]]
- [[integrating-spatial-fm-forecasting]]

## Key Concepts

- [Chronos-2](../concepts/chronos-2.md): A large-scale, general-purpose time-series foundation model evaluated for transportation forecasting tasks.

## Datasets

- [highway traffic volume and flow datasets](../datasets/highway-traffic-volume-and-flow-datasets.md)
- [urban traffic speed datasets](../datasets/urban-traffic-speed-datasets.md)
- [bike-sharing demand datasets](../datasets/bike-sharing-demand-datasets.md)
- [electric vehicle charging station data datasets](../datasets/electric-vehicle-charging-station-data-datasets.md)

## Limitations

The evaluation is strictly zero-shot, leaving open the potential gains from lightweight fine-tuning or prompt engineering on these specialized domains.

## Links

- [Abstract](https://arxiv.org/abs/2602.24238)
- [PDF](https://arxiv.org/pdf/2602.24238)

