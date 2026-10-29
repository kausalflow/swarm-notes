---
# CSL-compatible fields
title: "A Diagnostic Protocol for GNNs in Electricity Load Forecasting: Separating Parameter Sharing from Neighborhood Access"
author:
  - literal: "Eloi Campagne"
  - literal: "Yvenn Amara-Ouali"
  - literal: "Yannig Goude"
  - literal: "Itai Zehavi"
  - literal: "Argyris Kalogeratos"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35074"

# Custom fields
paper_id: "2610.35074"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "gnn"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:11:05Z"
created_at: "2026-10-29T11:11:05Z"
---

# A Diagnostic Protocol for GNNs in Electricity Load Forecasting: Separating Parameter Sharing from Neighborhood Access

**Authors**: Eloi Campagne, Yvenn Amara-Ouali, Yannig Goude, Itai Zehavi, Argyris Kalogeratos
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35074](https://arxiv.org/abs/2610.35074)

## Summary

Graph neural networks (GNNs) for electricity load forecasting combine parameter sharing and neighborhood aggregation, but distinguishing which mechanism drives performance improvements is challenging. This paper introduces a diagnostic protocol utilizing reference models and degree-preserving rewiring to separate parameter sharing from neighborhood access. Empirical evaluations on regional and low-voltage UK/French datasets reveal that parameter sharing—rather than the graph edges themselves—accounts for the majority of the GNN's performance advantage over per-node models.

## Key Contributions

- Proposes a model diagnostic protocol that isolates parameter sharing from neighborhood access in GNN-based electricity load forecasting by comparing against per-node networks, shared networks without neighbors, and edge-ablated GNNs.
- Demonstrates on regional French load and UK low-voltage feeder datasets that parameter sharing rather than graph edge topology accounts for the majority of the GNN error gap over node-specific models.
- Shows through synthetic and short-history experiments that neighbor contributions degrade or yield negligible gains when local histories are uninformative or noisy, proving that GNN forecasting gains require rigorous separation baselines.

## Archivist Review

Evaluated the paper which presents a diagnostic protocol for separating parameter sharing from neighborhood access in GNN-based electricity load forecasting. The proposed open question is generic future work rather than an explicit, well-defined open bottleneck, so no items are approved in accordance with our strict selection policy.

### Rejected Candidates
- [open_question] Time-Varying Graphs and Probabilistic Forecasts (`time-varying-graphs-probabilistic-forecasts`) - weak_evidence: The open question is broad future work proposing extensions to time-varying graphs and probabilistic forecasts without defining a concrete, specific research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.35074)
- [PDF](https://arxiv.org/pdf/2610.35074)

