---
# CSL-compatible fields
title: "Learning Dissipative Dynamics with Dissipativity-by-Construction Discrete-Time Neural Networks"
author:
  - literal: "Tuan Luong"
  - literal: "Hyungpil Moon"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27188"

# Custom fields
paper_id: "2609.27188"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "robotics"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:38:09Z"
created_at: "2026-09-26T09:38:09Z"
---

# Learning Dissipative Dynamics with Dissipativity-by-Construction Discrete-Time Neural Networks

**Authors**: Tuan Luong, Hyungpil Moon
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27188](https://arxiv.org/abs/2609.27188)

## Summary

This paper proposes a discrete-time deep multilayer perceptron method for learning incrementally dissipative dynamics from input-output time-series data without relying on continuous-time ODE solvers. By using a constrained parameterization and a dedicated training procedure, the model guarantees incremental dissipativity by construction rather than through soft regularization. Lyapunov-based analysis confirms its stability properties, and robotic simulation results verify its computational efficiency, predictive accuracy, and strict preservation of dissipativity compared to existing baselines.

## Key Contributions

- Proposes a discrete-time deep multilayer perceptron for learning incrementally dissipative dynamics directly from input-output time-series data without requiring ODE solvers.
- Introduces a constrained parameterization and dedicated training procedure that guarantees incremental dissipativity by construction rather than through soft regularization.
- Establishes rigorous dissipativity and stability guarantees through Lyapunov-based analysis.
- Demonstrates competitive prediction accuracy, computational efficiency, and consistent preservation of incremental dissipativity on robotic dynamical systems compared to baseline methods.

## Archivist Review

Adhering strictly to the review policy, I have rejected both proposed open questions because one is a narrow implementation detail (negative slope activation bounds) and the other is generic boilerplate future work (scaling to more complex systems). No concepts or datasets met the threshold for standalone vault notes.

### Rejected Candidates
- [open_question] Negative Slope Activation Extensions (`negative-slope-activation-dissipative-networks`) - paper_local: Too narrow and paper-specific to activation slope formulations in discrete-time dissipative networks.
- [open_question] Complex Dynamics and Network Extensions (`complex-dynamics-and-network-extensions`) - generic: Generic future work proposing to scale models to larger systems and alternative architectures.

## Links

- [Abstract](https://arxiv.org/abs/2609.27188)
- [PDF](https://arxiv.org/pdf/2609.27188)

