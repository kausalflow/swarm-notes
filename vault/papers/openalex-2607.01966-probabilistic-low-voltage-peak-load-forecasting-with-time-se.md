---
# CSL-compatible fields
title: "Probabilistic Low-Voltage Peak Load Forecasting with Time Series Foundation Models Evaluated on Application-Oriented Metrics"
author:
  - literal: "Benedikt Kaas"
  - literal: "Manuel Treutlein"
  - literal: "H. Gerber"
  - literal: "Oliver Neumann"
  - literal: "Cheewan Phatthanakhuha"
  - literal: "Oliver Resch"
  - literal: "Ralf Mikut"
  - literal: "Veit Hagenmeyer"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01966"

# Custom fields
paper_id: "2607.01966"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "language-model"
  - "uncertainty-estimation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "application-oriented-grid-planning-metric"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:51:48Z"
created_at: "2026-07-05T07:51:48Z"
---

# Probabilistic Low-Voltage Peak Load Forecasting with Time Series Foundation Models Evaluated on Application-Oriented Metrics

**Authors**: Benedikt Kaas, Manuel Treutlein, H. Gerber, Oliver Neumann, Cheewan Phatthanakhuha, Oliver Resch, Ralf Mikut, Veit Hagenmeyer
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01966](https://arxiv.org/abs/2607.01966)

## Summary

This paper evaluates the performance of state-of-the-art time series foundation models, including Chronos-2, for probabilistic low-voltage net load forecasting. Using 200 real-world low-voltage feeders, the authors demonstrate that foundation models offer superior peak load prediction and robust uncertainty estimation compared to traditional baselines. Furthermore, the study introduces a novel application-oriented metric that translates forecasting accuracy into actionable grid management trade-offs, specifically balancing cost efficiency with operational reliability.

## Key Contributions

- Evaluates time series foundation models (Chronos-Bolt, Chronos-2, TabPFN-TS) on short-term net load forecasting using 200 real-world low-voltage feeder datasets.
- Demonstrates that foundation models like Chronos-2 outperform traditional baseline models in peak load prediction and uncertainty estimation.
- Introduces an application-oriented metric quantifying the trade-off between grid asset cost reduction and operational failure risk.

## Open Questions & Future Work

- [[robust-covariate-integration-tsfm]]
- [[aligning-loss-functions-with-grid-kpis]]

## Key Concepts

- [[application-oriented-grid-planning-metric]]: A forecasting metric that evaluates model performance by balancing cost reduction against grid failure risk in asset planning.

## Archivist Review

The paper contributes a useful application-oriented metric for energy grid forecasting and identifies meaningful bottlenecks regarding covariate integration and objective alignment. Concepts and questions were selected to reflect these contributions while rejecting routine performance benchmarks and baseline comparisons.

### Approved Concepts
- Application-Oriented Grid Planning Metric: Bridges the gap between raw time-series forecasting metrics and real-world utility grid asset planning outcomes.

### Approved Open Questions
- Robust Covariate Integration in TSFMs: As load forecasting becomes increasingly dependent on weather-sensitive variables, the inability to effectively leverage these signals without performance loss limits the deployment of foundation models in grid operations.
- Aligning Loss Functions with Grid KPIs: Aligning training objectives with utility-specific KPIs is crucial for transitioning research models into critical infrastructure applications.

## Links

- [Abstract](https://arxiv.org/abs/2607.01966)
- [PDF](https://arxiv.org/pdf/2607.01966)

