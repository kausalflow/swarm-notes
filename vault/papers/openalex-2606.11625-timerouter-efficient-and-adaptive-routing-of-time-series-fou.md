---
# CSL-compatible fields
title: "TimeRouter: Efficient and Adaptive Routing of Time-Series Foundation Models"
author:
  - literal: "Kanghui Ning"
  - literal: "Yushan Jiang"
  - literal: "Kashif Rasul"
  - literal: "Anderson Schneider"
  - literal: "Yuriy Nevmyvaka"
  - literal: "Dongjin Song"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.11625"

# Custom fields
paper_id: "2606.11625"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "timerouter-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:15:49Z"
created_at: "2026-06-13T08:15:49Z"
---

# TimeRouter: Efficient and Adaptive Routing of Time-Series Foundation Models

**Authors**: Kanghui Ning, Yushan Jiang, Kashif Rasul, Anderson Schneider, Yuriy Nevmyvaka, Dongjin Song
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.11625](https://arxiv.org/abs/2606.11625)

## Summary

TimeRouter is a lightweight and efficient routing framework designed to optimize the use of time-series foundation models (TSFMs) by adaptively selecting the best expert for specific forecasting regimes. By replacing expensive LLM-based controllers with a discriminative routing head, selective gate, and ensemble fallback mechanism, the system minimizes inference overhead. The approach achieves state-of-the-art results on the GIFT-EVAL benchmark, providing a practical, modular solution for integrating multiple TSFMs into agentic time-series systems.

## Key Contributions

- Proposes TimeRouter, an efficient framework for routing requests across a pool of pretrained time-series foundation models (TSFMs).
- Achieves state-of-the-art performance on the GIFT-EVAL leaderboard with an LB MASE of 0.6765.
- Demonstrates that lightweight discriminative routing and selective gating enable adaptive expert selection without the high inference overhead of LLM-based controllers.

## Open Questions & Future Work

- [[adaptive-tsfm-expert-routing-scaling]]

## Key Concepts

- [[timerouter-framework]]: A modular routing framework that uses discriminative routing and selective gating to coordinate a pool of time-series foundation models without LLM inference overhead.

## Archivist Review

I have approved the TimeRouter Framework as a novel routing approach that replaces heavy LLM-based orchestration with lightweight discriminative routing. I also identified a key open question regarding the scaling and automation of expert routing in TSFM ensembles, which is currently a bottleneck for deployment. Generic terms were rejected, and existing datasets were ignored per the policy to limit dataset notes.

### Approved Concepts
- TimeRouter Framework: Introduces a modular, lightweight alternative to expensive LLM-based controllers for coordinating heterogeneous time-series foundation models.

### Approved Open Questions
- Scaling Adaptive TSFM Expert Routing: Addresses the bottleneck of manual threshold tuning and static pool composition in multi-model forecasting systems.

### Rejected Candidates
- [concept] TimeRouter (`timerouter`) - other: Renamed to TimeRouter Framework to better distinguish it as an architectural methodology rather than a specific tool implementation.
- [open_question] Adaptive thresholding and pool optimization (`adaptive-thresholding-pool-composition`) - other: Replaced with a more formal research question on scaling expert routing.

## Links

- [Abstract](https://arxiv.org/abs/2606.11625)
- [PDF](https://arxiv.org/pdf/2606.11625)

