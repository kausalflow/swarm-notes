---
# CSL-compatible fields
title: "FMplex: Model Virtualization for Serving Extensible Foundation Models"
author:
  - literal: "Hetvi Shastri"
  - literal: "Pragya Sharma"
  - literal: "Walid A. Hanafy"
  - literal: "David Irwin"
  - literal: "Mani Srivastava"
  - literal: "Prashant Shenoy"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09643"

# Custom fields
paper_id: "2606.09643"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "multimodal"
  - "vision-language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fmplex"
  - "virtual-foundation-model-vfm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:08:04Z"
created_at: "2026-06-11T09:08:04Z"
---

# FMplex: Model Virtualization for Serving Extensible Foundation Models

**Authors**: Hetvi Shastri, Pragya Sharma, Walid A. Hanafy, David Irwin, Mani Srivastava, Prashant Shenoy
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09643](https://arxiv.org/abs/2606.09643)

## Summary

FMplex is a foundation model serving system that addresses the inefficiencies of independent model deployment by virtualizing model backbones. It introduces the virtual foundation model (vFM) abstraction, which provides task-specific isolation and independent lifecycle management while sharing a single underlying physical backbone. To optimize performance, FMplex utilizes a batch-aware fair-queueing scheduler that coordinates cross-task batching, significantly improving both latency and cluster-scale task density across diverse foundation model variants.

## Key Contributions

- Introduced FMplex, a virtualization-based model serving system that enables multiple downstream tasks to share a single physical foundation model backbone.
- Developed the virtual foundation model (vFM) abstraction to provide task-level isolation and independent lifecycles while maintaining shared resource utilization.
- Designed a batch-aware fair-queueing scheduler that integrates weighted task-level sharing with inter- and intra-task batching to optimize throughput and latency.
- Demonstrated significant performance improvements, including an 80% reduction in latency compared to spatial partitioning and a 6x increase in task density at cluster scale.

## Key Concepts

- [[fmplex]]: A serving system that virtualizes foundation model backbones to allow shared deployment across multiple independent downstream tasks.
- [[virtual-foundation-model-vfm]]: A logical abstraction that provides tasks with the appearance of a private foundation model instance while leveraging a shared underlying physical backbone.

## Archivist Review

Approved the core serving system and its primary abstraction, as they define a novel paradigm for foundation model deployment that is likely to become a standard reference for resource-efficient LLM serving. No open questions or datasets were identified that meet the strict requirements for standalone archival notes.

### Approved Concepts
- FMplex: Central system architecture introduced to enable model virtualization for foundation models.
- virtual foundation model (vFM): Core abstraction provided to users, separating logical task privacy from physical resource sharing.

## Links

- [Abstract](https://arxiv.org/abs/2606.09643)
- [PDF](https://arxiv.org/pdf/2606.09643)

