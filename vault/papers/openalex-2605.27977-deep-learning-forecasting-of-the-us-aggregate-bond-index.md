---
# CSL-compatible fields
title: "Deep Learning Forecasting of the U.S. Aggregate Bond Index"
author:
  - literal: "Ajay Kumar Verma"
  - literal: "Jul Jon Ramirez General"
  - literal: "Yvan Landry Ndzonde Fonkou"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27977"

# Custom fields
paper_id: "2605.27977"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stationary-but-maximally-persistent-representation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:00Z"
created_at: "2026-05-30T07:36:00Z"
---

# Deep Learning Forecasting of the U.S. Aggregate Bond Index

**Authors**: Ajay Kumar Verma, Jul Jon Ramirez General, Yvan Landry Ndzonde Fonkou
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27977](https://arxiv.org/abs/2605.27977)

## Summary

This study evaluates the short-horizon predictability of the U.S. aggregate bond index using both MLP and CNN architectures. By comparing index levels, log returns, and a fractionally differenced "stationary but maximally persistent" representation, the authors show that predictive performance depends primarily on the degree of stationarity and memory retained rather than architectural complexity. The results reveal that while MLPs perform well on lagged representations, CNNs trained on Gramian Angular Field (GAF) images fail to provide meaningful forecasting improvements for this asset class.

## Key Contributions

- Demonstrates that the transformation strategy—specifically fractional differencing to balance stationarity and memory—is a stronger determinant of forecast performance than model complexity for US aggregate bond index data.
- Shows that simple MLP architectures outperform complex GAF-based CNN approaches for short-horizon next-step prediction in persistent financial time series.
- Provides empirical evidence that persistence-dominated bond market indicators are better handled by lag-based neural models than pattern-based image encodings.

## Open Questions & Future Work

- [[deep-learning-finance-forecasting-architectures-and-features]]

## Key Concepts

- [[stationary-but-maximally-persistent-representation]]: A data transformation strategy using fractional differencing to achieve covariance stationarity while preserving long-memory features for time-series forecasting.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 1 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Stationary but Maximally Persistent Representation: Highlights that for persistent financial series, data representation (balancing stationarity and memory) is often more critical to forecasting success than model architecture.

### Approved Open Questions
- Optimizing Deep Learning Finance Forecasts: Understanding the limits of univariate versus multivariate and static versus sequence-aware architectures is a core bottleneck in advancing financial time-series forecasting.

### Rejected Candidates
- [concept] Stationary but Maximally Persistent Representation (`stationary-but-maximally-persistent-representation`) - other: This was approved, but the rejection template requires structured records for ALL candidates (including the ones I chose to approve, the rejection list should technically only contain the ones NOT approved). Wait, the prompt implies the rejection list is for candidates NOT approved. I will only populate this list with candidates I rejected.

## Links

- [Abstract](https://arxiv.org/abs/2605.27977)
- [PDF](https://arxiv.org/pdf/2605.27977)

