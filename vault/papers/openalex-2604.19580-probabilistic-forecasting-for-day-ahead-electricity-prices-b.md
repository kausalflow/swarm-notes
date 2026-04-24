---
# CSL-compatible fields
title: "Probabilistic Forecasting for Day-ahead Electricity Prices, Battery Trading Strategies and the Economic Evaluation of Predictive Accuracy"
author:
  - literal: "Simon Hirsch"
  - literal: "Florian Ziel"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19580"

# Custom fields
paper_id: "2604.19580"
paper_source: "openalex"
domain: "finance"
tags:
  - "forecasting"
  - "time-series"
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
processed_at: "2026-04-24T06:59:54Z"
created_at: "2026-04-24T06:59:54Z"
---

# Probabilistic Forecasting for Day-ahead Electricity Prices, Battery Trading Strategies and the Economic Evaluation of Predictive Accuracy

**Authors**: Simon Hirsch, Florian Ziel
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19580](https://arxiv.org/abs/2604.19580)

## Summary

This paper addresses the gap between statistical forecast accuracy and economic utility in day-ahead electricity markets. The authors critique current quantile-based trading strategies (QBTS) used as benchmarks, noting their inability to handle intertemporal price dependencies and their failure to incentivize honest probabilistic modeling. They propose a robust stochastic programming approach for battery arbitrage and provide a German electricity market case study to show how model rankings based on simplified trading strategies may result in unreliable economic conclusions. The work concludes by establishing better practices for linking statistical quality to decision-making performance in energy applications.

## Key Contributions

- Identifies and theoretically demonstrates two critical flaws in quantile-based trading strategies (QBTS): lack of incentives for honest probabilistic forecasting and neglect of intertemporal price dependencies.
- Proposes a stochastic programming framework for battery arbitrage that utilizes fully probabilistic forecasts instead of quantile-based simplifications.
- Empirically demonstrates that ranking forecasting models via application-based battery trading benchmarks can be misleading and provides guidance for more reliable economic evaluation of predictive accuracy.

## Open Questions & Future Work

- [[forecast-economic-alignment]]

## Archivist Review

The paper provides a significant critique of current evaluation practices in electricity price forecasting but focuses on analyzing existing methods rather than proposing new reusable ML architectures or mechanisms. I approved the open question regarding the alignment of statistical forecast accuracy with economic utility, as this is a fundamental, recurring challenge in decision-focused forecasting that requires broader investigation beyond this specific study.

### Approved Open Questions
- Economic Value of Forecasts: The authors identify this as a gap where current literature provides only ad-hoc solutions, and emphasize the need for new, objective-aligned evaluation measures to avoid spurious conclusions in forecast assessment.

### Rejected Candidates
- [concept] Quantile-based Trading Strategies (QBTS) Flaw Analysis (`qbts-flaws-analysis`) - not_novel: The analysis of these strategies is a critical contribution but represents a critique of an existing method rather than a novel, reusable forecasting mechanism or architecture.
- [concept] Stochastic Programming for Battery Arbitrage (`stochastic-programming-for-battery-arbitrage`) - not_novel: This is an application of an existing mathematical optimization technique (stochastic programming) to a specific domain (battery storage) rather than a fundamental ML methodology.

## Links

- [Abstract](https://arxiv.org/abs/2604.19580)
- [PDF](https://arxiv.org/pdf/2604.19580)

