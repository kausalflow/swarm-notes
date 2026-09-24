---
# CSL-compatible fields
title: "WPBench: A Comprehensive Benchmark for Wind Power Forecasting"
author:
  - literal: "Yuhan Zhu"
  - literal: "Jilin Hu"
  - literal: "Xinying Cai"
  - literal: "Yingshan Li"
  - literal: "Li Ma"
  - literal: "Xiangfei Qiu Linsen Li"
  - literal: "Kai Zhang"
  - literal: "Yao Fu"
  - literal: "Weihao Jiang"
  - literal: "Bin Yang"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24444"

# Custom fields
paper_id: "2609.24444"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:41Z"
created_at: "2026-09-24T09:38:41Z"
---

# WPBench: A Comprehensive Benchmark for Wind Power Forecasting

**Authors**: Yuhan Zhu, Jilin Hu, Xinying Cai, Yingshan Li, Li Ma, Xiangfei Qiu Linsen Li, Kai Zhang, Yao Fu, Weihao Jiang, Bin Yang
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24444](https://arxiv.org/abs/2609.24444)

## Summary

The paper introduces WPBench, a comprehensive and extensible benchmark for wind power forecasting that addresses gaps in existing evaluations by integrating 26 public datasets, 19 representative models across diverse families, domain-aligned metrics, and structure-aware diagnostics.

## Key Contributions

- Introduces WPBench, a comprehensive benchmark for wind power forecasting integrating 26 public datasets across diverse turbine scales and variable compositions.
- Evaluates 19 representative models spanning traditional methods, deep temporal models, spatio-temporal models, and foundation models under unified protocols.
- Provides structure-aware diagnostics across temporal, variable-dependency, and spatial-dependency perspectives alongside forecast-curve fidelity and computational efficiency metrics.

## Open Questions & Future Work

- [[balancing-numerical-accuracy-and-curve-fidelity]]

## Archivist Review

Rejected the benchmark concept note as benchmarks are archiving-level suites rather than standalone methodological concepts, but approved the open question regarding balancing point-wise accuracy and forecast-curve fidelity as it highlights a persistent, reusable evaluation and architectural challenge in energy forecasting.

### Approved Open Questions
- Balancing Accuracy and Curve Fidelity: Crucial for deployment in power system dispatch and grid operations where missing abrupt ramp events poses significant risks, even if point-wise errors are low.

### Rejected Candidates
- [concept] WPBench (`wpbench`) - low_impact: WPBench is a benchmark suite and platform rather than a reusable forecasting model, algorithm, or methodological concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.24444)
- [PDF](https://arxiv.org/pdf/2609.24444)

