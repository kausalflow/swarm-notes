---
# CSL-compatible fields
title: "Scenario Generation for Time Series and Curves: A Comparison of Nonparametric and Semiparametric Bootstrap"
author:
  - literal: "Nicola Baldoni"
  - literal: "Michele Sparviero"
  - literal: "Lorenzo Viola"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.11859"

# Custom fields
paper_id: "2606.11859"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:15:52Z"
created_at: "2026-06-13T08:15:52Z"
---

# Scenario Generation for Time Series and Curves: A Comparison of Nonparametric and Semiparametric Bootstrap

**Authors**: Nicola Baldoni, Michele Sparviero, Lorenzo Viola
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.11859](https://arxiv.org/abs/2606.11859)

## Summary

This paper investigates the effectiveness of various bootstrap methodologies for generating stochastic asset-class trajectories. The authors highlight that while traditional nonparametric bootstrap methods preserve the empirical distribution of historical returns, they often fail to capture the economic realism required for individual simulated paths, particularly in complex structures like interest rate yield curves. By comparing these against semiparametric approaches that combine parametric dynamics with residual resampling, the study demonstrates that semiparametric models yield more coherent and economically plausible scenario simulations.

## Key Contributions

- Conducts a comparative study of nonparametric and semiparametric bootstrap techniques for stochastic trajectory generation in quantitative finance.
- Identifies that purely nonparametric stationary bootstrap methods often generate statistically valid return distributions while producing economically unrealistic individual paths.
- Demonstrates that semiparametric bootstrap approaches—integrating parametric structures (e.g., autoregressive or mean-reverting models) with residual resampling—significantly improve the coherence and realism of simulated yield-curve dynamics in fixed-income applications.

## Links

- [Abstract](https://arxiv.org/abs/2606.11859)
- [PDF](https://arxiv.org/pdf/2606.11859)

