---
# CSL-compatible fields
title: "Anomaly detection in smart power grids with graph-regularized MS-SVDD: a multimodal subspace learning approach"
author:
  - literal: "Thomas Debelle"
  - literal: "Fahad Sohrab"
  - literal: "Pekka Abrahamsson"
  - literal: "Moncef Gabbouj"
issued:
  date-parts:
    - [2026, 4, 24]
url: "https://arxiv.org/abs/2502.15793"

# Custom fields
paper_id: "2502.15793"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "graph-neural-network"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multimodal-subspace-support-vector-data-description"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-27T07:29:41Z"
created_at: "2026-04-27T07:29:41Z"
---

# Anomaly detection in smart power grids with graph-regularized MS-SVDD: a multimodal subspace learning approach

**Authors**: Thomas Debelle, Fahad Sohrab, Pekka Abrahamsson, Moncef Gabbouj
**Date**: 2026-04-24
**Paper ID**: [openalex:2502.15793](https://arxiv.org/abs/2502.15793)

## Summary

This paper introduces a Multimodal Subspace Support Vector Data Description (MS-SVDD) model designed to improve anomaly detection in complex smart power grid systems. The proposed framework projects heterogeneous data streams into a shared low-dimensional subspace while enforcing modality-specific structure through Laplacian graph regularization. Experimental results show that this approach significantly enhances detection robustness by better leveraging the relational and structural priors inherent in multimodal sensor data.

## Key Contributions

- Proposes a Multimodal Subspace SVDD (MS-SVDD) that projects heterogeneous modalities into a shared low-dimensional subspace.
- Integrates graph-embedded regularization to preserve modality-specific structural dependencies during subspace learning.
- Demonstrates superior robustness in anomaly detection for smart power grid event streams compared to standard SVDD-based approaches.

## Open Questions & Future Work

- [[real-time-scalability-of-multimodal-anomaly-detection]]

## Key Concepts

- [[multimodal-subspace-support-vector-data-description]]: A generalized SVDD framework that projects multiple modalities into a shared subspace while preserving structure via Laplacian regularizers.

## Archivist Review

I approved the core MS-SVDD concept as it presents a distinct, reusable approach to incorporating structural graph priors into subspace-based anomaly detection. The open question was narrowed to focus on the broader challenge of real-time scalability in multimodal anomaly detection, as this is a fundamental bottleneck for deploying such methods in critical infrastructure. No datasets were approved as none were provided or identified as unique, persistent benchmarks.

### Approved Concepts
- Multimodal Subspace Support Vector Data Description (MS-SVDD): Combines multimodal subspace projection with graph-embedded regularization for robust one-class classification, a useful pattern for high-dimensional sensor data.

### Approved Open Questions
- Real-time scalability of MS-SVDD: Addresses the critical gap between proposed algorithmic robustness and practical, real-world deployment requirements for infrastructure-critical monitoring systems.

## Links

- [Abstract](https://arxiv.org/abs/2502.15793)
- [PDF](https://arxiv.org/pdf/2502.15793)

