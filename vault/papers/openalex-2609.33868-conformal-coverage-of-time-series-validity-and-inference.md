---
# CSL-compatible fields
title: "Conformal Coverage of Time Series: Validity and Inference"
author:
  - literal: "Percy S. Zhai"
  - literal: "Maggie X. Cheng"
  - literal: "Wei Biao Wu"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33868"

# Custom fields
paper_id: "2609.33868"
paper_source: "openalex"
domain: "time-series"
tags:
  - "conformal-prediction"
  - "time-series"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:14Z"
created_at: "2026-09-30T10:49:14Z"
---

# Conformal Coverage of Time Series: Validity and Inference

**Authors**: Percy S. Zhai, Maggie X. Cheng, Wei Biao Wu
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33868](https://arxiv.org/abs/2609.33868)

## Summary

This paper investigates the validity and inference of realized coverage for split conformal prediction on temporally dependent time series. Using the functional dependence measure, the authors derive non-asymptotic bounds on marginal coverage error without requiring mixing assumptions. They establish a Bahadur representation and a central limit theorem for realized coverage under temporal dependence, supported by a consistent block-based estimator for hypothesis testing. Furthermore, the work extends to long-memory time series, showing that strong temporal dependence alters coverage uncertainty and yields non-Gaussian limiting laws for Gaussian linear processes.

## Key Contributions

- Derived non-asymptotic bounds on marginal coverage error for split conformal prediction under temporal dependence using the functional dependence measure without mixing assumptions.
- Established a Bahadur representation and derived the first central limit theorem for realized coverage of split conformal prediction under temporal dependence.
- Proposed a consistent block-based estimator of the standard error to yield an asymptotically justified test for realized coverage.
- Analyzed long-memory time series, demonstrating that strong temporal dependence leads to a non-Gaussian limiting law of realized coverage for Gaussian linear processes and established block-sampling inference.

## Open Questions & Future Work

- [[nonstationary-adaptive-conformal-inference]]

## Archivist Review

The paper presents theoretical advances in conformal prediction coverage for dependent time series. No distinct reusable concepts were proposed that warrant standalone vault notes under our strict selection standard, but the open question regarding nonstationary and adaptive conformal inference is valuable and retained.

### Approved Open Questions
- Nonstationary and adaptive conformal inference: Important for practical time-series forecasting where models are continuously retrained or data distributions drift over time.

## Links

- [Abstract](https://arxiv.org/abs/2609.33868)
- [PDF](https://arxiv.org/pdf/2609.33868)

