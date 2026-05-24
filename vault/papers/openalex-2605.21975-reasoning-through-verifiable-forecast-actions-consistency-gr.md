---
# CSL-compatible fields
title: "Reasoning through Verifiable Forecast Actions: Consistency-Grounded RL for Financial LLMs"
author:
  - literal: "Jialin Chen"
  - literal: "Aosong Feng"
  - literal: "Harshit Verma"
  - literal: "Siyi Gu"
  - literal: "Haiwen Wang"
  - literal: "Ali Maatouk"
  - literal: "Yixuan He"
  - literal: "Yifeng Gao"
  - literal: "Leandros Tassiulas"
  - literal: "Rex Ying"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.21975"

# Custom fields
paper_id: "2605.21975"
paper_source: "openalex"
domain: "finance,nlp"
tags:
  - "llm"
  - "language-model"
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
  - "reasoning"
  - "tool-use"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "verifiable-forecast-action-mechanism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:45:46Z"
created_at: "2026-05-24T07:45:46Z"
---

# Reasoning through Verifiable Forecast Actions: Consistency-Grounded RL for Financial LLMs

**Authors**: Jialin Chen, Aosong Feng, Harshit Verma, Siyi Gu, Haiwen Wang, Ali Maatouk, Yixuan He, Yifeng Gao, Leandros Tassiulas, Rex Ying
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.21975](https://arxiv.org/abs/2605.21975)

## Summary

StockR1 addresses the disconnect between qualitative financial reasoning and quantitative time-series forecasting in LLMs. The model employs a two-stage approach: it first generates a structured 'forecast action' as a tool call, then uses this action to condition a time-series decoder for trajectory prediction. The entire pipeline is trained via reinforcement learning with rewards based on forecast accuracy, reasoning validity, and consistency, modulated by sample-level market uncertainty. Results show substantial improvements in both financial question answering and forecasting accuracy compared to standard LLM and time-series approaches.

## Key Contributions

- Introduced StockR1, which unifies stock forecasting and financial reasoning using a verifiable tool-call action mechanism.
- Proposed a reinforcement learning framework that optimizes for answer validity, forecast accuracy, and action-dynamics consistency.
- Implemented sample-level uncertainty reweighting to adapt model learning to varying financial market volatility.
- Achieved significant gains in reasoning accuracy, improving performance by 17.7% (4B) and 25.9% (8B) over baselines on a 10-year financial benchmark.

## Open Questions & Future Work

- [[scalability-of-action-based-financial-forecasting]]

## Key Concepts

- [[verifiable-forecast-action-mechanism]]: A forecasting design where an LLM emits structured, verifiable intermediate actions to condition a time-series decoder.

## Archivist Review

The review focused on extracting the architectural contribution (the decomposition of reasoning and forecasting through structured actions) as a reusable concept, while rejecting the model-specific name. The open question was reframed to specifically target the scalability of this new action-based paradigm in financial domains, rather than listing generic limitations of financial LLMs.

### Approved Concepts
- Verifiable Forecast Action Mechanism: It establishes a bridge between qualitative LLM reasoning and quantitative time-series forecasting by forcing models to commit to structured, verifiable intermediate representations. This paradigm is likely to generalize to other domain-aware forecasting tasks that require reasoning.

### Approved Open Questions
- Scalability of action-based forecasting: Addressing these limitations is critical for evolving from narrow stock-specific forecasting toward comprehensive, cross-domain financial market modeling using LLMs.

### Rejected Candidates
- [concept] StockR1 (`stockr1`) - subcomponent_of_broader_mechanism: This is the specific name of the model in the paper; the underlying architectural contribution (Verifiable Forecast Action Mechanism) is the more reusable concept.
- [open_question] Expanding financial LLM capabilities (`financial-llm-scaling-limitations`) - duplicate_existing: The proposed title and description were broad and duplicative of the new, more focused open question about action-based forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.21975)
- [PDF](https://arxiv.org/pdf/2605.21975)

