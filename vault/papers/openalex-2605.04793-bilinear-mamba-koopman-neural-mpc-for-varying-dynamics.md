---
# CSL-compatible fields
title: "Bilinear Mamba-Koopman Neural MPC for Varying Dynamics"
author:
  - literal: "Matan Pagi"
  - literal: "Zohar Sorek"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04793"

# Custom fields
paper_id: "2605.04793"
paper_source: "openalex"
domain: "robotics,time-series"
tags:
  - "mamba"
  - "ssm"
  - "time-series"
  - "forecasting"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bilinear-koopman-dynamics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:03:33Z"
created_at: "2026-05-09T07:03:33Z"
---

# Bilinear Mamba-Koopman Neural MPC for Varying Dynamics

**Authors**: Matan Pagi, Zohar Sorek
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04793](https://arxiv.org/abs/2605.04793)

## Summary

This paper introduces Bilinear Mamba-Koopman Neural MPC, which addresses the limitations of standard Koopman-based models that assume independence between the system operator and control input. By incorporating a low-rank bilinear structure, the model enables control-dependent latent dynamics while maintaining convexity and admiting exact Jacobians for Sequential Convex Programming. Experimental results on CartPole and RSCP benchmarks demonstrate that this approach improves forecasting accuracy and provides significantly higher robustness to stale-plan execution in time-varying regimes.

## Key Contributions

- Proposes Bilinear Mamba-Koopman Neural MPC to enable control-dependent latent dynamics in Koopman-based forecasting frameworks.
- Introduces a low-rank bilinear structure that preserves exact model Jacobians for efficient Sequential Convex Programming (SCP).
- Demonstrates superior robustness and forecasting accuracy over standard linear Koopman baselines, particularly under stale-plan execution and time-varying dynamics in CartPole and RSCP tasks.

## Open Questions & Future Work

- [[runtime-stability-of-control-dependent-operators]]

## Key Concepts

- [[bilinear-koopman-dynamics]]: A modeling approach that introduces control-dependent coupling into Koopman operator dynamics via low-rank structures to allow adaptation to varying control inputs.

## Archivist Review

I have approved 'Bilinear Koopman Dynamics' as the core conceptual contribution, as it generalizes linear Koopman operators to handle control-dependence while remaining amenable to convex optimization. The architecture name was rejected as being too paper-specific. I also approved the open question regarding runtime stability for such models, as formal verification of stability for learned operators is a critical, unresolved, and broadly relevant challenge in control-oriented machine learning.

### Approved Concepts
- Bilinear Koopman Dynamics: It provides a principled way to relax the conditional-independence constraint in Koopman-based forecasting while maintaining convexity and model Jacobians suitable for efficient optimization.

### Approved Open Questions
- Runtime Stability of Operators: Formal stability is a necessary precursor to using these models in safety-critical autonomous systems.

### Rejected Candidates
- [concept] Bilinear Mamba-Koopman Neural MPC (`bilinear-mamba-koopman-neural-mpc`) - paper_local: This is a paper-specific architecture name; the underlying reusable mechanism is better captured by 'Bilinear Koopman Dynamics'.
- [open_question] Physically-Informed Bilinear Coupling Priors (`physical-priors-bilinear-koopman`) - low_impact: This is a specific architectural enhancement request rather than a fundamental bottleneck; it is also highly tied to the specific bilinear model proposed.

## Links

- [Abstract](https://arxiv.org/abs/2605.04793)
- [PDF](https://arxiv.org/pdf/2605.04793)

