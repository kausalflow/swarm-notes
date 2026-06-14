---
# CSL-compatible fields
title: "A Quadratic Order Reduction -- Gaussian Process Ordinary Differential Equation framework for the inference of Large Continuous Dynamical Systems"
author:
  - literal: "Guglielmo Padula"
  - literal: "Michele Girfoglio"
  - literal: "Gianluigi Rozza"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13063"

# Custom fields
paper_id: "2606.13063"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "physics-informed-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gaussian-process-ordinary-differential-equations"
  - "quadratic-order-reduced-order-modelling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:38:37Z"
created_at: "2026-06-14T08:38:37Z"
---

# A Quadratic Order Reduction -- Gaussian Process Ordinary Differential Equation framework for the inference of Large Continuous Dynamical Systems

**Authors**: Guglielmo Padula, Michele Girfoglio, Gianluigi Rozza
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13063](https://arxiv.org/abs/2606.13063)

## Summary

This paper introduces a forecasting framework for large-scale continuous dynamical systems that combines Gaussian Process Ordinary Differential Equations (GP-ODE) with Quadratic Order Model Reduction (Q-ROM). By utilizing GP-ODEs, the model achieves accurate short-term forecasting with rigorous uncertainty quantification and theoretical convergence properties. The integration of Q-ROM and sphere projection enables efficient latent space learning, significantly improving numerical stability compared to traditional ROM approaches. Empirical results demonstrate the method's superior performance over standard baseline methods in both accuracy and computational overhead.

## Key Contributions

- Proposes a novel forecasting framework integrating Gaussian Process ODEs with Quadratic Order Model Reduction and sphere projection.
- Provides theoretical convergence proofs for the GP-ODE component toward the true autonomous equation in smooth regimes.
- Outperforms established baseline methods (e.g., EDMD, Bagging-ODMD) in both predictive accuracy and computational efficiency for complex dynamical systems.

## Open Questions & Future Work

- [[non-equispaced-derivative-estimation-gprode]]

## Key Concepts

- [[gaussian-process-ordinary-differential-equations]]: A framework for forecasting dynamical systems that uses Gaussian Processes to learn autonomous differential equations, providing uncertainty quantification and convergence guarantees.
- [[quadratic-order-reduced-order-modelling]]: A reduced-order modeling technique that approximates nonlinear dynamical systems using quadratic formulations to improve computational efficiency and stability.

## Archivist Review

I approved the two core methodological components, as they represent distinct, reusable paradigms for coupling physics-informed reduced-order modeling with GP-based ODE inference. I also approved the open question regarding non-equispaced derivative estimation, as it identifies a critical bottleneck for deploying these models in real-world, irregular time-series scenarios. Routine benchmarks and subcomponents were rejected to ensure the vault remains focused on fundamental contributions.

### Approved Concepts
- Gaussian Process Ordinary Differential Equations (GP-ODE): It provides a powerful, physics-informed framework for dynamical system modeling that inherently couples uncertainty quantification with structural ODE constraints.
- Quadratic Order Reduced-Order Modelling (Q-ROM): It provides a systematic strategy for handling high-dimensional state spaces by approximating nonlinear dynamics via quadratic formulations, ensuring stability.

### Approved Open Questions
- Non-equispaced derivative estimation in GP-ODE: This is a fundamental bottleneck for applying GP-ODE models to real-world, irregular observational data, impacting both model accuracy and computational feasibility.

## Links

- [Abstract](https://arxiv.org/abs/2606.13063)
- [PDF](https://arxiv.org/pdf/2606.13063)

