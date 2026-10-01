---
# CSL-compatible fields
title: "Graph-Spectral Flow Matching for Multivariate Time Series Anomaly Detection"
author:
  - literal: "Zepeng Zhang"
  - literal: "Jhony H. Giraldo"
  - literal: "Wenbin Wang"
  - literal: "Olga Fink"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36765"

# Custom fields
paper_id: "2609.36765"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "diffusion-model"
  - "graph-neural-network"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "graph-spectral-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:11Z"
created_at: "2026-10-01T11:15:11Z"
---

# Graph-Spectral Flow Matching for Multivariate Time Series Anomaly Detection

**Authors**: Zepeng Zhang, Jhony H. Giraldo, Wenbin Wang, Olga Fink
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36765](https://arxiv.org/abs/2609.36765)

## Summary

Multivariate time series anomaly detection is addressed via GRASP, a novel flow matching framework featuring a graph-spectral path. By incorporating graph structure into the probability path via a fixed-endpoint action combining kinetic and graph Dirichlet energy, GRASP obtains a closed-form path via graph-frequency-dependent hyperbolic interpolation. A velocity predictor trained on normal data detects anomalies using weighted velocity discrepancies, achieving superior performance across four benchmarks.

## Key Contributions

- Proposes GRASP, a flow matching framework with a graph-spectral path that incorporates graph structures into probability paths by minimizing an action combining kinetic and graph Dirichlet energy.
- Derives a closed-form path based on graph-frequency-dependent hyperbolic interpolation for multivariate time series.
- Establishes theoretical guarantees including Laplacian eigenbasis invariance and decomposition of expected oracle anomaly score into bounded endpoint uncertainty and graph-frequency-weighted Fisher discrepancy.
- Demonstrates superior anomaly detection performance across four benchmarks.

## Open Questions & Future Work

- [[dynamic-graph-flow-matching]]

## Key Concepts

- [[graph-spectral-flow-matching]]: A flow matching framework incorporating graph structures into the probability path via graph Dirichlet energy for multivariate time series anomaly detection.

## Archivist Review

Approved the core concept of graph-spectral flow matching and its open question on dynamic graph extensions, adhering to strict scarcity limits and ensuring high reusability standards.

### Approved Concepts
- Graph-Spectral Flow Matching: Introduces a novel flow matching probability path incorporating graph structures via graph Dirichlet energy for multivariate time series anomaly detection.

### Approved Open Questions
- Dynamic Graph Flow Matching: Extending flow-matching anomaly detection to dynamic graphs is vital for real-world industrial environments where sensor interdependencies change constantly.

## Links

- [Abstract](https://arxiv.org/abs/2609.36765)
- [PDF](https://arxiv.org/pdf/2609.36765)

