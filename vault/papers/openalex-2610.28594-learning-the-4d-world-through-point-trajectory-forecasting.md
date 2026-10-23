---
# CSL-compatible fields
title: "Learning the 4D World through Point Trajectory Forecasting"
author:
  - literal: "Byungwoo Jeon"
  - literal: "Sunghwan Hong"
  - literal: "Dohyeon Kim"
  - literal: "Jonghoon Lee"
  - literal: "Jungwoo Park"
  - literal: "Inhee Lee"
  - literal: "Doosan Baek"
  - literal: "Jinil Kim"
  - literal: "Taehyun Lim"
  - literal: "Hanbyul Joo"
  - literal: "Marc Pollefeys"
  - literal: "Saining Xie"
  - literal: "Jinwoo Shin"
issued:
  date-parts:
    - [2026, 10, 20]
url: "https://arxiv.org/abs/2610.28594"

# Custom fields
paper_id: "2610.28594"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "autonomous-agent"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "video-point-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:40:11Z"
created_at: "2026-10-23T09:40:11Z"
---

# Learning the 4D World through Point Trajectory Forecasting

**Authors**: Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park, Inhee Lee, Doosan Baek, Jinil Kim, Taehyun Lim, Hanbyul Joo, Marc Pollefeys, Saining Xie, Jinwoo Shin
**Date**: 2026-10-20
**Paper ID**: [openalex:2610.28594](https://arxiv.org/abs/2610.28594)

## Summary

The authors introduce the Video-Point Model (VPM), a multi-view world model that jointly forecasts future videos and 3D persistent point trajectories conditioned on video histories and language instructions. By supervising 3D trajectories alongside video generation, VPM anchors appearance changes to a shared 3D motion description, improving both video fidelity and 3D motion accuracy. Additionally, the framework extends to robot control by integrating action tokens into the point-supervised generative backbone, enhancing manipulation success in simulated and real environments.

## Key Contributions

- Introduces Video-Point Model (VPM), a multi-view world model that jointly forecasts future videos from arbitrary viewpoints and 3D trajectories of persistent scene points conditioned on video histories and language instructions.
- Proposes camera-conditioned multi-view processing and a point trajectory head that anchors appearance changes across cameras to a shared 3D motion representation.
- Builds VPM-Data (a simulation corpus pairing multi-view videos with point trajectories) and VP-WorldBench for forecasting evaluation across simulated and real environments.
- Extends VPM to robot control by incorporating action tokens into the generator, showing that joint point supervision improves manipulation success in simulated and real-robot experiments.

## Open Questions & Future Work

- [[scaling-trajectory-supervision-real-world-videos]]

## Key Concepts

- [[video-point-model]]: A world model that conditions on multi-view video histories and language instruction to jointly forecast future videos from arbitrary viewpoints and 3D trajectories of persistent scene points.

## Archivist Review

Applied strict selection standards by approving only the overarching Video-Point Model concept and the fundamental open question regarding scaling trajectory supervision to unannotated real-world data. Newly introduced simulation corpora and benchmarks were excluded from the vault notes as they lack independent long-term reusability history at this stage.

### Approved Concepts
- Video-Point Model: VPM is the core model introduced in the paper, jointly forecasting multi-view future videos and 3D persistent point trajectories.

### Approved Open Questions
- Scaling Trajectory Supervision from Real Videos: Overcoming the dependency on simulation or synthetic datasets and pre-calibrated cameras is crucial for scaling world models and 4D trajectory forecasting to open-world, in-the-wild video data.

## Links

- [Abstract](https://arxiv.org/abs/2610.28594)
- [PDF](https://arxiv.org/pdf/2610.28594)

