---
# CSL-compatible fields
title: "A Functional Central Limit Theorem for Localized Partial Sums of Non-Stationary Time Series"
author:
  - literal: "Florian Heinrichs"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17697"

# Custom fields
paper_id: "2607.17697"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:26:45Z"
created_at: "2026-07-23T07:26:45Z"
---

# A Functional Central Limit Theorem for Localized Partial Sums of Non-Stationary Time Series

**Authors**: Florian Heinrichs
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17697](https://arxiv.org/abs/2607.17697)

## Summary

This paper establishes a localized functional central limit theorem for kernel-weighted partial sum processes of piecewise locally stationary time series under physical dependence conditions. The authors prove weak convergence of the localized process to a centered Gaussian random distribution and an isonormal Gaussian process on $L^2([0,1])$. Furthermore, weak convergence is derived for processes indexed by totally bounded subsets of $L^2([0,1])$. As a practical application, this localized limit theory is leveraged to construct non-parametric regression tests for constant mean functions against various structural alternatives.

## Key Contributions

- Establishes a localized functional central limit theorem for kernel-weighted partial sum processes of piecewise locally stationary time series under geometric decay of the physical dependence measure.
- Proves weak convergence of the localized process to a centered Gaussian random distribution in $D'(0,1)$ extending to an isonormal Gaussian process on $L^2([0,1])$.
- Derives weak convergence for processes indexed by totally bounded subsets of $L^2([0,1])$.
- Applies the localized limit theory to construct non-parametric regression tests for constant mean functions against linear, polynomial, and general alternatives under locally stationary errors.

## Open Questions & Future Work

- [[finite-sample-size-calibration-nonstationary-tests]]

## Archivist Review

Strictly applied the review policy, approving no concepts because the paper is purely theoretical mathematical statistics without a reusable machine learning architecture or representation, and approving one open question regarding finite-sample size control in non-stationary tests.

### Approved Open Questions
- Finite-Sample Size Control in Non-Stationary Tests: Finite-sample size control is critical for practical deployment of change detection tests in non-stationary time series, making the reduction of these distortions a key methodological priority.

### Rejected Candidates
- [open_question] Finite-Sample Size Control in Non-Stationary Tests (`finite-sample-size-calibration-nonstationary-tests`) - other: The open question is well-formulated but we are choosing to approve no concepts and one precise question; wait, it is approved.

## Links

- [Abstract](https://arxiv.org/abs/2607.17697)
- [PDF](https://arxiv.org/pdf/2607.17697)

