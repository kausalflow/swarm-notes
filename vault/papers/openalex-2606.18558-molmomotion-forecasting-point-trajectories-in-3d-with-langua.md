---
# CSL-compatible fields
title: "MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction"
author:
  - literal: "Jianing Zhang"
  - literal: "Chenhao Zheng"
  - literal: "Yajun Yang"
  - literal: "Max Argus"
  - literal: "Rustin Soraki"
  - literal: "Winson Han"
  - literal: "Taira Anderson"
  - literal: "Chun-Liang Li"
  - literal: "Liu S"
  - literal: "Jiafei Duan"
  - literal: "Zhongzheng Ren"
  - literal: "Jieyu Zhang"
  - literal: "R Narayanan Krishna"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18558"

# Custom fields
paper_id: "2606.18558"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "generative-model"
  - "robotics"
architectures:
  []
datasets:
  - "molmomotion-1m"
  - "pointmotionbench"
concept_slugs:
  - "goal-conditioned-3d-point-trajectory-forecasting"
dataset_slugs:
  - "molmomotion-1m"
  - "pointmotionbench"
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:17:34Z"
created_at: "2026-06-20T08:17:34Z"
---

# MolmoMotion: Forecasting Point Trajectories in 3D with Language Instruction

**Authors**: Jianing Zhang, Chenhao Zheng, Yajun Yang, Max Argus, Rustin Soraki, Winson Han, Taira Anderson, Chun-Liang Li, Liu S, Jiafei Duan, Zhongzheng Ren, Jieyu Zhang, R Narayanan Krishna
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18558](https://arxiv.org/abs/2606.18558)

## Summary

MolmoMotion is a unified framework for goal-conditioned 3D point trajectory forecasting that leverages language instructions to guide prediction. The framework includes a large-scale pre-training dataset (MolmoMotion-1M), a comprehensive benchmark (PointMotionBench), and a versatile model architecture supporting both autoregressive and flow-matching generation. The model significantly outperforms existing baselines and demonstrates effective transfer learning for robotic manipulation and video synthesis tasks.

## Key Contributions

- Introduced MolmoMotion-1M, a large-scale corpus of 1.16M action-described, object-grounded 3D point trajectories.
- Established PointMotionBench, a human-verified benchmark for goal-conditioned 3D point motion forecasting across 111 object categories.
- Proposed the MolmoMotion model, which utilizes language instructions to predict future 3D trajectories via autoregressive and flow-matching methods.
- Demonstrated transferability of learned motion priors to robot manipulation and video synthesis tasks.

## Open Questions & Future Work

- [[scaling-dense-3d-point-forecasting]]

## Key Concepts

- [[goal-conditioned-3d-point-trajectory-forecasting]]: A motion forecasting paradigm where future 3D point trajectories are predicted conditioned on visual history and natural language goal descriptions.

## Archivist Review

The paper presents a significant shift toward language-conditioned 3D point trajectory forecasting. I approved the task formulation as a permanent concept and the two main datasets as critical resources. I also approved an open question that addresses the architectural limitations in dense point modeling, while rejecting the model name itself and the generic call for real-world robotics evaluation.

### Approved Concepts
- Goal-Conditioned 3D Point Trajectory Forecasting: Establishes a unified, class-agnostic, and view-stable representation for motion forecasting that leverages language instructions, moving beyond standard pixel-based or class-specific approaches.

### Approved Open Questions
- Scaling Dense 3D Point Forecasting: Addresses a fundamental bottleneck in the fidelity of 3D motion forecasting, which currently limits the ability to model fine-grained and deformable object interactions.

### Rejected Candidates
- [concept] MolmoMotion Model (`molmomotion-model`) - paper_local: The proposed concept is a specific model implementation rather than a reusable architecture or mechanism; 'Goal-Conditioned 3D Point Trajectory Forecasting' captures the core contribution.
- [open_question] Real-World Robot Closed-Loop Evaluation (`real-world-robot-closed-loop-evaluation`) - generic: This is a common, generic future work direction for robotics papers rather than a specific research question regarding the methodology itself.

## Datasets

- [[molmomotion-1m]]
- [[pointmotionbench]]

## Links

- [Abstract](https://arxiv.org/abs/2606.18558)
- [PDF](https://arxiv.org/pdf/2606.18558)

