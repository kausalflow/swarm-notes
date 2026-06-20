---
# CSL-compatible fields
title: "ForecastBench-Sim: A Simulated-World Forecasting Benchmark"
author:
  - literal: "Jaeho Lee"
  - literal: "Nick Merrill"
  - literal: "Ezra Karger"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18686"

# Custom fields
paper_id: "2606.18686"
paper_source: "openalex"
domain: "time-series"
tags:
  - "benchmark"
  - "forecasting"
  - "time-series"
  - "reasoning"
architectures:
  []
datasets:
  - "Freeciv"
concept_slugs:
  - "forecastbench-sim"
dataset_slugs:
  - "freeciv"
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:25Z"
created_at: "2026-06-20T08:17:25Z"
---

# ForecastBench-Sim: A Simulated-World Forecasting Benchmark

**Authors**: Jaeho Lee, Nick Merrill, Ezra Karger
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18686](https://arxiv.org/abs/2606.18686)

## Summary

ForecastBench-Sim addresses the limitations of real-world forecasting benchmarks by using simulated game environments to generate high-resolution, counterfactual-ready forecasting tasks. The platform uses turn-based strategy game rollouts to create structured snapshots of world states, allowing for the immediate and systematic evaluation of AI probabilistic reasoning. By providing a controlled sandbox, it enables researchers to study model performance on rare events and causal questions that are often impossible to score in real-world contexts.

## Key Contributions

- Introduces ForecastBench-Sim, a turn-based strategy game environment for controlled, immediate evaluation of forecasting models.
- Enables generation of counterfactual and rare-event forecasting questions at arbitrary horizons by leveraging deterministic game state rollouts.
- Provides a standardized protocol and pipeline for scoring model-generated probabilistic forecasts in simulated worlds.

## Open Questions & Future Work

- [[brier-crps-ranking-divergence]]

## Key Concepts

- [[forecastbench-sim]]: A simulated-world forecasting benchmark using game rollouts to enable controlled evaluation of probabilistic reasoning and counterfactual analysis.

## Archivist Review

I approved the benchmark concept and dataset as they provide a systematic, reproducible, and controlled testbed for forecasting, which is a significant methodological contribution over noisy real-world benchmarks. I also approved the open question regarding score divergence, as metric choice is a chronic, under-investigated source of ambiguity in the evaluation of probabilistic models.

### Approved Concepts
- ForecastBench-Sim: It addresses core challenges in real-world forecasting by offering a simulated environment for scalable, counterfactual, and high-frequency resolution of probabilistic forecasts.

### Approved Open Questions
- Brier vs. CRPS Performance Divergence: Understanding the divergence between these two common metrics is essential for interpreting forecasting benchmarks correctly.

## Datasets

- [[freeciv]]

## Links

- [Abstract](https://arxiv.org/abs/2606.18686)
- [PDF](https://arxiv.org/pdf/2606.18686)

