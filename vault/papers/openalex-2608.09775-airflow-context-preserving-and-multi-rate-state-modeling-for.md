---
# CSL-compatible fields
title: "AirFlow: Context Preserving and Multi-Rate State Modeling for Air Quality Forecasting"
author:
  - literal: "Fan Yang"
  - literal: "Nan Chen"
  - literal: "Yijie Dong"
  - literal: "Yuchen Zhang"
  - literal: "Wei Zhang"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09775"

# Custom fields
paper_id: "2608.09775"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "state-space-model"
  - "ssm"
  - "multivariate-time-series"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "airflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:16Z"
created_at: "2026-08-13T06:09:16Z"
---

# AirFlow: Context Preserving and Multi-Rate State Modeling for Air Quality Forecasting

**Authors**: Fan Yang, Nan Chen, Yijie Dong, Yuchen Zhang, Wei Zhang
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09775](https://arxiv.org/abs/2608.09775)

## Summary

AirFlow is a lightweight, pollutant-aware dual-stream framework for air quality forecasting that addresses heterogeneous channel distributions and multi-scale temporal dynamics without relying on graph propagation or signal decomposition. It features a statistic-guided normalization routing mechanism and a hierarchical dual-stream state model with gated bidirectional cross-attention. Extensive experiments demonstrate that AirFlow achieves state-of-the-art accuracy with minimal computational overhead.

## Key Contributions

- Proposes AirFlow, a pollutant-aware dual-stream framework for air quality forecasting that avoids additional graph propagation and predefined signal decomposition.
- Introduces a statistic-guided normalization routing mechanism that dynamically selects normalization paths based on 24-hour autocorrelation and distribution drift per pollutant channel.
- Designs a hierarchical dual-stream state model combining multi-scale state space propagation and gated bidirectional cross-attention for adaptive representation fusion.
- Achieves top performance across multiple city benchmarks, winning 34 of 36 metrics comparisons with up to 11.11% RMSE reduction while using only 0.0483M parameters and 0.0215G FLOPs.

## Limitations

Future work could extend the framework to handle broader spatio-temporal dynamics across sparse monitoring networks.

## Open Questions & Future Work

- [[incorporating-multimodal-urban-covariates-and-physical-priors]]

## Key Concepts

- [[airflow]]: A pollutant-aware dual-stream forecasting framework combining statistic-guided normalization routing and hierarchical dual-stream state modeling for multivariate air quality prediction.

## Archivist Review

Approved the core framework concept 'airflow' and the open question regarding multimodal urban atmospheric modeling. Both items are well-defined, address key challenges in multivariate time series and air quality forecasting, and meet vault standards for novelty and reusability.

### Approved Concepts
- AirFlow: AirFlow introduces a pollutant-aware dual-stream framework addressing heterogeneous periodicity and distribution drift across pollutant channels via statistic-guided normalization routing and hierarchical dual-state modeling.

### Approved Open Questions
- Multimodal Urban Atmospheric Modeling: Crucial for advancing air quality prediction models from purely historical/univariate-multivariate time series approaches to robust, physically grounded multi-modal urban environmental systems.

## Links

- [Abstract](https://arxiv.org/abs/2608.09775)
- [PDF](https://arxiv.org/pdf/2608.09775)

