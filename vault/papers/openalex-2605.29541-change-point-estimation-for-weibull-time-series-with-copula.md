---
# CSL-compatible fields
title: "Change-point estimation for Weibull time series with copula-based Markov models"
author:
  - literal: "Li‐Hsien Sun"
  - literal: "Zong-Yuan Huang"
  - literal: "Yi-Ling Huang"
  - literal: "Chi‐Yang Chiu"
  - literal: "Ning Ning"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29541"

# Custom fields
paper_id: "2605.29541"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:19Z"
created_at: "2026-05-31T08:09:19Z"
---

# Change-point estimation for Weibull time series with copula-based Markov models

**Authors**: Li‐Hsien Sun, Zong-Yuan Huang, Yi-Ling Huang, Chi‐Yang Chiu, Ning Ning
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29541](https://arxiv.org/abs/2605.29541)

## Summary

This paper introduces an offline change-point detection framework for non-negative time series data characterized by non-linear serial dependence. By utilizing a copula-based Markov chain model with Weibull marginals, the approach leverages Clayton and Joe copulas to capture asymmetric dependence structures. The model parameters and change points are estimated via maximum likelihood, with confidence intervals derived from parametric bootstrapping. Empirical evaluation confirms the method's robustness and accuracy, illustrated by detecting structural shifts in the VIX index during the COVID-19 pandemic.

## Key Contributions

- Proposes a copula-based Markov chain model with Weibull marginal distributions for offline change-point detection in non-negative, non-linearly dependent time series.
- Incorporates Clayton and Joe copulas to explicitly model asymmetric lower-tail and upper-tail serial dependence structures.
- Demonstrates high estimation accuracy in terms of RMSE and relative error for change-point detection through numerical studies and an application to VIX index volatility.

## Open Questions & Future Work

- [[multiple-change-point-estimation-copula-models]]

## Archivist Review

The paper proposes a specific copula-based Markov model for single change-point detection. The conceptual contributions (Weibull marginals with Clayton/Joe copulas) are specific model choices rather than reusable architectural or algorithmic paradigms, so no new concepts were approved. The open question regarding multiple change-point estimation and computational efficiency is a significant, non-trivial research direction in this field and was therefore approved.

### Approved Open Questions
- Multiple change-point estimation development: This addresses the primary scalability limitation of copula-based change-point modeling, which is essential for applying these methods to real-world, non-stationary time series beyond single-event shifts.

## Links

- [Abstract](https://arxiv.org/abs/2605.29541)
- [PDF](https://arxiv.org/pdf/2605.29541)

