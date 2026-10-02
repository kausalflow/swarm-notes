---
# CSL-compatible fields
title: "Can Language Models Learn to Forecast Stock Prices"
author:
  - literal: "Jiacheng Guo"
  - literal: "Suozhi Huang"
  - literal: "Shuzhen Li"
  - literal: "Yunlong Gao"
  - literal: "Zerui Cheng"
  - literal: "Jason Ge"
  - literal: "Shushu Liang"
  - literal: "Zihao Li"
  - literal: "Hao Lu"
  - literal: "Ming Yin"
  - literal: "Shilong Liu"
  - literal: "Jiashuo Liu"
  - literal: "Xu Kuang"
  - literal: "Mengdi Wang"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36914"

# Custom fields
paper_id: "2609.36914"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "reinforcement-learning"
  - "rlhf"
  - "tool-use"
  - "time-series"
  - "forecasting"
  - "fine-tuning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:21Z"
created_at: "2026-10-02T10:47:21Z"
---

# Can Language Models Learn to Forecast Stock Prices

**Authors**: Jiacheng Guo, Suozhi Huang, Shuzhen Li, Yunlong Gao, Zerui Cheng, Jason Ge, Shushu Liang, Zihao Li, Hao Lu, Ming Yin, Shilong Liu, Jiashuo Liu, Xu Kuang, Mengdi Wang
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36914](https://arxiv.org/abs/2609.36914)

## Summary

This paper investigates whether post-training techniques—specifically supervised fine-tuning on tool-use demonstrations and proximal policy optimization (PPO) using terminal return rewards—can improve language models in financial stock price forecasting. The authors introduce AURA-4B, built on Qwen3-4B, which operates within a chronological stock-price sandbox by gathering market evidence and predicting future returns. Results show that post-training more than doubles the model's direction-magnitude score from 20.94 to 43.31, matching frontier language models while significantly shifting its information-gathering and tool-use strategies.

## Key Contributions

- Introduces a chronological stock-price sandbox environment where language models gather multi-faceted market evidence and predict future returns.
- Demonstrates that post-training via supervised fine-tuning on tool-use demonstrations followed by proximal policy optimization (PPO) with terminal return rewards substantially improves financial forecasting.
- AURA-4B more than doubles the starting direction-magnitude score from 20.94 to 43.31, matching frontier language models on the benchmark.
- Shows that post-training shifts model behavior to expand tool use, increasing the share of ranking and market-context queries.

## Archivist Review

The candidate open question was rejected because it calls for standard experimental ablations (comparing specific tool queries) rather than addressing a foundational theoretical or methodological bottleneck. No concepts or datasets met the strict novelty and reusability standards for permanent standalone vault notes.

### Rejected Candidates
- [open_question] Controlled Tool-Access in Forecasting (`controlled-tool-access-financial-forecasting`) - low_impact: This open question is a descriptive experimental ablation request rather than an enduring structural bottleneck or theoretical limitation.

## Links

- [Abstract](https://arxiv.org/abs/2609.36914)
- [PDF](https://arxiv.org/pdf/2609.36914)

