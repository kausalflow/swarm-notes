---
# CSL-compatible fields
title: "OpenWatch: A Multimodal Benchmark for Hand Gesture Recognition on Smartwatches"
author:
  - literal: "Pietro Bonazzi"
  - literal: "Youssef Ahmed"
  - literal: "Daniel Eckert"
  - literal: "Andrea Ronco"
  - literal: "Junjie Zeng"
  - literal: "Dengxin Dai"
  - literal: "Michele Magno"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04791"

# Custom fields
paper_id: "2605.04791"
paper_source: "openalex"
domain: "speech"
tags:
  - "multimodal"
  - "time-series"
  - "lora"
  - "benchmark"
  - "dataset"
  - "mixture-of-experts"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mixtoken"
  - "normwear-lora"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:03:08Z"
created_at: "2026-05-09T07:03:08Z"
---

# OpenWatch: A Multimodal Benchmark for Hand Gesture Recognition on Smartwatches

**Authors**: Pietro Bonazzi, Youssef Ahmed, Daniel Eckert, Andrea Ronco, Junjie Zeng, Dengxin Dai, Michele Magno
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04791](https://arxiv.org/abs/2605.04791)

## Summary

OpenWatch is the first multimodal benchmark for wrist-based gesture recognition, featuring 10 hours of synchronized IMU and PPG data from 50 participants across 59 gesture categories. The authors demonstrate that adding PPG signals improves F1-scores by 12.5% for foundation models. They further propose two novel methods, MixToken and NormWear-Lora, to address resource-constrained environments, showing that specialized task-specific architectures can achieve superior performance and memory efficiency compared to fine-tuning general foundation models.

## Key Contributions

- Introduces OpenWatch, the first open-access multimodal benchmark for wrist-based gesture recognition with 10 hours of synchronized IMU and PPG data.
- Proposes MixToken, a mixture-of-experts architecture achieving 90% F1-score with 223k parameters, significantly outperforming foundation model fine-tuning.
- Develops NormWear-Lora for efficient adaptation of smartwatch foundation models and provides empirical guidance on modality fusion and architectural trade-offs.

## Open Questions & Future Work

- [[wearable-gesture-personalization]]
- [[in-the-wild-gesture-robustness]]

## Key Concepts

- [[mixtoken]]: A task-specific mixture-of-experts architecture that fuses per-channel IMU filterbank features with cross-channel statistical tokens through learned logit mixing for gesture recognition.
- [[normwear-lora]]: A low-rank adaptation module specifically optimized for adapting smartwatch-scale foundation models.

## Archivist Review

I have approved the two methodologies proposed as they represent modular, reusable architectural patterns for resource-constrained wearable time-series analysis. I have approved two open questions that specifically target the critical bottlenecks of personalization and longitudinal robustness in wearable computing, which are vital for transitioning from benchmarking to deployment. I rejected the dataset because while OpenWatch is a useful benchmark, it does not currently exhibit the cross-paper traction or distinct impact level required for a standalone vault entry.

### Approved Concepts
- MixToken: Provides a memory-efficient mixture-of-experts approach to wearable time-series classification, addressing resource-constrained deployment needs.
- NormWear-Lora: Offers a specialized approach to low-rank adaptation specifically tuned for the constraints of wearable foundation models.

### Approved Open Questions
- Personalization for Gesture Recognition: Personalization is a critical bottleneck for making gesture recognition functional across diverse populations and reducing per-user calibration requirements.
- Robustness in Wild Deployment: Robustness to longitudinal drift and expanded gesture sets is essential for transitioning wearable interfaces from benchmarks to reliable everyday utilities.

## Links

- [Abstract](https://arxiv.org/abs/2605.04791)
- [PDF](https://arxiv.org/pdf/2605.04791)

