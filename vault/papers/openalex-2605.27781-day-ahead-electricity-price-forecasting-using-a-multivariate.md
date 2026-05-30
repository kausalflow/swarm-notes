---
# CSL-compatible fields
title: "Day-Ahead Electricity Price Forecasting Using a Multivariate Group Lasso Method"
author:
  - literal: "Keyi Wang"
  - literal: "Jiaxiang Ji"
  - literal: "Mahan Mansouri"
  - literal: "Ahmed Aziz Ezzat"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27781"

# Custom fields
paper_id: "2605.27781"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "CAISO"
concept_slugs:
  - "multivariate-group-lasso-forecasting"
dataset_slugs:
  - "caiso"
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:07Z"
created_at: "2026-05-30T07:36:07Z"
---

# Day-Ahead Electricity Price Forecasting Using a Multivariate Group Lasso Method

**Authors**: Keyi Wang, Jiaxiang Ji, Mahan Mansouri, Ahmed Aziz Ezzat
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27781](https://arxiv.org/abs/2605.27781)

## Summary

This paper introduces a multivariate statistical forecasting approach based on a Group Lasso formulation designed to address complex temporal group effects in day-ahead electricity price signals. By accounting for the persistent influence of explanatory variables across consecutive time blocks, the method achieves significant improvements in forecasting accuracy. Extensive evaluation on CAISO market data and comparative analysis against competitive baseline models and operational systems confirm the effectiveness, interpretability, and low computational complexity of the proposed framework.

## Key Contributions

- Proposes a multivariate Group Lasso method to capture multi-feature temporal group effects in day-ahead electricity price forecasting.
- Demonstrates superior point and probabilistic forecast performance on two years of CAISO market data compared to existing statistical and deep learning models.
- Validates the method's effectiveness against operational systems and high-performing entries in international forecasting challenges, confirming its practical relevance and high performance-to-information efficiency.

## Open Questions & Future Work

- [[dynamic-forecaster-ensembling]]
- [[spatial-multivariate-epf]]

## Key Concepts

- [[multivariate-group-lasso-forecasting]]: A statistical forecasting framework that uses Group Lasso to model persistent multi-feature temporal dependencies in electricity price vectors.

## Archivist Review

I approved the concept of Multivariate Group Lasso Forecasting for its clear contribution to capturing temporal dependencies via group sparsity, as well as the CAISO dataset as a central evaluation benchmark. Two open questions regarding dynamic model ensembling and spatial-multivariate modeling were approved for their substantial research significance in power systems forecasting. I applied a strict filter to ensure only reusable forecasting paradigms and critical unresolved systemic bottlenecks were retained.

### Approved Concepts
- Multivariate Group Lasso Forecasting: It addresses complex temporal dependencies in electricity pricing signals by enforcing group sparsity, which captures persistent influences across time blocks.

### Approved Open Questions
- Dynamic ensemble strategies for EPF: Developing robust ensemble strategies is critical for improving the reliability and accuracy of electricity price forecasts in complex market conditions, moving beyond simple averaging.
- Spatial-multivariate electricity forecasting: Incorporating spatial dependence is essential for scaling forecasting models to multi-node power systems and for maintaining consistency between locational marginal prices.

## Datasets

- [[caiso]]

## Links

- [Abstract](https://arxiv.org/abs/2605.27781)
- [PDF](https://arxiv.org/pdf/2605.27781)

