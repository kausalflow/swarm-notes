---
# CSL-compatible fields
title: "Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters"
author:
  - literal: "Chao He"
  - literal: "Jianyu Xu"
  - literal: "Xinyi Guo"
  - literal: "Ruiqi Liu"
  - literal: "Haobin Ding"
  - literal: "Ruiqi He"
  - literal: "Yuntong Xie"
  - literal: "Dongqing Song"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.07834"

# Custom fields
paper_id: "2610.07834"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "freshcast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:33:42Z"
created_at: "2026-10-09T11:33:42Z"
---

# Retrieval Is Not Enough: Refreshing Memory for Frozen Time-Series Forecasters

**Authors**: Chao He, Jianyu Xu, Xinyi Guo, Ruiqi Liu, Haobin Ding, Ruiqi He, Yuntong Xie, Dongqing Song
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.07834](https://arxiv.org/abs/2610.07834)

## Summary

Retrieval-augmented time-series forecasting typically constructs memory only from training data and leaves post-training observations unused, rendering retrieved information stale during deployment. The authors propose FreshCast, a plug-in framework that keeps pre-trained forecasters frozen while continuously updating a non-parametric memory with new observations and calibrating retrieval influence via closed-form validation. Extensive evaluations across seven benchmarks and ten architectures demonstrate that FreshCast consistently reduces mean squared error compared to static retrieval and online baselines.

## Key Contributions

- Proposes FreshCast, a plug-in retrieval framework that keeps time-series forecasters frozen while continuously updating a non-parametric memory with newly revealed post-training observations.
- Formulates a memory forecast using relational kernel regression and calibrates its combination weight in closed form on validation data.
- Reduces average MSE across seven benchmarks and ten architectures by 14.6% and 5.6% at input lengths 96 and 720, outperforming existing retrieval-augmented and online baselines.

## Open Questions & Future Work

- [[query-level-reference-trust-forecasting]]

## Key Concepts

- [[freshcast]]: A plug-in retrieval framework for frozen time-series forecasters that continuously updates non-parametric memory with new observations and calibrates its influence in closed form.

## Archivist Review

Approved the primary framework FreshCast as a reusable plug-in retrieval method for frozen time-series forecasters, along with the open question regarding query-level reference trust in forecasting. All other routine candidates were excluded to maintain knowledge vault standards.

### Approved Concepts
- FreshCast: FreshCast is the core framework introduced in the paper to continuously update non-parametric retrieval memory and calibrate weights for frozen time-series forecasters.

### Approved Open Questions
- Query-Level Reference Trust in Forecasting: Understanding how to reliably evaluate and trust historical references query-by-query is fundamental to advancing retrieval-augmented forecasting without risking performance degradation.

## Links

- [Abstract](https://arxiv.org/abs/2610.07834)
- [PDF](https://arxiv.org/pdf/2610.07834)

