---
# CSL-compatible fields
title: "Count data modeling and forecasting of malaria incidence using generalized time series regression"
author:
  - literal: "Adithya B. Somaraj"
  - literal: "Praveen D. Chougale"
  - literal: "Usha Ananthakumar"
  - literal: "Karthika M. Satyanarayanan"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25902"

# Custom fields
paper_id: "2606.25902"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:42:49Z"
created_at: "2026-06-27T07:42:49Z"
---

# Count data modeling and forecasting of malaria incidence using generalized time series regression

**Authors**: Adithya B. Somaraj, Praveen D. Chougale, Usha Ananthakumar, Karthika M. Satyanarayanan
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25902](https://arxiv.org/abs/2606.25902)

## Summary

This study addresses the challenge of predicting malaria incidence using count-based time series models. By analyzing monthly surveillance data from Mumbai, the authors demonstrate that standard Poisson regression fails to account for significant overdispersion and serial dependence inherent in the data. The proposed GLARMA-Negative Binomial model provides improved predictive accuracy and stability, highlighting the importance of capturing both temporal correlation and distributional variance for public health surveillance.

## Key Contributions

- Demonstrates that a Generalized Linear Autoregressive Moving Average (GLARMA) framework with a negative binomial distribution effectively handles both overdispersion and serial dependence in malaria incidence count data.
- Identifies that seasonal effects are more strongly associated with malaria incidence in the Mumbai region than individual climatic covariates.
- Shows that the proposed GLARMA-Negative Binomial model achieves superior predictive accuracy and stability compared to standard Poisson and negative binomial regression baselines on monthly surveillance data from 2012–2019.

## Open Questions & Future Work

- [[glarma-error-accumulation-stability]]

## Archivist Review

The paper provides a standard application of statistical count time series models to epidemiological data. I approved the open question regarding GLARMA forecast stability because it addresses a fundamental limitation in non-Gaussian, observation-driven models that extends beyond this specific study. I rejected the model itself as a concept because it is an implementation of established statistical frameworks rather than a novel conceptual contribution.

### Approved Open Questions
- GLARMA Forecast Stability Analysis: Understanding error accumulation in multi-step forecasting is critical for the reliable deployment of early warning systems in public health, as instability in long-term predictions can lead to incorrect resource allocation decisions.

### Rejected Candidates
- [concept] GLARMA-Negative Binomial Model (`glarma-negative-binomial-model`) - paper_local: This is a specific statistical model combination rather than a reusable architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.25902)
- [PDF](https://arxiv.org/pdf/2606.25902)

