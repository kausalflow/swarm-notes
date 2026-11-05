---
# CSL-compatible fields
title: "Cross-Domain Joint-Embedding Pretraining For Heterogeneous Industrial Time Series"
author:
  - literal: "Jonathan Adam Rico"
  - literal: "Nagarajan Raghavan"
  - literal: "Senthilnath Jayavelu"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02489"

# Custom fields
paper_id: "2611.02489"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "self-supervised-learning"
  - "representation-learning"
  - "pre-training"
  - "fine-tuning"
  - "anomaly-detection"
  - "robustness"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "jepa-hits"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:51:42Z"
created_at: "2026-11-05T12:51:42Z"
---

# Cross-Domain Joint-Embedding Pretraining For Heterogeneous Industrial Time Series

**Authors**: Jonathan Adam Rico, Nagarajan Raghavan, Senthilnath Jayavelu
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02489](https://arxiv.org/abs/2611.02489)

## Summary

The paper introduces JEPA-HITS, a cross-domain self-supervised pretraining framework using joint-embedding predictive architecture designed for heterogeneous industrial time series. By training a single encoder across diverse domains such as batteries, semiconductor chemical mechanical planarization, CNC machining, and bearings while preserving temporal scales, the method yields robust representations for downstream regression and classification. Extensive evaluation shows that leave-one-domain-out pretraining substantially outperforms random initialization across multiple predictive maintenance benchmarks under reduced-label conditions.

## Key Contributions

- Proposes JEPA-HITS, a cross-domain self-supervised pretraining framework using a joint-embedding predictive architecture for heterogeneous industrial time series.
- Demonstrates that leave-one-domain-out (LODO) pretraining across diverse domains (battery, CMP, CNC machining, and bearing) significantly improves representation reuse on downstream regression and classification tasks under reduced-label settings.
- Reduces RMSE on battery remaining useful life (RUL) from 10.72 to 7.95, CMP from 4.34 to 3.89, and tool wear regression from 13.53 to 11.72 compared to random initialization.
- Improves bearing fault diagnosis macro-F1 from 0.547 to 0.737 over random initialization baselines.

## Limitations

Future work could explore scaling to a wider variety of industrial domains and analyzing the impact of domain discrepancy on representation quality.

## Open Questions & Future Work

- [[robustness-to-outliers-and-distribution-shifts]]

## Key Concepts

- [[jepa-hits]]: A cross-domain self-supervised pretraining framework using joint-embedding predictive architecture for heterogeneous industrial time series.

## Archivist Review

Approved the core JEPA-HITS framework concept and its associated open question regarding robustness to outliers and distribution shifts. No standalone datasets were approved since only broad industry sectors were named.

### Approved Concepts
- Joint-Embedding Predictive Architecture for Heterogeneous Industrial Time Series (JEPA-HITS): JEPA-HITS is the primary methodological contribution of the paper, enabling cross-domain self-supervised pretraining across diverse industrial time series while preserving temporal scales.

### Approved Open Questions
- Robustness to Outliers and Distribution Shifts: Real-world industrial data is frequently plagued by missing values, sensor failures, and severe distribution shifts; understanding how cross-domain pretraining copes with these conditions is crucial for robust industrial deployment.

## Links

- [Abstract](https://arxiv.org/abs/2611.02489)
- [PDF](https://arxiv.org/pdf/2611.02489)

