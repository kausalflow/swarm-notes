---
# CSL-compatible fields
title: "Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams"
author:
  - literal: "Zewen Liu"
  - literal: "Zhan Shi"
  - literal: "Yisi Sang"
  - literal: "Bing He"
  - literal: "Minhua Lin"
  - literal: "Tianxin Wei"
  - literal: "Dakuo Wang"
  - literal: "Benoit Dumoulin"
  - literal: "Wei Jin"
  - literal: "Hanqing Lu"
issued:
  date-parts:
    - [2026, 6, 1]
url: "https://arxiv.org/abs/2606.01770"

# Custom fields
paper_id: "2606.01770"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "agent"
  - "autonomous-agent"
  - "instruction-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-auto-harness"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-04T08:46:29Z"
created_at: "2026-06-04T08:46:29Z"
---

# Adaptive Auto-Harness: Sustained Self-Improvement for Agentic System Deployment on Open-Ended Task Streams

**Authors**: Zewen Liu, Zhan Shi, Yisi Sang, Bing He, Minhua Lin, Tianxin Wei, Dakuo Wang, Benoit Dumoulin, Wei Jin, Hanqing Lu
**Date**: 2026-06-01
**Paper ID**: [openalex:2606.01770](https://arxiv.org/abs/2606.01770)

## Summary

Adaptive Auto-Harness addresses the brittleness of traditional auto-harnessing systems when applied to open-ended task streams where task distributions shift over time. By decomposing the performance gap into evolution and adaptation losses, the framework leverages a stateful multi-agent evolver and a harness tree with solve-time routing to sustain agent performance. Experiments across diverse domains such as event forecasting and security competitions show the system maintains robustness where standard dense updates fail.

## Key Contributions

- Introduces the Adaptive Auto-Harness framework, which mitigates performance degradation in open-ended task streams by decomposing performance gaps into evolution and adaptation losses.
- Proposes a harness tree architecture with solve-time routing and a stateful multi-agent evolver to sustain agent performance under shifting task distributions.
- Demonstrates superior performance across prediction-market, security-competition, and event-forecasting streams compared to five existing auto-harness baselines.

## Open Questions & Future Work

- [[quantifying-auto-harness-evolution-adaptation-losses]]

## Key Concepts

- [[adaptive-auto-harness]]: A framework for sustained agent harness construction that decomposes performance gaps into evolution and adaptation losses, using a stateful multi-agent evolver and harness-tree routing.

## Archivist Review

I approved the Adaptive Auto-Harness framework and the associated open question regarding the formal estimation of evolution and adaptation losses. These concepts provide a structured, diagnostic way to handle non-stationary task streams in agentic systems, moving beyond simple static evaluation. I rejected no candidates as none were provided.

### Approved Concepts
- Adaptive Auto-Harness: Addresses the critical challenge of harness brittleness and performance degradation in open-ended task streams through task-wise adaptation and a harness tree structure.

### Approved Open Questions
- Direct Estimation of Auto-Harness Losses: Formalizing these losses into directly computable metrics would allow for automated, per-task diagnostics in real-world deployments, enabling systems to dynamically decide whether to invest more compute in evolving general capabilities or in improving solve-time routing strategies.

## Links

- [Abstract](https://arxiv.org/abs/2606.01770)
- [PDF](https://arxiv.org/pdf/2606.01770)

