---
# CSL-compatible fields
title: "NoRIN: Backbone-Adaptive Reversible Normalization for Time-Series Forecasting"
author:
  - literal: "Shun Zhang"
  - literal: "Yuyang Xiao"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10823"

# Custom fields
paper_id: "2605.10823"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "normalization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "norin"
  - "degeneration-problem-in-normalization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:36:49Z"
created_at: "2026-05-14T07:36:49Z"
---

# NoRIN: Backbone-Adaptive Reversible Normalization for Time-Series Forecasting

**Authors**: Shun Zhang, Yuyang Xiao
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10823](https://arxiv.org/abs/2605.10823)

## Summary

NoRIN addresses the limitations of standard affine reversible normalization (RevIN) in time-series forecasting, which fails to correct non-Gaussian distribution properties like skewness and heavy tails. The authors identify a 'degeneration problem' where gradient-based optimization of non-linear normalization parameters collapses to linear scaling. By decoupling shape parameter estimation from backbone training using quantile-based initialization and Bayesian optimization, NoRIN consistently outperforms standard normalization across diverse backbones and datasets.

## Key Contributions

- Introduces NoRIN, a non-linear reversible normalization method that uses Johnson SU transforms to model skewness and heavy tails.
- Identifies the 'degeneration problem' where gradient-based joint training of shape parameters collapses back to linear Z-score normalization.
- Proposes a decoupled shape optimization strategy using closed-form quantile initialization and Bayesian validation-based refinement to bypass degeneration.
- Demonstrates across 90 experimental configurations that backbones benefit significantly from tailored, non-linear normalization parameters.

## Open Questions & Future Work

- [[higher-capacity-non-linear-normalization]]

## Key Concepts

- [[norin]]: A non-linear reversible normalization technique using Johnson SU transforms to handle distribution skewness and heavy tails in time-series data.
- [[degeneration-problem-in-normalization]]: A phenomenon where gradient-based joint training of non-linear normalization parameters causes the model to collapse back to linear Z-score normalization.

## Archivist Review

I approved the NoRIN concept and the associated 'degeneration problem' as they represent a reusable framework and a notable training phenomenon in time-series normalization. The open question regarding higher-capacity normalization is approved as it addresses a fundamental limitation in current distributional modeling for time-series. No datasets were approved as none were introduced or identified as the central novelty.

### Approved Concepts
- NoRIN: Provides a non-linear normalization alternative to standard affine RevIN, addressing distribution shape limitations in time-series forecasting.
- Degeneration Problem in Normalization: Identifies a fundamental obstacle in training non-linear normalization layers alongside backbones, where parameters collapse to linear scaling.

### Approved Open Questions
- Higher-capacity non-linear normalization families: Determining the limits of current parameterization and whether increased model capacity is necessary for complex temporal dynamics is crucial for advancing time-series normalization techniques.

## Links

- [Abstract](https://arxiv.org/abs/2605.10823)
- [PDF](https://arxiv.org/pdf/2605.10823)

