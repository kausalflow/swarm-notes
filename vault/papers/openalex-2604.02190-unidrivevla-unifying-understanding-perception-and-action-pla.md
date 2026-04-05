---
# CSL-compatible fields
title: "UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving"
author:
  - literal: "Yongkang Li"
  - literal: "Lijun Zhou"
  - literal: "Sixu Yan"
  - literal: "Bencheng Liao"
  - literal: "Tianyi Yan"
  - literal: "Kaixin Xiong"
  - literal: "Long Chen"
  - literal: "Hongwei Xie"
  - literal: "Bing Wang"
  - literal: "Guang Chen"
  - literal: "Hangjun Ye"
  - literal: "Wenyu Liu"
  - literal: "Haiyang Sun"
  - literal: "Xinggang Wang"
issued:
  date-parts:
    - [2026, 4, 2]
url: "https://arxiv.org/abs/2604.02190"

# Custom fields
paper_id: "2604.02190"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "vision-language-model"
  - "vlm"
  - "multimodal"
  - "autonomous-agent"
  - "attention-mechanism"
  - "mixture-of-experts"
  - "planning"
architectures:
  - "encoder-decoder"
datasets:
  - "nuScenes"
  - "Bench2Drive"
concept_slugs:
  - "mixture-of-transformers-mot"
dataset_slugs:
  - "nuscenes"
  - "bench2drive"
skill: "TimeSeriesSkill"
processed_at: "2026-04-05T06:09:35Z"
created_at: "2026-04-05T06:09:35Z"
---

# UniDriveVLA: Unifying Understanding, Perception, and Action Planning for Autonomous Driving

**Authors**: Yongkang Li, Lijun Zhou, Sixu Yan, Bencheng Liao, Tianyi Yan, Kaixin Xiong, Long Chen, Hongwei Xie, Bing Wang, Guang Chen, Hangjun Ye, Wenyu Liu, Haiyang Sun, Xinggang Wang
**Date**: 2026-04-02
**Paper ID**: [openalex:2604.02190](https://arxiv.org/abs/2604.02190)

## Summary

UniDriveVLA addresses the inherent trade-off between spatial perception and semantic reasoning in Vision-Language-Action (VLA) models for autonomous driving. By utilizing a Mixture-of-Transformers architecture with decoupled experts for understanding, perception, and planning, the model resolves the conflict of shared parameter optimization. Coupled with a sparse perception paradigm and three-stage progressive training, it achieves state-of-the-art performance in both open-loop and closed-loop driving benchmarks.

## Key Contributions

- Proposes UniDriveVLA, a VLA architecture utilizing Mixture-of-Transformers to decouple driving understanding, scene perception, and action planning.
- Introduces a sparse perception paradigm and a three-stage progressive training strategy to mitigate the perception-reasoning conflict.
- Achieves state-of-the-art results on nuScenes (open-loop) and Bench2Drive (closed-loop) benchmarks across diverse tasks including 3D detection and motion forecasting.

## Key Concepts

- [[mixture-of-transformers-mot]]: An architectural design for multi-task models that decouples processing streams (e.g., perception, reasoning, planning) through specialized expert modules coordinated by attention mechanisms.

## Archivist Review

The paper introduces a Mixture-of-Transformers architecture specifically designed to mitigate the conflict between perception and reasoning in multi-task VLA models. This architectural pattern is deemed sufficiently generalizable as a modular design for future multimodal systems. I have approved the two central benchmarks used to validate this, while rejecting specific training recipes and sub-component paradigms as either too implementation-specific or better categorized as subsets of the broader MoT architecture.

### Approved Concepts
- Mixture-of-Transformers (MoT): Addresses the inherent conflict between spatial perception and semantic reasoning in driving vision-language-action (VLA) models by decoupling specialized expert modules.

### Rejected Candidates
- [concept] Sparse Perception Paradigm (`sparse-perception-paradigm`) - subcomponent_of_broader_mechanism: This is a specific architectural choice rather than a generalizable framework component.
- [concept] Three-Stage Progressive Training (`three-stage-progressive-training`) - paper_local: Training schedules are typically highly specific to the task and model architecture.

## Datasets

- [[nuscenes]]
- [[bench2drive]]

## Links

- [Abstract](https://arxiv.org/abs/2604.02190)
- [PDF](https://arxiv.org/pdf/2604.02190)

