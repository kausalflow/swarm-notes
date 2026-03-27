---
# CSL-compatible fields
title: "TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models"
author:
  - literal: "Jiaying Zhou"
  - literal: "Zhihao Zhan"
  - literal: "Ruifeng Zhai"
  - literal: "Qinhan Lyu"
  - literal: "Hao Liu"
  - literal: "Keze Wang"
  - literal: "Liang Lin"
  - literal: "Guangrun Wang"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24584"

# Custom fields
paper_id: "2603.24584"
paper_source: "arxiv"
domain: "robotics"
tags:
  - "vision-language-model"
  - "robotics"
  - "agent"
  - "guidance"
  - "object-detection"
  - "vision-language-action-model"
  - "tool-use"
architectures:
  []
datasets:
  - "LIBERO"
  - "LIBERO-Plus"
  - "VLABench"
skill: "GeneralMLSkill"
processed_at: "2026-03-26T06:26:20Z"
created_at: "2026-03-26T06:26:20Z"
---

# TAG: Target-Agnostic Guidance for Stable Object-Centric Inference in Vision-Language-Action Models

**Authors**: Jiaying Zhou, Zhihao Zhan, Ruifeng Zhai, Qinhan Lyu, Hao Liu, Keze Wang, Liang Lin, Guangrun Wang
**Date**: 2026-03-25
**Paper ID**: [arxiv:2603.24584](https://arxiv.org/abs/2603.24584)

## Summary

This paper addresses the reliability degradation in Vision-Language-Action (VLA) models, particularly in cluttered scenes caused by instance-level grounding failures, by introducing Target-Agnostic Guidance (TAG). TAG is an inference-time mechanism inspired by classifier-free guidance, which computes a residual steering signal as the difference between the policy's action prediction on the original observation and an object-erased observation. This signal explicitly strengthens the evidence related to the target object, improving grounding accuracy without modifying the core VLA policy architecture. Evaluations on benchmarks like LIBERO and VLABench confirm that TAG significantly enhances robustness under clutter and reduces erroneous actions on the wrong object instance.

## Key Contributions

- Proposed Target-Agnostic Guidance (TAG), a novel inference-time mechanism that uses prediction differences between standard and object-erased observations to reduce distractor bias in VLA policies.
- Demonstrated that TAG consistently improves the robustness of VLA models against scene clutter and reduces near-miss or wrong-object execution errors across manipulation benchmarks.
- TAG is a policy-agnostic method that requires minimal architectural or training modifications to existing Vision-Language-Action models.

## Limitations

The primary limitation is the reliance on an object-erased observation, which necessitates a reliable mechanism (like an object mask) to generate the counterfactual input, potentially adding overhead or introducing mask-related errors.

## Open Questions & Future Work

- [[extending-residual-guidance-to-additional-factors]]
- [[improving-robustness-to-imperfect-visual-observations]]

## Key Concepts

- [Target-Agnostic Guidance](../concepts/target-agnostic-guidance.md): An inference-time guidance mechanism for VLA models that uses the difference between predictions on the original observation and an object-erased observation to steer actions toward the intended target.

## Datasets

- [LIBERO](../datasets/libero.md)
- [LIBERO-Plus](../datasets/libero-plus.md)
- [VLABench](../datasets/vlabench.md)

## Limitations

The primary limitation is the reliance on an object-erased observation, which necessitates a reliable mechanism (like an object mask) to generate the counterfactual input, potentially adding overhead or introducing mask-related errors.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.24584)
- [PDF](https://arxiv.org/pdf/2603.24584)

