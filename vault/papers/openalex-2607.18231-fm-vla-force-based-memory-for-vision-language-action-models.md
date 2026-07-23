---
# CSL-compatible fields
title: "FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation"
author:
  - literal: "Ruicheng Li"
  - literal: "Qixiu Li"
  - literal: "Ru Z"
  - literal: "Yu Deng"
  - literal: "Lin Luo"
  - literal: "Zhiying Du"
  - literal: "Jianfeng Xiang"
  - literal: "Huizhi Liang"
  - literal: "Ruicheng Wang"
  - literal: "Jiaolong Yang"
  - literal: "B. Guo"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.18231"

# Custom fields
paper_id: "2607.18231"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "robotics"
  - "reinforcement-learning"
  - "transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:36Z"
created_at: "2026-07-23T07:27:36Z"
---

# FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

**Authors**: Ruicheng Li, Qixiu Li, Ru Z, Yu Deng, Lin Luo, Zhiying Du, Jianfeng Xiang, Huizhi Liang, Ruicheng Wang, Jiaolong Yang, B. Guo
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.18231](https://arxiv.org/abs/2607.18231)

## Summary

Vision-language-action (VLA) models often struggle in contact-rich tasks where temporal events are visually ambiguous or non-Markovian. To address this, the authors propose FM-VLA, which integrates a force-based memory mechanism using a VAE to encode force histories into compact conditioning tokens. By feeding these force latent representations into the action expert module, FM-VLA successfully reasons over contact event history in tasks like button pressing and dish wiping with minimal inference overhead.

## Key Contributions

- Proposed FM-VLA, a vision-language-action model integrating force-based memory for contact-rich robotic manipulation.
- Employs a VAE pretrained with force time series reconstruction to encode force histories into compact memory tokens.
- Achieves over 80% success rate on three memory-dependent tasks (finding a hidden block, pressing a button, wiping a dish) with minimal inference overhead compared to vision-based memory approaches.

## Archivist Review

The submitted candidate addresses robotic VLA force memory compression, which falls outside the core forecasting, modeling, and general time-series analysis scope of the vault. Therefore, the candidate was rejected.

### Rejected Candidates
- [open_question] Hierarchical Force Memory Compression (`hierarchical-adaptive-force-compression`) - low_impact: Future work proposing hierarchical compression for VLA force memory is specific to robotic manipulation and does not directly address core time-series forecasting, anomaly detection, or statistical modeling challenges.

## Links

- [Abstract](https://arxiv.org/abs/2607.18231)
- [PDF](https://arxiv.org/pdf/2607.18231)

