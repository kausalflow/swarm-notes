---
# CSL-compatible fields
title: "Impermanent: A Live Benchmark for Temporal Generalization in Time Series Forecasting"
author:
  - literal: "Azul Garza"
  - literal: "Renée Rosillo"
  - literal: "Rodrigo Mendoza-Smith"
  - literal: "David Salinas"
  - literal: "Andrew Williams"
  - literal: "Arjun Ashok"
  - literal: "Mononito Goswami"
  - literal: "José Martín Juárez"
issued:
  date-parts:
    - [2026, 3, 9]
url: "https://arxiv.org/abs/2603.08707"

# Custom fields
paper_id: "2603.08707"
paper_source: "openalex"
domain: "time-series"
tags:
  - "benchmark"
  - "time-series"
  - "evaluation"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  - "GitHub open-source activity"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:19Z"
created_at: "2026-03-27T14:08:19Z"
---

# Impermanent: A Live Benchmark for Temporal Generalization in Time Series Forecasting

**Authors**: Azul Garza, Renée Rosillo, Rodrigo Mendoza-Smith, David Salinas, Andrew Williams, Arjun Ashok, Mononito Goswami, José Martín Juárez
**Date**: 2026-03-09
**Paper ID**: [openalex:2603.08707](https://arxiv.org/abs/2603.08707)

## Summary

This paper introduces Impermanent, a novel live benchmark designed to rigorously evaluate the temporal generalization capabilities of time series forecasting models, particularly foundation models, under conditions of continuous open-world change. Existing static benchmarks are criticized for potential data leakage and for only measuring one-off accuracy rather than sustained performance under distribution shift. Impermanent addresses this by continuously updating its data streams—derived from GitHub repository activity like issues and pull requests—and scoring forecasts sequentially over a rolling window. This methodology moves the research focus toward assessing temporal robustness and performance stability as the environment naturally evolves, providing a more meaningful assessment of foundation-level generalization claims in time series.

## Key Contributions

- Introduction of Impermanent, a live benchmark for time series forecasting that evaluates models sequentially over continuously updated data streams rather than on static splits.
- The benchmark is instantiated using activity metrics (issues, PRs, pushes, stargazers) from the top 400 GitHub repositories, creating a highly non-stationary, real-world dataset.
- Impermanence shifts the evaluation focus from one-off accuracy to sustained performance, temporal robustness, and distributional shift resistance.
- Establishment of standardized protocols and live leaderboards to ensure reproducible, ongoing comparison of forecasting models under open-world temporal change.

## Limitations

The initial instantiation focuses specifically on GitHub activity metrics, which may not generalize to all time-series domains. Performance stability must be monitored over very long horizons to fully test generalization capabilities.

## Open Questions & Future Work

- [[impermanent-future-covariates]]
- [[impermanent-additional-streams]]
- [[impermanent-longer-horizons]]
- [[temporal-vs-static-translation]]
- [[impermanent-enrich-context]]

## Datasets

- [GitHub open-source activity](../datasets/github-open-source-activity.md)

## Limitations

The initial instantiation focuses specifically on GitHub activity metrics, which may not generalize to all time-series domains. Performance stability must be monitored over very long horizons to fully test generalization capabilities.

## Links

- [Abstract](https://arxiv.org/abs/2603.08707)
- [PDF](https://arxiv.org/pdf/2603.08707)

