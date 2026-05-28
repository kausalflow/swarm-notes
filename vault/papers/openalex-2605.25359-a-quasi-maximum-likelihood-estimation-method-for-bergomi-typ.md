---
# CSL-compatible fields
title: "A Quasi Maximum Likelihood Estimation Method for Bergomi-Type Volatility Models"
author:
  - literal: "Masaaki Fukasawa"
  - literal: "Haruki Tomita"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25359"

# Custom fields
paper_id: "2605.25359"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quasi-maximum-likelihood-for-bergomi-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:38:17Z"
created_at: "2026-05-28T08:38:17Z"
---

# A Quasi Maximum Likelihood Estimation Method for Bergomi-Type Volatility Models

**Authors**: Masaaki Fukasawa, Haruki Tomita
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25359](https://arxiv.org/abs/2605.25359)

## Summary

This paper introduces a quasi maximum likelihood estimation method to address parameter recovery in Bergomi-type stochastic volatility models. The authors represent the cumulative forward variance as an infinite-dimensional stochastic differential equation and mitigate model degeneracy by utilizing a non-degenerate proxy likelihood derived from the Euler-Maruyama approximation. Theoretical proofs verify the estimator's consistency and asymptotic mixed normality, while empirical results on SPXW option data demonstrate practical feasibility for high-frequency financial time-series.

## Key Contributions

- Proposes a quasi maximum likelihood estimation method for Bergomi-type models that resolves the model degeneracy through Euler-Maruyama proxy likelihoods.
- Establishes consistency and asymptotic mixed normality for the proposed estimator under defined kernel classes.
- Demonstrates empirical utility for recovering kernel parameters from high-frequency option price time-series.

## Open Questions & Future Work

- [[instability-of-joint-estimation-bergomi-volatility]]

## Key Concepts

- [[quasi-maximum-likelihood-for-bergomi-models]]: A parameter estimation framework for Bergomi-type stochastic volatility models that uses a non-degenerate proxy likelihood derived from Euler-Maruyama approximations.

## Archivist Review

The paper proposes a specific, mathematically grounded quasi maximum likelihood method for estimating parameters in Bergomi-type volatility models, which are influential in financial mathematics. The approved concept captures a reusable estimation framework for high-dimensional stochastic processes, and the approved open question identifies a fundamental challenge in parameter identifiability within these models that will likely persist in future research. Other candidates were rejected to maintain the strict scarcity and novelty requirements of the vault.

### Approved Concepts
- Quasi Maximum Likelihood Estimation for Bergomi-Type Models: Addresses the computational difficulty of estimating parameters in infinite-dimensional Bergomi models by mapping them to finite-dimensional proxies.

### Approved Open Questions
- Instability of Joint Estimation in Bergomi Models: The joint estimation of memory parameters and volatility scale is critical for characterizing market dynamics correctly; persistent instability here suggests potential model misspecification or inherent identification issues that impact the reliability of risk pricing and volatility surface modeling.

### Rejected Candidates
- [dataset] SPXW option data (`spxw-option-data`) - generic: This is a generic financial market data descriptor rather than a specific, stable named dataset for archiving.

## Links

- [Abstract](https://arxiv.org/abs/2605.25359)
- [PDF](https://arxiv.org/pdf/2605.25359)

