---
# CSL-compatible fields
title: "Mittag-Leffler-Type Forecast-Error Growth as a Diagnostic Indicator of Fractional Dynamics"
author:
  - literal: "N'Gbo N'Gbo"
  - literal: "Andrei Velichko"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08588"

# Custom fields
paper_id: "2607.08588"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mittag-leffler-type-forecast-error-growth"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:24:15Z"
created_at: "2026-07-12T07:24:15Z"
---

# Mittag-Leffler-Type Forecast-Error Growth as a Diagnostic Indicator of Fractional Dynamics

**Authors**: N'Gbo N'Gbo, Andrei Velichko
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08588](https://arxiv.org/abs/2607.08588)

## Summary

This paper introduces a diagnostic pipeline to identify fractional dynamics in scalar time series by analyzing the growth characteristics of multi-horizon k-nearest neighbors (kNN) forecast errors. Unlike chaotic systems which typically exhibit exponential error divergence, fractional systems demonstrate Mittag-Leffler or power-law growth, which the authors use to construct a preliminary fractionality indicator. The proposed method successfully distinguishes between fractional and chaotic regimes, outperforming exponential models on both fractional chaotic systems and stable relaxation settings. The findings highlight the potential of using forecast-error geometry for the dynamical characterization of fractional systems.

## Key Contributions

- Introduced a data-driven pipeline for identifying fractional dynamics by comparing empirical forecast-error growth against exponential and Mittag-Leffler models.
- Demonstrated a 58% RMSE reduction in fractional chaotic system modeling using the Mittag-Leffler model compared to standard exponential error-growth models.
- Validated the approach in a stable fractional relaxation setting, showing significant performance improvements in kNN contraction tests with RMSE reduced by nearly an order of magnitude.

## Open Questions & Future Work

- [[fractional-order-parameter-recovery]]

## Key Concepts

- [[mittag-leffler-type-forecast-error-growth]]: A diagnostic framework that detects fractional dynamics by identifying power-law or Mittag-Leffler growth patterns in multi-horizon forecast errors, distinguishing them from exponential error growth in chaotic systems.

## Archivist Review

I have approved the core concept of Mittag-Leffler-type forecast-error growth for its novelty in applying error geometry for fractional dynamical characterization. I also approved the open question on fractional order parameter recovery, as it highlights the significant bottleneck in moving from diagnostic indicators to true physical system identification. All other candidates were rejected as they were either too specific to the proposed diagnostic framework or did not meet the criteria for independent vault entries.

### Approved Concepts
- Mittag-Leffler-type forecast-error growth: It provides a novel, data-driven diagnostic for identifying fractional dynamics—which are increasingly common in complex time series—without requiring knowledge of the governing equations.

### Approved Open Questions
- Recovering Fractional System Orders: Establishing this link is essential for moving beyond pattern-matching toward accurate system identification and physical interpretation in fractional time series.

## Links

- [Abstract](https://arxiv.org/abs/2607.08588)
- [PDF](https://arxiv.org/pdf/2607.08588)

