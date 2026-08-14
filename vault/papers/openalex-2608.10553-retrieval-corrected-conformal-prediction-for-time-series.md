---
# CSL-compatible fields
title: "Retrieval-Corrected Conformal Prediction for Time Series"
author:
  - literal: "진상진"
  - literal: "KangMin Kim"
  - literal: "Junhyeong Lee"
  - literal: "Yongjae Lee"
  - literal: "Jin Sangjin"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10553"

# Custom fields
paper_id: "2608.10553"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
  - "uncertainty-quantification"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "retrieval-corrected-conformal-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-14T06:07:02Z"
created_at: "2026-08-14T06:07:02Z"
---

# Retrieval-Corrected Conformal Prediction for Time Series

**Authors**: 진상진, KangMin Kim, Junhyeong Lee, Yongjae Lee, Jin Sangjin
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10553](https://arxiv.org/abs/2608.10553)

## Summary

This paper introduces Retrieval-Corrected Conformal Prediction (RCCP), a retrieval-augmented calibration method designed to produce reliable prediction intervals for time series. RCCP constructs asymmetric intervals by retrieving similar past residuals as local evidence and then applies a scalar conformal correction to ensure proper coverage. Theoretical analysis establishes a coverage-gap bound based on the stability of the normalized retrieval error distribution, and experiments across standard benchmarks show that RCCP achieves superior Winkler scores and low computational overhead.

## Key Contributions

- Proposed Retrieval-Corrected Conformal Prediction (RCCP), a retrieval-augmented calibration method that uses retrieved one-sided residuals for local evidence combined with scalar conformal correction.
- Provided a theoretical coverage-gap bound based on the stability of the normalized retrieval error distribution.
- Demonstrated across standard benchmarks and backbone forecasters that RCCP consistently attains target coverage and achieves lower Winkler scores with lower overhead.

## Open Questions & Future Work

- [[multivariate-multistep-retrieval-conformal-prediction-extension]]

## Key Concepts

- [[retrieval-corrected-conformal-prediction]]: A retrieval-augmented conformal calibration method for time series that uses similar past residuals as local evidence and a scalar conformal correction to guarantee coverage.

## Archivist Review

Approved the core retrieval-corrected conformal prediction framework as a distinct and reusable time series uncertainty quantification concept, along with its natural open extension to multivariate and multi-step forecasting horizons.

### Approved Concepts
- Retrieval-Corrected Conformal Prediction: Introduces a novel retrieval-augmented conformal prediction framework for time series that combines nearest-neighbor residual retrieval with scalar conformal correction.

### Approved Open Questions
- Extension to Multivariate and Multi-step Forecasting: Crucial for scaling uncertainty quantification and conformal prediction methods to complex multivariate and multi-step industrial time series applications.

## Links

- [Abstract](https://arxiv.org/abs/2608.10553)
- [PDF](https://arxiv.org/pdf/2608.10553)

