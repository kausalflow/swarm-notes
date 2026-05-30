---
# CSL-compatible fields
title: "FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations"
author:
  - literal: "Xuesi Hu"
  - literal: "Peng Wang"
  - literal: "Jinpeng Miao"
  - literal: "Xilin Tao"
  - literal: "Caiwei Li"
  - literal: "Yue Ma"
  - literal: "Jie He"
  - literal: "Qiancheng Zhang"
  - literal: "Yuntao Zou"
  - literal: "Dagang Li"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27896"

# Custom fields
paper_id: "2605.27896"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "financial-reasoning"
  - "benchmark"
  - "reasoning"
  - "planning"
  - "agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "finboardbench"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:37:35Z"
created_at: "2026-05-30T07:37:35Z"
---

# FinBoardBench: Benchmarking Dynamic Wealth Management and Strategic Financial Reasoning of LLMs via Board Game Simulations

**Authors**: Xuesi Hu, Peng Wang, Jinpeng Miao, Xilin Tao, Caiwei Li, Yue Ma, Jie He, Qiancheng Zhang, Yuntao Zou, Dagang Li
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27896](https://arxiv.org/abs/2605.27896)

## Summary

This paper introduces FinBoardBench, a new evaluation framework designed to assess the dynamic wealth management and strategic financial decision-making capabilities of LLMs using three classic financial board games. By placing models in complex, interactive, and competitive environments, the authors demonstrate a significant gap between static financial reasoning performance and success in dynamic, real-world-like scenarios. Experimental results across nine advanced LLMs reveal that these models often prioritize immediate asset acquisition, failing to maintain the liquidity necessary to survive crises triggered by random events.

## Key Contributions

- Introduces FinBoardBench, a novel benchmark evaluating LLM dynamic wealth management using board game simulations (Cashflow, Acquire, Monopoly).
- Demonstrates that LLMs struggle with long-term liquidity management and strategic interaction, despite strong static reasoning performance.
- Identifies a systemic vulnerability in current LLMs to financial crises due to a bias toward immediate asset acquisition over liquidity preservation.

## Open Questions & Future Work

- [[llm-dynamic-financial-decision-gap]]

## Key Concepts

- [[finboardbench]]: A comprehensive evaluation suite using financial board games to benchmark LLM dynamic wealth management and strategic financial reasoning capabilities.

## Archivist Review

Approved the novel benchmarking framework FinBoardBench and the identified performance gap as a critical open question for financial AI. Rejected the inclusion of the board game names themselves as datasets, as the paper uses these as task environments rather than as source data for model training or evaluation in the traditional sense. Evaluated strictly against the provided forecasting and reasoning criteria.

### Approved Concepts
- FinBoardBench: It is the primary contribution of the paper, establishing a new methodology for benchmarking dynamic financial reasoning in LLMs.

### Approved Open Questions
- LLM Dynamic Financial Decision-making Gap: Understanding the misalignment between static knowledge and dynamic decision-making is critical for deploying LLMs in real-world financial systems where adaptation to stochastic events and multi-agent competition is required.

## Links

- [Abstract](https://arxiv.org/abs/2605.27896)
- [PDF](https://arxiv.org/pdf/2605.27896)

