---
# CSL-compatible fields
title: "Orthogonal JEPA: Factorized Predictive States for Latent World Models"
author:
  - literal: "Taoyong Cui"
  - literal: "Pheng Ann Heng"
  - literal: "Wanli Ouyang"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20065"

# Custom fields
paper_id: "2608.20065"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "self-supervised-learning"
  - "multimodal"
  - "representation-learning"
  - "planning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "orthogonal-jepa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:20:15Z"
created_at: "2026-08-23T05:20:15Z"
---

# Orthogonal JEPA: Factorized Predictive States for Latent World Models

**Authors**: Taoyong Cui, Pheng Ann Heng, Wanli Ouyang
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20065](https://arxiv.org/abs/2608.20065)

## Summary

World models built on Joint-Embedding Predictive Architectures (JEPAs) typically rely on a single monolithic representation, which can cause dominant signals to overshadow weaker predictive structures. To overcome this limitation, the authors introduce Orthogonal JEPA, a framework that factorizes latent states into orthogonal predictive components using learned basis matrices and dedicated prediction pathways. The approach uses specialized regularization objectives—including orthogonality, factor activity, and variance regularization—to prevent collapse and ensure diverse component capture. Experiments across vision, biological, medical, and control benchmarks show enhanced representation quality, forecasting accuracy, and long-horizon stability.

## Key Contributions

- Introduced Orthogonal JEPA (Orthogonal-JEPA), a latent world-modeling framework that uses orthogonal predictive factorization to decompose target states into multiple components via learned basis matrices and dedicated prediction branches.
- Proposed an objective incorporating predictive regression, orthogonality objectives to discourage repeated directions, factor-activity regularization, and online variance regularization to prevent encoder collapse.
- Demonstrated across controlled vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics that factorized predictive states improve representation quality, forecasting, planning, and long-horizon stability compared to monolithic JEPAs.

## Open Questions & Future Work

- [[stochastic-multimodal-world-models]]

## Key Concepts

- [[orthogonal-jepa]]: A latent world-modeling framework that factorizes target states into orthogonal predictive components using learned basis matrices and dedicated prediction branches.

## Archivist Review

Approved the core framework concept 'Orthogonal JEPA' as a novel architectural contribution to joint-embedding predictive architectures, along with an open question on extending factorized latent world models to stochastic and multimodal futures. Adhered strictly to the scarcity and quality guidelines.

### Approved Concepts
- Orthogonal JEPA: Provides a reusable mechanism for factorizing latent state predictions in joint-embedding predictive architectures via orthogonal basis matrices, overcoming monolithic representation collapse.

### Approved Open Questions
- Stochastic and Multimodal World Models: Enables joint-embedding predictive architectures to handle uncertainty and multimodal distributions over future states in complex world-modeling environments.

## Links

- [Abstract](https://arxiv.org/abs/2608.20065)
- [PDF](https://arxiv.org/pdf/2608.20065)

