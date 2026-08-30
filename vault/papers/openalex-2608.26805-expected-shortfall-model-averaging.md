---
# CSL-compatible fields
title: "Expected Shortfall Model Averaging"
author:
  - literal: "Jianming Wu"
  - literal: "Xinyu Zhang"
  - literal: "Jie Zeng"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26805"

# Custom fields
paper_id: "2608.26805"
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
processed_at: "2026-08-30T10:11:01Z"
created_at: "2026-08-30T10:11:01Z"
---

# Expected Shortfall Model Averaging

**Authors**: Jianming Wu, Xinyu Zhang, Jie Zeng
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26805](https://arxiv.org/abs/2608.26805)

## Summary

This paper introduces a two-stage cross-validation model averaging framework for expected shortfall (ES) forecasting to overcome the challenges of non-elicitability and model uncertainty in tail risk estimation. The first stage estimates conditional value-at-risk via quantile model averaging, while the second stage applies mean squared error-based model averaging on a constructed transformed response. Theoretical guarantees, such as estimator consistency and asymptotic optimality of forecasting risk, are established under correct and misspecified settings. Empirical evaluations on U.S. stock returns and macroeconomic GDP growth confirm the method's accuracy, stability, and computational efficiency.

## Key Contributions

- Proposes a two-stage cross-validation model averaging method for expected shortfall (ES) forecasting that addresses the non-elicitability of ES.
- Establishes theoretical properties including consistency of estimators and asymptotic optimality of forecasting risk under both correct specification and model misspecification.
- Demonstrates through simulation studies and empirical applications to U.S. stock returns and macroeconomic GDP growth that the approach provides accurate, stable, and computationally efficient tail risk forecasts.

## Open Questions & Future Work

- [[robust-loss-model-averaging-misspecification]]

## Archivist Review

Evaluated the paper on Expected Shortfall Model Averaging. The core concept is an application of model averaging to a specific financial risk measure (expected shortfall), which is too paper-local to justify a permanent concept note. However, the open question concerning robust loss model averaging under misspecification is a substantive theoretical gap worth tracking.

### Approved Open Questions
- Robust Loss Model Averaging: Extending model averaging methods to handle heavy-tailed data and outliers robustly without theoretical breakdown under misspecification is a crucial frontier in financial risk forecasting.

### Rejected Candidates
- [concept] Expected Shortfall Model Averaging (`expected-shortfall-model-averaging`) - paper_local: This is a paper-specific application of standard model averaging to expected shortfall rather than a reusable core machine learning concept.

## Links

- [Abstract](https://arxiv.org/abs/2608.26805)
- [PDF](https://arxiv.org/pdf/2608.26805)

