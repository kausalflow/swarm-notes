---
# CSL-compatible fields
title: "Quantizing Time-Series Models As Dynamical Systems: Trajectory-Based Quantization Sensitivity Score"
author:
  - literal: "Mariya Pavlova"
  - literal: "Hong Zhu"
  - literal: "Elizsveta Semenova"
  - literal: "Yingzhen Li"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13300"

# Custom fields
paper_id: "2606.13300"
paper_source: "openalex"
domain: "time-series"
tags:
  - "model-compression"
  - "quantization"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "trajectory-based-quantization-sensitivity-score-tqs"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:37:31Z"
created_at: "2026-06-14T08:37:31Z"
---

# Quantizing Time-Series Models As Dynamical Systems: Trajectory-Based Quantization Sensitivity Score

**Authors**: Mariya Pavlova, Hong Zhu, Elizsveta Semenova, Yingzhen Li
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13300](https://arxiv.org/abs/2606.13300)

## Summary

This paper introduces the Trajectory-based Quantization Sensitivity Score (TQS), a novel metric for assessing model sensitivity to post-training quantization (PTQ) by analyzing network rollouts as discrete-time dynamical systems. By focusing on how quantization errors propagate and amplify over a rollout horizon, the approach allows for quantization budget planning without the need for calibration data or second-order approximations. The authors demonstrate the effectiveness of this approach through TQS-PTQ, a mixed-precision framework that achieves robust performance in low-precision, resource-constrained deployments.

## Key Contributions

- Introduces TQS, a metric that models network rollouts as discrete-time dynamical systems to characterize error propagation over a rollout horizon.
- Enables a priori quantization sensitivity estimation that is decoupled from specific quantizers or bit-width assignments.
- Develops TQS-PTQ, a data-free, mixed-precision quantization framework that avoids costly second-order approximations.

## Open Questions & Future Work

- [[noise-model-sensitivity-in-quantization]]

## Key Concepts

- [[trajectory-based-quantization-sensitivity-score-tqs]]: A post-training quantization metric that evaluates error propagation in neural networks by treating them as discrete-time dynamical systems.

## Archivist Review

The approved items capture the central contribution—reframing model quantization through dynamical systems theory—and a specific, non-boilerplate technical open question regarding the robustness of this sensitivity analysis to underlying noise model assumptions. Other candidates were excluded as they were subcomponents or boilerplate.

### Approved Concepts
- Trajectory-based Quantization Sensitivity Score (TQS): It offers a novel way to quantify quantization sensitivity by reframing network rollouts as dynamical systems, enabling budget planning without calibration data.

### Approved Open Questions
- Noise Model Sensitivity in Quantization: The noise model choice impacts the layer-wise precision assignment, which directly dictates the model's accuracy-compression trade-off. Clarifying the noise model's role is critical for robust, generalizable quantization frameworks.

## Links

- [Abstract](https://arxiv.org/abs/2606.13300)
- [PDF](https://arxiv.org/pdf/2606.13300)

