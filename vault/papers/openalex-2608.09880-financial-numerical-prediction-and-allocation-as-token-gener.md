---
# CSL-compatible fields
title: "Financial Numerical Prediction and Allocation as Token Generation"
author:
  - literal: "Xu Ouyang"
  - literal: "Moontae Lee"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09880"

# Custom fields
paper_id: "2608.09880"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "autoregressive"
  - "reinforcement-learning"
  - "time-series"
  - "forecasting"
  - "optimization"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:37Z"
created_at: "2026-08-13T06:09:37Z"
---

# Financial Numerical Prediction and Allocation as Token Generation

**Authors**: Xu Ouyang, Moontae Lee
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09880](https://arxiv.org/abs/2608.09880)

## Summary

The authors introduce FinATOM, a unified, head-free causal language model framework that replaces traditional regression and policy heads with constrained token generation for stock return forecasting and portfolio allocation. Trained via ordinal/ranking supervision and reward-driven policy optimization (such as DAPO-augmented GRPO), FinATOM successfully predicts volatility-standardized returns and generates normalized asset allocation weights. Empirical evaluations on 2023-2025 ETF tests and FinTexTS demonstrate improvements in pooled net Sharpe ratios and cumulative returns compared to traditional pipelines.

## Key Contributions

- Introduces FinATOM, a unified, head-free causal language model interface that performs financial numerical prediction and allocation via constrained token generation without task-specific regression or policy heads.
- Demonstrates superior performance on 2023-2025 ETF tests, improving pooled net Sharpe from 1.394 to 1.494 under a 5-bp transaction-cost model.
- Achieves 73.72% cumulative return and a 2.69 Sharpe ratio on FinTexTS through supervised fine-tuning and policy optimization.

## Limitations

Requires broader testing across additional assets, market regimes, and random seeds.

## Archivist Review

Evaluated the proposed concept (FinATOM) and open question. FinATOM is arch-specific to this paper and represents an application rather than a reusable standalone machine learning methodology. The open question is primarily a call for more empirical evaluations and broader testing across seeds and assets rather than a deep theoretical or methodological bottleneck. Therefore, all candidates were rejected to maintain vault strictness.

### Rejected Candidates
- [concept] FinATOM (`finatom`) - paper_local: FinATOM is a paper-specific framework combining existing concepts like token generation and reinforcement learning for finance.
- [open_question] Robustness of Token-Native Financial Modeling (`robustness-of-token-native-financial-modeling-across-assets-and-seeds-slug`) - low_impact: The question largely asks for broader empirical testing across more assets, seeds, and baselines rather than addressing a deep conceptual bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.09880)
- [PDF](https://arxiv.org/pdf/2608.09880)

