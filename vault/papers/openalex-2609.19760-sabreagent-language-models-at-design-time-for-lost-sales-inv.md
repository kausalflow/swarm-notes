---
# CSL-compatible fields
title: "SabreAgent: Language Models at Design Time for Lost-Sales Inventory Control"
author:
  - literal: "Yang Liu"
  - literal: "Yulin Huang"
  - literal: "Xue Yu"
  - literal: "Jiong Dong"
  - literal: "Jianshen Zhang"
  - literal: "Yongzhi Qi"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19760"

# Custom fields
paper_id: "2609.19760"
paper_source: "openalex"
domain: "time-series"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sabreagent"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-20T09:30:30Z"
created_at: "2026-09-20T09:30:30Z"
---

# SabreAgent: Language Models at Design Time for Lost-Sales Inventory Control

**Authors**: Yang Liu, Yulin Huang, Xue Yu, Jiong Dong, Jianshen Zhang, Yongzhi Qi
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19760](https://arxiv.org/abs/2609.19760)

## Summary

SabreAgent introduces a design-time language model framework for lost-sales inventory control that constructs product-specific seasonal priors and capped base-stock policy families while requiring zero LLM calls during operation. Built around an operations-research core featuring specialized projected-inventory rules and order destruction mechanisms, the approach outperforms existing published baselines on InventoryBench. Ablation studies reveal that the OR core provides the majority of the performance gains, complemented by marginal improvements from the seasonal and search components.

## Key Contributions

- Introduces SabreAgent, which uses language models at design time to construct product-specific seasonal priors and validation-selected capped base-stock policy families for inventory control with zero operational LLM calls.
- Incorporates an operations-research core utilizing a zero-lead-time optimality result and a projected-inventory rule for positive deterministic lead times, alongside handling stochastic lead times with order destruction.
- Achieves a top score of 0.6311 on InventoryBench, outperforming the strongest published baseline of 0.5380 and ranking first across all six benchmark cells.
- Demonstrates via ablations that the OR core drives the majority of the performance gain, with seasonal and search components providing complementary improvements.

## Open Questions & Future Work

- [[runtime-vs-designtime-llm-control]]

## Key Concepts

- [[sabreagent]]: A design-time language model framework for constructing seasonal priors and policy families for inventory control with zero operational LLM calls.

## Archivist Review

Approved SabreAgent as a distinct design-time LLM integration framework for operational control, and approved the open question on runtime versus design-time LLM control. No datasets met the strict standalone criteria.

### Approved Concepts
- SabreAgent: Central framework introduced in the paper for leveraging language models at design time to construct inventory control components.

### Approved Open Questions
- Runtime Versus Design-Time LLM Control: This open question is technically important because it directly addresses the boundary between offline/design-time LLM reasoning and online/runtime adjustments, providing crucial guidelines for deploying hybrid AI-OR systems in sequential decision-making.

## Links

- [Abstract](https://arxiv.org/abs/2609.19760)
- [PDF](https://arxiv.org/pdf/2609.19760)

