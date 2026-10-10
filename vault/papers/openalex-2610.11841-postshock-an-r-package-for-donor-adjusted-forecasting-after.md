---
# CSL-compatible fields
title: "postshock: An R Package for Donor-Adjusted Forecasting After Structural Shocks"
author:
  - literal: "Qiyang Wang"
  - literal: "Daniel J. Eck"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11841"

# Custom fields
paper_id: "2610.11841"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:53:18Z"
created_at: "2026-10-10T10:53:18Z"
---

# postshock: An R Package for Donor-Adjusted Forecasting After Structural Shocks

**Authors**: Qiyang Wang, Daniel J. Eck
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11841](https://arxiv.org/abs/2610.11841)

## Summary

The paper presents postshock, an R package designed for donor-adjusted time-series forecasting when a structural shock has occurred and the target response remains unobserved. The framework leverages historical donor episodes, balances donors via matching features, and transfers adjustments to improve both conditional mean (ARIMA, ARIMAX) and conditional variance (GARCH-X) forecasts. It features structured donor pools, automated model selection, and reproducible workflows.

## Key Contributions

- Introduces the postshock R package for donor-adjusted forecasting following structural shocks.
- Implements a framework that estimates shock effects from historical donor episodes and transfers adjustments to target-series forecasts.
- Supports conditional mean and variance forecasting via integrated ARIMA, ARIMAX, and GARCH-X models with automated order selection.

## Open Questions & Future Work

- [[adaptive-donor-transferability-learning]]

## Archivist Review

Reviewed the paper presenting the 'postshock' R package. No standalone core forecasting method or dataset qualifies for permanent vault storage under our strict novelty and reusability standards, but the open question regarding adaptive donor transferability captures a substantive methodological limitation.

### Approved Open Questions
- Adaptive Learning of Donor Transferability: Extending the framework to dynamically learn donor transferability and update relevance sequentially addresses a primary limitation of static donor-weighting schemes, enhancing robustness across diverse structural break applications.

### Rejected Candidates
- [open_question] Adaptive Learning of Donor Transferability (`adaptive-donor-transferability-learning`) - low_impact: The paper primarily presents an R package for structural shock forecasting without introducing a novel foundational concept or dataset; the open question represents standard software extensions.

## Links

- [Abstract](https://arxiv.org/abs/2610.11841)
- [PDF](https://arxiv.org/pdf/2610.11841)

