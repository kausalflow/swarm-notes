---
# CSL-compatible fields
title: "When and Why Naïve Diversification Works: A Simple Diagnostic Strategy"
author:
  - literal: "Han Feng"
  - literal: "Difang Huang"
  - literal: "Jue Wang"
  - literal: "Zhengjun Zhang"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11054"

# Custom fields
paper_id: "2607.11054"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "golden-criterion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:36Z"
created_at: "2026-07-16T07:14:36Z"
---

# When and Why Naïve Diversification Works: A Simple Diagnostic Strategy

**Authors**: Han Feng, Difang Huang, Jue Wang, Zhengjun Zhang
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11054](https://arxiv.org/abs/2607.11054)

## Summary

This paper addresses the persistence of naïve diversification by linking equal-weighting optimality to the uniformity of the forecast-error covariance matrix eigenstructure, termed the 'Golden Criterion'. The authors propose a two-stage adaptive strategy that blends naïve and optimized weights by measuring empirical deviations from this uniform condition. Empirical testing on U.S. equity premium forecasting reveals that naïve diversification is often superior at short horizons, while optimized approaches become more effective at longer horizons.

## Key Contributions

- Identifies a theoretical 'Golden Criterion' for when naïve diversification matches or exceeds minimum-variance optimization.
- Introduces a two-stage adaptive weighting strategy that dynamically balances naïve and optimized portfolios based on eigenstructure uniformity.
- Demonstrates consistent out-of-sample improvements in U.S. equity premium forecasting using the proposed adaptive approach.

## Key Concepts

- [[golden-criterion]]: A theoretical condition for the optimality of equal-weighted portfolios based on the uniformity of the forecast-error covariance matrix eigenstructure.

## Archivist Review

I approved the 'Golden Criterion' as it provides a robust, theoretically grounded diagnostic tool for managing the bias-variance trade-off in portfolio weighting, a common challenge in time-series forecasting and finance. No other concepts or datasets were sufficiently novel or reusable enough for inclusion in the vault. The analysis correctly identifies this as a potential contribution that could generalize to other weight-blending contexts beyond the specific application in the paper.

### Approved Concepts
- Golden Criterion: It provides a theoretical foundation for understanding when and why equal-weighted (naïve) diversification outperforms optimized weight strategies.

## Links

- [Abstract](https://arxiv.org/abs/2607.11054)
- [PDF](https://arxiv.org/pdf/2607.11054)

