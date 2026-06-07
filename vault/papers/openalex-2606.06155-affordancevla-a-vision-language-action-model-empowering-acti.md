---
# CSL-compatible fields
title: "AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding"
author:
  - literal: "Qize Yu"
  - literal: "Jiadi You"
  - literal: "Yuran Wang"
  - literal: "Jiaqi Liang"
  - literal: "Bowen Ping"
  - literal: "Yang Tian"
  - literal: "Yue Chen"
  - literal: "Minghong Cai"
  - literal: "Zeying Gong"
  - literal: "Ruihai Wu"
  - literal: "Yinchuan Li"
  - literal: "Junwei Liang"
  - literal: "Yingcong Chen"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06155"

# Custom fields
paper_id: "2606.06155"
paper_source: "openalex"
domain: "robotics"
tags:
  - "vision-language-model"
  - "vlm"
  - "robotics"
  - "mixture-of-experts"
  - "moe"
  - "transformer"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "affordance-forecasting-for-vla"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:20:35Z"
created_at: "2026-06-07T08:20:35Z"
---

# AffordanceVLA: A Vision-Language-Action Model Empowering Action Generation through Affordance-Aware Understanding

**Authors**: Qize Yu, Jiadi You, Yuran Wang, Jiaqi Liang, Bowen Ping, Yang Tian, Yue Chen, Minghong Cai, Zeying Gong, Ruihai Wu, Yinchuan Li, Junwei Liang, Yingcong Chen
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06155](https://arxiv.org/abs/2606.06155)

## Summary

AffordanceVLA is a novel vision-language-action (VLA) framework designed to address the structural mismatch between pretrained VLM semantic spaces and embodied control requirements. The model employs a three-part decomposition strategy—Which2Act, Where2Act, and How2Act—to generate spatially and semantically grounded affordance cues that guide manipulation policies. By integrating these modules into a Mixture-of-Transformer (MoT) architecture and using an automated data augmentation pipeline, the framework achieves robust performance in diverse robotic manipulation scenarios.

## Key Contributions

- Introduces AffordanceVLA, a unified VLA model utilizing affordance forecasting as an intermediate representation to bridge vision-language semantics and control policies.
- Decomposes manipulation into Which2Act (object grounding), Where2Act (interaction localization), and How2Act (geometric reasoning) to enhance precision.
- Employs a Mixture-of-Transformer (MoT) architecture with a progressive training curriculum to optimize the perception-action mapping.
- Develops an automated data augmentation pipeline to mitigate the scarcity of dense affordance labels in robotic datasets.

## Open Questions & Future Work

- [[long-horizon-planning-limitations-vla]]

## Key Concepts

- [[affordance-forecasting-for-vla]]: The use of structured affordance forecasting as an intermediate representation to align VLM semantics with embodied robotic control policies.

## Archivist Review

I approved the 'Affordance Forecasting for VLA' concept as it represents a generalizable architectural pattern for aligning VLMs with embodied control, and I approved the open question regarding long-horizon planning as it identifies a clear, persistent limitation in modern robotic foundation models. The model-specific name 'AffordanceVLA' was rejected in favor of the more descriptive and reusable mechanism it implements.

### Approved Concepts
- Affordance Forecasting for VLA: It provides a principled way to bridge the semantic-to-action gap in robotic models by injecting task-specific spatial grounding.

### Approved Open Questions
- Long-Horizon Planning in VLAs: Long-horizon manipulation is a critical frontier for moving from short-task instruction following to complex, multi-stage robotic autonomy.

### Rejected Candidates
- [concept] AffordanceVLA (`affordancevla`) - subcomponent_of_broader_mechanism: The core mechanism is better represented by the generic affordance forecasting approach rather than the specific model name.

## Links

- [Abstract](https://arxiv.org/abs/2606.06155)
- [PDF](https://arxiv.org/pdf/2606.06155)

