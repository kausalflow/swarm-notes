---
# CSL-compatible fields
title: "Predicting Dynamics of Ultra-Large Complex Systems by Inferring Governing Equations"
author:
  - literal: "Qi Shao"
  - literal: "Duxin Chen"
  - literal: "Jiawen Chen"
  - literal: "Yujie Zeng"
  - literal: "Athen Ma"
  - literal: "Wenwu Yu"
  - literal: "Vito Latora"
  - literal: "Wei Lin"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00599"

# Custom fields
paper_id: "2604.00599"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
  - "interpretability"
architectures:
  - "graph-neural-network"
datasets:
  []
concept_slugs:
  - "sparse-identification-graph-neural-network-sign"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:50:32Z"
created_at: "2026-04-04T05:50:32Z"
---

# Predicting Dynamics of Ultra-Large Complex Systems by Inferring Governing Equations

**Authors**: Qi Shao, Duxin Chen, Jiawen Chen, Yujie Zeng, Athen Ma, Wenwu Yu, Vito Latora, Wei Lin
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00599](https://arxiv.org/abs/2604.00599)

## Summary

The paper addresses the fundamental trade-off in complex system modeling between interpretable equation discovery and scalable black-box neural networks. The authors propose the Sparse Identification Graph Neural Network (SIGN), which decouples symbolic discovery from network size by processing dynamics at the edge level. This approach enables the recovery of governing equations in systems with over 100,000 nodes, outperforming traditional discovery methods in scalability and robustness. Practical evaluation on climate data demonstrates the ability to identify compact predictive models for sea surface temperatures over long-term horizons.

## Key Contributions

- Introduces SIGN, a GNN framework that enables scalable symbolic equation discovery by reformulating identification as an edge-level task.
- Demonstrates robust performance on networks with over 100,000 nodes, maintaining accuracy under conditions of noise, sparse sampling, and missing data.
- Successfully recovers governing equations and provides long-term forecasting for large-scale sea surface temperature dynamics (71,987 nodes) up to two years ahead.

## Open Questions & Future Work

- [[modeling-complex-interaction-structures]]
- [[multi-channel-state-discovery]]

## Key Concepts

- [[sparse-identification-graph-neural-network-sign]]: A GNN-based framework that enables interpretable, scalable governing equation discovery for ultra-large complex networks by formulating symbolic discovery at the edge level.

## Archivist Review

I approved the primary contribution (SIGN) as it offers a novel approach to scaling symbolic equation discovery for graph-structured time series. I also approved two research directions that address key limitations of current equation discovery frameworks regarding interaction complexity and multi-channel state representations. These additions are valuable for the long-term track of interpretable dynamical system modeling.

### Approved Concepts
- Sparse Identification Graph Neural Network (SIGN): Addresses the trade-off between equation-discovery interpretability and scalability by moving symbolic discovery to the edge-level.

### Approved Open Questions
- Modeling complex interaction structures: Current frameworks are primarily limited to pairwise interactions; generalizing to higher-order dependencies is crucial for modeling many real-world complex systems accurately.
- Multi-channel dynamical system discovery: Standard symbolic identification often assumes simple state representations; extending to multi-channel systems is required for high-fidelity modeling.

## Links

- [Abstract](https://arxiv.org/abs/2604.00599)
- [PDF](https://arxiv.org/pdf/2604.00599)

