---
# CSL-compatible fields
title: "Multi-Scale Markov Switching GARCH"
author:
  - literal: "Jayesh Chaudhary"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06190"

# Custom fields
paper_id: "2606.06190"
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
  - "triple-timeframe-markov-switching-garch"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:28Z"
created_at: "2026-06-07T08:20:28Z"
---

# Multi-Scale Markov Switching GARCH

**Authors**: Jayesh Chaudhary
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06190](https://arxiv.org/abs/2606.06190)

## Summary

This paper addresses the non-stationarity of financial volatility by proposing a triple-timeframe Markov-Switching GARCH (MS-GARCH) framework. By independently modeling market dynamics across daily, four-hour, and hourly horizons, the approach synthesizes distinct regime behaviors into a 27-state cross-scale probability tensor. The method leverages time-varying transition probabilities at micro and meso levels to capture market stress, significantly improving out-of-sample forecasting performance against traditional benchmarks.

## Key Contributions

- Introduces a triple-timeframe MS-GARCH framework capturing macro, meso, and micro volatility dynamics across daily, four-hour, and hourly horizons.
- Integrates Filardo-style TVTP at shorter horizons using composite stress indicators to inform regime transitions.
- Demonstrates superior out-of-sample volatility forecasting performance for EUR/USD compared to standard single-timescale GARCH models.

## Open Questions & Future Work

- [[path-dependent-ms-garch-computational-bottleneck]]
- [[duration-dependence-in-ms-garch]]

## Key Concepts

- [[triple-timeframe-markov-switching-garch]]: A volatility modeling framework that estimates independent regime dynamics across macro, meso, and micro scales and aggregates them into a cross-scale probability tensor.

## Archivist Review

The proposed triple-timeframe MS-GARCH concept introduces a structured approach to hierarchical regime detection that is reusable across non-stationary domains. I approved the two open questions as they address significant, long-standing limitations in regime-switching models, specifically regarding path-dependence and the first-order Markov constraint, which are central to the field of financial time-series forecasting. No datasets were approved as 'EUR/USD' is a generic financial pair rather than a curated research dataset.

### Approved Concepts
- Triple-timeframe Markov-Switching GARCH: The core novelty lies in integrating regimes across distinct temporal scales into a unified probability tensor.

### Approved Open Questions
- Path-Dependent MS-GARCH Computation: The persistence of residual ARCH effects suggests that the current model, while superior to a single-regime GARCH, still fails to fully capture volatility clustering. This remains a significant bottleneck in volatility forecasting and risk management applications where accurately accounting for volatility carry-over is crucial.
- Regime Duration Dependence Modeling: The first-order Markov assumption is a known simplification that likely fails to capture the 'memory' of market states. Incorporating duration dependence is essential for improving the accuracy of regime transition timing and duration forecasting in complex, non-stationary financial time series.

## Links

- [Abstract](https://arxiv.org/abs/2606.06190)
- [PDF](https://arxiv.org/pdf/2606.06190)

