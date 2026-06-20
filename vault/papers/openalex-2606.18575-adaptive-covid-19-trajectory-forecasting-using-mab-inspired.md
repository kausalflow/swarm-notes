---
# CSL-compatible fields
title: "Adaptive COVID-19 Trajectory Forecasting Using MAB-Inspired Ensemble Weighting"
author:
  - literal: "Hamed Karami"
  - literal: "Javier Redondo Antón"
  - literal: "Geunsoo Jang"
  - literal: "K. Selçuk Candan"
  - literal: "Gerardo Chowell"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18575"

# Custom fields
paper_id: "2606.18575"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "ensemble-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mab-inspired-adaptive-ensemble-weighting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:03Z"
created_at: "2026-06-20T08:18:03Z"
---

# Adaptive COVID-19 Trajectory Forecasting Using MAB-Inspired Ensemble Weighting

**Authors**: Hamed Karami, Javier Redondo Antón, Geunsoo Jang, K. Selçuk Candan, Gerardo Chowell
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18575](https://arxiv.org/abs/2606.18575)

## Summary

This paper investigates the use of Multi-Armed Bandit (MAB) algorithms to adaptively weight ensembles of heterogeneous epidemic models for COVID-19 trajectory forecasting. By treating model selection as a bandit problem, the proposed strategies (such as EXP3 and epsilon-greedy) effectively respond to time-varying model performance across different epidemic phases. Evaluation on U.S. incidence data reveals that while point forecast accuracy is comparable to simple benchmarks, MAB-inspired ensembles significantly improve probabilistic forecast quality and uncertainty quantification. The study highlights the effectiveness of adaptive weighting in settings where component models exhibit non-stationary performance.

## Key Contributions

- Introduces MAB-inspired strategies (UCB, EXP3, epsilon-greedy) to dynamically weight component models in epidemic ensembles.
- Demonstrates that EXP3Stoch, EXP3Det, and EPSStoch variants consistently improve probabilistic forecast quality, specifically Weighted Interval Score (WIS) and interval coverage, on US COVID-19 epidemic waves.
- Provides a comprehensive empirical comparison against individual statistical/mechanistic models and conventional unweighted/inverse-WIS ensemble baselines.

## Open Questions & Future Work

- [[mab-ensemble-generality-prospective-performance]]

## Key Concepts

- [[mab-inspired-adaptive-ensemble-weighting]]: A strategy that uses Multi-Armed Bandit algorithms to dynamically weight component forecasting models based on their time-varying performance.

## Archivist Review

The concept of MAB-inspired ensemble weighting captures a reusable, performance-aware aggregation strategy applicable to general non-stationary time-series forecasting. The approved open question addresses the critical, unresolved bottleneck of identifying the conditions under which adaptive ensemble strategies meaningfully outperform static or simpler baseline methods in prospective, real-world deployment scenarios.

### Approved Concepts
- MAB-inspired adaptive ensemble weighting: Provides a dynamic, performance-aware mechanism for ensemble aggregation in non-stationary forecasting environments.

### Approved Open Questions
- Generalizability of Adaptive Ensemble Weighting: The study identifies that adaptive weighting is configuration-dependent; determining the specific conditions where adaptive methods outperform static baselines is critical for operational forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2606.18575)
- [PDF](https://arxiv.org/pdf/2606.18575)

