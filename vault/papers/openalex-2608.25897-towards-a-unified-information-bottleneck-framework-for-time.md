---
# CSL-compatible fields
title: "Towards A Unified Information Bottleneck Framework for Time Series Explanations"
author:
  - literal: "Xu Zheng"
  - literal: "Zichuan Liu"
  - literal: "Zhuomin Chen"
  - literal: "Mayur Akewar"
  - literal: "Janki Bhimani"
  - literal: "Jason Liu"
  - literal: "Mo Sha"
  - literal: "Jingchao Ni"
  - literal: "Wei Cheng"
  - literal: "Dongsheng Luo"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25897"

# Custom fields
paper_id: "2608.25897"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "explainability"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:20Z"
created_at: "2026-08-28T16:59:20Z"
---

# Towards A Unified Information Bottleneck Framework for Time Series Explanations

**Authors**: Xu Zheng, Zichuan Liu, Zhuomin Chen, Mayur Akewar, Janki Bhimani, Jason Liu, Mo Sha, Jingchao Ni, Wei Cheng, Dongsheng Luo
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25897](https://arxiv.org/abs/2608.25897)

## Summary

This paper introduces a unified information-theoretic framework for time-series explainability that bridges attribution and counterfactual reasoning through the Information Bottleneck principle. By formulating a novel objective function that prevents trivial solutions and out-of-distribution counterfactuals, the proposed framework learns a parametric transformation network to generate faithful temporal attributions and stable counterfactual explanations. Extensive evaluations across synthetic and real-world benchmarks demonstrate consistent performance improvements over state-of-the-art baselines.

## Key Contributions

- Proposes a unified information-theoretic objective function that bridges attribution and counterfactual reasoning for time-series explanations.
- Introduces an explanation framework based on the Information Bottleneck principle to prevent trivial solutions and out-of-distribution counterfactuals.
- Demonstrates through comprehensive experiments on synthetic and real-world benchmarks that the proposed approach outperforms competing baselines in generating faithful attributions and stable counterfactuals.

## Archivist Review

Applied strict selection criteria. The sole proposed open question regarding hyperparameter sensitivity is too generic across machine learning explainability and does not represent a reusable standalone concept or core temporal forecasting challenge. No items approved.

### Rejected Candidates
- [open_question] Reducing Hyperparameter Sensitivity in Explainability (`hyperparameter-sensitivity-time-series-explainability`) - low_impact: Too generic and applies broadly to any machine learning explainability or modeling technique rather than exposing a specific unresolved forecasting or temporal dynamic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.25897)
- [PDF](https://arxiv.org/pdf/2608.25897)

