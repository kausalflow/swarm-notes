---
# CSL-compatible fields
title: "Estimating value-at-risk: LSTM vs. GARCH"
author:
  - literal: "Weronika Ormaniec"
  - literal: "Marcin Pitera"
  - literal: "Sajad Safarveisi"
  - literal: "Thorsten Schmidt"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2207.10539"

# Custom fields
paper_id: "2207.10539"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "evaluation"
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
processed_at: "2026-10-03T10:07:06Z"
created_at: "2026-10-03T10:07:06Z"
---

# Estimating value-at-risk: LSTM vs. GARCH

**Authors**: Weronika Ormaniec, Marcin Pitera, Sajad Safarveisi, Thorsten Schmidt
**Date**: 2026-10-01
**Paper ID**: [openalex:2207.10539](https://arxiv.org/abs/2207.10539)

## Summary

This paper proposes a novel non-parametric Value-at-Risk (VaR) estimator using a Long Short-Term Memory (LSTM) network to address heteroskedastic dynamics and limited sample sizes in time series data. Through evaluation on simulated and market datasets, the authors show that the LSTM-based estimator successfully recovers GARCH-like conditional risk dynamics and achieves competitive calibration alongside improved quantile scores compared to classical benchmarks. These findings highlight the LSTM estimator as a flexible, robust tool for tail risk assessment under time-varying volatility.

## Key Contributions

- Proposes a novel non-parametric Value-at-Risk (VaR) estimator based on Long Short-Term Memory (LSTM) networks for time series with heteroskedastic dynamics.
- Demonstrates that the LSTM-based estimator successfully recovers GARCH-like conditional risk dynamics when evaluated on simulated parametric volatility data.
- Shows that LSTM-based VaR forecasts achieve competitive calibration and frequently lower average quantile scores compared to classical parametric GARCH benchmarks on market data.

## Archivist Review

Applied strict selectivity filters, rejecting standard future work extensions since they lack core novelty or specific methodological challenges. No concepts or datasets met the strict reusability and uniqueness criteria.

### Rejected Candidates
- [open_question] Expected Shortfall Risk Estimation (`expected-shortfall-risk-measures`) - generic: The proposed question is standard future work suggesting the extension of value-at-risk to expected shortfall, lacking a specific methodological bottleneck or technical mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2207.10539)
- [PDF](https://arxiv.org/pdf/2207.10539)

