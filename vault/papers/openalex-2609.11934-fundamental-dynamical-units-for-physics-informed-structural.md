---
# CSL-compatible fields
title: "Fundamental dynamical units for physics-informed structural inference from perturbation time-series in networked systems"
author:
  - literal: "Nima Nouri"
issued:
  date-parts:
    - [2026, 10, 3]
url: "https://arxiv.org/abs/2609.11934"

# Custom fields
paper_id: "2609.11934"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
  - "physics-informed-neural-networks"
  - "ordinary-differential-equations"
  - "causal-inference"
  - "dynamical-systems"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fundamental-dynamical-units"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:48:53Z"
created_at: "2026-10-04T10:48:53Z"
---

# Fundamental dynamical units for physics-informed structural inference from perturbation time-series in networked systems

**Authors**: Nima Nouri
**Date**: 2026-10-03
**Paper ID**: [openalex:2609.11934](https://arxiv.org/abs/2609.11934)

## Summary

This paper addresses the challenge of recovering signed interaction structures from perturbation time-series in networked dynamical systems by introducing Fundamental Dynamical Units (FDUs), which are signed three-node interaction patterns acting as composable primitives. By leveraging local interaction structures to guide intervention design and embedding FDU regularization within physics-informed neural ordinary differential equations, the framework achieves joint recovery of network interaction structures and trajectories. Validated on synthetic benchmarks, the approach provides a principled and mechanistically interpretable solution for structural inference.

## Key Contributions

- Introduces Fundamental Dynamical Units (FDUs) as signed three-node interaction patterns to transform combinatorial interaction hypothesis spaces into tractable constructive representations.
- Demonstrates that local interaction structure dictates required perturbation conditions for distinguishing direct from relayed influence, enabling motif-prescribed intervention design.
- Embeds FDU-regularized structural inference within a physics-informed neural ordinary differential equation framework for joint recovery of interaction structure and perturbation-resolved trajectories.

## Limitations

Validated exclusively on synthetic benchmarks with known ground truth.

## Open Questions & Future Work

- [[robustness-and-joint-estimation-in-fdu-inference-from-noisy-data]]

## Key Concepts

- [[fundamental-dynamical-units]]: Signed three-node interaction patterns serving as composable primitives for tractable structural inference in networked dynamical systems.

## Archivist Review

Approved the core conceptual innovation of Fundamental Dynamical Units (FDUs) and the specific open question concerning joint parameter estimation and noise robustness in networked dynamical systems. Both items are well-defined, highly relevant to physics-informed structural inference, and avoid generic terminology.

### Approved Concepts
- Fundamental Dynamical Units: Introduces a novel reductionist primitive (signed three-node interaction patterns) for tractably representing and inferring networked interaction structures from perturbation time-series.

### Approved Open Questions
- Robustness and Joint Parameter Estimation: Real-world applications involve noisy, irregularly sampled data and unknown kinetic parameters, making joint parameter estimation and noise robustness critical next steps for practical deployment.

## Links

- [Abstract](https://arxiv.org/abs/2609.11934)
- [PDF](https://arxiv.org/pdf/2609.11934)

