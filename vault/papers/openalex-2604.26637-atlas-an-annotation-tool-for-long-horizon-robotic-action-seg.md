---
# CSL-compatible fields
title: "ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation"
author:
  - literal: "Sergej Stanovcic"
  - literal: "Daniel Sliwowski"
  - literal: "Dongheui Lee"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26637"

# Custom fields
paper_id: "2604.26637"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "dataset"
architectures:
  []
datasets:
  - "REASSEMBLE"
concept_slugs:
  - "atlas-annotation-tool"
dataset_slugs:
  - "reassemble"
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:56:37Z"
created_at: "2026-05-02T06:56:37Z"
---

# ATLAS: An Annotation Tool for Long-horizon Robotic Action Segmentation

**Authors**: Sergej Stanovcic, Daniel Sliwowski, Dongheui Lee
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26637](https://arxiv.org/abs/2604.26637)

## Summary

ATLAS is a specialized annotation tool designed to streamline the labeling of long-horizon robotic demonstrations by integrating multi-view video with synchronized proprioceptive time-series data. By offering a modular dataset abstraction layer that handles standard formats like ROS bags and RLDS, it significantly lowers the barrier for preparing high-quality data for manipulation policy learning. Empirical evaluation demonstrates that this multi-modal approach substantially increases both the speed and temporal precision of action boundary segmentation compared to traditional vision-only tools.

## Key Contributions

- ATLAS enables time-synchronized visualization of multi-view video and proprioceptive signals for efficient robotic action labeling.
- The tool incorporates a modular dataset abstraction layer that natively supports ROS bags and RLDS formats, facilitating cross-dataset adoption.
- Experiments on the REASSEMBLE dataset show that ATLAS reduces per-action annotation time by at least 6% and improves temporal boundary accuracy by fivefold compared to vision-only tools.

## Open Questions & Future Work

- [[cognitive-load-vs-interface-in-annotation]]

## Key Concepts

- [[atlas-annotation-tool]]: A modular, keyboard-centric annotation tool for synchronized multi-modal robotic long-horizon action segmentation.

## Archivist Review

The approved tool and dataset represent significant contributions to the robotics pipeline for data curation, while the open question addresses the essential trade-off between annotation accuracy and human cognitive burden. I applied a strict filter to ensure only the core framework and relevant dataset were kept, rejecting sub-components or generic tool features.

### Approved Concepts
- ATLAS Annotation Tool: It addresses the critical bottleneck of synchronized multi-modal annotation in robotics, providing a reusable framework for handling heterogeneous data formats like ROS bags and RLDS.

### Approved Open Questions
- Annotation cognitive load bottleneck: Identifying whether the slowdown is caused by cognitive load or interface limitations is critical for balancing annotation efficiency with the precision provided by multi-modal sensor data in robotics research.

## Datasets

- [[reassemble]]

## Links

- [Abstract](https://arxiv.org/abs/2604.26637)
- [PDF](https://arxiv.org/pdf/2604.26637)

