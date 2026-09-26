---
# CSL-compatible fields
title: "Multivariate Continuous-Time Autoregressive Moving Average Processes for Astronomical Multiband Time Series"
author:
  - literal: "Izak Schmidlkofer"
  - literal: "Zhirui Hu"
  - literal: "Lishan Shi"
  - literal: "Weixiang Yu"
  - literal: "Hyungsuk Tak"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.28419"

# Custom fields
paper_id: "2609.28419"
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
  - "multivariate-continuous-time-autoregressive-moving-average-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:24Z"
created_at: "2026-09-26T09:37:24Z"
---

# Multivariate Continuous-Time Autoregressive Moving Average Processes for Astronomical Multiband Time Series

**Authors**: Izak Schmidlkofer, Zhirui Hu, Lishan Shi, Weixiang Yu, Hyungsuk Tak
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.28419](https://arxiv.org/abs/2609.28419)

## Summary

The paper introduces a multivariate continuous-time autoregressive moving average (MCARMA) framework tailored for irregularly sampled, heteroscedastic, and partially observed multi-band astronomical time series. By modeling cross-band dependencies via correlated Brownian drivers and employing state-space and spectral representations, the approach enables likelihood-based inference. Through simulations and analysis of Sloan Digital Sky Survey quasars using the open-source mcarma Python package, the authors demonstrate that joint multivariate modeling outperforms separate single-band fits in parameter and spectral recovery.

## Key Contributions

- Developed a structured multivariate continuous-time autoregressive moving average (MCARMA) framework to handle irregular sampling, heteroscedastic errors, and partially observed bands in astronomical multi-band time series.
- Proposed a two-stage estimation procedure utilizing a numerically stabilized preliminary fit followed by maximum likelihood estimation.
- Demonstrated through simulations that joint multivariate estimation improves parameter and spectral recovery across 23/27 and 26/27 settings respectively compared to single-band fits.
- Applied the mcarma Python package to Sloan Digital Sky Survey Stripe 82 quasars, showing how joint multiband modeling improves marginal dynamics inference.

## Limitations

Higher-order stochastic structures can become weakly identifiable due to limited temporal resolution or near pole-zero cancellation.

## Open Questions & Future Work

- [[identifiable-structured-multivariate-carma]]

## Key Concepts

- [[multivariate-continuous-time-autoregressive-moving-average-processes]]: A structured continuous-time autoregressive moving average framework designed to model irregularly sampled multivariate time series with heteroscedastic measurement errors and cross-band correlations.

## Archivist Review

Approved the core multivariate continuous-time autoregressive moving average framework and the explicit open question regarding structured identifiability under irregular sampling. Applied strict scarcity and quality filters, rejecting routine dataset mentions and paper-internal details.

### Approved Concepts
- Multivariate Continuous-Time Autoregressive Moving Average Processes: The core methodological framework introduced in the paper for modeling irregularly sampled multivariate time series in astronomy.

### Approved Open Questions
- Identifiable Structured Multivariate CARMA: Crucial for extending continuous-time multivariate stochastic models beyond frequency-independent coherence while maintaining statistical identifiability and computational tractability under realistic astronomical observation constraints.

## Links

- [Abstract](https://arxiv.org/abs/2609.28419)
- [PDF](https://arxiv.org/pdf/2609.28419)

