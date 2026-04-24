---
# CSL-compatible fields
title: "Graph Signal Generative Diffusion Models"
author:
  - literal: "Yiğit Berkay Uslu"
  - literal: "Samar Hadou"
  - literal: "Sergio Rozada"
  - literal: "Shirin Saeedi Bidokhti"
  - literal: "Alejandro Ribeiro"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.17250"

# Custom fields
paper_id: "2509.17250"
paper_source: "openalex"
domain: "graph-learning"
tags:
  - "graph-neural-network"
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "u-shaped-encoder-decoder-graph-neural-networks-u-gnns"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:50Z"
created_at: "2026-04-24T07:00:50Z"
---

# Graph Signal Generative Diffusion Models

**Authors**: Yiğit Berkay Uslu, Samar Hadou, Sergio Rozada, Shirin Saeedi Bidokhti, Alejandro Ribeiro
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.17250](https://arxiv.org/abs/2509.17250)

## Summary

The paper introduces U-shaped encoder-decoder graph neural networks (U-GNNs) for generating graph signals via denoising diffusion. By utilizing a zero-padding-based pooling mechanism, the architecture avoids lossy graph coarsening and preserves convolutional structure across multiple resolutions. The model is specifically evaluated for its ability to produce probabilistic forecasts, effectively capturing uncertainty and tail risk in stock price dynamics.

## Key Contributions

- Introduces U-GNNs, a multi-resolution graph neural network architecture utilizing zero-padded pooling to maintain convolutional alignment with the original graph.
- Demonstrates the efficacy of applying denoising diffusion processes to graph signal generation for probabilistic forecasting tasks.
- Outperforms deterministic forecasting models by capturing uncertainty and tail events in stock price prediction scenarios.

## Open Questions & Future Work

- [[ugnn-architectural-generalization-and-optimization]]

## Key Concepts

- [[u-shaped-encoder-decoder-graph-neural-networks-u-gnns]]: A multi-resolution graph neural network architecture that employs zero-padding-based pooling to maintain convolutional structure across resolutions without explicit graph coarsening.

## Archivist Review

The paper is approved for the novel U-GNN architecture which specifically addresses the limitation of lossy graph coarsening in multi-resolution graph neural networks via a zero-padding mechanism. The open question regarding its generalization and scaling is tracked as it highlights a clear technical bottleneck in applying U-Net principles to arbitrary graph structures. All other candidates were rejected as they were either too generic or effectively described by the approved concept.

### Approved Concepts
- U-shaped encoder-decoder graph neural networks (U-GNNs): It introduces a U-Net-like multi-resolution learning mechanism for graph data that circumvents the need for lossy graph coarsening by using a zero-padding strategy.

### Approved Open Questions
- Generalizing U-GNN for Graph Diffusion: Establishing robust architectures for graph-based diffusion is critical for moving beyond task-specific implementations and enabling scalability.

### Rejected Candidates
- [concept] Graph Signal Generative Diffusion Models (`graph-neural-network-diffusion-generation`) - generic: This is a generic description of the paper topic rather than a specific method or concept.

## Links

- [Abstract](https://arxiv.org/abs/2509.17250)
- [PDF](https://arxiv.org/pdf/2509.17250)

