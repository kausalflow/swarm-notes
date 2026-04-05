---
# CSL-compatible fields
title: "Network Structure in UK Payment Flows: Evidence on Economic Interdependencies and Implications for Real-Time Measurement"
author:
  - literal: "Aditya Humnabadkar"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.02068"

# Custom fields
paper_id: "2604.02068"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "network-augmented-macroeconomic-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:08:59Z"
created_at: "2026-04-05T06:08:59Z"
---

# Network Structure in UK Payment Flows: Evidence on Economic Interdependencies and Implications for Real-Time Measurement

**Authors**: Aditya Humnabadkar
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.02068](https://arxiv.org/abs/2604.02068)

## Summary

This paper explores the application of network science to UK inter-industry payment flows to improve macroeconomic nowcasting. By integrating graph-theoretic topological features with traditional time-series methods, the proposed approach significantly outperforms standard models, particularly during periods of economic instability. The findings highlight the systemic importance of sectors like Financial and Professional Services and demonstrate that network-based monitoring provides a resilient leading indicator of structural economic shifts.

## Key Contributions

- Introduces a framework for incorporating graph-theoretic features, such as centrality and clustering coefficients, into economic payment flow models.
- Demonstrates that network-augmented models improve payment flow forecasting by 8.8 percentage points over traditional time-series approaches.
- Validates the robustness of network-based indicators during economic disruptions, showing a performance improvement of +13.8 percentage points during the COVID-19 pandemic.

## Open Questions & Future Work

- [[dynamic-weighting-of-network-and-temporal-forecasts]]

## Key Concepts

- [[network-augmented-macroeconomic-forecasting]]: A forecasting methodology that integrates graph-theoretic topological features, such as centrality and clustering coefficients, to improve economic time-series prediction accuracy.

## Archivist Review

I approved a general concept for network-augmented macroeconomic forecasting to capture the utility of graph-theoretic priors in time-series modeling. I also approved an open question regarding the dynamic weighting of these structural indicators against temporal models, as this is a fundamental challenge in robust forecasting during structural breaks. Other candidates were rejected to avoid paper-local specificity or duplicate terminology.

### Approved Concepts
- Network-Augmented Macroeconomic Forecasting: Captures the shift from univariate time-series to topological, graph-based structural modeling for macroeconomic nowcasting, particularly during regime shifts.

### Approved Open Questions
- Dynamic network-temporal model weighting: This addresses the critical challenge of model robustness and adaptive weighting when historical temporal dependencies fail.

### Rejected Candidates
- [concept] Network-enhanced payment flow forecasting (`network-enhanced-payment-flow-forecasting`) - duplicate_existing: This is effectively a specific application instance of a broader mechanism, which I have renamed to 'Network-Augmented Macroeconomic Forecasting' for better generality and vault alignment.

## Links

- [Abstract](https://arxiv.org/abs/2604.02068)
- [PDF](https://arxiv.org/pdf/2604.02068)

