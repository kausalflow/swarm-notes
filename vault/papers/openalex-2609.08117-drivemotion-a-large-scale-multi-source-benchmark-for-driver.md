---
# CSL-compatible fields
title: "DriveMotion: A Large-Scale Multi-Source Benchmark for Driver Motion Sequence Modeling and Forecasting"
author:
  - literal: "Yuhang Wang"
  - literal: "Chuheng Wei"
  - literal: "Jingxin Yang"
  - literal: "Xishun Liao"
  - literal: "Hao Zhou"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08117"

# Custom fields
paper_id: "2609.08117"
paper_source: "openalex"
domain: "robotics"
tags:
  - "benchmark"
  - "dataset"
  - "evaluation"
  - "multimodal"
architectures:
  []
datasets:
  - "drivemotion"
concept_slugs:
  []
dataset_slugs:
  - "drivemotion"
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:16:54Z"
created_at: "2026-09-10T09:16:54Z"
---

# DriveMotion: A Large-Scale Multi-Source Benchmark for Driver Motion Sequence Modeling and Forecasting

**Authors**: Yuhang Wang, Chuheng Wei, Jingxin Yang, Xishun Liao, Hao Zhou
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08117](https://arxiv.org/abs/2609.08117)

## Summary

This paper introduces DriveMotion, a large-scale multi-source benchmark for continuous driver motion sequence modeling and forecasting, integrating 393 hours of 133-keypoint motion sequences from 360 drivers. To overcome the limitation where naturalistic driving consists largely of static periods, the authors propose a dynamics-anchored evaluation strategy that targets forecasting windows around vehicle maneuvers identified from CAN signals. Extensive experiments show that learned models trained on the unified multi-source corpus achieve significantly improved forecasting accuracy and behavior prediction over persistence baselines.

## Key Contributions

- Introduces DriveMotion, a large-scale multi-source benchmark comprising 393 hours of 133-keypoint continuous driver motion sequences from 360 drivers at 10 Hz.
- Proposes dynamics-anchored evaluation, which positions forecasting evaluation windows around vehicle maneuvers identified via CAN signals without requiring CAN signals at inference time.
- Demonstrates that training on the full multi-source corpus reduces forecasting error on held-out web drivers by 38% compared to single-source training.

## Archivist Review

Applied rigorous selectivity rules for the ML vault. No generic concepts qualified. Approved one high-quality dataset note for DriveMotion while rejecting the paper-internal open question as task-local.

### Rejected Candidates
- [open_question] Bridging Ranked and Decoded Motion States (`bridging-ranked-and-decoded-motion-states-in-driver-forecasting`) - paper_local: The open question is paper-internal and speculative regarding specific driver motion modeling architectures.

## Datasets

- [[drivemotion]]

## Links

- [Abstract](https://arxiv.org/abs/2609.08117)
- [PDF](https://arxiv.org/pdf/2609.08117)

