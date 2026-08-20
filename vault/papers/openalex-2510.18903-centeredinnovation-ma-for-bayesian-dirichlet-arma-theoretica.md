---
# CSL-compatible fields
title: "Centered‐Innovation MA for Bayesian Dirichlet ARMA: Theoretical Equivalence and an Application to Bank‐Asset Shares"
author:
  - literal: "Harrison Katz"
issued:
  date-parts:
    - [2026, 8, 18]
url: "https://arxiv.org/abs/2510.18903"

# Custom fields
paper_id: "2510.18903"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:35Z"
created_at: "2026-08-20T05:21:35Z"
---

# Centered‐Innovation MA for Bayesian Dirichlet ARMA: Theoretical Equivalence and an Application to Bank‐Asset Shares

**Authors**: Harrison Katz
**Date**: 2026-08-18
**Paper ID**: [openalex:2510.18903](https://arxiv.org/abs/2510.18903)

## Summary

This paper introduces a centered-innovation moving-average modification for observation-driven Bayesian Dirichlet ARMA models designed for compositional time series. The authors prove a recursion-level first-order equivalence between the centered specification and a digamma-link DARMA under fixed parameters. Empirical evaluation on weekly Federal Reserve H.8 bank-asset shares shows that while predictive performance is nearly identical between the raw and centered specifications, centering drastically reduces Hamiltonian Monte Carlo divergent transitions by mitigating localized posterior pathologies.

## Key Contributions

- Proves recursion-level first-order equivalence between centered-innovation and digamma-link Bayesian Dirichlet ARMA (B-DARMA) specifications at fixed parameters under interior and lag-stability conditions.
- Demonstrates across 104 rolling weekly origins of Federal Reserve H.8 bank-asset shares that centered and raw specifications yield no statistically significant differences in predictive performance metrics.
- Shows that centered innovations reduce Hamiltonian Monte Carlo divergent transitions by an order of magnitude by eliminating localized raw posterior pathologies, ensuring stable operational production workflows.

## Limitations

Evaluated primarily on compositional bank-asset shares from the Federal Reserve H.8 dataset; theoretical equivalence holds at fixed parameters and does not fully govern posterior geometry under re-estimation.

## Open Questions & Future Work

- [[stationarity-ergodicity-dirichlet-arma]]

## Archivist Review

In accordance with the stringent selection policy, no new vault concepts or datasets were approved as they are too specialized or paper-local. One foundational open question regarding the stationarity and ergodicity of observation-driven Dirichlet ARMA models was retained.

### Approved Open Questions
- Stationarity and Ergodicity of Dirichlet ARMA: Important for establishing formal asymptotic properties, consistency, and stability guarantees for Bayesian Dirichlet time series models.

### Rejected Candidates
- [concept] Centered-Innovation Bayesian Dirichlet ARMA (`centered-innovation-bayesian-dirichlet-arma`) - paper_local: Too paper-local and specific to Dirichlet ARMA moving-average parameterizations.

## Links

- [Abstract](https://arxiv.org/abs/2510.18903)
- [PDF](https://arxiv.org/pdf/2510.18903)

