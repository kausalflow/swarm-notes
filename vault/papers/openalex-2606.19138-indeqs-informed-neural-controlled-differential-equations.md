---
# CSL-compatible fields
title: "INDEQS: Informed Neural controlled Differential EQuationS"
author:
  - literal: "Michael Detzel"
  - literal: "Gabriel Nobis"
  - literal: "Kristiyan Blagov"
  - literal: "Juri Schubert"
  - literal: "J Y"
  - literal: "Wojciech Samek"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.19138"

# Custom fields
paper_id: "2606.19138"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "gnn"
architectures:
  []
datasets:
  []
concept_slugs:
  - "indeqs-informed-neural-controlled-differential-equations"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:18:08Z"
created_at: "2026-06-20T08:18:08Z"
---

# INDEQS: Informed Neural controlled Differential EQuationS

**Authors**: Michael Detzel, Gabriel Nobis, Kristiyan Blagov, Juri Schubert, J Y, Wojciech Samek
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.19138](https://arxiv.org/abs/2606.19138)

## Summary

INDEQS is a graph-based Neural Controlled Differential Equation (NCDE) framework designed to incorporate known directed graph structures into the forecasting process. By separating the mixing of hidden states across nodes from the interactions between vector fields and control inputs, the model achieves better performance through targeted structural informedness. The authors validate this approach using a novel synthetic advection simulation and real-world hydrological and traffic datasets, showing significant improvements over standard uninformed NCDEs.

## Key Contributions

- Introduces INDEQS, a framework that integrates known directed graph structures into NCDEs at distinct inner and outer architectural positions.
- Develops a continuous advection simulation to generate synthetic spatio-temporal datasets with ground-truth flow for systematic evaluation of graph informedness.
- Demonstrates that incorporating outer informedness consistently improves Mean Absolute Error in hydrological and traffic forecasting benchmarks compared to uninformed NCDEs.
- Shows that continuous-time decoders outperform discrete convolutional counterparts in both accuracy and temporal flexibility for spatio-temporal prediction.

## Open Questions & Future Work

- [[optimal-integration-of-prior-versus-learned-graph-structure]]

## Key Concepts

- [[indeqs-informed-neural-controlled-differential-equations]]: A graph-based NCDE forecasting framework that embeds known directed graph topologies at 'inner' (state mixing) or 'outer' (vector field/control interaction) architectural positions.

## Archivist Review

The INDEQS framework is approved for its novel and modular architectural approach to injecting structural priors into NCDEs, which is a reusable concept in the spatiotemporal forecasting domain. The open question regarding the trade-off between structural priors and learned graph dependencies captures a significant unresolved bottleneck in graph-neural-operator research. Other candidates were rejected because they were either subcomponents or local synthetic evaluation artifacts.

### Approved Concepts
- Informed Neural controlled Differential EQuationS (INDEQS): It provides a principled way to integrate known directed graph structures into continuous-time NCDE forecasting, moving beyond black-box graph learning.

### Approved Open Questions
- Prior vs Learned Graph Integration: Determining the utility of structural informedness is critical for building reliable, physically-consistent digital twins in complex networks.

### Rejected Candidates
- [dataset] Continuous Advection Simulation Dataset (`continuous-advection-simulation-dataset`) - paper_local: The dataset is synthetic and serves as a local evaluation tool rather than a standard reusable community benchmark.

## Links

- [Abstract](https://arxiv.org/abs/2606.19138)
- [PDF](https://arxiv.org/pdf/2606.19138)

