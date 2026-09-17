---
# CSL-compatible fields
title: "On Detecting Multiple Simultaneous Change-points in High Dimensional Non-Stationary Time Series"
author:
  - literal: "Richard Song"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15479"

# Custom fields
paper_id: "2609.15479"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fused-group-lasso-for-change-point-detection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:32Z"
created_at: "2026-09-17T09:43:32Z"
---

# On Detecting Multiple Simultaneous Change-points in High Dimensional Non-Stationary Time Series

**Authors**: Richard Song
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15479](https://arxiv.org/abs/2609.15479)

## Summary

This paper investigates the detection of multiple simultaneous structural change points in high-dimensional non-stationary economic and financial time series using standard and adaptive fused group lasso methods with mixed L_{2,1} penalties. The author establishes theoretical L_2 and L_0 consistency guarantees, quantifying conditions on change magnitude, number of change points, and sample size. Empirical performance is demonstrated through an analysis of a large panel of U.S. economic and financial data spanning 50 years.

## Key Contributions

- Proposes a standard and adaptive fused group lasso framework with mixed L_{2,1} penalties for detecting multiple simultaneous change points in high-dimensional non-stationary time series.
- Establishes L_2 consistency and L_0 consistency (correct model selection with probability approaching unity) under appropriate theoretical conditions.
- Quantifies the asymptotic interplay between structural change magnitude, number of change points, and sample size required for consistent discovery.

## Key Concepts

- [[fused-group-lasso-for-change-point-detection]]: A mixed L_{2,1} penalized framework using standard and adaptive fused group lasso for simultaneous multiple change-point detection in high-dimensional non-stationary time series.

## Archivist Review

Evaluated the single candidate concept against vault standards, approving the reusable fused group lasso methodological framework for structural break detection while maintaining strict scarcity constraints. No new open questions or datasets met the strict novelty and centralization thresholds.

### Approved Concepts
- Fused Group Lasso for Change-Point Detection: Serves as the core statistical methodology for detecting multiple simultaneous change points in high-dimensional non-stationary time series.

### Rejected Candidates
- [concept] Simultaneous Change-Point Detection (`simultaneous-change-point-detection`) - subcomponent_of_broader_mechanism: Subcomponent of broader mechanism or standard terminology already captured by the fused group lasso concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.15479)
- [PDF](https://arxiv.org/pdf/2609.15479)

