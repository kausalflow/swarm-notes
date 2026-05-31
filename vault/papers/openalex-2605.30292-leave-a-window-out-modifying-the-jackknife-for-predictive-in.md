---
# CSL-compatible fields
title: "Leave a Window Out: Modifying the Jackknife for Predictive Inference in Time Series"
author:
  - literal: "Hanyang Jiang"
  - literal: "Rina Foygel Barber"
  - literal: "Ashwin Pananjady"
  - literal: "Yao Xie"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.30292"

# Custom fields
paper_id: "2605.30292"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "conformal-prediction"
architectures:
  []
datasets:
  []
concept_slugs:
  - "leave-a-window-out-lwo"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:07Z"
created_at: "2026-05-31T08:09:07Z"
---

# Leave a Window Out: Modifying the Jackknife for Predictive Inference in Time Series

**Authors**: Hanyang Jiang, Rina Foygel Barber, Ashwin Pananjady, Yao Xie
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.30292](https://arxiv.org/abs/2605.30292)

## Summary

This paper addresses the failure of standard jackknife predictive inference methods in the presence of temporal dependence, which violates the exchangeability assumptions required for valid conformal prediction. The authors propose the 'leave-a-window-out' (LWO) method, a modification that excludes a block of temporally correlated data to preserve coverage guarantees. By quantifying departures from cyclic exchangeability, the method enables reliable uncertainty quantification with tighter prediction intervals than those produced by split conformal prediction. The approach is shown to be effective for memory-based time series predictors under mild stability conditions.

## Key Contributions

- Demonstrates that the vanilla jackknife suffers from arbitrary coverage loss in time series with temporal dependence.
- Introduces the 'leave-a-window-out' (LWO) method to achieve valid coverage in time series predictive inference without the efficiency loss of sample splitting.
- Provides theoretical proofs for valid coverage based on novel coefficients that measure the departure of data from cyclic exchangeability.
- Empirically validates that LWO provides valid coverage with narrower prediction intervals than split conformal prediction across time series experiments.

## Open Questions & Future Work

- [[lwo-validity-without-stability]]
- [[data-driven-lwo-window-selection]]

## Key Concepts

- [[leave-a-window-out-lwo]]: A modified jackknife predictive inference method that maintains coverage guarantees under temporal dependence by excluding a window of observations rather than a single point.

## Archivist Review

I approved the LWO method as it introduces a novel, reusable temporal conformal prediction framework that directly addresses the limitations of standard jackknife approaches. The two open questions capture significant theoretical and practical gaps—stability dependency and automated hyperparameter selection—that are essential for the maturation of this research direction. I did not find any unique or central datasets that warranted a permanent vault entry.

### Approved Concepts
- Leave-a-window-out (LWO): It addresses the fundamental failure of the vanilla jackknife in time series predictive inference while improving on the efficiency of split conformal prediction.

### Approved Open Questions
- LWO validity without stability: Relaxing stability requirements would significantly broaden the applicability of LWO-type methods, as many modern black-box predictors do not satisfy rigorous stability criteria.
- Data-driven window selection: Automated hyperparameter selection is critical for the practical deployment of LWO, as improper window size selection can lead to either invalid coverage or unnecessary statistical inefficiency.

## Links

- [Abstract](https://arxiv.org/abs/2605.30292)
- [PDF](https://arxiv.org/pdf/2605.30292)

