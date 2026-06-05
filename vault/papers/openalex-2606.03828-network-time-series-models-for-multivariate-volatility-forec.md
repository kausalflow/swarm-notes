---
# CSL-compatible fields
title: "Network Time Series Models for Multivariate Volatility Forecasting"
author:
  - literal: "Chiara Boetti"
  - literal: "Matthew A. Nunes"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03828"

# Custom fields
paper_id: "2606.03828"
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
  - "generalised-network-heterogeneous-autoregressive-model-gnhar"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:37:48Z"
created_at: "2026-06-05T08:37:48Z"
---

# Network Time Series Models for Multivariate Volatility Forecasting

**Authors**: Chiara Boetti, Matthew A. Nunes
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03828](https://arxiv.org/abs/2606.03828)

## Summary

This paper introduces the Generalised Network Heterogeneous Autoregressive (GNHAR) model for multivariate realized volatility forecasting. By integrating cross-sectional spillovers via directed graphs—constructed using Granger-causality or connectedness indices—the GNHAR model achieves a parsimonious representation of complex financial networks. The approach outperforms standard HAR benchmarks across multiple forecasting horizons and provides interpretable, time-varying insights into cross-market dependencies and market stability.

## Key Contributions

- Proposes the GNHAR model, a parsimonious multivariate extension of the HAR framework for realized variance processes.
- Demonstrates that incorporating directed graph-based cross-sectional spillovers improves volatility forecasting performance in both tranquil and crisis market regimes.
- Provides a concise parameter set that allows for tracking evolving cross-market dependencies, serving as a quantitative indicator of market stability.

## Open Questions & Future Work

- [[dynamic-network-structure-selection-volatility]]

## Key Concepts

- [[generalised-network-heterogeneous-autoregressive-model-gnhar]]: A multivariate volatility forecasting framework that extends the heterogeneous autoregressive (HAR) approach by incorporating cross-sectional spillovers via a directed graph.

## Archivist Review

The GNHAR model is approved as it offers a distinct, parsimonious approach to multivariate time-series forecasting by integrating topological priors directly into the HAR framework. The open question regarding dynamic network selection is approved because it addresses the core challenge of balancing structural complexity and interpretability in non-stationary financial regimes. No datasets were approved as they were not named or explicitly detailed in the provided materials.

### Approved Concepts
- Generalised Network Heterogeneous Autoregressive Model (GNHAR): It is the core methodological contribution, providing a parsimonious multivariate framework for volatility forecasting that accounts for cross-sectional market dependencies.

### Approved Open Questions
- Dynamic Network Structure Selection: Automated or adaptive network selection is critical for practical financial applications where manually choosing a graph for each rolling window is computationally expensive and prone to bias, limiting scalability and reliability.

## Links

- [Abstract](https://arxiv.org/abs/2606.03828)
- [PDF](https://arxiv.org/pdf/2606.03828)

