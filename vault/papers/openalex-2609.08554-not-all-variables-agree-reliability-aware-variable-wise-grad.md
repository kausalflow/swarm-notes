---
# CSL-compatible fields
title: "Not All Variables Agree: Reliability-Aware Variable-Wise Gradient Surgery for Multivariate Time-Series Forecasting"
author:
  - literal: "Jinwoo Park"
  - literal: "Hyeongwon Kang"
  - literal: "Pilsung Kang"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08554"

# Custom fields
paper_id: "2609.08554"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "per-variable-surgery"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:15:47Z"
created_at: "2026-09-10T09:15:47Z"
---

# Not All Variables Agree: Reliability-Aware Variable-Wise Gradient Surgery for Multivariate Time-Series Forecasting

**Authors**: Jinwoo Park, Hyeongwon Kang, Pilsung Kang
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08554](https://arxiv.org/abs/2609.08554)

## Summary

Multivariate time-series forecasting is typically trained by optimizing an aggregated scalar loss, which conceals underlying gradient conflicts among variables. To address this, the authors find that variable-wise gradient disagreements are prevalent and propose Per-Variable Surgery (PV-Surgery), an optimizer-side training method that uses reliability-aware selection, conditional pooling, and gradient alignment. Experiments across multiple backbones, datasets, and horizons demonstrate consistent reductions in MSE and MAE.

## Key Contributions

- Reveals that 30.6% of pairwise variable-wise gradient cosine similarities are negative on average in multivariate time-series forecasting, yet conflict does not uniformly predict performance harm.
- Proposes Per-Variable Surgery (PV-Surgery), an optimizer-side strategy utilizing reliability-aware selection and conditional pooling to align variable-wise gradients while restoring input norms.
- Demonstrates across five backbones, seven datasets, and four forecasting horizons that PV-Surgery reduces MSE by 3.61% and MAE by 2.93% on average.

## Open Questions & Future Work

- [[efficient-reliability-aware-variable-wise-gradient-surgery]]

## Key Concepts

- [[per-variable-surgery]]: An optimizer-side training strategy that performs reliability-aware variable-wise gradient surgery to resolve gradient conflicts in multivariate time-series forecasting.

## Archivist Review

Approved the overarching optimization concept 'Per-Variable Surgery' as it provides a distinct, reusable gradient alignment approach for multivariate time-series forecasting. Approved the corresponding open question regarding computational efficiency and fidelity scaling of gradient proxies. No datasets met the strict novelty and naming threshold.

### Approved Concepts
- Per-Variable Surgery: Introduces a novel variable-wise gradient surgery optimizer-side strategy to resolve gradient conflicts in multivariate time-series forecasting without dropping variables.

### Approved Open Questions
- Efficient Reliability-Aware Variable-Wise Gradient Surgery: Addressing training overhead and fidelity limits in variable-wise gradient surgery is crucial for scaling these optimization strategies to larger multivariate time-series models and diverse real-world datasets.

## Links

- [Abstract](https://arxiv.org/abs/2609.08554)
- [PDF](https://arxiv.org/pdf/2609.08554)

