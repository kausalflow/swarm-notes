---
# CSL-compatible fields
title: "FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts"
author:
  - literal: "Yiji Zhao"
  - literal: "Zihao Zhong"
  - literal: "Ao Wang"
  - literal: "Haomin Wen"
  - literal: "Ming Jin"
  - literal: "Yuxuan Liang"
  - literal: "Huaiyu Wan"
  - literal: "Hao Wu"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2601.05174"

# Custom fields
paper_id: "2601.05174"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "graph-neural-network"
  - "attention-mechanism"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-graph-agent-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:56:02Z"
created_at: "2026-04-23T06:56:02Z"
---

# FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts

**Authors**: Yiji Zhao, Zihao Zhong, Ao Wang, Haomin Wen, Ming Jin, Yuxuan Liang, Huaiyu Wan, Hao Wu
**Date**: 2026-04-20
**Paper ID**: [openalex:2601.05174](https://arxiv.org/abs/2601.05174)

## Summary

FaST is a spatial-temporal graph forecasting framework designed to overcome the computational bottlenecks of long-horizon, large-scale network modeling. The approach employs an adaptive graph agent attention mechanism to replace inefficient graph convolutions and a parallel mixture-of-experts module based on Gated Linear Units to optimize scaling. Empirical evaluations demonstrate that the model enables accurate one-week-ahead predictions for networks with thousands of nodes while significantly outperforming state-of-the-art baselines in computational efficiency.

## Key Contributions

- Introduces FaST, a framework for long-horizon spatial-temporal graph forecasting that supports one-week-ahead predictions on large-scale networks.
- Develops an adaptive graph agent attention mechanism that improves scalability compared to traditional graph convolution and self-attention.
- Proposes a parallel Mixture-of-Experts module using Gated Linear Units (GLUs) to replace standard feed-forward networks, enhancing computational efficiency and throughput.

## Open Questions & Future Work

- [[foundation-model-stg-forecasting-integration]]

## Key Concepts

- [[adaptive-graph-agent-attention]]: An attention mechanism that uses agent-based node representations to reduce the computational overhead of standard graph convolutions and self-attention in large networks.

## Archivist Review

I approved the adaptive graph agent attention mechanism as it represents a distinct strategy for scaling GNN-based forecasting. I rejected the parallel MoE component as it is a specific architectural implementation of known techniques (MoEs and GLUs) rather than a novel conceptual advancement. The open question was refined to capture the broader challenge of integrating foundation model techniques into the specialized domain of STG forecasting.

### Approved Concepts
- Adaptive Graph Agent Attention: Addresses the critical bottleneck of computational complexity in large-scale spatial-temporal graph forecasting.

### Approved Open Questions
- Foundation Model STG Integration: Foundation models offer the potential to unify feature extraction and improve generalization, which is currently a major limitation of task-specific STG models.

### Rejected Candidates
- [concept] Parallel Mixture-of-Experts with Gated Linear Units (`parallel-moe-module-glu`) - subcomponent_of_broader_mechanism: The use of GLUs within an MoE framework is a specific architectural design choice that does not constitute a novel, reusable concept distinct from general MoE implementations.

## Links

- [Abstract](https://arxiv.org/abs/2601.05174)
- [PDF](https://arxiv.org/pdf/2601.05174)

