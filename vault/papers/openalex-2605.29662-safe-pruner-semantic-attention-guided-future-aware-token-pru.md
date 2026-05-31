---
# CSL-compatible fields
title: "SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation"
author:
  - literal: "Shilin Ma"
  - literal: "Chubin Zhang"
  - literal: "Changyuan Wang"
  - literal: "Yuji Wang"
  - literal: "Yue Wu"
  - literal: "Zixuan Wang"
  - literal: "Jingqi Tian"
  - literal: "Zheng Zhu"
  - literal: "Yansong Tang"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29662"

# Custom fields
paper_id: "2605.29662"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "model-compression"
  - "pruning"
  - "robotics"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "semantic-attention-consistency"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:57Z"
created_at: "2026-05-31T08:10:57Z"
---

# SAFE-Pruner: Semantic Attention-Guided Future-Aware Token Pruning for Efficient Vision-Language-Action Manipulation

**Authors**: Shilin Ma, Chubin Zhang, Changyuan Wang, Yuji Wang, Yue Wu, Zixuan Wang, Jingqi Tian, Zheng Zhu, Yansong Tang
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29662](https://arxiv.org/abs/2605.29662)

## Summary

SAFE-Pruner is an efficient token pruning framework designed for real-time vision-language-action (VLA) models in robotic control. Unlike standard approaches that rely solely on shallow visual cues, this method utilizes 'semantic attention consistency' to forecast the future saliency of tokens in deeper layers. Combined with an adaptive subtask division strategy to manage attention shifts, SAFE-Pruner delivers significant inference acceleration while preserving the accuracy required for successful robotic manipulation.

## Key Contributions

- Introduces SAFE-Pruner, a plug-and-play token pruning framework that uses future-layer attention cues to prevent the premature removal of critical visual information.
- Identifies semantic attention consistency as a core property of VLA models, enabling a forward-looking token saliency forecasting strategy.
- Implements an adaptive subtask division mechanism to detect abrupt attention shifts, maintaining reliability during dynamic robotic control tasks.
- Achieves up to 1.89x inference speedup in vision-language-action models with <1.7% success rate degradation, outperforming existing state-of-the-art methods by up to 1.9%.

## Open Questions & Future Work

- [[predicting-late-stage-token-saliency-vla]]

## Key Concepts

- [[semantic-attention-consistency]]: The tendency of vision-language-action models to maintain consistent attention on specific semantic entities across temporal execution steps.

## Archivist Review

I approved the concept 'Semantic Attention Consistency' as it provides a novel and potentially generalizable empirical observation regarding VLA model behavior. The open question 'Predicting Late-Stage VLA Saliency' is approved because it articulates a fundamental challenge in dynamic token pruning for real-time robotic control that extends beyond the specific pruning implementation of this paper. All other candidates were rejected as they were either paper-local implementation details or not sufficiently novel.

### Approved Concepts
- Semantic Attention Consistency: It serves as the core empirical insight that enables future-layer saliency forecasting for token pruning in VLA models.

### Approved Open Questions
- Predicting Late-Stage VLA Saliency: This bottleneck is central to the efficiency-accuracy trade-off in embodied AI and represents a key challenge for deploying VLA models on latency-constrained hardware.

## Links

- [Abstract](https://arxiv.org/abs/2605.29662)
- [PDF](https://arxiv.org/pdf/2605.29662)

