---
# CSL-compatible fields
title: "SpatialEpiBench: Benchmarking Spatial Information and Epidemic Priors in Forecasting"
author:
  - literal: "Ruiqi Lyu"
  - literal: "Alistair Turcan"
  - literal: "Bryan Wilder"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06530"

# Custom fields
paper_id: "2605.06530"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spatialepibench"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:21:22Z"
created_at: "2026-05-10T07:21:22Z"
---

# SpatialEpiBench: Benchmarking Spatial Information and Epidemic Priors in Forecasting

**Authors**: Ruiqi Lyu, Alistair Turcan, Bryan Wilder
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06530](https://arxiv.org/abs/2605.06530)

## Summary

This paper introduces SpatialEpiBench, a new benchmark designed to address the lack of standardized evaluation frameworks in spatiotemporal epidemic forecasting. By incorporating 11 diverse epidemic datasets and implementing rolling evaluations that mimic real-time public health practice, the authors reveal that contemporary models struggle significantly against simple baselines. The study systematically categorizes failure modes, providing actionable insights into the limitations of current geographic-adjacency and epidemic-prior-based forecasting techniques.

## Key Contributions

- Introduces SpatialEpiBench, a standardized benchmark consisting of 11 epidemic datasets featuring rolling evaluations and outbreak-specific metrics.
- Demonstrates that current state-of-the-art adjacency-informed models often fail to outperform a simple last-value baseline across varying forecast horizons.
- Identifies three critical failure modes in existing epidemic forecasting approaches: poor outbreak anticipation, limited robustness to sparsity/noise, and insufficient utility of static geographic adjacency.

## Open Questions & Future Work

- [[utility-of-geographic-adjacency-for-epidemic-forecasting]]

## Key Concepts

- [[spatialepibench]]: A standardized benchmark for evaluating spatiotemporal epidemic forecasting models using rolling evaluations and outbreak-specific metrics.

## Archivist Review

Approved the benchmark itself as it formalizes an evaluation protocol for a specific, difficult forecasting domain. Also approved the open question regarding the validity of spatial adjacency, as the paper provides systematic evidence questioning this common assumption in spatiotemporal modeling. Other dataset/concept candidates were rejected to maintain high selectivity.

### Approved Concepts
- SpatialEpiBench: Provides the first standardized evaluation framework for spatiotemporal epidemic forecasting under realistic public health constraints.

### Approved Open Questions
- Utility of Geographic Adjacency: Understanding the limitations of geographic adjacency is critical for moving beyond current performance plateaus in spatiotemporal epidemic forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.06530)
- [PDF](https://arxiv.org/pdf/2605.06530)

