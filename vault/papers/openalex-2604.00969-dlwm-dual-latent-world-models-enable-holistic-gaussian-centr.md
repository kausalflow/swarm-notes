---
# CSL-compatible fields
title: "DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving"
author:
  - literal: "Yiyao Zhu"
  - literal: "Ying Xue"
  - literal: "Haiming Zhang"
  - literal: "Guangfeng Jiang"
  - literal: "Wending Zhou"
  - literal: "Xu Yan"
  - literal: "Jiantao Gao"
  - literal: "Yingjie Cai"
  - literal: "Bingbing Liu"
  - literal: "Zhen Li"
  - literal: "Shaojie Shen"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00969"

# Custom fields
paper_id: "2604.00969"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "autonomous-agent"
  - "planning"
  - "pre-training"
  - "self-supervised-learning"
architectures:
  []
datasets:
  - "SurroundOcc"
  - "nuScenes"
concept_slugs:
  - "dual-latent-world-models-dlwm"
dataset_slugs:
  - "surroundocc"
  - "nuscenes"
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:50:08Z"
created_at: "2026-04-04T05:50:08Z"
---

# DLWM: Dual Latent World Models enable Holistic Gaussian-centric Pre-training in Autonomous Driving

**Authors**: Yiyao Zhu, Ying Xue, Haiming Zhang, Guangfeng Jiang, Wending Zhou, Xu Yan, Jiantao Gao, Yingjie Cai, Bingbing Liu, Zhen Li, Shaojie Shen
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00969](https://arxiv.org/abs/2604.00969)

## Summary

DLWM is a two-stage pre-training paradigm for vision-based autonomous driving that represents scenes using 3D semantic Gaussians. The framework employs dual latent world models: one for Gaussian-flow-guided temporal occupancy forecasting, and another for ego-planning-guided motion prediction. This architecture enables holistic scene understanding and achieves superior performance across perception, forecasting, and planning benchmarks like SurroundOcc and nuScenes.

## Key Contributions

- Introduces DLWM, a dual latent world model paradigm that decouples 3D Gaussian-based perception-forecasting and motion planning.
- Achieves significant performance gains on SurroundOcc and nuScenes for 3D occupancy perception, 4D occupancy forecasting, and motion planning tasks.
- Enables holistic Gaussian-centric pre-training by reconstructing multi-view semantic and depth images in the first stage.

## Open Questions & Future Work

- [[full-lifecycle-gaussian-pretraining]]

## Key Concepts

- [[dual-latent-world-models-dlwm]]: A two-stage autonomous driving pre-training paradigm using separate latent world models for perception-forecasting and motion planning.

## Archivist Review

The approved concept defines a novel, reusable architectural paradigm for autonomous driving pre-training. The approved datasets are widely recognized and essential benchmarks for evaluating the performance claims of the proposed approach. The approved open question addresses a fundamental limitation in the current research landscape of Gaussian-centric autonomous driving models, specifically the lack of unified, self-supervised lifecycle pre-training.

### Approved Concepts
- Dual Latent World Models (DLWM): The paper introduces a two-stage pre-training paradigm using separate latent world models for occupancy forecasting and ego-planning, which is the core architectural innovation.

### Approved Open Questions
- Full-lifecycle Gaussian pre-training: This is critical for reducing reliance on manual annotations and establishing foundational models that generalize across perception, temporal forecasting, and planning in autonomous systems.

## Datasets

- [[surroundocc]]
- [[nuscenes]]

## Links

- [Abstract](https://arxiv.org/abs/2604.00969)
- [PDF](https://arxiv.org/pdf/2604.00969)

