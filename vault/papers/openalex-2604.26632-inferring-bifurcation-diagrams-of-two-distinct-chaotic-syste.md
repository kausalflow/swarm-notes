---
# CSL-compatible fields
title: "Inferring bifurcation diagrams of two distinct chaotic systems by a single machine"
author:
  - literal: "Jianmin Guo"
  - literal: "Yao Du"
  - literal: "Yizhen Yu"
  - literal: "Yong Zou"
  - literal: "Xingang Wang"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26632"

# Custom fields
paper_id: "2604.26632"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dual-channel-reservoir-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:56:43Z"
created_at: "2026-05-02T06:56:43Z"
---

# Inferring bifurcation diagrams of two distinct chaotic systems by a single machine

**Authors**: Jianmin Guo, Yao Du, Yizhen Yu, Yong Zou, Xingang Wang
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26632](https://arxiv.org/abs/2604.26632)

## Summary

The authors propose a dual-channel reservoir computing framework capable of learning the dynamics of multiple chaotic systems within a single model. By incorporating dedicated system-label and parameter-control channels, the reservoir can predict both short-term trajectories and long-term statistical behaviors of previously unseen system states. The method effectively reconstructs bifurcation diagrams for complex systems like the Lorenz and Rössler attractors, as well as physical circuits, from limited training data. This approach advances the capabilities of multifunctional and parameter-aware reservoir computing for nonlinear system identification.

## Key Contributions

- Proposes a dual-channel reservoir computing scheme that allows a single model to learn the dynamics of two distinct chaotic systems simultaneously.
- Demonstrates the reconstruction of full bifurcation diagrams for Lorenz, Rössler, Chua, and experimental circuits from sparse partial observations.
- Provides functional-network analysis showing distinct encoding of target systems within the reservoir dynamics.

## Open Questions & Future Work

- [[scaling-multifunctional-reservoir-computing]]

## Key Concepts

- [[dual-channel-reservoir-computing]]: A reservoir computing architecture augmented with system-label and parameter-control channels to learn and reconstruct the dynamics of multiple distinct chaotic systems.

## Archivist Review

I approved the dual-channel reservoir computing concept as it presents a distinct architectural methodology for multifunctional dynamical system identification. The open question on scaling was approved because it addresses a fundamental limitation in multifunctional RC frameworks identified by the authors as requiring future investigation. Other candidates were rejected for being either too generic or failing the strict selectivity criteria for the vault.

### Approved Concepts
- Dual-channel reservoir computing: Introduces a specific architectural augmentation to reservoir computing using system-label and parameter-control channels to enable multi-system learning.

### Approved Open Questions
- Scaling multifunctional reservoir computing: Scaling to handle multiple distinct attractors is a fundamental bottleneck for deploying resource-constrained neuromorphic hardware in complex dynamical environments.

### Rejected Candidates
- [open_question] Inference across different dimensions (`rc-heterogeneous-dimensionality-inference`) - generic: The problem of heterogeneous dimensionality is a common issue in machine learning rather than a specific open question unique to the paper's contribution.

## Links

- [Abstract](https://arxiv.org/abs/2604.26632)
- [PDF](https://arxiv.org/pdf/2604.26632)

