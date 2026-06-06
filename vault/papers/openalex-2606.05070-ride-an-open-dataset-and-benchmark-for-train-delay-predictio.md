---
# CSL-compatible fields
title: "RIDE: An Open Dataset and Benchmark for Train Delay Prediction"
author:
  - literal: "Clément Elliker"
  - literal: "Mathis Le Bail"
  - literal: "Clément Mantoux"
  - literal: "Jesse Read"
  - literal: "Sonia Vanier"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.05070"

# Custom fields
paper_id: "2606.05070"
paper_source: "openalex"
domain: "time-series"
tags:
  - "benchmark"
  - "dataset"
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
architectures:
  []
datasets:
  - "ride"
concept_slugs:
  - "ride-benchmark"
dataset_slugs:
  - "ride"
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:40:47Z"
created_at: "2026-06-06T07:40:47Z"
---

# RIDE: An Open Dataset and Benchmark for Train Delay Prediction

**Authors**: Clément Elliker, Mathis Le Bail, Clément Mantoux, Jesse Read, Sonia Vanier
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.05070](https://arxiv.org/abs/2606.05070)

## Summary

The paper addresses the lack of standardized benchmarking in railway delay prediction by introducing RIDE, a massive, nationwide dataset covering the Belgian railway network. The dataset includes integrated railway events and weather data with a unified evaluation protocol to allow for fair comparisons between various modeling approaches. Empirical results demonstrate that learning-based methods, particularly graph neural networks, outperform non-learning and traditional statistical baselines. The study also provides fine-grained performance analysis segmented by prediction horizon and delay characteristics to offer deeper insights into model behavior.

## Key Contributions

- Introduces RIDE, a nationwide railway delay prediction dataset containing 94.5M events, 3.6M journeys, and 35.7M weather records.
- Provides a standardized evaluation protocol that supports consistent comparison across statistical and deep learning models on a shared prediction task.
- Conducts the first comprehensive benchmarking of non-learning, statistical, and graph-based learning methods for train delay forecasting, identifying graph neural networks as high-performers.

## Open Questions & Future Work

- [[model-architecture-vs-feature-design-in-transportation-forecasting]]

## Key Concepts

- [[ride-benchmark]]: A large-scale, standardized open dataset and evaluation framework for nationwide railway delay prediction, integrating railway event logs with weather data.

## Archivist Review

I approved the RIDE benchmark and its associated dataset as a valuable contribution to the transportation time-series domain, as it provides a much-needed standardized evaluation protocol. The open question was reframed to explicitly focus on the trade-off between architectural complexity and domain-specific feature design in the context of logistics/transportation forecasting, separating the bottleneck analysis from general model-selection tasks.

### Approved Concepts
- RIDE Benchmark: Provides a standardized, nationwide-scale dataset and evaluation framework for a critical logistics problem (train delay prediction) that previously lacked such benchmarks.

### Approved Open Questions
- Architectural vs Feature Design Limitations: Identifying whether progress in this field is bottlenecked by model architecture or by data/feature limitations is crucial for guiding future methodological investments in logistics forecasting.

## Datasets

- [[ride]]

## Links

- [Abstract](https://arxiv.org/abs/2606.05070)
- [PDF](https://arxiv.org/pdf/2606.05070)

