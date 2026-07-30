---
# CSL-compatible fields
title: "Tree Tensor Network Reservoir Computing: Hierarchical Ensemble with Invariant Phase Boundaries"
author:
  - literal: "Daiki Sasaki"
  - literal: "Chih-Chieh Chen"
  - literal: "Tomah Sogabe"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24127"

# Custom fields
paper_id: "2607.24127"
paper_source: "openalex"
domain: "time-series"
tags:
  - "reservoir-computing"
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tree-tensor-network-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:27:04Z"
created_at: "2026-07-30T07:27:04Z"
---

# Tree Tensor Network Reservoir Computing: Hierarchical Ensemble with Invariant Phase Boundaries

**Authors**: Daiki Sasaki, Chih-Chieh Chen, Tomah Sogabe
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24127](https://arxiv.org/abs/2607.24127)

## Summary

The authors propose Tree Tensor Network Reservoir Computing (TTN-RC), a quantum-inspired reservoir framework that uses hierarchical Tree Tensor Networks for time-series prediction. To mitigate exponential concentration or divergence, they introduce a hierarchical ensemble method that partitions reservoirs into independent sub-reservoirs. Theoretical analyses using the reservoir Jacobian and mean-field statistics establish an asymptotic stability boundary at $\sigma_T=\sqrt{2}$ in the large per-tree-size limit.

## Key Contributions

- Proposed Tree Tensor Network Reservoir Computing (TTN-RC), a quantum-inspired reservoir computing framework leveraging hierarchical Tree Tensor Network topologies.
- Introduced a hierarchical ensemble method partitioning fixed-size reservoirs to control exponential concentration or divergence of outputs.
- Derived an expected contraction rate and mean-field description identifying an asymptotic stability boundary at $\sigma_T=\sqrt{2}$.

## Open Questions & Future Work

- [[tensor-network-structure-comparison]]

## Key Concepts

- [[tree-tensor-network-reservoir-computing]]: A quantum-inspired reservoir computing framework leveraging the hierarchical structure of Tree Tensor Networks for time-series prediction.

## Archivist Review

Approved the central quantum-inspired reservoir architecture concept and its specific comparative tensor network open question, while maintaining strict adherence to vault scarcity and quality criteria.

### Approved Concepts
- Tree Tensor Network Reservoir Computing: Introduces a novel quantum-inspired reservoir computing architecture based on tree tensor networks for time-series prediction with hierarchical ensemble stabilization.

### Approved Open Questions
- Comparative Analysis of Tensor Network Structures: Crucial for understanding the inductive biases and computational trade-offs of different tensor network topologies in reservoir computing.

## Links

- [Abstract](https://arxiv.org/abs/2607.24127)
- [PDF](https://arxiv.org/pdf/2607.24127)

