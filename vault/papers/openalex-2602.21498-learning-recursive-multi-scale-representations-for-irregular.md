---
# CSL-compatible fields
title: "Learning Recursive Multi-Scale Representations for Irregular Multivariate Time Series Forecasting"
author:
  - literal: "Boyuan Li"
  - literal: "Zhen Liu"
  - literal: "Yicheng Luo"
  - literal: "Qianli Ma"
issued:
  date-parts:
    - [2026, 2, 25]
url: "https://arxiv.org/abs/2602.21498"

# Custom fields
paper_id: "2602.21498"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "irregular-data"
  - "multi-scale-modeling"
architectures:
  []
datasets:
  - "real-world datasets"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:51Z"
created_at: "2026-03-27T14:08:51Z"
---

# Learning Recursive Multi-Scale Representations for Irregular Multivariate Time Series Forecasting

**Authors**: Boyuan Li, Zhen Liu, Yicheng Luo, Qianli Ma
**Date**: 2026-02-25
**Paper ID**: [openalex:2602.21498](https://arxiv.org/abs/2602.21498)

## Summary

This paper introduces ReIMTS, a novel Recursive multi-scale modeling approach designed to address the challenge of forecasting Irregular Multivariate Time Series (IMTS) without losing the informative sampling pattern information typically lost during resampling. ReIMTS maintains the original, irregular timestamps by recursively splitting the series into subsamples with shorter time periods, allowing it to model dependencies across multiple scales directly. A key component is the irregularity-aware representation fusion mechanism, which combines features learned across these varying scales based on the true sampling timestamps to capture global-to-local relationships. Extensive evaluations show that ReIMTS significantly improves forecasting accuracy, achieving an average performance gain of 27.1% across multiple benchmarks and models.

## Key Contributions

- Proposed ReIMTS, a Recursive multi-scale modeling approach for Irregular Multivariate Time Series (IMTS) that avoids resampling to preserve valuable sampling pattern information.
- Introduced an irregularity-aware representation fusion mechanism that leverages original sampling timestamps across recursively generated long-to-short subsamples to capture global-to-local dependencies.
- Demonstrated an average performance improvement of 27.1% in forecasting tasks across different models and real-world datasets compared to existing methods.

## Limitations

The paper focuses primarily on modeling dependencies and improvements over existing multi-scale methods; detailed analysis of specific failure modes or sensitivity to extreme irregularity is not provided in the abstract.

## Open Questions & Future Work

- [[reimts-ode-model-compatibility]]
- [[reimts-diffusion-model-integration]]
- [[wider-backbone-compatibility-assessment]]

## Key Concepts

- [Recursive Multi-scale Modeling for IMTS](../concepts/recursive-multi-scale-modeling-imts.md): A novel method that recursively splits irregular multivariate time series into subsamples with progressively shorter time periods without resampling to preserve original sampling information.
- [Irregularity-Aware Representation Fusion](../concepts/irregularity-aware-representation-fusion.md): A mechanism that fuses representations learned across different time scales based on the original, unchanged sampling timestamps to capture global-to-local dependencies.

## Datasets

- [real-world datasets](../datasets/real-world-datasets.md)

## Limitations

The paper focuses primarily on modeling dependencies and improvements over existing multi-scale methods; detailed analysis of specific failure modes or sensitivity to extreme irregularity is not provided in the abstract.

## Links

- [Abstract](https://arxiv.org/abs/2602.21498)
- [PDF](https://arxiv.org/pdf/2602.21498)

