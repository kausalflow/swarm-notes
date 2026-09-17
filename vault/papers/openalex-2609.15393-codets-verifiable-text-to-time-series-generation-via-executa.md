---
# CSL-compatible fields
title: "CodeTS: Verifiable Text-to-Time Series Generation via Executable Code"
author:
  - literal: "Xudong Yuan"
  - literal: "Shunyu Liu"
  - literal: "Tongya Zheng"
  - literal: "Huiping Zhuang"
  - literal: "Mingli Song"
  - literal: "Kaixuan Chen"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15393"

# Custom fields
paper_id: "2609.15393"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "llm"
  - "reinforcement-learning"
  - "zero-shot-learning"
  - "code-generation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "codets"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:43:20Z"
created_at: "2026-09-17T09:43:20Z"
---

# CodeTS: Verifiable Text-to-Time Series Generation via Executable Code

**Authors**: Xudong Yuan, Shunyu Liu, Tongya Zheng, Huiping Zhuang, Mingli Song, Kaixuan Chen
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15393](https://arxiv.org/abs/2609.15393)

## Summary

CodeTS is a verifiable framework for text-to-time series generation that uses executable code as an intermediate interface (Text-to-Code-to-TS). By constructing aligned triplets from structured attributes for initialization and leveraging multi-stage execution-based rewards via Reinforcement Learning with Verifiable Rewards (RLVR), CodeTS achieves robust zero-shot synthesis across eight benchmarks, outperforming existing LLM and supervised baselines.

## Key Contributions

- Proposes CodeTS, a text-to-time series generation framework that reformulates synthesis as a Text-to-Code-to-TS process using executable code as an intermediate interface.
- Constructs aligned Text-Code-TS triplets from structured temporal attributes for supervised initialization without requiring real code annotations.
- Designs multi-stage execution-based rewards to verify format validity, code executability, and time series quality under a reinforcement learning with verifiable rewards (RLVR) paradigm.
- Achieves state-of-the-art zero-shot performance across eight benchmarks spanning short, medium, and long generation lengths, outperforming LLM and supervised generative baselines.

## Open Questions & Future Work

- [[multivariate-text-to-time-series-generation]]

## Key Concepts

- [[codets]]: A verifiable framework for text-to-time series generation that uses executable code as an intermediate generation interface.

## Archivist Review

Approved the novel CodeTS framework for text-to-time series generation via executable code and verifiable rewards, along with the corresponding open question on multivariate extension. Applied strict vault selectivity standards.

### Approved Concepts
- CodeTS: Introduces the core Text-to-Code-to-TS reformulation using executable code as an intermediate generation interface.

### Approved Open Questions
- Multivariate Text-to-Time Series Generation: Extending code-based verifiable generation to multivariate time series is crucial for handling complex real-world inter-series dependencies and expanding applicability to domains like multi-sensor monitoring and financial portfolio synthesis.

## Links

- [Abstract](https://arxiv.org/abs/2609.15393)
- [PDF](https://arxiv.org/pdf/2609.15393)

