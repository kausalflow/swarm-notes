---
# CSL-compatible fields
title: "FinRankGRPO: Optimizing LLMs for Listwise Financial Asset Ranking via Group Relative Policy Optimization"
author:
  - literal: "Ningyuan Deng"
  - literal: "Jinyuan Wang"
  - literal: "Qi Li"
  - literal: "Jia Zhang"
  - literal: "Yi Yang"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24175"

# Custom fields
paper_id: "2609.24175"
paper_source: "openalex"
domain: "finance"
tags:
  - "llm"
  - "language-model"
  - "reinforcement-learning"
  - "fintech"
  - "alignment"
  - "chain-of-thought"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "finrankgrpo"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:39:14Z"
created_at: "2026-09-24T09:39:14Z"
---

# FinRankGRPO: Optimizing LLMs for Listwise Financial Asset Ranking via Group Relative Policy Optimization

**Authors**: Ningyuan Deng, Jinyuan Wang, Qi Li, Jia Zhang, Yi Yang
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24175](https://arxiv.org/abs/2609.24175)

## Summary

This paper introduces FinRankGRPO, a framework that reformulates LLM-based portfolio construction from unstable numerical forecasting to listwise financial asset ranking. The method features a two-stage training pipeline comprising supervised fine-tuning on Chain-of-Thought reasoning data and Group Relative Policy Optimization driven by a Spearman rank correlation reward. Experiments demonstrate that FinRankGRPO surpasses traditional quantitative models and state-of-the-art commercial LLMs in financial asset allocation performance.

## Key Contributions

- Proposes FinRankGRPO, shifting LLM-based portfolio construction from direct numerical prediction to listwise asset ranking.
- Introduces a two-stage training process combining supervised fine-tuning on Chain-of-Thought reasoning data and Group Relative Policy Optimization.
- Employs a Spearman rank correlation reward function to explicitly align generative model preferences with ground truth market orderings.
- Achieves a Sharpe ratio of 0.636 and Spearman correlation of 0.023, outperforming traditional quantitative and commercial baselines.

## Open Questions & Future Work

- [[multilingual-financial-asset-ranking]]

## Key Concepts

- [[finrankgrpo]]: A framework optimizing LLMs for listwise financial asset ranking using group relative policy optimization and Spearman rank correlation reward.

## Archivist Review

Approved the core framework concept 'FinRankGRPO' as it introduces a distinct listwise ranking alignment approach for financial portfolios using group relative policy optimization. The open question on multilingual financial asset ranking was approved because it addresses a clear cross-domain generalization bottleneck in financial LLM deployment. No datasets met the strict novelty and standalone archival criteria.

### Approved Concepts
- FinRankGRPO: Central framework of the paper that introduces listwise asset ranking via group relative policy optimization for financial LLMs.

### Approved Open Questions
- Multilingual Financial Asset Ranking: Important for generalization across international markets where localized news and non-English financial documents drive significant asset volatility.

## Links

- [Abstract](https://arxiv.org/abs/2609.24175)
- [PDF](https://arxiv.org/pdf/2609.24175)

