---
# CSL-compatible fields
title: "ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall"
author:
  - literal: "Yichi Zhang"
  - literal: "Ke Zhu"
  - literal: "Zhoufan Zhu"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.04576"

# Custom fields
paper_id: "2606.04576"
paper_source: "openalex"
domain: "finance"
tags:
  - "finance"
  - "time-series"
  - "forecasting"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "resga-retrieval-enhanced-self-grouping-autoencoder"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:40:21Z"
created_at: "2026-06-06T07:40:21Z"
---

# ReSGA: A Large Tail Risk Model for Learning Value-at-Risk and Expected Shortfall

**Authors**: Yichi Zhang, Ke Zhu, Zhoufan Zhu
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.04576](https://arxiv.org/abs/2606.04576)

## Summary

ReSGA is a large-scale, retrieval-enhanced self-grouping autoencoder designed to model tail risks in financial assets by capturing complex cross-sectional dependencies and temporal dynamics. Evaluated on nearly a century of US equity data, the model significantly outperforms diverse econometric and machine learning baselines in both statistical backtesting and economic portfolio performance. The authors further provide insights into model interpretability through group-importance analysis and clarify the drivers of performance improvements through a systematic scaling study.

## Key Contributions

- Introduces ReSGA, a large-scale retrieval-enhanced autoencoder for joint estimation of Value-at-Risk (VaR) and Expected Shortfall (ES).
- Demonstrates superior out-of-sample forecasting performance against 12 state-of-the-art econometric and ML baselines using US equity data (1926-2023).
- Introduces a size-enhanced left-side momentum strategy that yields significant economic gains from ReSGA-based risk forecasts.
- Provides a systematic scaling analysis showing that joint VaR-ES forecast improvements are primarily driven by data complexity rather than model parameter counts.

## Open Questions & Future Work

- [[universal-large-tail-risk-models]]

## Key Concepts

- [[resga-retrieval-enhanced-self-grouping-autoencoder]]: A large-scale autoencoder architecture that leverages retrieval and self-grouping to capture cross-sectional and temporal risk dynamics.

## Archivist Review

I have approved the ReSGA architecture as a novel approach to tail risk modeling that combines retrieval and autoencoding, and the open question regarding universal tail-risk models, as it captures a fundamental paradigm shift away from asset-specific estimation in finance. Other potential concepts like the 'size-enhanced left-side momentum strategy' were rejected as they are domain-specific investment strategies rather than generalizable machine learning mechanisms.

### Approved Concepts
- Retrieval-Enhanced Self-Grouping Autoencoder (ReSGA): It is the central architecture introduced for jointly forecasting Value-at-Risk (VaR) and Expected Shortfall (ES).

### Approved Open Questions
- Universal Large-Scale Tail-Risk Models: Understanding the feasibility and performance of universal, large-scale models in financial tail risk forecasting is critical, as it challenges the standard econometric reliance on asset-specific modeling and potentially provides a more robust, scalable approach to managing systemic risk across thousands of assets.

## Links

- [Abstract](https://arxiv.org/abs/2606.04576)
- [PDF](https://arxiv.org/pdf/2606.04576)

