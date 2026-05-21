---
# CSL-compatible fields
title: "4DLidarOpen: An Open 4D FMCW Lidar Dataset for Motion-Aware Autonomous Driving"
author:
  - literal: "Kane Qian"
  - literal: "Xin Zhao"
  - literal: "Yining Shi"
  - literal: "Rujun Yan"
  - literal: "Zhengqing Pan"
  - literal: "Kaojin Zhu"
  - literal: "Mengmeng Yang"
  - literal: "Kai Sun"
  - literal: "Diange Yang"
  - literal: "Kun Jiang"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18074"

# Custom fields
paper_id: "2605.18074"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "dataset"
  - "autonomous-agent"
  - "planning"
  - "object-detection"
  - "image-segmentation"
architectures:
  []
datasets:
  - "4DLidarOpen"
concept_slugs:
  - "4d-fmcw-lidar-perception"
dataset_slugs:
  - "4dlidaropen"
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:37:32Z"
created_at: "2026-05-21T08:37:32Z"
---

# 4DLidarOpen: An Open 4D FMCW Lidar Dataset for Motion-Aware Autonomous Driving

**Authors**: Kane Qian, Xin Zhao, Yining Shi, Rujun Yan, Zhengqing Pan, Kaojin Zhu, Mengmeng Yang, Kai Sun, Diange Yang, Kun Jiang
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18074](https://arxiv.org/abs/2605.18074)

## Summary

4DLidarOpen is a large-scale multimodal autonomous driving dataset featuring 4D FMCW Lidar, which provides additional point-wise radial velocity measurements alongside traditional geometric sensors. The dataset covers complex urban environments, including dense traffic and pedestrian interactions, with high-quality synchronized 3D bounding-box annotations and persistent track IDs. Experiments show that integrating velocity-aware data improves motion-related perception, forecasting, and planning compared to purely geometric sensing modalities. The release includes an evaluation toolkit to facilitate research in 4D scene understanding and motion-aware autonomous systems.

## Key Contributions

- Introduces 4DLidarOpen, a large-scale multimodal dataset for autonomous driving featuring 4D FMCW Lidar with point-wise radial velocity measurements.
- Establishes benchmarks for 3D object detection, BEV segmentation, flow prediction, and motion forecasting.
- Demonstrates that direct velocity measurements significantly improve performance in motion-related perception and planning for complex urban scenarios.

## Open Questions & Future Work

- [[optimal-heterogeneous-lidar-fusion-strategies]]

## Key Concepts

- [[4d-fmcw-lidar-perception]]: A motion-aware sensing modality providing direct point-wise radial velocity measurements for dynamic scene understanding.

## Archivist Review

I approved the '4D FMCW Lidar Perception' concept because it represents a distinct, emerging sensor paradigm shift towards motion-aware autonomous driving. The 4DLidarOpen dataset was approved as a core resource for evaluating this new modality. I also approved a refined open question regarding heterogeneous sensor fusion, as it addresses the core research challenge of integrating disparate sensor-driven motion cues in autonomous systems.

### Approved Concepts
- 4D FMCW Lidar Perception: Velocity-aware perception is an emerging paradigm shift for autonomous driving that will likely necessitate new sensor-fusion architectures.

### Approved Open Questions

## Datasets

- [[4dlidaropen]]

## Links

- [Abstract](https://arxiv.org/abs/2605.18074)
- [PDF](https://arxiv.org/pdf/2605.18074)

