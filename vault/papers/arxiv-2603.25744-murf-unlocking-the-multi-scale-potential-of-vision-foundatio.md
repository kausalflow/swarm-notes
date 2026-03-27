---
# CSL-compatible fields
title: "MuRF: Unlocking the Multi-Scale Potential of Vision Foundation Models"
author:
  - literal: "Bocheng Zou"
  - literal: "Mu Cai"
  - literal: "Mark Stanley"
  - literal: "Dingfu Lu"
  - literal: "Yong Jae Lee"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25744"

# Custom fields
paper_id: "2603.25744"
paper_source: "arxiv"
domain: "computer-vision"
tags:
  - "vision-transformer"
  - "multimodal"
  - "self-supervised-learning"
  - "efficient-transformer"
  - "evaluation"
  - "dino"
architectures:
  []
datasets:
  []
skill: "GeneralMLSkill"
processed_at: "2026-03-27T06:07:00Z"
created_at: "2026-03-27T06:07:00Z"
---

# MuRF: Unlocking the Multi-Scale Potential of Vision Foundation Models

**Authors**: Bocheng Zou, Mu Cai, Mark Stanley, Dingfu Lu, Yong Jae Lee
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25744](https://arxiv.org/abs/2603.25744)

## Summary

This paper introduces Multi-Resolution Fusion (MuRF), a training-free inference-time strategy designed to overcome the limitations of single-scale processing in Vision Foundation Models (VFMs). MuRF leverages the complementary nature of visual information across scales by processing an input image at multiple resolutions using a frozen VFM. The resulting features from these different views are then fused to create a unified, richer representation. The authors validate MuRF's universal applicability by successfully enhancing performance across various computer vision tasks using different VFM architectures, such as DINOv2 and SigLIP2.

## Key Contributions

- Proposed MuRF, a training-free, architecture-agnostic inference-time strategy for Vision Foundation Models that fuses features derived from multi-scale processing of the input image.
- Demonstrated MuRF's universal effectiveness across a broad spectrum of computer vision tasks using diverse VFM families, including DINOv2 and SigLIP2.
- Showcased that combining low-resolution (global semantics) and high-resolution (fine-grained detail) views via MuRF unlocks complementary inductive biases inherent in visual perception.

## Limitations

The primary limitation is the increased inference cost due to processing the same image multiple times at different resolutions, which must be balanced against the performance gains.

## Key Concepts

- [Multi-Resolution Fusion (MuRF)](../concepts/multi-resolution-fusion-murf.md): A training-free, universally applicable strategy that processes an image at multiple resolutions through a frozen Vision Foundation Model (VFM) and fuses the resulting features to enhance visual representations.

## Limitations

The primary limitation is the increased inference cost due to processing the same image multiple times at different resolutions, which must be balanced against the performance gains.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25744)
- [PDF](https://arxiv.org/pdf/2603.25744)

