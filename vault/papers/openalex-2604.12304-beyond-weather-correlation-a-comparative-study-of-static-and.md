---
# CSL-compatible fields
title: "Beyond Weather Correlation: A Comparative Study of Static and Temporal Neural Architectures for Fine-Grained Residential Energy Consumption Forecasting in Melbourne, Australia"
author:
  - literal: "Prasad Nimantha Madusanka Ukwatta Hewage"
  - literal: "Hao Wu"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12304"

# Custom fields
paper_id: "2604.12304"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "neural-network"
architectures:
  - "lstm"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:42Z"
created_at: "2026-04-17T06:29:42Z"
---

# Beyond Weather Correlation: A Comparative Study of Static and Temporal Neural Architectures for Fine-Grained Residential Energy Consumption Forecasting in Melbourne, Australia

**Authors**: Prasad Nimantha Madusanka Ukwatta Hewage, Hao Wu
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12304](https://arxiv.org/abs/2604.12304)

## Summary

This study evaluates the relative importance of temporal autocorrelation versus static meteorological features for 5-minute resolution residential energy forecasting in Melbourne. Using smart meter data from two households, the authors compare MLP and LSTM architectures, finding that temporal memory significantly outperforms weather-driven models. The results highlight that while weather variables contribute to forecasting solar PV-integrated households, they are insufficient as primary predictors compared to historical consumption sequences.

## Key Contributions

- Demonstrates that temporal autocorrelation dominates weather features for 5-minute interval residential energy forecasting, achieving R^2 of 0.883 for grid-connected households.
- Identifies a significant performance gap between LSTM (R^2 = 0.865) and weather-only MLP (R^2 = 0.410) in solar PV-integrated households, illustrating the limitations of static meteorological inputs.
- Provides a rigorous comparative analysis using 14 months of 5-minute resolution smart meter data across two distinct residential household types in Melbourne.

## Open Questions & Future Work

- [[hybrid-weather-sequence-forecasting]]
- [[solar-pv-load-disaggregation]]

## Archivist Review

The paper provides a baseline empirical comparison for high-frequency residential load forecasting but does not introduce sufficiently novel methods or architectures to warrant new concept entries in the vault. The proposed open questions regarding hybrid modeling and load/generation disaggregation represent significant, actionable research bottlenecks in the energy forecasting domain and are therefore approved.

### Approved Open Questions
- Hybrid Weather-Sequence Load Forecasting: Establishing whether exogenous features provide marginal or significant gains in hybrid architectures is critical for optimizing smart grid management and demand response strategies.
- Solar PV Load Disaggregation: Precise disaggregation is necessary for residential energy management systems to optimize battery dispatch and load scheduling without being misled by solar generation patterns.

## Links

- [Abstract](https://arxiv.org/abs/2604.12304)
- [PDF](https://arxiv.org/pdf/2604.12304)

