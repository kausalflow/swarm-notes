---
# CSL-compatible fields
title: "Forecasting Individual NetFlows using a Predictive Masked Graph Autoencoder"
author:
  - literal: "Georgios Anyfantis"
  - literal: "Pere Barlet-Ros"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20483"

# Custom fields
paper_id: "2604.20483"
paper_source: "openalex"
domain: "nlp"
tags:
  - "graph-neural-network"
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
processed_at: "2026-04-25T06:15:32Z"
created_at: "2026-04-25T06:15:32Z"
---

# Forecasting Individual NetFlows using a Predictive Masked Graph Autoencoder

**Authors**: Georgios Anyfantis, Pere Barlet-Ros
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20483](https://arxiv.org/abs/2604.20483)

## Summary

This paper introduces a Graph Neural Network (GNN) model designed to forecast individual NetFlow traffic by capturing the complex evolution of network structure and connection features. By representing network traffic as heterogeneous graphs of IPs, Ports, and Connections within a sliding-window framework, the approach effectively learns dynamic topological relationships. The method outperforms standard forecasting baselines in identifying structural connection attachments and demonstrates robust performance in feature reconstruction.

## Key Contributions

- Introduced a GNN-based framework for per-flow NetFlow prediction by modeling network traffic as heterogeneous bidirectional graphs.
- Demonstrated superior performance in identifying connection associations (IP/Port nodes) compared to traditional baseline models.
- Maintained competitive feature reconstruction accuracy against state-of-the-art forecasting baselines.

## Open Questions & Future Work

- [[variable-graph-size-forecasting]]

## Archivist Review

I reviewed the paper's contribution regarding GNN-based NetFlow prediction. I rejected the model name as a concept because it is a specific architectural instance, but I approved the open question regarding variable graph sizes, as it addresses a fundamental, reusable research bottleneck in graph-based time-series forecasting.

### Approved Open Questions
- Variable Graph Size Forecasting: Most real-world network traffic is dynamic; restricting models to fixed graph sizes limits their practical applicability in production environments where node and edge counts fluctuate significantly.

### Rejected Candidates
- [concept] Predictive Masked Graph Autoencoder (`predictive-masked-graph-autoencoder`) - subcomponent_of_broader_mechanism: This is a specific model architecture instance rather than a reusable forecasting mechanism or theoretical contribution.

## Links

- [Abstract](https://arxiv.org/abs/2604.20483)
- [PDF](https://arxiv.org/pdf/2604.20483)

