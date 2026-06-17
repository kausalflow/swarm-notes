---
# CSL-compatible fields
title: "COMODO: Cross-Modal Video-to-IMU Distillation for Efficient Egocentric Human Activity Recognition"
author:
  - literal: "Baiyu Chen"
  - literal: "Wilson Wongso"
  - literal: "Zechen Li"
  - literal: "Yonchanok Khaokaew"
  - literal: "Hao Xue"
  - literal: "Flora D. Salim"
issued:
  date-parts:
    - [2026, 6, 15]
url: "https://arxiv.org/abs/2503.07259"

# Custom fields
paper_id: "2503.07259"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "self-supervised-learning"
  - "knowledge-distillation"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cross-modal-video-to-imu-distillation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:27:28Z"
created_at: "2026-06-17T09:27:28Z"
---

# COMODO: Cross-Modal Video-to-IMU Distillation for Efficient Egocentric Human Activity Recognition

**Authors**: Baiyu Chen, Wilson Wongso, Zechen Li, Yonchanok Khaokaew, Hao Xue, Flora D. Salim
**Date**: 2026-06-15
**Paper ID**: [openalex:2503.07259](https://arxiv.org/abs/2503.07259)

## Summary

COMODO is a self-supervised cross-modal distillation framework designed to bridge the gap between high-performance egocentric video-based activity recognition and efficient, privacy-preserving IMU sensing. By leveraging a frozen video encoder as a teacher and a dynamic instance queue for feature alignment, it allows an IMU student encoder to learn rich semantic structures without labeled data. Extensive experiments show that COMODO improves performance across various HAR datasets, achieving results competitive with fully supervised models.

## Key Contributions

- Proposes COMODO, a self-supervised cross-modal distillation framework that enables IMU-based models to leverage semantic knowledge from egocentric video encoders.
- Implements a dynamic instance queue mechanism for aligning the feature distributions of video and IMU embeddings without requiring paired activity labels.
- Demonstrates that COMODO-distilled models match or surpass fully supervised performance while maintaining the energy efficiency and privacy of IMU-based recognition.

## Open Questions & Future Work

- [[temporal-asynchronicity-in-cross-modal-distillation]]

## Key Concepts

- [[cross-modal-video-to-imu-distillation]]: A self-supervised framework for aligning and transferring learned semantic representations from frozen video encoders to efficient IMU-based time-series models.

## Archivist Review

I approved the cross-modal distillation concept as it provides a valuable framework for leveraging high-dimensional foundation models to guide efficient time-series learners. I also approved the open question concerning temporal asynchronicity, as it captures a critical real-world constraint for sensor-based HAR that future research must address. Other candidates were either redundant or too specific to the paper's naming conventions.

### Approved Concepts
- Cross-Modal Video-to-IMU Distillation: Provides a scalable approach for enriching time-series representations using latent semantic knowledge from video encoders, bypassing the need for expensive manual labeling in wearable HAR.

### Approved Open Questions
- Asynchronous Cross-Modal Distillation: Temporal alignment is a fundamental barrier to scaling cross-modal learning for in-the-wild wearable devices.

### Rejected Candidates
- [concept] COMODO Framework (`comodo-framework`) - subcomponent_of_broader_mechanism: The COMODO framework is a specific implementation of a broader class of cross-modal distillation methods; the proposed concept name is more descriptive of the actual mechanism.
- [open_question] Mutual Distillation in HAR (`mutual-distillation-for-egocentric-har`) - low_impact: The proposed open question is generic to distillation literature rather than being a specific, high-priority bottleneck identified for the time-series forecasting or HAR domains.

## Links

- [Abstract](https://arxiv.org/abs/2503.07259)
- [PDF](https://arxiv.org/pdf/2503.07259)

