---
# CSL-compatible fields
title: "DecompKAN: Decomposed Patch-KAN for Long-Term Time Series Forecasting"
author:
  - literal: "Naveen Mysore"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.23968"

# Custom fields
paper_id: "2604.23968"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  - "ppg-dalia-dataset"
concept_slugs:
  - "decompkan"
dataset_slugs:
  - "ppg-dalia-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:23:41Z"
created_at: "2026-04-30T07:23:41Z"
---

# DecompKAN: Decomposed Patch-KAN for Long-Term Time Series Forecasting

**Authors**: Naveen Mysore
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.23968](https://arxiv.org/abs/2604.23968)

## Summary

DecompKAN is a novel, attention-free forecasting architecture that enhances model transparency by replacing traditional neural network weights with inspectable B-spline Kolmogorov-Arnold Network (KAN) edge functions. By combining trend-residual decomposition, channel-wise patching, and learned instance normalization, the model captures complex temporal dynamics while remaining lightweight. Empirical evaluation across nine datasets, including the PPG-DaLiA benchmark, shows that DecompKAN achieves state-of-the-art performance in scientific forecasting tasks characterized by smooth temporal structures.

## Key Contributions

- Proposes DecompKAN, a lightweight attention-free architecture that integrates trend-residual decomposition and channel-wise patching with KAN edge functions for interpretable forecasting.
- Achieves competitive forecasting performance, notably reducing MSE on Solar (-17%) and ECL (-10%) datasets compared to state-of-the-art transformers like iTransformer.
- Demonstrates that while the structural pipeline drives performance, the KAN formulation allows for direct visualization and inspection of latent nonlinearities across diverse scientific domains.

## Open Questions & Future Work

- [[kan-basis-function-selection-for-forecasting]]

## Key Concepts

- [[decompkan]]: A lightweight attention-free architecture for time series forecasting that replaces standard MLPs with B-spline KAN edge functions to improve interpretability and performance.

## Archivist Review

DecompKAN is approved for its distinct integration of KANs into time-series forecasting, providing a clear path for future architectural comparisons. PPG-DaLiA is approved as a representative scientific benchmark for this class of physiological time-series models. I have approved one open question regarding KAN basis function selection, while rejecting the GNN integration question as it is a generic, widely pursued topic in the field.

### Approved Concepts
- DecompKAN: It is the core architectural contribution of the paper, uniquely combining trend-residual decomposition with KAN-based edge functions for time series.

### Approved Open Questions
- Optimal KAN Basis Functions: The basis function choice is central to the KAN representational framework and impacts domain-specific performance, making it a critical research direction for KAN-based time series modeling.

### Rejected Candidates
- [open_question] Cross-Variate GNN Integration (`gnn-integration-multivariate-forecasting`) - generic: This is a broad, well-trodden research direction in multivariate forecasting rather than a specific unresolved mechanism tied to the current work's contribution.

## Datasets

- [[ppg-dalia-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2604.23968)
- [PDF](https://arxiv.org/pdf/2604.23968)

