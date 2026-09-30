---
# CSL-compatible fields
title: "Valid and Efficient Split Conformal Regression for Time Series"
author:
  - literal: "Percy S. Zhai"
  - literal: "Maggie X. Cheng"
  - literal: "Wei Biao Wu"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33866"

# Custom fields
paper_id: "2609.33866"
paper_source: "openalex"
domain: "time-series"
tags:
  - "conformal-prediction"
  - "time-series"
  - "forecasting"
  - "uncertainty-estimation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:28Z"
created_at: "2026-09-30T10:49:28Z"
---

# Valid and Efficient Split Conformal Regression for Time Series

**Authors**: Percy S. Zhai, Maggie X. Cheng, Wei Biao Wu
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33866](https://arxiv.org/abs/2609.33866)

## Summary

This paper investigates conformalized quantile and median regression for time series by replacing restrictive mixing conditions with the functional dependence measure, which accommodates long-memory processes. The authors establish simultaneous non-asymptotic coverage guarantees and interval length accuracy for split conformal regression. Additionally, they prove that the calibrated interval length converges faster than the estimated center itself for Gaussian linear processes with long memory, supported by matching lower bounds.

## Key Contributions

- Establishes non-asymptotic coverage guarantees and interval length accuracy simultaneously for split conformal regression on time series using the functional dependence measure instead of restrictive mixing conditions.
- Proves that the calibrated conformal interval length converges faster than the estimated center itself for Gaussian linear processes with long memory.
- Provides matching lower bounds for standard centers when the calibration block is sufficiently large relative to the training block under long memory.

## Open Questions & Future Work

- [[rolling-refits-nonstationary-time-series]]

## Archivist Review

Evaluated the submission under strict scientific filtering. No reusable novel concept note qualified standalone vault entry, as the paper contributes theoretical analysis (using the functional dependence measure for conformal regression) rather than a distinct algorithmic architecture or method. One open question on rolling refits and nonstationary series was approved because it addresses a fundamental practical bottleneck in conformal prediction for streaming time series.

### Approved Open Questions
- Rolling Refits and Nonstationary Series: Extending split conformal methods to rolling refits and nonstationary processes is critical for practical deployment in streaming financial, energy, and sensor time-series forecasting.

### Rejected Candidates
- [open_question] Non-Gaussian Symmetric Innovations Analysis (`non-gaussian-symmetric-innovations-long-memory`) - low_impact: Too narrow and specific to technical proofs for Hermite expansions in long-memory linear processes.

## Links

- [Abstract](https://arxiv.org/abs/2609.33866)
- [PDF](https://arxiv.org/pdf/2609.33866)

