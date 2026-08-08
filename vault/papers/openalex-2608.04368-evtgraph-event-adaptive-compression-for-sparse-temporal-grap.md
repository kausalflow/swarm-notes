---
# CSL-compatible fields
title: "EvtGraph: Event-Adaptive Compression for Sparse Temporal Graph Learning in Multimodal Time Series"
author:
  - literal: "Ziqian Wang"
  - literal: "Tingxiong Xiao"
  - literal: "Yuxiao Cheng"
  - literal: "Jinli Suo"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04368"

# Custom fields
paper_id: "2608.04368"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "time-series"
  - "graph-neural-network"
  - "transformer"
  - "efficiency"
architectures:
  []
datasets:
  []
concept_slugs:
  - "evtgraph"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:29Z"
created_at: "2026-08-08T05:34:29Z"
---

# EvtGraph: Event-Adaptive Compression for Sparse Temporal Graph Learning in Multimodal Time Series

**Authors**: Ziqian Wang, Tingxiong Xiao, Yuxiao Cheng, Jinli Suo
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04368](https://arxiv.org/abs/2608.04368)

## Summary

EvtGraph is a unified framework for multimodal temporal learning that addresses the irregular and uneven information density of multimodal data via event-adaptive compression, node budget constraints, and temporally constrained sparse graph reasoning. By transforming dense sequences into structured computations over salient events under explicit budget constraints, EvtGraph achieves a superior performance-efficiency trade-off compared to conventional Transformer-based and recurrent baselines. Experiments on clinical and cross-domain benchmarks validate its effectiveness in preserving critical transitions while improving computational efficiency.

## Key Contributions

- Proposes EvtGraph, a unified framework aligning computation with temporal salience under explicit budget constraints for multimodal time series.
- Introduces event-adaptive compression (EAMC) and node budget constraint (NBC) to reparameterize sequences into event-level tokens and select compact subsets.
- Performs temporally constrained sparse graph reasoning (T2SG) to reduce complexity while preserving critical transitions.
- Demonstrates superior performance over Transformer-based and recurrent baselines on multimodal clinical and cross-domain benchmarks while improving efficiency.

## Open Questions & Future Work

- [[long-range-event-adaptive-compression]]

## Key Concepts

- [[evtgraph]]: A unified framework that aligns computation with temporal salience under explicit budget constraints for sparse temporal graph learning.

## Archivist Review

Approved the core EvtGraph framework concept for event-adaptive sparse temporal graph learning and the corresponding open question on long-range adaptation limits. All paper-local auxiliary modules (EAMC, NBC, T2SG) were rejected as subcomponents of the overarching framework to adhere to the scarcity and reusability policy. No standalone datasets were approved since MIMIC-IV is already tracked under existing vault items.

### Approved Concepts
- EvtGraph: It introduces event-adaptive compression and node budget constraints for sparse temporal graph learning.

### Approved Open Questions
- Long-Range Event-Adaptive Compression: Addressing variable and long-range structures without coarse partitioning is crucial for generalizing event-adaptive temporal compression to a broader class of continuous or complex asynchronous sequential data.

## Links

- [Abstract](https://arxiv.org/abs/2608.04368)
- [PDF](https://arxiv.org/pdf/2608.04368)

