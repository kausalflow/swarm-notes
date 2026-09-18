---
# CSL-compatible fields
title: "Peak-Aware Short-Term Load Forecasting Across Distribution Grid Aggregation Levels"
author:
  - literal: "Souhardya Chattopadhyay"
  - literal: "Julian Oelhaf"
  - literal: "Antonia Schoening"
  - literal: "Jessica Deuschel"
  - literal: "Bitan Bhattacharyya"
  - literal: "Christian Bergler"
  - literal: "Andreas Maier"
  - literal: "Siming Bayer"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18588"

# Custom fields
paper_id: "2609.18588"
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
processed_at: "2026-09-18T09:17:14Z"
created_at: "2026-09-18T09:17:14Z"
---

# Peak-Aware Short-Term Load Forecasting Across Distribution Grid Aggregation Levels

**Authors**: Souhardya Chattopadhyay, Julian Oelhaf, Antonia Schoening, Jessica Deuschel, Bitan Bhattacharyya, Christian Bergler, Andreas Maier, Siming Bayer
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18588](https://arxiv.org/abs/2609.18588)

## Summary

This paper studies peak-aware short-term load forecasting (STLF) across multiple distribution grid aggregation levels (area codes, secondary substations, and low-voltage feeders) using open datasets from the UK and Switzerland. The authors evaluate statistical baselines, gradient-boosted trees, and time-series foundation models (Chronos Bolt and Chronos-2) under a peak-aware framework prioritizing high-demand periods. Results show that Chronos-2 significantly improves high-demand forecasting accuracy and reduces HD-NMAE by 20-51% compared to gradient-boosted machine learning models.

## Key Contributions

- Evaluates short-term load forecasting (STLF) across three distribution grid aggregation levels (area codes, secondary substations, and low-voltage feeders) under a peak-aware evaluation framework.
- Compares statistical baselines, gradient-boosted machines, and time-series foundation models (Chronos Bolt and Chronos-2) using NMAE and MAPE on overall and high-demand (HD) periods.
- Demonstrates that Chronos-2 reduces mean HD-NMAE by 20-51% compared to gradient-boosted models while maintaining competitive overall accuracy.
- Performs a quantile analysis on probabilistic foundation model outputs to identify aggregation-specific operating points for distribution system operators.

## Open Questions & Future Work

- [[model-predictive-control-integration]]

## Archivist Review

Applied strict selectivity filters: no concepts met the threshold for permanent vault storage as the paper evaluates existing time-series foundation models (Chronos-2) rather than introducing a novel foundational architecture. The open question regarding MPC integration is a standard downstream application step and was rejected as boilerplate future work.

### Approved Open Questions
- Uncertainty-Aware Model Predictive Control: Bridging the gap between peak-aware forecasting and active downstream grid control (such as MPC) is crucial for transforming offline forecast improvements into tangible operational reliability and congestion mitigation for distribution system operators.

### Rejected Candidates
- [open_question] Uncertainty-Aware Model Predictive Control (`model-predictive-control-integration`) - duplicate_existing: Duplicate or overly standard future-work direction regarding downstream control integration.

## Links

- [Abstract](https://arxiv.org/abs/2609.18588)
- [PDF](https://arxiv.org/pdf/2609.18588)

