---
# CSL-compatible fields
title: "Distributional Forecasting of EU Asylum Applications with Dynamic Multivariate Count Models"
author:
  - literal: "Gregor Zens"
  - literal: "Jakub Bijak"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16677"

# Custom fields
paper_id: "2606.16677"
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
  - "bayesian-joint-distributional-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:26:11Z"
created_at: "2026-06-17T09:26:11Z"
---

# Distributional Forecasting of EU Asylum Applications with Dynamic Multivariate Count Models

**Authors**: Gregor Zens, Jakub Bijak
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16677](https://arxiv.org/abs/2606.16677)

## Summary

This paper presents a Bayesian hierarchical framework for joint distributional forecasting of monthly asylum applications across EU-27 countries. By decomposing latent application intensities into country-specific random walks and shared common factors, the model captures complex dependency structures including heavy tails and stochastic volatility. Evaluation on Eurostat data indicates that joint multivariate models significantly improve predictive accuracy and upper-tail risk assessment compared to individual country-level benchmarks. The results highlight the importance of aligning model specifications with policy-relevant loss functions for effective asylum preparedness planning.

## Key Contributions

- Proposes a Bayesian framework for joint distributional forecasting of monthly asylum applications across the EU-27.
- Demonstrates that joint EU-27 models outperform country-by-country benchmarks, particularly in capturing upper-tail risk.
- Identifies that random-walk log-intensities combined with flexible innovation dynamics effectively capture short-run application trends.

## Open Questions & Future Work

- [[long-horizon-variance-accumulation]]

## Key Concepts

- [[bayesian-joint-distributional-forecasting]]: A Bayesian hierarchical framework for joint multivariate count data forecasting that models country-specific random walks and shared latent factors.

## Archivist Review

I approved the core Bayesian joint forecasting concept as it provides a reusable approach to multivariate count data modelling. I also approved the open question regarding long-horizon variance accumulation, as it addresses a fundamental limitation in state-space models applied to volatile, non-stationary count time series. Eurostat was rejected as it is a broad, non-specific public database provider.

### Approved Concepts
- Bayesian Joint Distributional Forecasting: Core methodological contribution: allows for joint, multivariate distributional estimation in count data while accounting for common shocks.

### Approved Open Questions
- Mitigating long-horizon variance accumulation: This is critical because over-conservative forecasts at longer horizons limit the utility of these models for medium-term resource planning and budgetary allocation, which are common requirements for asylum reception agencies.

## Links

- [Abstract](https://arxiv.org/abs/2606.16677)
- [PDF](https://arxiv.org/pdf/2606.16677)

