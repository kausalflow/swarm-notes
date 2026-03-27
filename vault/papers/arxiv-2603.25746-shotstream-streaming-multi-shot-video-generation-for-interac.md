---
# CSL-compatible fields
title: "ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling"
author:
  - literal: "Yawen Luo"
  - literal: "Xiaoyu Shi"
  - literal: "Junhao Zhuang"
  - literal: "Yutian Chen"
  - literal: "Quande Liu"
  - literal: "Xintao Wang"
  - literal: "Pengfei Wan"
  - literal: "Tianfan Xue"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25746"

# Custom fields
paper_id: "2603.25746"
paper_source: "arxiv"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "autoregressive"
  - "long-context"
  - "model-shot-generation"
  - "distillation"
  - "positional-encoding"
  - "efficient-transformer"
architectures:
  - "decoder-only"
datasets:
  []
skill: "GeneralMLSkill"
processed_at: "2026-03-27T06:06:58Z"
created_at: "2026-03-27T06:06:58Z"
---

# ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling

**Authors**: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue
**Date**: 2026-03-26
**Paper ID**: [arxiv:2603.25746](https://arxiv.org/abs/2603.25746)

## Summary

ShotStream introduces a novel causal, streaming architecture for multi-shot video generation specifically designed for interactive storytelling, addressing the latency and interactivity limitations of existing bidirectional models. The core idea involves fine-tuning a text-to-video model into a bidirectional next-shot generator, subsequently distilling it into an efficient causal student using Distribution Matching Distillation. To maintain visual quality, the method employs a dual-cache memory mechanism for inter-shot and intra-shot consistency, and a two-stage self-forcing distillation strategy to mitigate error accumulation common in autoregressive sequence modeling. The resulting model achieves high-quality, coherent video generation with sub-second latency, enabling real-time interactive narrative control.

## Key Contributions

- Proposing ShotStream, a novel causal multi-shot architecture that enables efficient, on-the-fly frame generation for interactive storytelling with sub-second latency.
- Introducing a dual-cache memory mechanism (global context cache and local context cache) alongside a RoPE discontinuity indicator to preserve visual coherence across and within shots, mitigating autoregressive error accumulation.
- Developing a two-stage distillation strategy involving intra-shot self-forcing followed by inter-shot self-forcing to effectively bridge the train-test gap and improve generation quality.
- Achieving competitive or superior video quality compared to slower bidirectional models while maintaining high frame rates (16 FPS on a single GPU) suitable for real-time interaction.

## Limitations

The paper does not explicitly detail limitations but the success relies on the effectiveness of the distillation process to overcome the inherent challenges of causal models in handling long-range dependencies compared to bidirectional ones.

## Open Questions & Future Work

- [[scaling-backbone-for-complex-scenarios]]
- [[acceleration-techniques-for-interactive-generation]]

## Key Concepts

- [Dual-Cache Memory Mechanism](../concepts/dual-cache-memory-mechanism.md): A mechanism combining a global context cache for inter-shot consistency and a local context cache for intra-shot consistency to maintain visual coherence in streaming video generation.
- [RoPE Discontinuity Indicator](../concepts/rope-discontinuity-indicator.md): A mechanism used to explicitly signal the boundary between different shots or context blocks within the input sequence to improve causal modeling accuracy.
- [Distribution Matching Distillation](../concepts/distribution-matching-distillation.md): A distillation technique used to transfer the generative capabilities from a larger, bidirectional teacher model to a smaller, causal student model by matching output distributions.

## Limitations

The paper does not explicitly detail limitations but the success relies on the effectiveness of the distillation process to overcome the inherent challenges of causal models in handling long-range dependencies compared to bidirectional ones.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.25746)
- [PDF](https://arxiv.org/pdf/2603.25746)

