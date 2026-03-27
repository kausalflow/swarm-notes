---
# CSL-compatible fields
title: "SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms"
author:
  - literal: "Longkun Xu"
  - literal: "Xiaochun Zhang"
  - literal: "Qiantu Tuo"
  - literal: "Rui Li"
issued:
  date-parts:
    - [2026, 3, 5]
url: "https://arxiv.org/abs/2603.04873"

# Custom fields
paper_id: "2603.04873"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "reasoning"
  - "reinforcement-learning"
  - "evolutionary-algorithm"
  - "benchmark"
  - "emergent-abilities"
architectures:
  []
datasets:
  - "Solar-Energy benchmark"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:46Z"
created_at: "2026-03-27T14:09:46Z"
---

# SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms

**Authors**: Longkun Xu, Xiaochun Zhang, Qiantu Tuo, Rui Li
**Date**: 2026-03-05
**Paper ID**: [openalex:2603.04873](https://arxiv.org/abs/2603.04873)

## Summary

The Self-Evolving Agent for Time Series Algorithms (SEA-TS) framework addresses limitations in conventional ML development by autonomously generating and optimizing forecasting code through an iterative loop. Key innovations include Metric-Advantage Monte Carlo Tree Search (MA-MCTS) for reward-agnostic guidance, automated Code Review with prompt refinement to learn from execution errors, and Global Steerable Reasoning for cross-trajectory knowledge sharing. The approach uses a MAP-Elites archive to maintain architectural diversity. SEA-TS significantly outperforms state-of-the-art methods like TimeMixer, demonstrating its capability to engineer genuinely novel, high-performing algorithmic components for time series forecasting tasks.

## Key Contributions

- Proposed SEA-TS, an autonomous framework that generates, validates, and optimizes time series forecasting code via an iterative self-evolution loop.
- Introduced Metric-Advantage Monte Carlo Tree Search (MA-MCTS) for more discriminative guidance in the code search process by using normalized advantage scores instead of fixed rewards.
- Developed a Code Review mechanism with running prompt refinement that encodes corrective patterns from execution errors to prevent the recurrence of similar mistakes.
- Achieved significant performance gains, including a 40% MAE reduction over TimeMixer on the Solar-Energy benchmark, and surpassed human-engineered baselines on proprietary datasets.
- The evolved algorithms discovered novel, physics-informed architectural patterns, such as monotonic decay heads and learnable bias corrections.

## Limitations

The performance and robustness of the generated code on domains outside of energy forecasting are not fully explored. The computational cost of the iterative self-evolution loop is likely high.

## Open Questions & Future Work

- [[combining-coding-and-research-agents]]
- [[context-pruning-for-cost-reduction]]
- [[automated-map-elites-dimension-discovery]]
- [[advanced-mcts-search-algorithms]]
- [[systematic-domain-knowledge-injection]]
- [[multi-objective-optimization-for-deployment]]

## Key Concepts

- [Metric-Advantage Monte Carlo Tree Search](../concepts/metric-advantage-mcts.md): A search algorithm variant that uses a normalized advantage score derived from performance metrics instead of fixed rewards to guide exploration in an evolutionary code generation framework.
- [Global Steerable Reasoning](../concepts/global-steerable-reasoning.md): A mechanism within an evolutionary agent that compares the current state against the globally best and worst solutions found so far to facilitate cross-trajectory knowledge transfer.

## Datasets

- [Solar-Energy benchmark](../datasets/solar-energy-benchmark.md)

## Limitations

The performance and robustness of the generated code on domains outside of energy forecasting are not fully explored. The computational cost of the iterative self-evolution loop is likely high.

## Links

- [Abstract](https://arxiv.org/abs/2603.04873)
- [PDF](https://arxiv.org/pdf/2603.04873)

