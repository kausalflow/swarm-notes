---
# CSL-compatible fields
title: "Into the ORBIT for Time Series: Training Regimes for Foundation Models"
author:
  - literal: "Hongjie Xia"
  - literal: "Yiding Liu"
  - literal: "Yifan Hu"
  - literal: "Peiyuan Liu"
  - literal: "Zewei Dong"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13262"

# Custom fields
paper_id: "2608.13262"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "transformer"
  - "encoder-only"
  - "zero-shot-learning"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  - "gift-eval"
  - "fev-bench"
concept_slugs:
  - "orbit"
dataset_slugs:
  - "gift-eval"
  - "fev-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:17:32Z"
created_at: "2026-08-16T05:17:32Z"
---

# Into the ORBIT for Time Series: Training Regimes for Foundation Models

**Authors**: Hongjie Xia, Yiding Liu, Yifan Hu, Peiyuan Liu, Zewei Dong
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13262](https://arxiv.org/abs/2608.13262)

## Summary

This paper investigates training regimes for time series foundation models, noting that prior work focused primarily on architectural innovations while neglecting pre-training distribution control. The authors introduce ORBIT, a training paradigm featuring Bootstrap Multi-Level Sampling and Omni-Range Incremental Training, alongside a Rank-Guided Cross-Depth Alignment objective. Using ORBIT, they train Falcon-2.0, a univariate encoder-only Transformer that achieves strong zero-shot forecasting performance on GIFT-Eval and fev-bench.

## Key Contributions

- Introduces ORBIT, a controllable training paradigm combining Bootstrap Multi-Level Sampling and Omni-Range Incremental Training for time series foundation models.
- Proposes Rank-Guided Cross-Depth Alignment as a training objective that utilizes late-layer representations as stop-gradient teachers for shallow layers without extra inference cost.
- Trains Falcon-2.0, a univariate encoder-only Transformer utilizing missingness-aware triple-channel patch tokenization and parallel patch prediction under the ORBIT paradigm.
- Demonstrates strong zero-shot forecasting performance across diverse domains and frequencies on GIFT-Eval and fev-bench benchmarks.

## Open Questions & Future Work

- [[multivariate-covariate-forecasting-limits]]

## Key Concepts

- [[orbit]]: A training paradigm for time series foundation models that combines bootstrap multi-level sampling and omni-range incremental training to explicitly control data distributions, context windows, and prediction horizons.

## Archivist Review

Approved the primary training paradigm concept (ORBIT), the two datasets evaluated in the paper, and the open question regarding covariate-rich forecasting limits. All candidates meet the rigorous vault inclusion criteria.

### Approved Concepts
- ORBIT (Omni-Range Bootstrap Incremental Training): Introduces a novel training paradigm combining bootstrap multi-level sampling and omni-range incremental training to control pre-training distributions for time series foundation models.

### Approved Open Questions
- Multivariate and Covariate-Rich Forecasting Limits: Crucial for bridging the performance gap between univariate and multivariate/covariate-aware forecasting tasks in time series foundation models.

## Datasets

- [[gift-eval]]
- [[fev-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2608.13262)
- [PDF](https://arxiv.org/pdf/2608.13262)

