---
# CSL-compatible fields
title: "Multivariate reconciliation for hierarchical time series"
author:
  - literal: "Ana Caroline Pinheiro"
  - literal: "Rodrigo de Souza Bulhões"
  - literal: "Rob J. Hyndman"
  - literal: "Paulo Canas Rodrigues"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17920"

# Custom fields
paper_id: "2605.17920"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "forecast-reconciliation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multivariate-forecast-reconciliation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:28:21Z"
created_at: "2026-05-21T08:28:21Z"
---

# Multivariate reconciliation for hierarchical time series

**Authors**: Ana Caroline Pinheiro, Rodrigo de Souza Bulhões, Rob J. Hyndman, Paulo Canas Rodrigues
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17920](https://arxiv.org/abs/2605.17920)

## Summary

This paper introduces a multivariate reconciliation framework for hierarchical time series, addressing the limitation of existing methods that process variables independently. By incorporating correlations between variables alongside standard hierarchical constraints, the proposed approach ensures coherent and more accurate forecasts. The methodology is rigorously evaluated through simulated scenarios and an application to Brazilian employment data, confirming its superior performance over univariate alternatives.

## Key Contributions

- Proposes a novel multivariate reconciliation methodology for hierarchical time series that accounts for both aggregation constraints and inter-variable correlations.
- Demonstrates that the proposed methodology outperforms univariate reconciliation approaches on simulated hierarchical scenarios.
- Validates the approach using real-world Brazilian employment data, showing improved forecasting accuracy compared to standard methods.

## Open Questions & Future Work

- [[scalable-multivariate-reconciliation]]
- [[coherent-probabilistic-reconciliation]]

## Key Concepts

- [[multivariate-forecast-reconciliation]]: A methodology for reconciling hierarchical time series forecasts that accounts for both hierarchical aggregation constraints and correlations across multiple variables.

## Archivist Review

The paper makes a clear, high-impact methodological contribution by extending forecast reconciliation from the univariate hierarchical case to the multivariate setting. The approved concepts and open questions address both the primary advancement and the fundamental scalability/probabilistic limitations of such frameworks. No datasets were approved as none were distinct, novel, or broadly canonical in the provided material.

### Approved Concepts
- Multivariate Forecast Reconciliation: Extends traditional univariate hierarchical forecast reconciliation to multivariate settings by modeling inter-variable correlations, which is essential for consistent multi-variable system forecasting.

### Approved Open Questions
- Scalable multivariate reconciliation estimation: The current approach suffers from the curse of dimensionality as the size of the hierarchy and the number of variables increase, limiting its applicability to massive real-world datasets.
- Coherent joint predictive distributions: Probabilistic coherence is essential for risk management, decision-making under uncertainty, and generating reliable confidence intervals across hierarchical structures.

## Links

- [Abstract](https://arxiv.org/abs/2605.17920)
- [PDF](https://arxiv.org/pdf/2605.17920)

