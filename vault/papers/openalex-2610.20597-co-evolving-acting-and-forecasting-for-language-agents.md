---
# CSL-compatible fields
title: "Co-Evolving Acting and Forecasting for Language Agents"
author:
  - literal: "Haofei Yu"
  - literal: "Yixing Chen"
  - literal: "Yining Zhao"
  - literal: "Xuyan Ye"
  - literal: "Yuxiang Liu"
  - literal: "Zhigang Hua"
  - literal: "Yan Xie"
  - literal: "Shuang Yang"
  - literal: "Jiaxuan You"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20597"

# Custom fields
paper_id: "2610.20597"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "reinforcement-learning"
  - "agent"
  - "autonomous-agent"
  - "sample-efficiency"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "co-evolving-acting-and-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:18Z"
created_at: "2026-10-17T08:55:18Z"
---

# Co-Evolving Acting and Forecasting for Language Agents

**Authors**: Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, Zhigang Hua, Yan Xie, Shuang Yang, Jiaxuan You
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20597](https://arxiv.org/abs/2610.20597)

## Summary

Training language agents via reinforcement learning is often bottlenecked by terminal rewards and poor intermediate supervision. The authors propose CoPE, which introduces multi-step action targets to enable the simultaneous co-evolution of policy acting and forecasting. Using a shared policy backbone without additional models or inference overhead, CoPE significantly improves sample efficiency and performance across five agentic benchmarks including ALFWorld and ScienceWorld.

## Key Contributions

- Proposes CoPE, a framework adding multi-step action targets to supervise intermediate steps in language agent reinforcement learning.
- Enables acting and forecasting to co-evolve using a shared policy backbone without auxiliary models or inference overhead.
- Achieves up to 1.9x and 2.0x higher sample efficiency than ECHO and GRPO respectively on ScienceWorld across five benchmarks.

## Open Questions & Future Work

- [[robust-success-conditioned-action-forecasting]]

## Key Concepts

- [[co-evolving-acting-and-forecasting]]: A framework for language agents that uses multi-step action targets to co-evolve acting and forecasting through a shared policy backbone.

## Archivist Review

Approved the central concept of co-evolving acting and forecasting via multi-step action targets for language agents, along with the open question regarding success-conditioned imitation failures on trivial trajectories. All datasets were rejected as they are a mix of established environment benchmarks rather than single standalone benchmark corpuses.

### Approved Concepts
- Co-Evolving Acting and Forecasting: Core methodological novelty of the paper, introducing multi-step action targets for language agents where acting and forecasting co-evolve.

### Approved Open Questions
- Robust Success-Conditioned Action Forecasting: Addressing failure modes in success-conditioned imitation and action forecasting is crucial for extending language agent RL to domains with frequent trivial or refusal-based successful trajectories without degrading performance on active reasoning tasks.

## Links

- [Abstract](https://arxiv.org/abs/2610.20597)
- [PDF](https://arxiv.org/pdf/2610.20597)

