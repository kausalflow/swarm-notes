---
# CSL-compatible fields
title: "Measuring Tail Dependence in Linear Processes: Theory and Empirics"
author:
  - literal: "Debanjana Datta"
  - literal: "Diganta Mukherjee"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10303"

# Custom fields
paper_id: "2605.10303"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:52Z"
created_at: "2026-05-14T07:38:52Z"
---

# Measuring Tail Dependence in Linear Processes: Theory and Empirics

**Authors**: Debanjana Datta, Diganta Mukherjee
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10303](https://arxiv.org/abs/2605.10303)

## Summary

This paper addresses the inadequacy of Gaussian models in capturing heavy-tailed marginals and extreme co-movements in financial time series. The authors introduce a novel dependence measure for joint extremes that functions independently of marginal distributions and applies to regularly varying processes. The approach is theoretically justified and empirically demonstrated using high-frequency cryptocurrency data, providing insights into the persistence of extreme dependence structures.

## Key Contributions

- Proposes a novel dependence measure for joint extremes in linear processes that accounts for both non-identical and identical regularly varying distributions.
- Establishes a theoretical framework for quantifying extreme co-movements in financial time series beyond standard Gaussian assumptions.
- Provides empirical validation using high-frequency cryptocurrency datasets to assess the persistence of extreme dependence properties.

## Open Questions & Future Work

- [[robustness-of-tail-dependence-under-contamination]]

## Archivist Review

I have approved the open question regarding the robustness of tail dependence measures as it represents a significant challenge for financial forecasting under non-stationary conditions. The proposed dependence measure itself was rejected as a concept because it currently exists as a specific statistical metric rather than a broader, reusable ML architectural component or learning framework. I maintained a strict threshold, approving only the most substantial research bottleneck.

### Approved Open Questions
- Robustness of Tail Dependence Measures: Financial time series are frequently characterized by non-stationarity and structural instabilities; establishing the robustness of dependence metrics is critical for valid risk management and forecasting under such conditions.

### Rejected Candidates
- [concept] Tail Dependence Measure for Linear Processes (`tail-dependence-measure`) - not_reusable: The concept is an incremental statistical measure for tail dependence which does not yet show evidence of broad reusability across ML-based forecasting architectures.

## Links

- [Abstract](https://arxiv.org/abs/2605.10303)
- [PDF](https://arxiv.org/pdf/2605.10303)

