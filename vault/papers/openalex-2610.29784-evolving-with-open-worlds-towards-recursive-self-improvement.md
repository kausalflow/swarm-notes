---
# CSL-compatible fields
title: "Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting"
author:
  - literal: "Zhipeng Chen"
  - literal: "Yongli Liang"
  - literal: "Yanxi Chen"
  - literal: "Hongkang Zhao"
  - literal: "Lingyun Feng"
  - literal: "Riyang Ren"
  - literal: "Guoxin Chen"
  - literal: "Jia Deng"
  - literal: "Feng Chang"
  - literal: "Chuan Hao"
  - literal: "Ran Tao"
  - literal: "Jian Yang"
  - literal: "Ji-Rong Wen"
  - literal: "Bryan Dai"
  - literal: "Wayne Xin Zhao"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29784"

# Custom fields
paper_id: "2610.29784"
paper_source: "openalex"
domain: "nlp"
tags:
  - "agent"
  - "autonomous-agent"
  - "llm"
  - "language-model"
  - "reasoning"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  - "FutureX"
concept_slugs:
  - "deepevolve"
dataset_slugs:
  - "futurex"
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:12:05Z"
created_at: "2026-10-24T09:12:05Z"
---

# Evolving with Open Worlds: Towards Recursive Self-Improvement for Future Forecasting

**Authors**: Zhipeng Chen, Yongli Liang, Yanxi Chen, Hongkang Zhao, Lingyun Feng, Riyang Ren, Guoxin Chen, Jia Deng, Feng Chang, Chuan Hao, Ran Tao, Jian Yang, Ji-Rong Wen, Bryan Dai, Wayne Xin Zhao
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29784](https://arxiv.org/abs/2610.29784)

## Summary

This paper introduces DeepEvolve, an agent system capable of recursive self-improvement (RSI) grounded in future event prediction within a dynamically evolving environment. The system features a recursive-evolution engine that decouples search from prediction to handle contamination-prone live environments and distills reusable skills from limited live trajectories. Evaluated on the live FutureX leaderboard, the self-improved forecaster ranked first across all systems for three consecutive weeks, demonstrating the efficacy of open-world co-evolution for AI growth.

## Key Contributions

- Introduces DeepEvolve, a sustainable agent system for recursive self-improvement grounded in future event prediction.
- Proposes a recursive-evolution engine that decouples search from prediction and distills reusable skills from live trajectories.
- Achieves first place across all systems over three consecutive weeks on the live FutureX leaderboard, with up to a 195% rating improvement.

## Limitations

Future work may explore expanding the open-ended evolution framework to broader domains beyond future event forecasting.

## Open Questions & Future Work

- [[scaling-recursive-self-improvement-under-environmental-drift]]

## Key Concepts

- [[deepevolve]]: A sustainable evolution agent system designed for recursive self-improvement through future event prediction in dynamically evolving environments.

## Archivist Review

We approved the primary framework DeepEvolve and its corresponding open question on scaling recursive self-improvement under environmental drift, alongside the FutureX benchmark dataset. Strict selectivity rules were enforced to maintain a clean and highly focused knowledge vault.

### Approved Concepts
- DeepEvolve: It is the core sustainable evolution agent system introduced for recursive self-improvement in future forecasting.

### Approved Open Questions
- Scaling Recursive Self-Improvement Under Environmental Drift: Understanding how to sustain recursive self-improvement under data scarcity and environmental drift is crucial for scaling autonomous learning agents beyond narrow domains or predictable task distributions.

## Datasets

- [[futurex]]

## Links

- [Abstract](https://arxiv.org/abs/2610.29784)
- [PDF](https://arxiv.org/pdf/2610.29784)

