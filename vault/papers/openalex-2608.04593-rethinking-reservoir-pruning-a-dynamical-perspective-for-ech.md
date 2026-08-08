---
# CSL-compatible fields
title: "Rethinking Reservoir Pruning: A Dynamical Perspective for Echo State Networks"
author:
  - literal: "Sudip Laudari"
  - literal: "Puspa Raj Adhikari"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04593"

# Custom fields
paper_id: "2608.04593"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "model-compression"
  - "pruning"
  - "recurrent-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamical-mode-pruning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:56Z"
created_at: "2026-08-08T05:34:56Z"
---

# Rethinking Reservoir Pruning: A Dynamical Perspective for Echo State Networks

**Authors**: Sudip Laudari, Puspa Raj Adhikari
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04593](https://arxiv.org/abs/2608.04593)

## Summary

Echo State Networks often suffer from over-parameterization and dynamic redundancy in their randomly initialized reservoirs. To address this, the authors propose Dynamical Mode Pruning (DMP), a pruning technique that ranks reservoir neurons by their contribution to dominant transition modes derived from a trajectory-averaged Jacobian Gramian. Experiments on chaotic and real-world time-series forecasting demonstrate that DMP effectively removes redundant components while preserving or improving predictive accuracy.

## Key Contributions

- Proposes Dynamical Mode Pruning (DMP), a novel pruning framework for Echo State Networks based on trajectory-averaged Jacobian Gramians.
- Ranks reservoir neurons by their contribution to dominant input-driven state transition modes rather than static connectivity or activation statistics.
- Demonstrates on chaotic and real-world time-series benchmarks that DMP maintains or improves forecasting accuracy while removing redundant reservoir components.

## Open Questions & Future Work

- [[scalable-dynamic-reservoir-pruning]]

## Key Concepts

- [[dynamical-mode-pruning]]: A reservoir pruning method for Echo State Networks that ranks neurons by their contribution to dominant transition modes from a trajectory-averaged Jacobian Gramian.

## Archivist Review

Approved the central concept of Dynamical Mode Pruning and the key computational open question on scalability. Rejected routine future work extensions.

### Approved Concepts
- Dynamical Mode Pruning: Introduces a principled pruning criterion for Echo State Networks based on dynamical systems theory rather than static activation statistics.

### Approved Open Questions
- Scalable Dynamic Reservoir Pruning: The cubic computational complexity with respect to reservoir size poses a significant bottleneck for scaling dynamical pruning methods to very large recurrent neural networks.

### Rejected Candidates
- [open_question] Multivariate and Task-Specific ESN Pruning (`multivariate-temporal-task-extension`) - weak_evidence: Standard boilerplate future work proposing extensions to new task types without a specific algorithmic mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.04593)
- [PDF](https://arxiv.org/pdf/2608.04593)

