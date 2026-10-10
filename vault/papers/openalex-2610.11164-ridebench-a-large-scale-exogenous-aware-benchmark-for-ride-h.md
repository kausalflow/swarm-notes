---
# CSL-compatible fields
title: "RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting"
author:
  - literal: "Shengsheng Lin"
  - literal: "Jing Hu"
  - literal: "Zhengyang Hu"
  - literal: "Jiazheng Sun"
  - literal: "Zichun Cao"
  - literal: "Siwei Sun"
  - literal: "Zhichao Zou"
  - literal: "Enyun Yu"
  - literal: "Dongdong Li"
  - literal: "Xinyi Hu"
  - literal: "Weiwei Lin"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11164"

# Custom fields
paper_id: "2610.11164"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ridebench"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:02Z"
created_at: "2026-10-10T10:52:02Z"
---

# RideBench: A Large-Scale Exogenous-Aware Benchmark for Ride-Hailing Time Series Forecasting

**Authors**: Shengsheng Lin, Jing Hu, Zhengyang Hu, Jiazheng Sun, Zichun Cao, Siwei Sun, Zhichao Zou, Enyun Yu, Dongdong Li, Xinyi Hu, Weiwei Lin
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11164](https://arxiv.org/abs/2610.11164)

## Summary

The authors introduce Ride-Hailing, a large four-year dataset synthesized from marketplace data across 200 spatial areas, and RideBench, a benchmark evaluating over 30 forecasting models on exogenous-aware ride-hailing forecasting. The study covers both regular week-ahead and long-horizon 8-week-ahead forecasting (up to 2,688 steps) under weather, holiday, and large-scale event scenarios. Results reveal significant limitations in current models' ability to leverage future-known exogenous variables and maintain simultaneous accuracy across short and long horizons.

## Key Contributions

- Introduces Ride-Hailing, a large-scale ride-hailing time series dataset spanning 4 years across 200 spatial areas with weather, holiday, and event exogenous scenarios.
- Releases RideBench, a comprehensive benchmark evaluating over 30 forecasting methods (endogenous, exogenous-aware, and foundation models) across week-ahead and 8-week-ahead horizons.
- Demonstrates that current exogenous-aware models struggle to capture disturbance-induced pattern changes and long-horizon trends, highlighting critical gaps in existing time series methodologies.

## Open Questions & Future Work

- [[long-horizon-multi-objective-balancing]]
- [[exogenous-driven-pattern-modeling]]

## Key Concepts

- [[ridebench]]: A comprehensive large-scale benchmark for exogenous-aware ride-hailing time series forecasting.

## Archivist Review

Approved the core benchmark concept RideBench along with two high-value open questions regarding long-horizon multi-objective balancing and exogenous-driven pattern modeling in urban mobility forecasting. The dataset itself was rejected as a standalone vault dataset due to its generic naming and vault guidelines against newly introduced proprietary dataset names.

### Approved Concepts
- RideBench: It establishes the first large-scale, exogenous-aware ride-hailing forecasting benchmark covering diverse disturbance scenarios and long horizons up to 2,688 steps.

### Approved Open Questions
- Long-Horizon Multi-Objective Balancing: Crucial for bridging the gap between short-term operational dispatching and long-term strategic planning in urban mobility systems.
- Exogenous-Driven Pattern Modeling: Essential for robust decision-making under weather anomalies, public holidays, and large-scale cultural or sporting events.

### Rejected Candidates
- [dataset] Ride-Hailing Dataset (`ride-hailing`) - not_reusable: Dataset name is generic and lacks broad multi-paper reusability as an independent domain benchmark outside this specific paper's introduction.

## Links

- [Abstract](https://arxiv.org/abs/2610.11164)
- [PDF](https://arxiv.org/pdf/2610.11164)

