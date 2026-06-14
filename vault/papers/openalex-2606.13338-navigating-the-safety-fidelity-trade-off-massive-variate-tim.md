---
# CSL-compatible fields
title: "Navigating the Safety-Fidelity Trade-off: Massive-Variate Time Series Forecasting for Power Systems via Probabilistic Scenarios"
author:
  - literal: "Kaijie Xu"
  - literal: "A F Wang"
  - literal: "Xilin Dai"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13338"

# Custom fields
paper_id: "2606.13338"
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
  - "powerphase"
concept_slugs:
  - "powerphase-benchmark"
  - "powerforge-forecaster"
dataset_slugs:
  - "powerphase"
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:37:11Z"
created_at: "2026-06-14T08:37:11Z"
---

# Navigating the Safety-Fidelity Trade-off: Massive-Variate Time Series Forecasting for Power Systems via Probabilistic Scenarios

**Authors**: Kaijie Xu, A F Wang, Xilin Dai
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13338](https://arxiv.org/abs/2606.13338)

## Summary

This paper addresses the gap in large-scale, constraint-aware time series forecasting for power systems by introducing the PowerPhase benchmark, which scales up to 36,964 channels. The authors identify a 'safety-fidelity' trade-off, where models optimized for distributional accuracy often struggle with operational constraint satisfaction. To mitigate this, they propose PowerForge, a scenario-based quantile forecaster that utilizes type-specific decoding and causal grouping to outperform eight baselines on the new benchmark.

## Key Contributions

- Introduced PowerPhase, a large-scale probabilistic forecasting benchmark featuring six transmission grids with up to 36,964 channels.
- Formulated the 'safety-fidelity' trade-off, demonstrating that distributional accuracy and constraint satisfaction often yield conflicting model rankings in power systems.
- Developed PowerForge, a scenario-based quantile forecaster achieving state-of-the-art performance across all PowerPhase grids.

## Open Questions & Future Work

- [[certifiable-physical-feasibility-large-scale-power-forecasting]]

## Key Concepts

- [[powerphase-benchmark]]: A large-scale probabilistic forecasting benchmark consisting of six transmission grids with up to 36,964 jointly forecasted channels.
- [[powerforge-forecaster]]: A scenario-based quantile forecasting model featuring type-specific decoding heads and a causal bridge between variable groups for multivariate time series.

## Archivist Review

The approved concepts capture a significant advance in benchmark scale (PowerPhase) and a tailored architectural approach (PowerForge) for managing safety-fidelity trade-offs in power systems. The approved open question addresses the critical gap between statistical accuracy and physical constraint enforcement in high-dimensional grid forecasting. Dataset approval is limited to the new benchmark to ensure focus on reusable, novel resources.

### Approved Concepts
- PowerPhase Benchmark: Addresses the lack of high-dimensional, constraint-aware benchmarks for power-system time series forecasting.
- PowerForge Forecaster: Provides a specialized architecture for high-dimensional scenarios that balances distributional accuracy with constraint satisfaction.

### Approved Open Questions
- Certifiable physical feasibility in power forecasting: Essential for transitioning from statistically accurate but physically dangerous forecasts to operationally safe grid-management tools.

## Datasets

- [[powerphase]]

## Links

- [Abstract](https://arxiv.org/abs/2606.13338)
- [PDF](https://arxiv.org/pdf/2606.13338)

