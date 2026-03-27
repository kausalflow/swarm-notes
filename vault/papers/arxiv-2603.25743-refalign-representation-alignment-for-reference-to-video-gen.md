---
# CSL-compatible fields
title: "RefAlign: Representation Alignment for Reference-to-Video Generation"
author:
  - literal: "Lei Wang"
  - literal: "YuXin Song"
  - literal: "Ge Wu"
  - literal: "Haocheng Feng"
  - literal: "Hang Zhou"
  - literal: "Jingdong Wang"
  - literal: "Yaxing Wang"
  - literal: "jian Yang"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25743"

# Custom fields
paper_id: "2603.25743"
paper_source: "arxiv"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "multimodal"
  - "vision-language-model"
  - "embedding"
  - "evaluation"
  - "alignment"
architectures:
  - "diffusion-model"
datasets:
  - "OpenS2V-Eval"
skill: "GeneralMLSkill"
processed_at: "2026-03-27T06:07:04Z"
created_at: "2026-03-27T06:07:04Z"
---

# RefAlign: Representation Alignment for Reference-to-Video Generation

**Authors**: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25743](https://arxiv.org/abs/2603.25743)

## Summary

This paper introduces RefAlign, a novel representation alignment framework designed to improve Reference-to-Video (R2V) generation by explicitly aligning features within the diffusion process. RefAlign addresses fidelity issues like copy-paste artifacts by leveraging a Visual Foundation Model (VFM) to guide the alignment of the Diffusion Transformer's (DiT) reference-branch features in the semantic space. The core mechanism is a custom loss function that enforces feature consistency by pulling corresponding features together and pushing unrelated features apart, which is applied only during training. Experiments on the OpenS2V-Eval benchmark show that RefAlign surpasses current state-of-the-art methods in TotalScore, successfully balancing text controllability with reference identity preservation.

## Key Contributions

- Proposed RefAlign, a training-only framework for Reference-to-Video (R2V) generation that explicitly aligns the Diffusion Transformer (DiT) reference-branch features with the semantic space of a Visual Foundation Model (VFM).
- Introduced a reference alignment loss that simultaneously minimizes the distance between same-subject features and maximizes the distance between different-subject features, enhancing identity consistency and semantic discriminability.
- Achieved state-of-the-art performance on the OpenS2V-Eval benchmark in terms of TotalScore, demonstrating superior balance between text controllability and reference fidelity compared to existing R2V methods.
- The alignment strategy is applied solely during training, resulting in zero inference-time overhead.

## Limitations

The abstract does not explicitly detail limitations, but the framework's reliance on a pre-trained VFM for feature alignment suggests potential dependency on the VFM's capabilities and inherent biases. Future work may explore domain generalization across different VFMs.

## Open Questions & Future Work

- [[r2v-data-diversity-tradeoff]]
- [[extend-r2v-to-long-videos]]
- [[multi-vfm-alignment-targets]]
- [[unified-modeling-for-video-understanding-generation]]

## Key Concepts

- [Reference Alignment Loss](../concepts/reference-alignment-loss.md): A novel loss function used in RefAlign that explicitly pulls reference features closer to visual foundation model features of the same subject and pushes them apart for different subjects.

## Datasets

- [OpenS2V-Eval](../datasets/opens2v-eval.md)

## Limitations

The abstract does not explicitly detail limitations, but the framework's reliance on a pre-trained VFM for feature alignment suggests potential dependency on the VFM's capabilities and inherent biases. Future work may explore domain generalization across different VFMs.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25743)
- [PDF](https://arxiv.org/pdf/2603.25743)

