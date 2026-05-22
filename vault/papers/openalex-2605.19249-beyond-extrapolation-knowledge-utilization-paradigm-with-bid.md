---
# CSL-compatible fields
title: "Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting"
author:
  - literal: "Liu Chong"
  - literal: "Yingjie Zhou"
  - literal: "Hao Li"
  - literal: "Pengyang Wang"
  - literal: "Qingsong Wen"
  - literal: "Ce Zhu"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.19249"

# Custom fields
paper_id: "2605.19249"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "knowledge-distillation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "kup-bi-paradigm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:16:37Z"
created_at: "2026-05-22T08:16:37Z"
---

# Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting

**Authors**: Liu Chong, Yingjie Zhou, Hao Li, Pengyang Wang, Qingsong Wen, Ce Zhu
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.19249](https://arxiv.org/abs/2605.19249)

## Summary

The authors introduce KUP-BI, a novel paradigm for time-series forecasting that addresses the limitations of standard one-way inference by incorporating structured knowledge about post-target trajectory evolution. By distilling an approximate post-target continuation proxy from a training-only historical library, the model gains structural inductive bias that improves forecasting stability. This approach is model-agnostic and integrates into standard backbones via a lightweight gating module, requiring no extra information at inference time while consistently outperforming state-of-the-art models on six public benchmarks.

## Key Contributions

- Proposes KUP-BI, a paradigm that enhances forecasting by distilling post-target continuation proxies from a training-only historical library.
- Implements a feature-level gating module to fuse input streams with continuation proxies, providing structured inductive bias without increasing inference-time data requirements.
- Demonstrates consistent performance improvements across six standard time-series forecasting benchmarks compared to state-of-the-art baselines.

## Open Questions & Future Work

- [[architecture-agnostic-knowledge-utilization-scaling]]

## Key Concepts

- [[kup-bi-paradigm]]: A time-series forecasting paradigm that uses a train-only historical library to distill a post-target continuation proxy for structural inductive bias.

## Archivist Review

I approved the KUP-BI concept as it presents a distinct model-agnostic paradigm for trajectory-based inductive bias. I also approved the open question regarding scaling knowledge utilization, as it reflects a key challenge in integrating retrieval mechanisms with modern large-scale forecasting backbones. Other candidates were rejected for being overly implementation-specific or derivative.

### Approved Concepts
- KUP-BI Paradigm: It introduces a novel training-only knowledge distillation approach that provides an inductive bias for forecasting by leveraging post-target trajectory continuation.

### Approved Open Questions
- Architecture-agnostic knowledge utilization scaling: This issue is critical for the practical adoption of retrieval-enhanced forecasting across a wide variety of existing model architectures, especially large-scale foundation models where full re-training or joint fine-tuning is computationally prohibitive.

### Rejected Candidates
- [open_question] Handling phase shifts in retrieval (`phase-shift-handling-in-retrieval-based-forecasting`) - paper_local: The problem is specific to the retrieval implementation choice within the paper rather than a fundamental scientific bottleneck in time-series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.19249)
- [PDF](https://arxiv.org/pdf/2605.19249)

