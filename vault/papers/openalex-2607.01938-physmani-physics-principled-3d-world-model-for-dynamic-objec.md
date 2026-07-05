---
# CSL-compatible fields
title: "PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation"
author:
  - literal: "Peng Yun"
  - literal: "Shouwang Huang"
  - literal: "Hao Li"
  - literal: "Jinxi Li"
  - literal: "Jianan Wang"
  - literal: "B Yang"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01938"

# Custom fields
paper_id: "2607.01938"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "autonomous-agent"
  - "robotics"
  - "benchmark"
architectures:
  []
datasets:
  - "physmani-bench"
concept_slugs:
  - "divergence-free-gaussian-velocity-field"
dataset_slugs:
  - "physmani-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:53:17Z"
created_at: "2026-07-05T07:53:17Z"
---

# PhysMani: Physics-principled 3D World Model for Dynamic Object Manipulation

**Authors**: Peng Yun, Shouwang Huang, Hao Li, Jinxi Li, Jianan Wang, B Yang
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01938](https://arxiv.org/abs/2607.01938)

## Summary

PhysMani is a framework designed for dynamic object manipulation in unstructured 3D environments, addressing the geometric and physical limitations of existing visual-language-action models. The framework combines a physics-principled 3D Gaussian world model, which utilizes a divergence-free velocity field for grounded dynamic predictions, with a future-aware action policy. Evaluations on the newly introduced PhysMani-Bench demonstrate significant improvements in manipulation success rates compared to existing state-of-the-art baselines.

## Key Contributions

- Introduces PhysMani, a 3D world model that couples a divergence-free Gaussian velocity field with a future-aware action policy.
- Achieves superior success rates in dynamic target manipulation across 16 tasks in both simulation and real-world robot experiments.
- Presents PhysMani-Bench, a new dynamic manipulation benchmark with 16 tasks for evaluating embodied AI under unstructured conditions.

## Open Questions & Future Work

- [[scaling-dynamic-manipulation-benchmarks]]

## Key Concepts

- [[divergence-free-gaussian-velocity-field]]: A physical constraint integrated into Gaussian world models to ensure mass-conserving, physically plausible velocity field predictions.

## Archivist Review

Approved the divergence-free velocity field concept as it represents a robust physical inductive bias for 3D world models. Included PhysMani-Bench as a domain-specific robotics benchmark. The open question on scaling dynamic benchmarks was included as it identifies a critical, unresolved research bottleneck in embodied AI evaluation.

### Approved Concepts
- Divergence-free Gaussian velocity field: Provides a physics-based inductive bias to 3D dynamics modeling, improving predictive accuracy for fast-moving targets.

### Approved Open Questions
- Scaling Dynamic Manipulation Benchmarks: Scalability is essential for evaluating the generalization capabilities of future embodied AI models in complex, unstructured dynamic environments.

### Rejected Candidates
- [concept] PhysMani Framework (`physmani-framework`) - paper_local: PhysMani is the name of the framework itself, not an abstract, reusable mechanism.

## Datasets

- [[physmani-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2607.01938)
- [PDF](https://arxiv.org/pdf/2607.01938)

