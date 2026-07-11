---
# CSL-compatible fields
title: "Ego-Human Motion Prediction with 3D-Aware LLM"
author:
  - literal: "Yujin Bae"
  - literal: "Jaewoo Jeong"
  - literal: "Hyeonseong Kim"
  - literal: "Kuk-Jin Yoon"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07001"

# Custom fields
paper_id: "2607.07001"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "llm"
  - "multimodal"
  - "vision-language-model"
  - "autoregressive"
  - "reinforcement-learning-from-human-feedback"
  - "instruction-tuning"
  - "group-relative-policy-optimization-grpo"
architectures:
  - "decoder-only"
datasets:
  - "Nymeria"
concept_slugs:
  - "ego3dlm"
dataset_slugs:
  - "nymeria"
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:59Z"
created_at: "2026-07-11T07:05:59Z"
---

# Ego-Human Motion Prediction with 3D-Aware LLM

**Authors**: Yujin Bae, Jaewoo Jeong, Hyeonseong Kim, Kuk-Jin Yoon
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07001](https://arxiv.org/abs/2607.07001)

## Summary

Ego3DLM is a novel framework for egocentric human motion prediction that treats pose and language forecasting as a unified task. By incorporating 3D spatial and semantic scene information, the model achieves better ground-truth adherence than standard language-prior methods. The architecture employs a three-stage training process, culminating in GRPO-based reinforcement fine-tuning to ensure consistency between predicted poses and textual action descriptions. Experiments on the Nymeria benchmark confirm its superior performance in predicting physically plausible future motions.

## Key Contributions

- Introduces Ego3DLM, a model that simultaneously decodes past and future poses and narrations in a single autoregressive pass.
- Integrates explicit 3D spatial and semantic scene awareness to ground human motion predictions, addressing the limitations of purely language-guided approaches.
- Achieves state-of-the-art performance on the Nymeria benchmark for future motion prediction, tracking, and description tasks.

## Open Questions & Future Work

- [[incremental-3d-scene-registration]]

## Key Concepts

- [[ego3dlm]]: An egocentric human motion forecasting model that simultaneously decodes past/future pose and past/future narration in a single autoregressive pass using 3D scene features.

## Archivist Review

The paper introduces a novel framework for egocentric motion prediction by unifying pose and language decoding within an autoregressive architecture grounded in 3D scene features. Ego3DLM is approved as a distinct and reusable paradigm for holistic multimodal forecasting. The Nymeria dataset is approved as a critical benchmark for this specific task. The open question regarding incremental 3D scene registration addresses a fundamental limitation in current embodied AI motion forecasting models that rely on static scenes.

### Approved Concepts
- Ego3DLM: This framework defines a novel paradigm by coupling 3D spatial scene grounding with holistic pose-language autoregressive decoding for egocentric motion prediction.

### Approved Open Questions
- Incremental 3D Scene Registration: Current reliance on fixed 3D scene data is a fundamental bottleneck for deploying motion forecasting in open-world, long-term embodied AI applications.

## Datasets

- [[nymeria]]

## Links

- [Abstract](https://arxiv.org/abs/2607.07001)
- [PDF](https://arxiv.org/pdf/2607.07001)

