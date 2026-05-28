---
# CSL-compatible fields
title: "PHGNet: Prototype-Guided Hypergraph Construction for Heterogeneous Spatiotemporal Forecasting"
author:
  - literal: "Ruiwen Gu"
  - literal: "Yahao Liu"
  - literal: "Zhenyu Liu"
  - literal: "Qitai Tan"
  - literal: "Xiao-Ping Zhang"
issued:
  date-parts:
    - [2026, 5, 25]
url: "https://arxiv.org/abs/2605.25554"

# Custom fields
paper_id: "2605.25554"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prototype-guided-hypergraph-construction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-28T08:37:50Z"
created_at: "2026-05-28T08:37:50Z"
---

# PHGNet: Prototype-Guided Hypergraph Construction for Heterogeneous Spatiotemporal Forecasting

**Authors**: Ruiwen Gu, Yahao Liu, Zhenyu Liu, Qitai Tan, Xiao-Ping Zhang
**Date**: 2026-05-25
**Paper ID**: [openalex:2605.25554](https://arxiv.org/abs/2605.25554)

## Summary

PHGNet is a spatiotemporal forecasting framework designed to address spatial heterogeneity in traffic systems by modeling high-order interactions beyond simple pairwise dependencies. The model employs a prototype learning mechanism to dynamically group pattern-similar nodes into hyperedges, alongside a global-local representation module for extracting time-consistent features. To achieve efficient and accurate predictions, it integrates iterative residual refinement and a Temporal Query Attention mechanism. Experiments on real-world traffic data show PHGNet significantly outperforms current state-of-the-art baselines.

## Key Contributions

- Proposes PHGNet, a spatiotemporal forecasting framework using prototype-guided hypergraph construction to capture high-order dynamic interactions.
- Introduces a global-local node representation module to ensure time-consistent features for robust dynamic hypergraph construction.
- Improves forecasting accuracy and parallel decoding efficiency through iterative residual refinement and Temporal Query Attention.

## Open Questions & Future Work

- [[dynamic-hypergraph-stability]]

## Key Concepts

- [[prototype-guided-hypergraph-construction]]: A method of constructing dynamic hypergraphs by assigning nodes to hyperedges based on learned representative traffic patterns.

## Archivist Review

I approved the core prototype-guided hypergraph construction mechanism as it represents a novel and reusable shift from adjacency-based to functional-similarity-based graph construction. The associated open question focuses on the stability of such dynamic structures, which is a major concern for spatiotemporal modeling. I rejected specific architectural subcomponents that are either generic optimization tactics or too tightly coupled to this specific implementation to be considered standalone research concepts.

### Approved Concepts
- Prototype-Guided Hypergraph Construction: It provides a reusable mechanism to capture high-order spatiotemporal interactions by grouping nodes based on functional similarity rather than fixed graph structures.

### Approved Open Questions
- Improving Dynamic Hypergraph Stability: Establishing stability in learned dynamic graphs is critical for the generalization and interpretability of spatiotemporal models in non-stationary environments.

### Rejected Candidates
- [concept] Global-Local Node Representation Module (`global-local-node-representation-module`) - subcomponent_of_broader_mechanism: This is an architecture-specific subcomponent that lacks evidence of general independent utility outside this specific framework.
- [concept] Iterative Residual Refinement (`iterative-residual-refinement`) - generic: Iterative refinement is a generic optimization and inference strategy common in many machine learning contexts.
- [concept] Temporal Query Attention (`temporal-query-attention`) - not_novel: Temporal attention variants are pervasive in time-series forecasting and this specific implementation is not sufficiently novel or distinct.

## Links

- [Abstract](https://arxiv.org/abs/2605.25554)
- [PDF](https://arxiv.org/pdf/2605.25554)

