---
# CSL-compatible fields
title: "Learning Local Heterogeneity and Cross-Region Context for Large-Scale Traffic Forecasting"
author:
  - literal: "Qi Feng"
  - literal: "Zidong Wang"
  - literal: "Bo Li"
  - literal: "Xiaoguang Gao"
  - literal: "Jiayu Zhang"
  - literal: "Chenfeng Wang"
  - literal: "Kaifang Wan"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27637"

# Custom fields
paper_id: "2609.27637"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "spatial-temporal"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lorest"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:40Z"
created_at: "2026-09-26T09:37:40Z"
---

# Learning Local Heterogeneity and Cross-Region Context for Large-Scale Traffic Forecasting

**Authors**: Qi Feng, Zidong Wang, Bo Li, Xiaoguang Gao, Jiayu Zhang, Chenfeng Wang, Kaifang Wan
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27637](https://arxiv.org/abs/2609.27637)

## Summary

This paper addresses the challenge of large-scale traffic forecasting by proposing LoReST, a Local-Region Spatial Temporal network that models spatial dependencies at two complementary granularities: node neighborhoods and road network regions. LoReST employs relation-aware local aggregation to capture heterogeneous dependencies within geographic neighborhoods while utilizing cross-region attention to efficiently exchange long-range context. Extensive experiments on the LargeST benchmark demonstrate significant performance improvements in MAE, RMSE, and MAPE over existing baselines.

## Key Contributions

- Proposes LoReST, a Local-Region Spatial Temporal network, to jointly model local spatial heterogeneity and cross-range regional context for large-scale traffic forecasting.
- Introduces relation-aware local aggregation using road and direction-specific feature transformations to capture heterogeneous spatial dependencies within geographic neighborhoods.
- Constructs regional representations via mean pooling and exchanges long-range context through inter-region attention to avoid high computational costs of all-pairs node interactions.
- Achieves average relative error reductions of 4.78% in MAE, 3.60% in RMSE, and 5.75% in MAPE across datasets of the LargeST benchmark.

## Open Questions & Future Work

- [[spatial-priors-in-time-series-foundation-models]]

## Key Concepts

- [[lorest]]: A local-region spatial temporal network for large-scale traffic forecasting that models spatial dependencies at node neighborhood and regional granularities.

## Archivist Review

Approved the core 'LoReST' architecture concept for capturing multi-granular spatial dependencies and the open question regarding spatial priors in time-series foundation models. Kept dataset approvals empty because the reference is to a benchmark suite rather than individual named datasets.

### Approved Concepts
- LoReST: Central model introduced in the paper for large-scale traffic forecasting, combining local heterogeneity aggregation and cross-region attention.

### Approved Open Questions
- Spatial Priors in Time-Series Foundation Models: Connecting specialized traffic forecasting inductive biases (such as local road heterogeneity and region partitions) with foundation models is a crucial step toward generalized, zero-shot spatio-temporal forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2609.27637)
- [PDF](https://arxiv.org/pdf/2609.27637)

