---
# CSL-compatible fields
title: "A Capacity-Aware Parr Model for Agile Projects"
author:
  - literal: "Pedro E. Colla"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01562"

# Custom fields
paper_id: "2607.01562"
paper_source: "openalex"
domain: "nlp"
tags:
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "capacity-aware-parr-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:58Z"
created_at: "2026-07-05T07:52:58Z"
---

# A Capacity-Aware Parr Model for Agile Projects

**Authors**: Pedro E. Colla
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01562](https://arxiv.org/abs/2607.01562)

## Summary

This paper addresses the limitations of applying classical effort distribution models, like the Parr curve, to agile software development environments where team capacity is strictly constrained. The author introduces a capacity-aware refactoring of the Parr model that combines a normalized latent effort demand with explicit capacity trajectories. This approach allows project managers to forecast completion times and identify capacity deficits or slack without assuming fixed activity paths. The framework includes a discrete sprint formulation and a calibration methodology validated against conventional management baselines.

## Key Contributions

- Proposes a capacity-aware refactoring of the Parr model to bridge the gap between classical effort distribution curves and real-world resource constraints.
- Enables forecasting of aggregate project progress, completion time, and capacity metrics (deficit/slack) using a compact parameter set (total effort, shape, origin constant, and capacity trajectory).
- Provides a discrete sprint formulation and a calibration method compatible with standard Scrum team data for practical project management.

## Open Questions & Future Work

- [[path-invariance-capacity-constraint-impact]]

## Key Concepts

- [[capacity-aware-parr-model]]: A refactored effort distribution model that treats latent effort demand as a driver modulated by explicit capacity trajectories.

## Archivist Review

The paper contributes a specialized, reusable forecasting approach for project management by refactoring classical curves to include external capacity constraints. The approved concept captures this methodology, while the approved open question identifies a meaningful theoretical gap regarding the validity of such decoupling. I have otherwise adhered to the scarcity mandate and avoided adding generic dataset or benchmark candidates.

### Approved Concepts
- Capacity-Aware Parr Model: It adapts classical effort distribution theory to modern resource-constrained agile environments, providing a formal bridge between theoretical effort curves and empirical capacity trajectories.

### Approved Open Questions
- Path Invariance Under Capacity Constraints: This addresses the theoretical limitations of decoupling latent effort from operational execution under resource scarcity.

## Links

- [Abstract](https://arxiv.org/abs/2607.01562)
- [PDF](https://arxiv.org/pdf/2607.01562)

