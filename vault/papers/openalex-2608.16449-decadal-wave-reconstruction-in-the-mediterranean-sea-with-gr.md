---
# CSL-compatible fields
title: "Decadal wave reconstruction in the Mediterranean Sea with graph neural networks"
author:
  - literal: "Federica Benassi"
  - literal: "Lorenzo Mentaschi"
  - literal: "Salvatore Causio"
  - literal: "Daniel Holmberg"
  - literal: "Iván Federico"
  - literal: "Nadia Pinardi"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16449"

# Custom fields
paper_id: "2608.16449"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "gnn"
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "wavegraph"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:21:48Z"
created_at: "2026-08-20T05:21:48Z"
---

# Decadal wave reconstruction in the Mediterranean Sea with graph neural networks

**Authors**: Federica Benassi, Lorenzo Mentaschi, Salvatore Causio, Daniel Holmberg, Iván Federico, Nadia Pinardi
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16449](https://arxiv.org/abs/2608.16449)

## Summary

This paper introduces WaveGraph, a graph neural network-based model designed to emulate basin-scale ocean wave dynamics on unstructured meshes with high coastal resolution. Trained on the Mediterranean Sea, the multiscale architecture combines unstructured model meshes and uniform graphs to capture both local coastal interactions and large-scale dynamics. The model achieves continuous autoregressive wave reconstruction over a 17-year period without drift or reinitialization, exhibiting skill comparable to observational data.

## Key Contributions

- WaveGraph emulates basin-scale ocean wave dynamics directly on unstructured meshes with high coastal resolution using a multiscale graph neural network architecture.
- Demonstrates autoregressive continuous decadal reconstruction (17-year period) of significant wave height, mean period, and mean direction without reinitialization or drift.
- Ablation experiments reveal that wind forcing drives long-term stability while wave history improves swell-driven and basin-scale dynamics.

## Key Concepts

- [[wavegraph]]: A graph neural network-based model for emulating basin-scale wave dynamics on unstructured meshes over decadal horizons.

## Archivist Review

Applied strict selectivity standards, approving only the core model concept 'WaveGraph' for unstructured graph-based ocean modeling while rejecting any redundant or paper-local subcomponents. No open questions or datasets met the rigorous bar for standalone vault notes.

### Approved Concepts
- WaveGraph: Introduces a graph neural network model specifically designed for emulating decadal basin-scale wave dynamics on unstructured meshes.

## Links

- [Abstract](https://arxiv.org/abs/2608.16449)
- [PDF](https://arxiv.org/pdf/2608.16449)

