---
# CSL-compatible fields
title: "Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models"
author:
  - literal: "An Zhao"
  - literal: "Shengyuan Zhang"
  - literal: "Zhongjian Sun"
  - literal: "Yixiang Zhou"
  - literal: "Zejian Li"
  - literal: "Ling Yang"
  - literal: "Tianrun Chen"
  - literal: "Lingyun Sun"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.11155"

# Custom fields
paper_id: "2606.11155"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "generative-adversarial-network"
  - "flow-matching"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mean-flow-distillation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:54:43Z"
created_at: "2026-06-12T08:54:43Z"
---

# Mean Flow Distillation: Robust and Stable Distillation for Flow Matching Models

**Authors**: An Zhao, Shengyuan Zhang, Zhongjian Sun, Yixiang Zhou, Zejian Li, Ling Yang, Tianrun Chen, Lingyun Sun
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.11155](https://arxiv.org/abs/2606.11155)

## Summary

Flow matching models are computationally demanding due to iterative ODE sampling, and existing distillation methods often lack stability. This paper introduces Mean Flow Distillation (MFD), a framework that leverages the geometric structure of flows by matching expected average velocities. Theoretically, MFD functions as a temporal low-pass filter, suppressing optimization noise and ensuring trajectory consistency. Experiments in 4D occupancy forecasting and text-to-image generation demonstrate that MFD enables high-fidelity single-step inference.

## Key Contributions

- Introduced Mean Flow Distillation (MFD), a framework that reduces inference computational overhead by enabling high-fidelity single-step generation.
- Provided theoretical evidence that MFD functions as a temporal low-pass filter, effectively suppressing optimization noise found in variational score distillation.
- Proved the Mean Flow Matching Theorem, demonstrating that aligning expected average velocities is sufficient for strict distribution matching in flow models.

## Open Questions & Future Work

- [[jacobian-omission-bound-ode-distillation]]

## Key Concepts

- [[mean-flow-distillation]]: A distillation framework for flow matching that matches expected average velocities to achieve distribution alignment while suppressing high-frequency optimization noise.

## Archivist Review

The paper introduces a significant distillation framework for flow-based generative models. I approved Mean Flow Distillation as it provides a distinct, theoretically grounded approach to reducing sampling latency, and the open question regarding Jacobian approximation bounds addresses a fundamental stability challenge in the field of neural ODE distillation.

### Approved Concepts
- Mean Flow Distillation: MFD serves as a temporal low-pass filter that suppresses optimization noise, enabling efficient, high-fidelity single-step generation for flow matching models.

### Approved Open Questions
- Theoretical Bound for Jacobian Omission: This approximation is critical for the stability of MFD, and characterizing its impact is essential for bridging the gap between empirical performance and formal optimization theory in generative model distillation.

## Links

- [Abstract](https://arxiv.org/abs/2606.11155)
- [PDF](https://arxiv.org/pdf/2606.11155)

