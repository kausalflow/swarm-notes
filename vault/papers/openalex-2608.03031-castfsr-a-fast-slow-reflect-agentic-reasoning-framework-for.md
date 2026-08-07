---
# CSL-compatible fields
title: "CastFSR: A Fast--Slow--Reflect Agentic Reasoning Framework for Context-Aware Time Series Forecasting"
author:
  - literal: "Xiaoyu Tao"
  - literal: "Mingyue Cheng"
  - literal: "潘柏凱"
  - literal: "Chuang Jiang"
  - literal: "Huanjian Zhang"
  - literal: "Tian Gao"
  - literal: "Ying Liu"
  - literal: "Qi Liu"
  - literal: "Enhong Chen"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03031"

# Custom fields
paper_id: "2608.03031"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "agent"
  - "llm"
  - "reasoning"
  - "reinforcement-learning"
  - "instruction-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "castfsr"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:03:44Z"
created_at: "2026-08-07T06:03:44Z"
---

# CastFSR: A Fast--Slow--Reflect Agentic Reasoning Framework for Context-Aware Time Series Forecasting

**Authors**: Xiaoyu Tao, Mingyue Cheng, 潘柏凱, Chuang Jiang, Huanjian Zhang, Tian Gao, Ying Liu, Qi Liu, Enhong Chen
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03031](https://arxiv.org/abs/2608.03031)

## Summary

The paper introduces CastFSR, an agentic reasoning framework for context-aware time series forecasting that implements a Fast--Slow--Reflect workflow. The fast phase generates data-driven priors using lightweight forecasters, the slow phase retrieves context and reasons about future dynamics, and the reflection phase iteratively validates and refines forecasts. CastFSR supports both zero-shot LLM inference and a two-stage fine-tuning and reinforcement learning strategy for compact models, outperforming standard baselines on public benchmarks.

## Key Contributions

- Proposes CastFSR, an agentic framework formulating context-aware time series forecasting as a Fast--Slow--Reflect workflow.
- Employs fast thinking to profile observations and select lightweight forecasters, slow deliberation to retrieve contextual evidence and reason about future dynamics, and reflection to refine forecasts against constraints.
- Supports both training-free inference with off-the-shelf LLMs and a two-stage SFT and reinforcement learning strategy to transfer orchestration capabilities to compact LLMs.
- Demonstrates consistent performance improvements over representative baselines across public datasets.

## Open Questions & Future Work

- [[dynamic-agentic-orchestration-optimization]]

## Key Concepts

- [[castfsr]]: An agentic reasoning framework for context-aware time series forecasting based on a Fast-Slow-Reflect workflow.

## Archivist Review

Approved the core framework CastFSR as a novel agentic forecasting paradigm and the associated open question on dynamic agentic orchestration optimization. No specific datasets were provided in the evaluation text, so datasets were omitted in accordance with the scarcity policy.

### Approved Concepts
- CastFSR: Central novelty of the paper introducing a Fast-Slow-Reflect agentic workflow for context-aware time series forecasting.

### Approved Open Questions
- Dynamic Agentic Orchestration Optimization: Crucial for improving the autonomy, adaptability, and sample efficiency of LLM-based agents in time-dependent environments.

## Links

- [Abstract](https://arxiv.org/abs/2608.03031)
- [PDF](https://arxiv.org/pdf/2608.03031)

