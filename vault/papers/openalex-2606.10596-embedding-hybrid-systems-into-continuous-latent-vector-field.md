---
# CSL-compatible fields
title: "Embedding Hybrid Systems into Continuous Latent Vector Fields"
author:
  - literal: "Sangli Teng"
  - literal: "Hang Liu"
  - literal: "Koushil Sreenath"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10596"

# Custom fields
paper_id: "2606.10596"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hybrid-system-embedding-theorem"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:54:23Z"
created_at: "2026-06-12T08:54:23Z"
---

# Embedding Hybrid Systems into Continuous Latent Vector Fields

**Authors**: Sangli Teng, Hang Liu, Koushil Sreenath
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10596](https://arxiv.org/abs/2606.10596)

## Summary

This paper provides a theoretical proof that discontinuous hybrid systems can be embedded into continuous vector fields within higher-dimensional Euclidean spaces when the target dimension exceeds twice the original system's dimension. Leveraging this result, the authors introduce a latent Neural ODE architecture that enforces consistency across both latent and state spaces to learn hybrid dynamics. Experiments on complex hybrid geometries show that this approach achieves superior performance compared to existing data-driven methods for hybrid system identification.

## Key Contributions

- Established a theoretical embedding theorem proving that n-dimensional hybrid systems can be represented as continuous vector fields in m > 2n dimensional Euclidean space.
- Proposed a latent Neural ODE framework with cross-space consistency losses for learning the flow of hybrid systems from time-series data.
- Demonstrated that the method outperforms existing hybrid system learning approaches across various geometries in experimental evaluations.

## Open Questions & Future Work

- [[continuous-latent-embedding-limitations]]

## Key Concepts

- [[hybrid-system-embedding-theorem]]: A mathematical result establishing that n-dimensional hybrid systems can be embedded into m-dimensional Euclidean space (m > 2n) as continuous vector fields.

## Archivist Review

The paper proposes a theoretical bridge between discontinuous hybrid systems and continuous vector fields. I have approved the embedding theorem as a foundational concept and the open question regarding its geometric constraints as a significant research direction. No datasets were approved as none were central, reusable, or explicitly named benchmarks in the provided analysis.

### Approved Concepts
- Hybrid System Embedding Theorem: Provides a theoretical foundation for representing discontinuous hybrid dynamics as continuous vector fields, enabling the use of standard differentiable optimization tools.

### Approved Open Questions
- Refining continuous latent embeddings: Establishing the robustness of the latent embedding across the full range of dimensions (including the critical m=2n case) and for more complex, piecewise-defined guard geometries is essential for the practical applicability of these models.

## Links

- [Abstract](https://arxiv.org/abs/2606.10596)
- [PDF](https://arxiv.org/pdf/2606.10596)

