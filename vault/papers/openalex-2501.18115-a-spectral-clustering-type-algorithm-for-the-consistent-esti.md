---
# CSL-compatible fields
title: "A Spectral Clustering-Type Algorithm for the Consistent Estimation of the Hurst Distribution in Moderately High Dimensions"
author:
  - literal: "Patrice Abry"
  - literal: "Gustavo Didier"
  - literal: "Oliver Orejola"
  - literal: "Herwig Wendt"
issued:
  date-parts:
    - [2026, 10, 11]
url: "https://arxiv.org/abs/2501.18115"

# Custom fields
paper_id: "2501.18115"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-12T12:32:38Z"
created_at: "2026-10-12T12:32:38Z"
---

# A Spectral Clustering-Type Algorithm for the Consistent Estimation of the Hurst Distribution in Moderately High Dimensions

**Authors**: Patrice Abry, Gustavo Didier, Oliver Orejola, Herwig Wendt
**Date**: 2026-10-11
**Paper ID**: [openalex:2501.18115](https://arxiv.org/abs/2501.18115)

## Summary

This paper introduces a provably convergent spectral clustering-type algorithm built on wavelet random matrices to consistently estimate the Hurst distribution of high-dimensional fractal systems. The methodology features an automated model selection procedure for tuning the clustering precision hyperparameter, performing efficiently under a joint asymptotic regime of dimension, sample size, and scale. Empirical evaluations via Monte Carlo simulations confirm its superiority over mixed-Gaussian modeling, and applications to macroeconomic time series reveal novel evidence of cointegration.

## Key Contributions

- Proposes a provably convergent spectral clustering-type algorithm for estimating the Hurst distribution in moderately high-dimensional fractal systems using wavelet random matrices.
- Integrates a principled model selection procedure to automatically tune the clustering precision hyperparameter.
- Establishes theoretical consistency guarantees in a joint asymptotic regime where dimension, sample size, and scale go to infinity.
- Demonstrates superior efficiency over mixed-Gaussian clustering via Monte Carlo simulations and uncovers cointegration evidence in real-world macroeconomic time series.

## Archivist Review

In accordance with the strict filtering policy, no concepts or open questions met the high bar for permanent standalone vault inclusion. The proposed open questions represent narrow mathematical proof asymptotics and standard modeling extensions rather than fundamental open bottlenecks in time series forecasting or representation learning.

### Rejected Candidates
- [open_question] Rates of convergence for wavelet random matrices (`rates-of-convergence-wavelet-random-matrices`) - low_impact: Too specialized and narrow around the mathematical proof details of wavelet random matrix asymptotics.
- [open_question] Robustness and universality beyond Gaussian measurements (`robustness-universality-fractal-measurements`) - low_impact: Standard boilerplate future work extending model assumptions.

## Links

- [Abstract](https://arxiv.org/abs/2501.18115)
- [PDF](https://arxiv.org/pdf/2501.18115)

