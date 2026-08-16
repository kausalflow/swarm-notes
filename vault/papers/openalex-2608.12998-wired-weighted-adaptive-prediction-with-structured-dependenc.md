---
# CSL-compatible fields
title: "WIRED: Weighted Adaptive Prediction with Structured Dependence for Probabilistic Multiseries Forecasting"
author:
  - literal: "Giancarlo Vercellino"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.12998"

# Custom fields
paper_id: "2608.12998"
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
processed_at: "2026-08-16T05:17:45Z"
created_at: "2026-08-16T05:17:45Z"
---

# WIRED: Weighted Adaptive Prediction with Structured Dependence for Probabilistic Multiseries Forecasting

**Authors**: Giancarlo Vercellino
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.12998](https://arxiv.org/abs/2608.12998)

## Summary

This paper introduces WIRED, an R package algorithm for joint probabilistic forecasting of multiple related time series that combines marginal predictive distributions, adaptive mixture weights, and copula modeling for cross-series dependence. Through extensive evaluation on synthetic data-generating processes and real financial data, the author uncovers an architectural bottleneck where CRPS-extrapolated softmax weighting fails to reliably outperform simpler baseline weighting strategies. Consequently, the study charts a clear research trajectory toward more regularized probabilistic ensemble construction.

## Key Contributions

- Introduces WIRED, an algorithm and R package for joint probabilistic multiseries forecasting combining marginal distributions, CRPS-based adaptive weights, and copula dependence reconstruction.
- Evaluates WIRED across four synthetic DGPs, three horizons, 30 replicates, and nine baselines/ablations, alongside a rolling-origin study on EuStockMarkets data.
- Demonstrates through architectural diagnostics that CRPS-extrapolated softmax weighting underperforms compared to simpler bootstrap or equal-weight alternatives, identifying a concrete bottleneck in marginal expert aggregation.

## Limitations

CRPS-extrapolated softmax weighting lacks sufficient robustness to consistently dominate simpler bootstrap or equal-weight aggregation alternatives.

## Open Questions & Future Work

- [[improving-marginal-aggregation-probabilistic-forecasting]]

## Archivist Review

Evaluated the candidates under the strict skill and vault review policies. No novel standalone concept candidates were provided by the analysis, but the open question regarding marginal aggregation in probabilistic forecasting represents a specific, highly reusable bottleneck in ensemble time series modeling and is approved.

### Approved Open Questions
- Improving Marginal Aggregation in Probabilistic Forecasting: While dependence reconstruction (copulas) proved useful in the framework, the adaptive marginal weighting layer failed to consistently outperform simpler uniform or bootstrap baselines, identifying a key algorithmic bottleneck for ensemble probabilistic forecasting.

### Rejected Candidates
- [open_question] Improving Marginal Aggregation in Probabilistic Forecasting (`improving-marginal-aggregation-probabilistic-forecasting`) - other: The open question is approved.

## Links

- [Abstract](https://arxiv.org/abs/2608.12998)
- [PDF](https://arxiv.org/pdf/2608.12998)

