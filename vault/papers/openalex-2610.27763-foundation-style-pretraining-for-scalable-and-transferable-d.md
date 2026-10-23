---
# CSL-compatible fields
title: "Foundation-Style Pretraining for Scalable and Transferable Distributed PV Forecasting"
author:
  - literal: "Dayin Chen"
  - literal: "Xiaodan Shi"
  - literal: "Xin Xu"
  - literal: "Zhongyue Su"
  - literal: "Shibo Zhu"
  - literal: "Ruizhe Deng"
  - literal: "Dongxiao Zhang"
  - literal: "Yuntian Chen"
  - literal: "Jinyue Yan"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.27763"

# Custom fields
paper_id: "2610.27763"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "zero-shot-learning"
  - "long-context"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:05Z"
created_at: "2026-10-23T09:40:05Z"
---

# Foundation-Style Pretraining for Scalable and Transferable Distributed PV Forecasting

**Authors**: Dayin Chen, Xiaodan Shi, Xin Xu, Zhongyue Su, Shibo Zhu, Ruizhe Deng, Dongxiao Zhang, Yuntian Chen, Jinyue Yan
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.27763](https://arxiv.org/abs/2610.27763)

## Summary

This paper introduces a foundation-style pretraining framework for distributed photovoltaic (PV) forecasting that learns from heterogeneous multi-site and multi-horizon data by formulating NWP-assisted prediction as a sequence-completion problem. By evaluating different pretraining objectives, the authors demonstrate that a mixed reconstruction objective provides superior zero-shot generalization and downstream adaptability across 479 distributed PV stations, outperforming existing generalist time-series foundation models and station-specific baselines.

## Key Contributions

- Proposes a domain-specific foundation-style pretraining framework that unifies historical PV power, meteorological observations, future NWP forecasts, and time encodings as a sequence-completion problem.
- Systematically evaluates three pretraining objectives (forecast-aligned reconstruction, generic reconstruction, and mixed reconstruction), showing that mixed reconstruction achieves the best balance across accuracy and downstream adaptation.
- Demonstrates zero-shot generalization across 139 spatially held-out PV stations spanning forecasting horizons from 6 hours to 7 days, outperforming station-specific baselines and generalist time-series foundation models.

## Archivist Review

The paper applies standard foundation-style pretraining and sequence-completion framing to distributed photovoltaic forecasting. Since no distinct, highly reusable algorithmic concept or non-boilerplate open question was provided, all candidates are rejected to preserve vault quality.

### Rejected Candidates
- [open_question] Cross-Regional Transfer in PV Forecasting (`cross-regional-transfer-pv-forecasting`) - low_impact: The open question is standard future work proposing to extend evaluation to new regions, which lacks a specific methodological gap or technical mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.27763)
- [PDF](https://arxiv.org/pdf/2610.27763)

