---
# CSL-compatible fields
title: "TPS-Drive: Task-Guided Representation Purification for VLM-based Autonomous Driving"
author:
  - literal: "Jiaxiang Li"
  - literal: "Yumao Liu"
  - literal: "Ke Ma"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27038"

# Custom fields
paper_id: "2605.27038"
paper_source: "openalex"
domain: "robotics"
tags:
  - "multimodal"
  - "vision-language-model"
  - "autonomous-agent"
  - "planning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "task-guided-representation-purification"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:39:05Z"
created_at: "2026-05-29T08:39:05Z"
---

# TPS-Drive: Task-Guided Representation Purification for VLM-based Autonomous Driving

**Authors**: Jiaxiang Li, Yumao Liu, Ke Ma
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27038](https://arxiv.org/abs/2605.27038)

## Summary

TPS-Drive addresses the challenges of bridging semantic reasoning and 3D spatial forecasting in vision-language models for autonomous driving. By replacing standard tokenization with an agent-centric, task-guided vector quantization approach, the framework purifies spatial representations by prioritizing critical dynamic entities over redundant background textures. This results in more accurate agent state forecasting and improved safety, as demonstrated by the framework's performance on the nuScenes, NAVSIMv1, and NAVSIMv2 benchmarks.

## Key Contributions

- Introduces TPS-Drive, a VLM-based autonomous driving framework that utilizes task-guided representation purification to mitigate spatial hallucinations and representation interference.
- Develops an Agent-Centric Tokenizer that reallocates codebook capacity to dynamic agents via a task-guided vector quantization mechanism supervised by a frozen 3D detection head.
- Demonstrates superior performance in open-loop nuScenes evaluations and establishes new safety records on closed-loop NAVSIMv1 and NAVSIMv2 benchmarks.

## Open Questions & Future Work

- [[vlm-autonomous-driving-spatial-real-time-bottleneck]]

## Key Concepts

- [[task-guided-representation-purification]]: A representation purification framework that uses task-guided vector quantization to compress spatial information for autonomous driving agents.

## Archivist Review

I approved the core concept of task-guided representation purification because it offers a novel, reusable strategy for tokenizing dense spatial data in VLMs. I also approved an open question regarding the latency and architectural bottlenecks inherent in these VLM-based driving frameworks. Standard benchmark datasets (nuScenes, NAVSIM) were rejected to maintain a high entry barrier for the knowledge vault.

### Approved Concepts
- Task-Guided Representation Purification: This core mechanism addresses the spatial information loss and representation interference inherent in current VLM-based autonomous driving by reallocating token capacity to dynamic agents.

### Approved Open Questions
- VLM Autonomous Driving Bottlenecks: The trade-off between semantic reasoning capability and real-time spatial processing efficiency is a foundational bottleneck for deploying VLM-based planners in practical, safety-critical autonomous driving systems.

### Rejected Candidates
- [dataset] nuScenes (`nuscenes`) - duplicate_existing: nuScenes is an existing, widely-used dataset and does not require a standalone vault entry.
- [dataset] NAVSIMv1 (`navsimv1`) - not_novel: This is a routine benchmark dataset that does not meet the high threshold for vault inclusion.
- [dataset] NAVSIMv2 (`navsimv2`) - not_novel: This is a routine benchmark dataset that does not meet the high threshold for vault inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2605.27038)
- [PDF](https://arxiv.org/pdf/2605.27038)

