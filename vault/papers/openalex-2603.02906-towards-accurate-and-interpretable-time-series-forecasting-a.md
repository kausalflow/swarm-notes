---
# CSL-compatible fields
title: "Towards Accurate and Interpretable Time-series Forecasting: A Polynomial Learning Approach"
author:
  - literal: "Bo Liu"
  - literal: "Shao-Bo Lin"
  - literal: "Changmiao Wang"
  - literal: "Xiaotong Liu"
issued:
  date-parts:
    - [2026, 3, 3]
url: "https://arxiv.org/abs/2603.02906"

# Custom fields
paper_id: "2603.02906"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "mathematical-reasoning"
architectures:
  []
datasets:
  - "Bitcoin price data"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:37Z"
created_at: "2026-03-27T14:08:37Z"
---

# Towards Accurate and Interpretable Time-series Forecasting: A Polynomial Learning Approach

**Authors**: Bo Liu, Shao-Bo Lin, Changmiao Wang, Xiaotong Liu
**Date**: 2026-03-03
**Paper ID**: [openalex:2603.02906](https://arxiv.org/abs/2603.02906)

## Summary

This paper introduces Interpretable Polynomial Learning (IPL), a novel time-series forecasting method designed to overcome the trade-off between accuracy and interpretability common in existing models. IPL explicitly models complex temporal dependencies by representing the time-series function as a polynomial in terms of the original features and their cross-interactions up to an arbitrary order. This structural approach inherently provides feature-level interpretability while maintaining high predictive performance, which is demonstrated on Bitcoin price and antenna sensor data. The model's flexibility allows users to adjust the polynomial degree to balance the need for prediction accuracy against the requirement for model simplicity and interpretability, leading to better-justified early warning systems.

## Key Contributions

- Proposed the Interpretable Polynomial Learning (IPL) method, which integrates interpretability directly into the model structure via polynomial representations of feature interactions.
- Demonstrated that IPL provides a flexible trade-off between prediction accuracy and interpretability by tuning the polynomial degree.
- Achieved high prediction accuracy on simulated and Bitcoin price data while showing superior interpretability compared to post-hoc explainability methods.
- Validated IPL's effectiveness in creating simpler and more efficient early warning mechanisms using field-collected antenna data.

## Limitations

The computational cost and complexity may increase significantly with a high polynomial degree, potentially impacting real-time performance on very large feature sets.

## Open Questions & Future Work

- [[ipl-polynomial-degree-tradeoff]]

## Key Concepts

- [Interpretable Polynomial Learning](../concepts/interpretable-polynomial-learning.md): A time-series forecasting method that explicitly models original features and their arbitrary-order interactions using polynomial representations to ensure both accuracy and structural interpretability.

## Datasets

- [Bitcoin price data](../datasets/bitcoin-price-data.md)

## Limitations

The computational cost and complexity may increase significantly with a high polynomial degree, potentially impacting real-time performance on very large feature sets.

## Links

- [Abstract](https://arxiv.org/abs/2603.02906)
- [PDF](https://arxiv.org/pdf/2603.02906)

