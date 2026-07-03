---
# CSL-compatible fields
title: "Asymmetric Garch Modelling Without Moment Conditions"
author:
  - literal: "Yuxin Tao"
  - literal: "Dong Li"
  - literal: "Dong Li"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2410.00574"

# Custom fields
paper_id: "2410.00574"
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
  - "sagarch"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:54:48Z"
created_at: "2026-07-03T07:54:48Z"
---

# Asymmetric Garch Modelling Without Moment Conditions

**Authors**: Yuxin Tao, Dong Li, Dong Li
**Date**: 2026-06-30
**Paper ID**: [openalex:2410.00574](https://arxiv.org/abs/2410.00574)

## Summary

This paper presents sAGARCH, an asymmetric GARCH model designed for financial time series characterized by heavy tails and stability issues. Unlike conventional GARCH models that require finite-moment assumptions, sAGARCH utilizes non-Gaussian stable innovations to accommodate infinite variance and mean. The study provides a rigorous inference framework and diagnostic testing toolkit, demonstrating the model's effectiveness through simulations and empirical applications to stock returns.

## Key Contributions

- Introduces the sAGARCH model, an asymmetric GARCH variant capable of handling infinite variance and mean via standardized non-Gaussian stable innovations.
- Establishes a robust inference framework for sAGARCH that ensures maximum likelihood estimator consistency and asymptotic normality in both stationary and explosive regimes.
- Provides a suite of diagnostic tests for asymmetry, strict stationarity, and model adequacy, including a modified Kolmogorov-type test statistic for heavy-tailed financial data.

## Open Questions & Future Work

- [[asymptotics-of-garch-critical-boundary]]
- [[skew-stable-garch-modeling]]

## Key Concepts

- [[sagarch]]: An asymmetric GARCH model using non-Gaussian stable innovations to model financial processes with infinite variance or mean.

## Archivist Review

The paper provides a significant advancement in GARCH-type modeling by removing finite-moment assumptions, which is highly relevant for financial time series. The approved concept and open questions address fundamental theoretical challenges in non-stationary modeling that transcend this specific work.

### Approved Concepts
- sAGARCH: It addresses the limitation of classical GARCH models requiring finite-moment conditions for financial time series with heavy tails.

### Approved Open Questions
- GARCH critical boundary behavior: Understanding this case is essential for a complete inferential theory of GARCH models, as real-world financial data often exist near the boundary of stationarity.
- Skewed stable GARCH modeling: Adding skewness to innovations could potentially better capture stylized financial features, but current estimation frameworks are limited by the computational complexity and non-identifiability concerns.

## Links

- [Abstract](https://arxiv.org/abs/2410.00574)
- [PDF](https://arxiv.org/pdf/2410.00574)

