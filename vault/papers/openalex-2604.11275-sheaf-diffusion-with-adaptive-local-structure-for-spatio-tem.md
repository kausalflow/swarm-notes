---
# CSL-compatible fields
title: "Sheaf Diffusion with Adaptive Local Structure for Spatio-Temporal Forecasting"
author:
  - literal: "Abeer Mostafa"
  - literal: "Raneen Younis"
  - literal: "Zahra Ahmadi"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11275"

# Custom fields
paper_id: "2604.11275"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "gnn"
  - "forecasting"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "st-sheaf-gnn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:26Z"
created_at: "2026-04-16T06:28:26Z"
---

# Sheaf Diffusion with Adaptive Local Structure for Spatio-Temporal Forecasting

**Authors**: Abeer Mostafa, Raneen Younis, Zahra Ahmadi
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11275](https://arxiv.org/abs/2604.11275)

## Summary

This paper addresses the limitations of conventional message passing in modeling complex spatio-temporal systems by reformulating forecasting as learning information flow over locally structured spaces. The authors propose the ST-Sheaf GNN, which embeds graph topology into sheaf-theoretic vector spaces connected by dynamic, learnable linear restriction maps. This approach allows the model to adapt to local spatio-temporal patterns and mitigate oversmoothing issues inherent in deep architectures. Evaluations across diverse real-world benchmarks demonstrate that this sheaf-theoretic framework achieves state-of-the-art performance for spatio-temporal graph learning.

## Key Contributions

- Introduces ST-Sheaf GNN, a novel spatio-temporal forecasting architecture that represents information flow via sheaf-theoretic vector spaces and learnable restriction maps.
- Enables dynamic adaptation of interaction patterns to local spatio-temporal structures by replacing static or globally shared transformations with evolving restriction maps.
- Achieves state-of-the-art performance on various real-world spatio-temporal forecasting benchmarks while effectively mitigating oversmoothing in deep graph neural network architectures.

## Open Questions & Future Work

- [[multi-relational-sheaf-diffusion]]

## Key Concepts

- [[st-sheaf-gnn]]: A graph neural network architecture that embeds graph topology into sheaf-theoretic vector spaces using dynamic, learned restriction maps for spatio-temporal forecasting.

## Archivist Review

I approved the core architecture (ST-Sheaf GNN) as it introduces a novel sheaf-theoretic approach to spatio-temporal GNNs that effectively addresses oversmoothing. The open question regarding multi-relational sheaves was approved because it addresses a fundamental limitation in applying these models to heterogeneous real-world graphs. No other candidates were proposed.

### Approved Concepts
- ST-Sheaf GNN: Central architectural proposal combining sheaf theory with spatio-temporal GNNs to model heterogeneous information flow.

### Approved Open Questions
- Incorporating Multi-relational Sheaves: Many real-world networks are heterogeneous (e.g., multi-modal traffic, diverse environmental sensors), and standard sheaf approaches typically assume a uniform sheaf structure across the entire graph. Enabling multi-relational sheaves is crucial for modeling such complex, real-world systems.

## Links

- [Abstract](https://arxiv.org/abs/2604.11275)
- [PDF](https://arxiv.org/pdf/2604.11275)

