---
# CSL-compatible fields
title: "LEAP: Likelihood Elicitation and Aggregation for LLM-based Probabilistic Forecasting"
author:
  - literal: "Yufei Chen"
  - literal: "Yiran Zhao"
  - literal: "Xiaogang Xu"
  - literal: "Qipeng Xie"
  - literal: "Jiafei Wu"
  - literal: "Zhe Liu"
  - literal: "Yufei Chen"
  - literal: "Yiran Zhao"
  - literal: "Xiaogang Xu"
  - literal: "Qipeng Xie"
  - literal: "Jiafei Wu"
  - literal: "Zhe Liu"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.01337"

# Custom fields
paper_id: "2609.01337"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "forecasting"
  - "agent"
  - "autonomous-agent"
  - "uncertainty"
architectures:
  []
datasets:
  []
concept_slugs:
  - "leap"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:10:54Z"
created_at: "2026-09-04T09:10:54Z"
---

# LEAP: Likelihood Elicitation and Aggregation for LLM-based Probabilistic Forecasting

**Authors**: Yufei Chen, Yiran Zhao, Xiaogang Xu, Qipeng Xie, Jiafei Wu, Zhe Liu, Yufei Chen, Yiran Zhao, Xiaogang Xu, Qipeng Xie, Jiafei Wu, Zhe Liu
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.01337](https://arxiv.org/abs/2609.01337)

## Summary

The paper introduces LEAP (Likelihood Elicitation and Aggregation for Probabilistic Forecasting), a framework that replaces monolithic LLM prediction with itemized likelihood elicitation and deterministic probabilistic aggregation. By analyzing each piece of evidence separately to elicit likelihood parameters and combining them with an explicit prior, LEAP preserves traceable evidence contributions and improves calibration and accuracy across forecasting, information-seeking, and browsing tasks.

## Key Contributions

- Proposes LEAP (Likelihood Elicitation and Aggregation for Probabilistic Forecasting), which replaces monolithic prediction by separately eliciting likelihoods for each evidence item.
- Combines elicited likelihoods with an explicit prior and deterministic probabilistic model to produce well-calibrated posterior distributions across continuous, single-choice, and multi-choice forecasts.
- Demonstrates consistent improvements across prediction and calibration metrics over monolithic prediction baselines across models, inference budgets, and agent frameworks.

## Open Questions & Future Work

- [[extending-leap-evaluation-domains-languages]]

## Key Concepts

- [[leap]]: A probabilistic forecasting framework that elicits likelihood parameters separately for each evidence item and aggregates them via a deterministic model.

## Archivist Review

Approved the core LEAP concept for its novel itemized likelihood elicitation and probabilistic aggregation framework, along with one focused open question on extending its evaluation domains and horizons. Applied strict scarcity and quality filters.

### Approved Concepts
- LEAP: LEAP replaces monolithic LLM prediction with separate likelihood elicitation per evidence item combined via an explicit prior and probabilistic model.

### Approved Open Questions
- Broader Evaluation of Probabilistic Forecasting: Important for testing the generalizability and robustness of decoupled probabilistic aggregation approaches in LLM forecasting across diverse multi-lingual and domain-specific challenges.

## Links

- [Abstract](https://arxiv.org/abs/2609.01337)
- [PDF](https://arxiv.org/pdf/2609.01337)

