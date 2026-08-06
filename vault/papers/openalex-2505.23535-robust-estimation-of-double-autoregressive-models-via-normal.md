---
# CSL-compatible fields
title: "Robust Estimation of Double Autoregressive Models via Normal Mixture QMLE*"
author:
  - literal: "Zhao Chen"
  - literal: "Shi Chen"
  - literal: "Christina Dan Wang"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2505.23535"

# Custom fields
paper_id: "2505.23535"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "normal-mixture-quasi-maximum-likelihood-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:32Z"
created_at: "2026-08-06T07:32:32Z"
---

# Robust Estimation of Double Autoregressive Models via Normal Mixture QMLE*

**Authors**: Zhao Chen, Shi Chen, Christina Dan Wang
**Date**: 2026-08-03
**Paper ID**: [openalex:2505.23535](https://arxiv.org/abs/2505.23535)

## Summary

This paper investigates the estimation of double autoregressive (DAR) models under skewed and heavy-tailed innovations by proposing a Normal Mixture Quasi-Maximum Likelihood Estimation (NM-QMLE) method. The approach addresses limitations of conventional QMLE by incorporating a normal mixture distribution to capture non-Gaussian characteristics and systematically evaluates model selection criteria for determining the number of components. Theoretical proofs establish consistency and asymptotic normality, while simulations and empirical evaluations on S&P 500 Value at Risk demonstrate improved estimation accuracy and risk assessment.

## Key Contributions

- Proposes a novel Normal Mixture Quasi-Maximum Likelihood Estimation (NM-QMLE) method for double autoregressive (DAR) models to handle skewed and heavy-tailed innovations.
- Establishes consistency and asymptotic normality of the NM-QMLE estimator for DAR(p) models under regularity conditions.
- Demonstrates superior estimation accuracy over conventional QMLE methods via simulation studies and improves Value at Risk (VaR) estimation on S&P 500 empirical data.

## Open Questions & Future Work

- [[optimal-mixture-component-selection-dar]]

## Key Concepts

- [[normal-mixture-quasi-maximum-likelihood-estimation]]: A quasi-maximum likelihood estimation method incorporating normal mixture distributions to handle heavy-tailed and skewed innovations in time series models.

## Archivist Review

Approved the core statistical estimation concept for double autoregressive models and the open question regarding optimal mixture component selection. Rejected the S&P 500 dataset as it is a standard financial index rather than a dedicated benchmark dataset.

### Approved Concepts
- Normal Mixture Quasi-Maximum Likelihood Estimation: Core methodological contribution providing robust estimation for double autoregressive models with skewed and heavy-tailed innovations.

### Approved Open Questions
- Optimal Component Selection in DAR Models: Determining the correct number of mixture components in time series mixture models directly impacts estimation consistency, finite-sample performance, and computational tractability.

## Links

- [Abstract](https://arxiv.org/abs/2505.23535)
- [PDF](https://arxiv.org/pdf/2505.23535)

