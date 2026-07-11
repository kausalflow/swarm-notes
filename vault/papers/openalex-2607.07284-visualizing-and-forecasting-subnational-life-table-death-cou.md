---
# CSL-compatible fields
title: "Visualizing and forecasting subnational life-table death counts: Gap forecasting methods"
author:
  - literal: "Han Lin Shang"
  - literal: "Andrea Nigri"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07284"

# Custom fields
paper_id: "2607.07284"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cumulative-distribution-function-transformation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:27Z"
created_at: "2026-07-11T07:05:27Z"
---

# Visualizing and forecasting subnational life-table death counts: Gap forecasting methods

**Authors**: Han Lin Shang, Andrea Nigri
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07284](https://arxiv.org/abs/2607.07284)

## Summary

This paper proposes a mortality forecasting framework that improves subnational life-table death count predictions by explicitly modeling gender and regional disparities as gaps. To satisfy the non-negativity and summability requirements of death count distributions, the authors apply a cumulative distribution function (CDF) transformation. The model is validated on Japanese age-specific data from 1947 to 2023, demonstrating robust point and interval forecast performance across national, subnational, and gender-regional 'double gap' scenarios.

## Key Contributions

- Introduces a forecasting framework that explicitly models mortality gender and regional gaps to improve subnational life-table death count predictions.
- Employs a cumulative distribution function (CDF) transformation to handle the inherent non-negativity and summability constraints of life-table death count data.
- Demonstrates improved multi-step-ahead (1 to 15-step) forecasting accuracy using long-term Japanese age-specific mortality data from 1947–2023.

## Open Questions & Future Work

- [[extending-mortality-gap-modeling]]

## Key Concepts

- [[cumulative-distribution-function-transformation]]: A one-to-one mapping used to transform constrained, non-negative, and summable time-series data (e.g., life-table death counts) into unconstrained space for forecasting.

## Archivist Review

I approved the CDF transformation as it offers a reusable methodological approach for handling simplex-constrained time series. The open question was approved for its focus on transitioning from descriptive gap forecasting to covariate-augmented modeling, which is a recognized research bottleneck in demography and time series. I rejected the 'Mortality Gap Forecasting Framework' as a concept because it is essentially a domain-specific application rather than a reusable architectural mechanism.

### Approved Concepts
- Cumulative Distribution Function Transformation (CDF Transformation): Provides a robust, reversible method to map constrained, non-negative, and summable data (like mortality life-tables) into an unconstrained space for forecasting, which is a common requirement in demographic and probability-density-based time series.

### Approved Open Questions
- Extending Mortality Gap Modeling: Moving from univariate gap forecasting to incorporating structural covariates is essential for improving the precision of public health policy and understanding the drivers of demographic divergence.

### Rejected Candidates
- [concept] Mortality Gap Forecasting Framework (`mortality-gap-forecasting-framework`) - subcomponent_of_broader_mechanism: The framework is a specific application of established gap-modeling techniques; the more reusable methodological innovation is the CDF transformation itself.

## Links

- [Abstract](https://arxiv.org/abs/2607.07284)
- [PDF](https://arxiv.org/pdf/2607.07284)

