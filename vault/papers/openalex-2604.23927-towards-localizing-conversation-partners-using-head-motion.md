---
# CSL-compatible fields
title: "Towards Localizing Conversation Partners using Head Motion"
author:
  - literal: "Payal Mohapatra"
  - literal: "Calvin Murdock"
  - literal: "Ali Aroudi"
  - literal: "Ishwarya Ananthabhotla"
  - literal: "Anjali Menon"
  - literal: "Buye Xu"
  - literal: "Morteza Khaleghimeybodi"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.23927"

# Custom fields
paper_id: "2604.23927"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "time-series"
  - "speech"
  - "wearable"
architectures:
  []
datasets:
  []
concept_slugs:
  - "halo-head-orientation-acoustic-zone-localization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:25:38Z"
created_at: "2026-04-30T07:25:38Z"
---

# Towards Localizing Conversation Partners using Head Motion

**Authors**: Payal Mohapatra, Calvin Murdock, Ali Aroudi, Ishwarya Ananthabhotla, Anjali Menon, Buye Xu, Morteza Khaleghimeybodi
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.23927](https://arxiv.org/abs/2604.23927)

## Summary

This paper addresses the challenge of identifying a user's acoustic zone of interest in noisy environments for speech enhancement in smartglasses. The authors propose HALo, a network that leverages IMU-captured head orientation, and CoCo, a classifier for estimating the number of conversation partners. Their approach significantly outperforms spatial audio-only methods and baseline time-series classifiers, providing a more robust mechanism for active listening in social settings.

## Key Contributions

- Introduces HALo, a model for inferring auditory zones of interest using head-orientation IMU data.
- Introduces CoCo, a partner-count classifier that achieves a 35% gain over rule-based baselines.
- Demonstrates that head-orientation-based localization significantly improves speech enhancement in noisy multi-party environments.

## Open Questions & Future Work

- [[dynamic-acoustic-zone-localization-challenges]]

## Key Concepts

- [[halo-head-orientation-acoustic-zone-localization]]: A network that uses head-orientation IMU data to non-invasively infer a user's auditory zones of interest in multi-party conversations.

## Archivist Review

I have approved the HALo framework as it provides a distinct, reusable behavioral-cue-based approach for user-focus localization in wearable devices. I have also approved an open question regarding dynamic acoustic localization, as it addresses the core limitation of existing wearable-sensor methods when moving beyond static, controlled scenarios. The classification submodule (CoCo) was rejected as a subcomponent of the broader research goal rather than a standalone fundamental concept.

### Approved Concepts
- HALo (Head-Orientation Acoustic Zone Localization): HALo provides a novel approach for utilizing behavioral IMU head-tracking data to improve acoustic beamforming and focus in wearable devices.

### Approved Open Questions
- Dynamic Acoustic Zone Localization Challenges: Achieving robustness in real-world, non-ideal settings is a primary bottleneck for conversational AI wearables.

### Rejected Candidates
- [concept] CoCo (`coco-conversation-partner-counting-model`) - subcomponent_of_broader_mechanism: This is a specific classification module for partner counting that, while useful, is less fundamental than the primary localization framework (HALo).

## Links

- [Abstract](https://arxiv.org/abs/2604.23927)
- [PDF](https://arxiv.org/pdf/2604.23927)

