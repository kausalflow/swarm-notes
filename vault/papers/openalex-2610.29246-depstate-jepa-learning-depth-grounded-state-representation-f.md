---
# CSL-compatible fields
title: "DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation"
author:
  - literal: "Xiujian Liang"
  - literal: "Liuyuan Na"
  - literal: "Zehao Du"
  - literal: "Jiacheng Xu"
  - literal: "Weixi Song"
  - literal: "Mingyang Sun"
  - literal: "Xingjun Ma"
  - literal: "Cewu Lu"
  - literal: "Jianhua Sun"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29246"

# Custom fields
paper_id: "2610.29246"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "reinforcement-learning"
  - "robotics"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "depstate-jepa"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:13:01Z"
created_at: "2026-10-24T09:13:01Z"
---

# DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation

**Authors**: Xiujian Liang, Liuyuan Na, Zehao Du, Jiacheng Xu, Weixi Song, Mingyang Sun, Xingjun Ma, Cewu Lu, Jianhua Sun
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29246](https://arxiv.org/abs/2610.29246)

## Summary

DepState-JEPA is a dual-stream RGB-Depth joint-embedding predictive architecture that connects spatial scene geometry with action-conditioned prediction via a shared latent state called DepState. By using depth both as a complementary observation stream and for metric 3D grounding, the framework aggregates shared information into DepState while retaining modality-private features for decoding. It incorporates object-trajectory supervision and calibrated forward kinematics to guide state learning, achieving strong performance in visual perception, conditioned visual forecasting, and robot manipulation tasks.

## Key Contributions

- Introduced DepState-JEPA, a dual-stream RGB-Depth joint-embedding predictive architecture connecting scene geometry with action-conditioned prediction through a shared latent state.
- Employs depth observations to ground both modalities in metric 3D space, aggregating shared information into DepState while preserving modality-private features via ray-conditioned readouts.
- Incorporates object-trajectory supervision and calibrated forward kinematics to shape state learning through motion targets and joint-TCP consistency.
- Demonstrated superior performance on feature completion, conditioned visual forecasting, RGB-encoder transfer, and robot manipulation success.

## Open Questions & Future Work

- [[moving-camera-and-zero-shot-embodiment-transfer]]

## Key Concepts

- [[depstate-jepa]]: A dual-stream RGB-Depth joint-embedding predictive architecture that connects spatial understanding with action-conditioned prediction through a shared latent state called DepState.

## Archivist Review

Approved the central framework DepState-JEPA and the key open question on generalizability of visual world models under moving cameras and embodiment shifts, maintaining strict selectivity standards.

### Approved Concepts
- DepState-JEPA: Central framework proposed for learning depth-grounded state representations for visual perception and robot manipulation.

### Approved Open Questions
- Generalizing Visual World Models: Important for scaling visual world models to unconstrained environments where camera motion and morphological changes are prevalent.

## Links

- [Abstract](https://arxiv.org/abs/2610.29246)
- [PDF](https://arxiv.org/pdf/2610.29246)

