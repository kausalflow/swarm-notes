---
# CSL-compatible fields
title: "Quantile autoregressive moving average models for ratio-based bounded time series"
author:
  - literal: "Helton Saulo"
  - literal: "Roberto Vila"
  - literal: "Filidor Vilca"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.26052"

# Custom fields
paper_id: "2605.26052"
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
  - "quls-arma"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:37:43Z"
created_at: "2026-05-28T08:37:43Z"
---

# Quantile autoregressive moving average models for ratio-based bounded time series

**Authors**: Helton Saulo, Roberto Vila, Filidor Vilca
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.26052](https://arxiv.org/abs/2605.26052)

## Summary

The paper introduces the Quantile Unit-Log-Symmetric Autoregressive Moving Average (QULS-ARMA) model to forecast time series bounded within the open unit interval (0,1). By reparameterizing the unit-log-symmetric family in terms of quantiles, the model avoids the limitations of mean-based approaches and effectively captures asymmetric distributions and heavy tails. The methodology supports flexible kernels, including Student-t distributions, and is validated through asymptotic analysis, Monte Carlo simulations, and a real-world application to hydroelectric energy storage proportions.

## Key Contributions

- Introduces the QULS-ARMA model, which integrates ARMA dynamics directly into the conditional quantile for bounded data on (0,1).
- Provides a flexible reparameterization that accommodates asymmetric behavior and heavy tails using log-symmetric kernels.
- Establishes asymptotic properties for the conditional maximum likelihood estimators and demonstrates superior performance in hydroelectric energy storage forecasting.

## Open Questions & Future Work

- [[multi-quantile-monotonicity-enforcement]]

## Key Concepts

- [[quls-arma]]: A quantile-based time series model for data on the unit interval that embeds ARMA dynamics into the conditional quantile to handle asymmetry and heavy tails.

## Archivist Review

The proposed QULS-ARMA model is a distinct statistical framework for bounded proportion forecasting that addresses the limitations of standard mean-based approaches, thus meriting a concept entry. I approved the quantile monotonicity open question as it identifies a substantive technical bottleneck common to dynamic quantile modeling, while rejecting the multivariate extension request as boilerplate future work.

### Approved Concepts
- Quantile Unit-Log-Symmetric ARMA (QULS-ARMA): It is the core model proposed in the paper for handling bounded time series (0,1) through quantile-based reparameterization.

### Approved Open Questions
- Enforcing quantile monotonicity: Monotonicity is a critical property for coherent multi-quantile forecasting; without it, interpretations of the conditional distribution's shape and extremes become invalid.

### Rejected Candidates
- [open_question] Multivariate QULS-ARMA extension (`multivariate-extension-bounded-series`) - low_impact: Multivariate extension is a common boilerplate future work goal for new univariate time series models.

## Links

- [Abstract](https://arxiv.org/abs/2605.26052)
- [PDF](https://arxiv.org/pdf/2605.26052)

