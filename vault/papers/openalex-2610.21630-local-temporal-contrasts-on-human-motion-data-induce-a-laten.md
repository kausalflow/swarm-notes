---
# CSL-compatible fields
title: "Local Temporal Contrasts on Human Motion Data Induce a Latent Geometry"
author:
  - literal: "Lourenço Rodrigues"
  - literal: "Felix Putze"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21630"

# Custom fields
paper_id: "2610.21630"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "contrastive-learning"
  - "self-supervised-learning"
  - "representation-learning"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "semtac"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:30Z"
created_at: "2026-10-18T09:13:30Z"
---

# Local Temporal Contrasts on Human Motion Data Induce a Latent Geometry

**Authors**: Lourenço Rodrigues, Felix Putze
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21630](https://arxiv.org/abs/2610.21630)

## Summary

This paper proposes SemTAC, an encoder model trained with a temporal-neighborhood contrastive loss designed to preserve the trajectory geometry of time series in representation space without relying on forecasting objectives. Evaluated on a human motion sequence discrimination task, SemTAC significantly outperforms standard classification and self-supervised baselines on truncated sequences, achieving a median F1 score of 0.77 one step prior to completion. Furthermore, introduction of a displacement-smoothness metric reveals that SemTAC's representations form uniquely interpretable, temporally ordered geometric structures.

## Key Contributions

- Proposes SemTAC, an encoder trained with a temporal-neighborhood contrastive loss to recover geometric structure in representation space without forecasting objectives.
- Achieves a median F1 of 0.77 one step before sequence completion on a motion sequence discrimination task, outperforming baselines ranging from 0.27 to 0.70.
- Demonstrates through a displacement-smoothness metric that SemTAC's representation trajectories exhibit interpretable geometric structures exceeding no-structure chance baselines.

## Limitations

Evaluated primarily on motion sequence discrimination tasks with a specific focus on temporal-neighborhood contrasts.

## Open Questions & Future Work

- [[balancing-temporal-contrast-tradeoffs]]

## Key Concepts

- [[semtac]]: An encoder model trained with a temporal-neighborhood contrastive loss that induces an interpretable latent geometric structure on human motion time series.

## Archivist Review

Approved the core framework concept 'SemTAC' and its associated open question on balancing temporal contrast trade-offs, following strict selectivity criteria for time-series representation learning.

### Approved Concepts
- SemTAC: SemTAC introduces a temporal-neighborhood contrastive loss for human motion time series that preserves trajectory geometry in representation space.

### Approved Open Questions
- Balancing Temporal Contrast Trade-offs: Understanding how to balance contrastive transformation rates is critical for designing universal time-series representation models that simultaneously preserve fine-grained component details and global trajectory structures.

## Links

- [Abstract](https://arxiv.org/abs/2610.21630)
- [PDF](https://arxiv.org/pdf/2610.21630)

