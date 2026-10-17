---
# CSL-compatible fields
title: "ReAl: Refine neural operators via aligning dynamical flow"
author:
  - literal: "Jing Xu"
  - literal: "Zenglin Xu"
  - literal: "Li Yi"
  - literal: "Ruoxi Jiang"
  - literal: "Yuan Qi"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20369"

# Custom fields
paper_id: "2610.20369"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "reinforcement-learning"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:56:01Z"
created_at: "2026-10-17T08:56:01Z"
---

# ReAl: Refine neural operators via aligning dynamical flow

**Authors**: Jing Xu, Zenglin Xu, Li Yi, Ruoxi Jiang, Yuan Qi
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20369](https://arxiv.org/abs/2610.20369)

## Summary

Neural PDE surrogates trained with MSE often miss high-frequency details, while generative models suffer from error accumulation during autoregressive rollouts. To resolve this, the authors propose ReAl, a model-agnostic plug-in consisting of a residual conditional flow-matching refinement stage and a trajectory-level alignment stage using rewards. Experiments show that ReAl consistently enhances high-frequency fidelity, forecasting accuracy, and long-horizon stability across various PDE tasks and surrogate architectures.

## Key Contributions

- Introduces ReAl, a model-agnostic plug-in that refines pretrained PDE surrogates by combining residual flow matching with trajectory-level dynamical alignment.
- Demonstrates that the refinement stage recovers missing high-frequency structures and fine-scale details lost by MSE-trained deterministic surrogates.
- Shows that the alignment stage utilizes trajectory-level rewards to mitigate generative discrepancies and ensure long-horizon stability during autoregressive rollouts in chaotic systems.
- Evaluated across diverse surrogate architectures and PDE tasks, consistently improving forecasting accuracy, high-frequency fidelity, and long-term stability.

## Open Questions & Future Work

- [[physics-guided-reward-formulation-pde-rollouts]]

## Archivist Review

Strictly adhered to the sparsity constraint by approving only the highly relevant open question on physics-guided reward formulation for PDE rollouts, while rejecting the paper-local ReAl framework concept to protect vault quality.

### Approved Open Questions
- Physics-Guided Reward Formulation for PDEs: Understanding how to correctly formulate proxy rewards for dynamical systems is crucial for aligning generative video/fluid models with real-world physical laws without destabilizing training.

### Rejected Candidates
- [concept] ReAl framework (`real`) - not_reusable: The proposed framework is too specific to residual PDE flow matching and does not represent a broadly reusable general time-series concept.

## Links

- [Abstract](https://arxiv.org/abs/2610.20369)
- [PDF](https://arxiv.org/pdf/2610.20369)

