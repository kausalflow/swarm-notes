---
# CSL-compatible fields
title: "Pneuma: A Large-Scale Real-World Time Series Benchmark for Commercial Aircraft Predictive Maintenance"
author:
  - literal: "Jiafeng Lin"
  - literal: "Yutian Zhang"
  - literal: "Huan Zhang"
  - literal: "Yuxuan Wang"
  - literal: "Jinyan Feng"
  - literal: "Yuhui Liu"
  - literal: "Zhongyi Pei"
  - literal: "Jianmin Wang"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37563"

# Custom fields
paper_id: "2610.37563"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "pneuma"
concept_slugs:
  []
dataset_slugs:
  - "pneuma"
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:04:40Z"
created_at: "2026-10-30T11:04:40Z"
---

# Pneuma: A Large-Scale Real-World Time Series Benchmark for Commercial Aircraft Predictive Maintenance

**Authors**: Jiafeng Lin, Yutian Zhang, Huan Zhang, Yuxuan Wang, Jinyan Feng, Yuhui Liu, Zhongyi Pei, Jianmin Wang
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37563](https://arxiv.org/abs/2610.37563)

## Summary

The paper introduces Pneuma, a large-scale public time-series benchmark designed for commercial aircraft predictive maintenance. Spanning over 920 million multivariate time steps across four aircraft types and 9 real-world fault scenarios, Pneuma targets three core tasks: multivariate forecasting, supervised fault classification, and unsupervised anomaly detection. Evaluating over 25 models reveals that current methods struggle with subtle fault signatures, establishing Pneuma as a rigorous foundation for reproducible aviation maintenance research.

## Key Contributions

- Introduced Pneuma, the first public large-scale benchmark for commercial aircraft predictive maintenance containing over 920 million multivariate time steps across 9 verified fault scenarios.
- Structured the benchmark across three core tasks: multivariate forecasting, supervised fault classification, and unsupervised anomaly detection using real maintenance logs.
- Evaluated over 25 models from four methodological families on 9 curated subsets, revealing that contemporary models struggle with subtle fault signatures in complex aviation time series.

## Archivist Review

In accordance with the review policy, dataset candidates are limited and Pneuma is approved as a key named dataset. The concept and open question candidates were rejected as they correspond primarily to a benchmark dataset and routine data extension work rather than reusable architectural concepts or profound algorithmic bottlenecks.

### Rejected Candidates
- [concept] Pneuma (`pneuma`) - not_reusable: Pneuma is primarily a benchmark dataset and evaluation suite rather than a reusable algorithmic mechanism or architectural concept.
- [open_question] Cross-System Aircraft Predictive Maintenance Generalization (`aircraft-predictive-maintenance-generalization`) - weak_evidence: The question proposes routine future work involving extending data coverage and adding more aircraft types rather than addressing a deep theoretical bottleneck.

## Datasets

- [[pneuma]]

## Links

- [Abstract](https://arxiv.org/abs/2610.37563)
- [PDF](https://arxiv.org/pdf/2610.37563)

