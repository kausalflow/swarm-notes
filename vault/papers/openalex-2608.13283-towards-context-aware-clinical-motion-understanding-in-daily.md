---
# CSL-compatible fields
title: "Towards Context-Aware Clinical Motion Understanding in Daily Living at Home: Freezing of Gait Detection with Egocentric Vision"
author:
  - literal: "Vayalet Stefanova"
  - literal: "Diwas Lamsal"
  - literal: "Margot Genbrugge"
  - literal: "Maxim Yudayev"
  - literal: "Christian Schlenstedt"
  - literal: "Moran Gilat"
  - literal: "Bart Vanrumste"
  - literal: "Benjamin Filtjens"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13283"

# Custom fields
paper_id: "2608.13283"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "time-series"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:21:03Z"
created_at: "2026-08-16T05:21:03Z"
---

# Towards Context-Aware Clinical Motion Understanding in Daily Living at Home: Freezing of Gait Detection with Egocentric Vision

**Authors**: Vayalet Stefanova, Diwas Lamsal, Margot Genbrugge, Maxim Yudayev, Christian Schlenstedt, Moran Gilat, Bart Vanrumste, Benjamin Filtjens
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13283](https://arxiv.org/abs/2608.13283)

## Summary

This paper investigates context-aware clinical motion understanding for freezing of gait (FOG) in Parkinson's disease during daily living at home, utilizing synchronized egocentric video and wearable IMU data from 13 participants. Evaluating pretrained ego-video models alongside time-series models and an IMU-based TCN under leave-one-subject-out evaluation, the authors find that the IMU-based TCN outperforms video-only features (42.3 vs 32.6 F1), though qualitative analysis indicates that ego-video captures complementary, FOG-relevant context.

## Key Contributions

- Investigates context-aware clinical motion understanding for freezing of gait (FOG) in Parkinson's disease using synchronized egocentric video and wearable IMUs collected in home environments from 13 participants.
- Evaluates pretrained ego-video foundation models (such as V-JEPA2) and time-series representations alongside an IMU-based TCN under leave-one-subject-out cross-validation.
- Demonstrates that an IMU-based TCN achieves superior event-detection performance (42.3 F1, 83.0 AUROC) compared to egocentric video features (32.6 F1, 77.2 AUROC), while qualitative analyses reveal ego-video captures FOG-relevant context independent of inertial sensors.

## Limitations

Egocentric vision alone underperformed dedicated IMU-based sensing for FOG detection, though it holds potential for supplementary context.

## Open Questions & Future Work

- [[interpreting-egocentric-vision-signals]]

## Archivist Review

Evaluated the paper against vault standards, approving the open question on egocentric vision interpretation while keeping concepts and datasets empty due to lack of distinct methodological novelty.

### Approved Open Questions
- Interpreting Egocentric Vision Signals: Understanding the precise nature of features extracted from egocentric foundation models is vital for building robust multimodal healthcare and motion monitoring systems.

### Rejected Candidates
- [open_question] Interpreting Egocentric Vision Signals (`interpreting-egocentric-vision-signals`) - duplicate_existing: Duplicate of existing open questions regarding interpretability and multimodal feature attribution in time-series and video domains.

## Links

- [Abstract](https://arxiv.org/abs/2608.13283)
- [PDF](https://arxiv.org/pdf/2608.13283)

