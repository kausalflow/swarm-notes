---
# CSL-compatible fields
title: "Nonlinear and Heavy-Tailed Predictability in Transition-Energy Financial Markets"
author:
  - literal: "Kpante Emmanuel Gnandi"
  - literal: "Fredy Pokou"
  - literal: "Jules Sadefo Kamdem"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26890"

# Custom fields
paper_id: "2605.26890"
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
  - "student-t-vector-autoregression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:50Z"
created_at: "2026-05-29T08:38:50Z"
---

# Nonlinear and Heavy-Tailed Predictability in Transition-Energy Financial Markets

**Authors**: Kpante Emmanuel Gnandi, Fredy Pokou, Jules Sadefo Kamdem
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26890](https://arxiv.org/abs/2605.26890)

## Summary

This paper addresses the limitations of Gaussian-linear frameworks in modeling transition-related financial assets, which are characterized by heavy tails and nonlinear volatility clustering. The authors propose a hybrid approach that filters returns using a Student-t Vector Autoregression and subsequently learns nonlinear residual patterns with recurrent neural networks. Empirical results demonstrate that this framework significantly outperforms traditional linear models and standalone machine learning methods, particularly during turbulent market periods. The study underscores the necessity of accounting for regime-sensitive, non-Gaussian dynamics when forecasting assets within the evolving energy landscape.

## Key Contributions

- Develops a hybrid forecasting framework that integrates Student-t Vector Autoregressions with recurrent neural network residuals to capture both linear heavy-tailed and nonlinear dynamics.
- Demonstrates that transition-energy sector assets exhibit significant nonlinear dependence and heavy-tailed behavior not addressed by standard Gaussian-linear models.
- Shows significant out-of-sample predictive improvements over benchmark models (VAR, standalone ML) during periods of high macro-financial stress, such as the COVID-19 pandemic and energy price shocks.

## Key Concepts

- [[student-t-vector-autoregression]]: A multivariate linear model utilizing Student-t distributions to account for excess kurtosis in financial time series.

## Archivist Review

I approved the concept of Student-t Vector Autoregression as it represents a distinct, reusable methodology for handling heavy-tailed financial time series data within a hybrid forecasting architecture. Other candidates were not submitted, and I focused on maintaining the vault's high standards for novel, reusable techniques rather than local empirical results.

### Approved Concepts
- Student-t Vector Autoregression: It provides a robust econometric foundation to handle the heavy-tailed nature of financial time series returns before modeling nonlinearities.

## Links

- [Abstract](https://arxiv.org/abs/2605.26890)
- [PDF](https://arxiv.org/pdf/2605.26890)

