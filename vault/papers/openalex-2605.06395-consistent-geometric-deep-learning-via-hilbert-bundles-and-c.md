---
# CSL-compatible fields
title: "Consistent Geometric Deep Learning via Hilbert Bundles and Cellular Sheaves"
author:
  - literal: "Kartik Tandon"
  - literal: "Julian Gould"
  - literal: "Tanishq Bhatia"
  - literal: "Francesca Dominici"
  - literal: "Alejandro Ribeiro"
  - literal: "Claudio Battiloro"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06395"

# Custom fields
paper_id: "2605.06395"
paper_source: "openalex"
domain: "nlp"
tags:
  - "graph-neural-network"
  - "geometric-deep-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hilbnets"
  - "hilbert-cellular-sheaf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:22Z"
created_at: "2026-05-10T07:23:22Z"
---

# Consistent Geometric Deep Learning via Hilbert Bundles and Cellular Sheaves

**Authors**: Kartik Tandon, Julian Gould, Tanishq Bhatia, Francesca Dominici, Alejandro Ribeiro, Claudio Battiloro
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06395](https://arxiv.org/abs/2605.06395)

## Summary

This paper addresses the need for a unified learning theory for infinite-dimensional signals on irregular domains by proposing HilbNets, a novel convolutional framework based on Hilbert bundles. By mapping manifold signals to Hilbert Cellular Sheaves, the authors provide a principled discretization strategy that preserves consistency with continuous operator-based learning. The approach formally generalizes the convergence of graph Laplacians to the manifold Laplacian, ensuring that learned filters are transferable across varying sampling densities.

## Key Contributions

- Introduced HilbNets, a convolutional learning framework for infinite-dimensional signals on manifolds using connection Laplacians.
- Proved that sampling a manifold induces a Hilbert Cellular Sheaf whose Laplacian converges in probability to the connection Laplacian.
- Established consistency and transferability results for discretized HilbNets across different manifold samplings.

## Open Questions & Future Work

- [[convergence-infinite-dimensional-bundle-laplacian]]

## Key Concepts

- [[hilbnets]]: A convolutional learning framework for infinite-dimensional signals supported on a manifold using Hilbert bundle connection Laplacians.
- [[hilbert-cellular-sheaf]]: A generalized graph structure that maps Hilbert feature spaces to nodes and defines coupling rules over edges to approximate connection Laplacians.

## Archivist Review

I approved the central architecture 'HilbNets' and its foundational mathematical structure 'Hilbert Cellular Sheaf', as these represent a novel approach to geometric deep learning on infinite-dimensional signals. I also approved the open question regarding the convergence of these operators, as it addresses a fundamental theoretical limitation in current geometric learning research. No datasets were approved as none were central to the paper's claimed contributions.

### Approved Concepts
- HilbNets: HilbNets provide a principled convolutional framework for infinite-dimensional signals on manifolds by leveraging connection Laplacians.
- Hilbert Cellular Sheaf: This structure serves as the essential theoretical link between continuous manifold-based signal processing and implementable discrete graph operations.

### Approved Open Questions
- Convergence of Infinite-Dimensional Bundle Laplacians: This is a critical theoretical bottleneck for ensuring that geometric deep learning architectures remain consistent and transferable when signals live in infinite-dimensional spaces.

## Links

- [Abstract](https://arxiv.org/abs/2605.06395)
- [PDF](https://arxiv.org/pdf/2605.06395)

