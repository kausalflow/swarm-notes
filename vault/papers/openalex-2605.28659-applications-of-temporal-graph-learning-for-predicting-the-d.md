---
# CSL-compatible fields
title: "Applications of temporal graph learning for predicting the dynamics of biological systems"
author:
  - literal: "Manuel Dileo"
  - literal: "Andrea Sottoriva"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28659"

# Custom fields
paper_id: "2605.28659"
paper_source: "openalex"
domain: "biology"
tags:
  - "graph-neural-network"
  - "time-series"
  - "language-model"
  - "transformer"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "pseudotime-resolved-gene-regulatory-networks"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:56Z"
created_at: "2026-05-30T07:36:56Z"
---

# Applications of temporal graph learning for predicting the dynamics of biological systems

**Authors**: Manuel Dileo, Andrea Sottoriva
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28659](https://arxiv.org/abs/2605.28659)

## Summary

This paper addresses the limitations of static biological foundation models in capturing cellular developmental dynamics by introducing a temporal graph-learning framework. By transforming single-cell transcriptomic data into a sequence of pseudotime-resolved gene regulatory networks, the method models the evolution of cellular states over time. Experiments on mouse development datasets show that this approach outperforms state-of-the-art static models in gene-expression forecasting and provides insights into regulatory dynamics through link prediction and centrality analysis.

## Key Contributions

- Introduces a framework for modeling cellular dynamics by representing pseudotime-resolved gene regulatory networks as evolving graph structures.
- Demonstrates that explicit temporal graph modeling outperforms static biological foundation models (e.g., scGPT, scFoundation) in gene-expression forecasting.
- Validates the framework's efficacy in identifying temporally important gene hubs through link prediction and centrality forecasting tasks on mouse developmental datasets.

## Open Questions & Future Work

- [[spectral-gnn-biological-regulatory-networks]]

## Key Concepts

- [[pseudotime-resolved-gene-regulatory-networks]]: A framework for representing cellular states as evolving graph structures derived from pseudotime-resolved gene regulatory networks.

## Archivist Review

The approved concept provides a novel methodological bridge between single-cell pseudotime trajectories and temporal graph learning, which is a significant architectural advancement for biological modeling. The open question identifies a specific, theoretically grounded bottleneck regarding the choice of graph convolutional mechanism (spectral vs. message-passing) in biological systems, which is a reusable research problem. Routine datasets and boilerplate future work were rejected.

### Approved Concepts
- Pseudotime-resolved Gene Regulatory Networks: It enables the conversion of static single-cell transcriptomic data into a dynamic graph structure, facilitating the application of temporal graph learning in developmental biology.

### Approved Open Questions
- Spectral GNNs for Regulatory Networks: Understanding the efficacy of spectral versus spatial GNNs for regulatory networks is critical for optimizing graph-based models in biological domains.

## Links

- [Abstract](https://arxiv.org/abs/2605.28659)
- [PDF](https://arxiv.org/pdf/2605.28659)

