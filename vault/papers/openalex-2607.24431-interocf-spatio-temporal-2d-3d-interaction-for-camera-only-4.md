---
# CSL-compatible fields
title: "InterOCF: Spatio-Temporal 2D-3D Interaction for Camera-Only 4D Occupancy Forecasting"
author:
  - literal: "Qi Zhang"
  - literal: "Xinquan Yu"
  - literal: "Kaiyi Zhang"
  - literal: "Hui Huang"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24431"

# Custom fields
paper_id: "2607.24431"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "multimodal"
  - "object-detection"
  - "autonomous-agent"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "interocf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:26:42Z"
created_at: "2026-07-30T07:26:42Z"
---

# InterOCF: Spatio-Temporal 2D-3D Interaction for Camera-Only 4D Occupancy Forecasting

**Authors**: Qi Zhang, Xinquan Yu, Kaiyi Zhang, Hui Huang
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24431](https://arxiv.org/abs/2607.24431)

## Summary

Camera-only 4D occupancy forecasting aims to predict future 3D semantic scenes from historical multi-view images, but existing methods often under-explore spatio-temporal modeling between frames. This paper introduces InterOCF, a novel framework that jointly models temporal dynamics in 3D voxel representations and multi-view segmentation sequences while explicitly coupling them via 2D-3D feature interaction. The framework consists of a 3D Spatio-Temporal module for volumetric forecasting, a 2D Spatio-Temporal module with auxiliary segmentation forecasting, and a Spatio-Temporal Interaction Modeling module. Experiments on nuScenes, Lyft-Level5, and nuScenes-Occupancy show that InterOCF outperforms existing baselines.

## Key Contributions

- Proposes InterOCF, a novel framework for camera-only 4D occupancy forecasting that jointly models temporal dynamics in 3D voxel-based representations and 2D multi-view segmentation sequences.
- Introduces a 3D Spatio-Temporal (3DST) module to learn volumetric dynamics from historical voxel states for future prediction.
- Incorporates a 2D Spatio-Temporal (2DST) module with an auxiliary temporal segmentation forecasting task to enhance temporal semantic dynamics.
- Designs a Spatio-Temporal Interaction Modeling (STIM) module enabling explicit cross-branch feature interaction between 2D and 3D representations.
- Demonstrates consistent performance improvements over existing baseline approaches across multiple autonomous driving datasets.

## Open Questions & Future Work

- [[long-term-2d-3d-occupancy-forecasting]]

## Key Concepts

- [[interocf]]: A camera-only 4D occupancy forecasting framework that jointly models temporal dynamics across 3D voxel and 2D multi-view segmentation branches.

## Archivist Review

Approved the InterOCF framework concept and the corresponding open question on long-term 2D-3D occupancy forecasting consistency. Standard autonomous driving datasets were rejected as they are already tracked in the vault.

### Approved Concepts
- InterOCF: Introduces a novel framework for camera-only 4D occupancy forecasting by explicitly incorporating spatio-temporal interaction between 2D and 3D branches.

### Approved Open Questions
- Long-Term 2D-3D Occupancy Forecasting: Crucial for pushing the accuracy limits of vision-based forecasting and reducing error accumulation over extended temporal horizons in autonomous driving.

### Rejected Candidates
- [dataset] nuScenes (`nuscenes`) - duplicate_existing: Standard existing dataset in autonomous driving; rejected per guideline to avoid routine dataset redundancy.
- [dataset] Lyft-Level5 (`lyft-level5`) - duplicate_existing: Standard existing dataset in autonomous driving; rejected per guideline to avoid routine dataset redundancy.

## Links

- [Abstract](https://arxiv.org/abs/2607.24431)
- [PDF](https://arxiv.org/pdf/2607.24431)

