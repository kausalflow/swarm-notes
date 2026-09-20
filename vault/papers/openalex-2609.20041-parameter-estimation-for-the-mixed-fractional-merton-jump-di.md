---
# CSL-compatible fields
title: "Parameter Estimation for the Mixed Fractional Merton Jump Diffusion Model with EM Algorithm"
author:
  - literal: "Chidiogo Joy Agboeke"
  - literal: "Hamidreza Maleki Almani"
  - literal: "Dario Gasbarra"
  - literal: "Foad Shokrollahi"
  - literal: "Tommi Sottinen"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20041"

# Custom fields
paper_id: "2609.20041"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:30:41Z"
created_at: "2026-09-20T09:30:41Z"
---

# Parameter Estimation for the Mixed Fractional Merton Jump Diffusion Model with EM Algorithm

**Authors**: Chidiogo Joy Agboeke, Hamidreza Maleki Almani, Dario Gasbarra, Foad Shokrollahi, Tommi Sottinen
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20041](https://arxiv.org/abs/2609.20041)

## Summary

This paper proposes an Expectation-Maximization algorithm combined with Metropolis-Hastings sampling to estimate parameters for the Mixed Fractional Merton Jump Diffusion model. The model incorporates fractional Brownian motion for long-range dependence and a compound Poisson jump process for abrupt financial movements. The latent jump process is handled using MCMC during the E-step, while the M-step maximizes the expected complete-data likelihood. Theoretical properties including consistency and asymptotic normality are established, and the approach is demonstrated on the Helsinki Stock Index (OMXH25).

## Key Contributions

- Proposes an Expectation-Maximization algorithm with Metropolis-Hastings sampling for parameter estimation in the Mixed Fractional Merton Jump Diffusion model
- Establishes consistency and asymptotic normality of the proposed estimator under regularity conditions
- Applies the estimation framework to the Helsinki Stock Index (OMXH25) to capture long-memory dependence and jump behavior in financial returns

## Open Questions & Future Work

- [[cross-market-validation-mfmjd]]
- [[predictive-modeling-mfmjd]]

## Archivist Review

Applied strict selection standards, approving no concepts due to lack of distinct reusable architectural mechanisms, but retaining two explicit open-ended research directions regarding cross-market validation and predictive modeling for mixed fractional jump-diffusion models.

### Approved Open Questions
- Cross-Market Validation of MFMJD: Crucial for demonstrating that complex stochastic volatility and long-memory jump-diffusion models are universally applicable rather than overfitted to specific regional market dynamics.
- Predictive Modeling and Forecasting: Bridges the gap between theoretical econometric estimation and practical quantitative trading or risk management applications.

## Links

- [Abstract](https://arxiv.org/abs/2609.20041)
- [PDF](https://arxiv.org/pdf/2609.20041)

