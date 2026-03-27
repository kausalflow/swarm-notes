---
# CSL-compatible fields
title: "Dynamic Multi-period Experts for Online Time Series Forecasting"
author:
  - literal: "Seungha Hong"
  - literal: "Sukang Chae"
  - literal: "Suyeon Kim"
  - literal: "Sanghwan Jang"
  - literal: "Hwanjo Yu"
issued:
  date-parts:
    - [2026, 3, 10]
url: "https://arxiv.org/abs/2603.09062"

# Custom fields
paper_id: "2603.09062"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "continual-learning"
architectures:
  []
datasets:
  - "benchmark datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:18Z"
created_at: "2026-03-27T14:09:18Z"
---

# Dynamic Multi-period Experts for Online Time Series Forecasting

**Authors**: Seungha Hong, Sukang Chae, Suyeon Kim, Sanghwan Jang, Hwanjo Yu
**Date**: 2026-03-10
**Paper ID**: [openalex:2603.09062](https://arxiv.org/abs/2603.09062)

## Summary

This paper addresses the limitation of existing Online Time Series Forecasting (OTSF) methods by categorizing concept drift into Recurring Drift and Emergent Drift. The authors introduce DynaME (Dynamic Multi-period Experts), a hybrid framework specifically designed to manage this dual nature of drift. DynaME employs a committee of specialized experts that adaptively fit to recurring historical periodic patterns, while simultaneously utilizing a stable, general expert when high uncertainty signals the emergence of novel patterns. Experiments on standard benchmarks confirm that DynaME effectively adapts to complex drift scenarios and establishes a new state-of-the-art performance.

## Key Contributions

- Redefined concept drift in Online Time Series Forecasting (OTSF) into two types: Recurring Drift and Emergent Drift.
- Proposed DynaME (Dynamic Multi-period Experts), a novel hybrid framework to handle the dual nature of concept drift in OTSF.
- For Recurring Drift, DynaME uses a committee of experts dynamically fitted to relevant historical periodic patterns.
- For Emergent Drift, DynaME detects high uncertainty and switches reliance to a stable, general expert.
- Demonstrated significant performance improvement over existing baselines across multiple benchmark datasets and backbones in OTSF tasks.

## Limitations

The abstract does not explicitly detail limitations, but a potential area for future work is characterizing the complexity of managing the expert committee under extreme drift scenarios.

## Open Questions & Future Work

- [[extending-dynamme-to-foundation-models]]

## Key Concepts

- [Dynamic Multi-period Experts (DynaME)](../concepts/dynamic-multi-period-experts-dynameme.md): A hybrid online time series forecasting framework that uses specialized experts for recurring drift and a general expert for emergent drift.

## Datasets

- [benchmark datasets](../datasets/benchmark-datasets.md)

## Limitations

The abstract does not explicitly detail limitations, but a potential area for future work is characterizing the complexity of managing the expert committee under extreme drift scenarios.

## Links

- [Abstract](https://arxiv.org/abs/2603.09062)
- [PDF](https://arxiv.org/pdf/2603.09062)

