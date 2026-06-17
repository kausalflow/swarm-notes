---
# CSL-compatible fields
title: "Phys-JEPA: Physics-Informed Latent World Models for Multivariate Time-Series Forecasting"
author:
  - literal: "Weizhi Nie"
  - literal: "Weichao Liu"
  - literal: "Honglin Guo"
  - literal: "Yuting Su"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2606.16076"

# Custom fields
paper_id: "2606.16076"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "world-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "phys-jepa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:02Z"
created_at: "2026-06-17T09:25:02Z"
---

# Phys-JEPA: Physics-Informed Latent World Models for Multivariate Time-Series Forecasting

**Authors**: Weizhi Nie, Weichao Liu, Honglin Guo, Yuting Su
**Date**: 2026-06-15
**Paper ID**: [openalex:2606.16076](https://arxiv.org/abs/2606.16076)

## Summary

Phys-JEPA is a novel joint-embedding predictive architecture that improves multivariate time-series forecasting by integrating physical constraints directly into the latent world model. By decomposing predictive states into physical and residual components, the model ensures that latent state evolution respects underlying scientific principles. Empirical evaluations on climate, traffic, and electricity benchmarks demonstrate that this latent-level physical grounding outperforms traditional output-constrained approaches in both interpretability and predictive accuracy.

## Key Contributions

- Introduced Phys-JEPA, which decomposes latent states into physical and residual components to enforce physics-informed constraints within the representation space.
- Demonstrated that enforcing physical consistency on latent transitions improves long-term forecasting accuracy on Jena Climate, Traffic, and Electricity datasets compared to output-only physics-informed models.
- Reduced H=192 MSE on the Traffic dataset from 0.800784 to 0.773873 by improving structural representation of dynamics.

## Open Questions & Future Work

- [[phys-jepa-strong-constraints-evaluation]]

## Key Concepts

- [[phys-jepa]]: A joint-embedding predictive architecture for multivariate time-series forecasting that enforces physical consistency directly on latent states and transitions.

## Archivist Review

I approved the core architectural concept, Phys-JEPA, as it represents a significant, reusable shift in designing world models by embedding physical constraints in the latent space rather than the output space. The open question was refined to focus on the scalability of this latent grounding to scenarios with explicit, known physical laws, which is a major, unresolved research direction in this field. I did not approve the datasets because they are standard, common benchmarks in the existing time-series literature.

### Approved Concepts
- Phys-JEPA: Moves physics-informed constraints from the output space to the latent predictive state space, enabling structured physical evolution in world models.

### Approved Open Questions
- Phys-JEPA under explicit constraints: Determining whether latent-level physical grounding scales to rigorous law-based systems is critical for verifying the generality of this approach.

## Links

- [Abstract](https://arxiv.org/abs/2606.16076)
- [PDF](https://arxiv.org/pdf/2606.16076)

