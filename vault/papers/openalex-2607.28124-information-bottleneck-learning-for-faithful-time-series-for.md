---
# CSL-compatible fields
title: "Information Bottleneck Learning for Faithful Time Series Forecasting Explanations"
author:
  - literal: "Xu Zheng"
  - literal: "Wei Cheng"
  - literal: "Zhuomin Chen"
  - literal: "Mo Sha"
  - literal: "Jingchao Ni"
  - literal: "Dongsheng Luo"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28124"

# Custom fields
paper_id: "2607.28124"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ib-forecast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:26:25Z"
created_at: "2026-08-02T07:26:25Z"
---

# Information Bottleneck Learning for Faithful Time Series Forecasting Explanations

**Authors**: Xu Zheng, Wei Cheng, Zhuomin Chen, Mo Sha, Jingchao Ni, Dongsheng Luo
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28124](https://arxiv.org/abs/2607.28124)

## Summary

The authors propose IB-Forecast, an inherently interpretable multivariate time-series forecasting framework that bridges the gap between interpretable-by-design forecasters and faithfulness-oriented verification. By decomposing forecasts into periodic and residual components using explainable masks with a budget-constrained information bottleneck, the model achieves state-of-the-art forecasting accuracy while providing high-fidelity explanations at zero additional inference cost.

## Key Contributions

- Proposes IB-Forecast, an inherently interpretable multivariate time-series forecasting framework that decomposes predictions into learned periodic and residual components.
- Integrates a budget-constrained information bottleneck into end-to-end optimization to directly control explanation sparsity and guarantee explanation fidelity.
- Demonstrates that IB-Forecast matches leading black-box forecasting accuracy while outperforming post-hoc explanation baselines under matched sparsity budgets.

## Open Questions & Future Work

- [[faithful-time-series-forecasting-explanations]]

## Key Concepts

- [[ib-forecast]]: An inherently interpretable multivariate time-series forecasting framework that uses a budget-constrained information bottleneck to deliver faithful explanations.

## Archivist Review

Approved the central interpretable forecasting framework (IB-Forecast) and its core open question regarding faithful explanations under non-stationary dynamics and complex horizons, strictly adhering to scarcity and uniqueness constraints.

### Approved Concepts
- IB-Forecast: It is the core methodological contribution, introducing a budget-constrained information bottleneck to provide natively faithful time-series forecasting explanations.

### Approved Open Questions
- Faithful Time Series Forecasting Explanations: Extending faithful bottleneck-based interpretability to broader classes of non-stationary and ultra-long-horizon multivariate forecasting problems is critical for reliable high-stakes decision making.

## Links

- [Abstract](https://arxiv.org/abs/2607.28124)
- [PDF](https://arxiv.org/pdf/2607.28124)

