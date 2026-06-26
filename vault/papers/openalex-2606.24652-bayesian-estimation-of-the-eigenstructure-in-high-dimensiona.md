---
# CSL-compatible fields
title: "Bayesian Estimation of the Eigenstructure in High-Dimensional Approximate Factor Models"
author:
  - literal: "Seongmin Kim"
  - literal: "Jaeyong Lee"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24652"

# Custom fields
paper_id: "2606.24652"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:26:13Z"
created_at: "2026-06-26T08:26:13Z"
---

# Bayesian Estimation of the Eigenstructure in High-Dimensional Approximate Factor Models

**Authors**: Seongmin Kim, Jaeyong Lee
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24652](https://arxiv.org/abs/2606.24652)

## Summary

This paper addresses the instability of principal component-based estimators for high-dimensional approximate factor models where the number of variables is large relative to the sample size. The authors introduce a Bayesian estimation framework designed to recover latent factor structures while mitigating distortions in eigenvalues and eigenvectors of the sample covariance matrix. Theoretical analysis confirms that the model achieves optimal posterior convergence rates, and experimental results show it outperforms traditional methods in both structural recovery and forecasting performance.

## Key Contributions

- Introduced a Bayesian estimation framework for approximate factor models to address eigenstructure distortion in high-dimensional economic data.
- Established theoretical posterior convergence rates that match benchmark spiked covariance models.
- Demonstrated superior accuracy in factor structure recovery through simulations and competitive performance in forecasting on macro-financial datasets.

## Open Questions & Future Work

- [[dynamic-time-varying-factor-eigenstructures]]

## Archivist Review

The proposed Bayesian framework for approximate factor models, while statistically rigorous, relies on standard concepts in high-dimensional spiked covariance models already established in existing literature. Consequently, I have approved only the research question regarding dynamic, time-varying eigenstructures as it addresses a substantive, unresolved limitation in modeling evolving latent factor relationships. No new concepts were approved as they would either duplicate existing entries or constitute routine implementations of Bayesian estimation in this context.

### Approved Open Questions
- Dynamic time-varying factor eigenstructures: Current static models fail to account for structural changes or evolving factor relationships over time, which are common in real-world economic data. Addressing this is crucial for more robust forecasting and structural analysis in non-stationary environments.

## Links

- [Abstract](https://arxiv.org/abs/2606.24652)
- [PDF](https://arxiv.org/pdf/2606.24652)

