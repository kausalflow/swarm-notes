---
# CSL-compatible fields
title: "Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters"
author:
  - literal: "Xiao Ye"
  - literal: "Jacob Dineen"
  - literal: "Evan Zhu"
  - literal: "S Lu"
  - literal: "Kevin Song"
  - literal: "Ben Zhou"
issued:
  date-parts:
    - [2026, 7, 15]
url: "https://arxiv.org/abs/2607.14051"

# Custom fields
paper_id: "2607.14051"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "forecasting"
  - "reasoning"
  - "benchmark"
  - "evaluation"
  - "retrieval-augmented-generation"
  - "rag"
architectures:
  []
datasets:
  - "polymarket-prediction-market-data"
concept_slugs:
  - "hindcast-evaluation-framework"
dataset_slugs:
  - "polymarket-prediction-market-data"
skill: "TimeSeriesSkill"
processed_at: "2026-07-18T06:52:20Z"
created_at: "2026-07-18T06:52:20Z"
---

# Hindcast: Replaying Prediction Markets to Evaluate LLM Forecasters

**Authors**: Xiao Ye, Jacob Dineen, Evan Zhu, S Lu, Kevin Song, Ben Zhou
**Date**: 2026-07-15
**Paper ID**: [openalex:2607.14051](https://arxiv.org/abs/2607.14051)

## Summary

The paper addresses the issue of data leakage in LLM forecasting benchmarks, where models inadvertently access post-event information through either training data or retrieval mechanisms. To solve this, the authors introduce Hindcast, an evaluation framework that enforces strict temporal cutoffs per market, allowing models to only access information available before a specific past date. By scoring forecasts against both real outcomes and historical prediction market prices, the framework ensures a reliable measure of true foresight rather than retrieval-based recall. Results show that retrieval performance is significantly modulated by the quality of available pre-event information in the archival source.

## Key Contributions

- Introduces Hindcast, a rigorous evaluation framework that eliminates data leakage by enforcing temporal cutoffs for both retrieval and training data.
- Demonstrates that closing leakage reveals that retrieval-augmented forecasting performance is highly contingent on the quality of pre-event archival information.
- Establishes a reusable benchmark methodology using historical prediction market prices as a human-baseline reference.

## Open Questions & Future Work

- [[temporal-forecasting-data-diversity-bottleneck]]

## Key Concepts

- [[hindcast-evaluation-framework]]: A framework for evaluating LLM forecasting capabilities by replaying markets against time-restricted snapshots.

## Archivist Review

I approved the Hindcast evaluation framework as a distinct and reusable concept for time-locked LLM evaluation. I selected Polymarket as a dataset as it is central to the framework's evaluation claims. I consolidated the open questions into a single robust query regarding the bottleneck of data diversity in temporal evaluation protocols, rejecting the generic request for more architecture benchmarking.

### Approved Concepts
- Hindcast Evaluation Framework: It provides a rigorous methodology for evaluating LLM foresight by enforcing temporal cutoffs and using market prices as a human-baseline, directly addressing data leakage.

### Approved Open Questions
- Temporal forecasting data diversity: The reliance on narrow data sources creates systemic evaluation bias, obscuring model performance on topics not well-represented in existing corpora.

### Rejected Candidates
- [open_question] Broadening hindcasting data sources (`broadening-hindcasting-data-sources`) - duplicate_existing: This is a near-duplicate of the broader temporal data diversity question, which I have generalized to better capture the research bottleneck.
- [open_question] Evaluating diverse agent architectures (`evaluating-diverse-agent-architectures`) - low_impact: This is a broad, boilerplate call for testing more models and architectures, which is standard future work for almost any benchmarking paper.

## Datasets

- [[polymarket-prediction-market-data]]

## Links

- [Abstract](https://arxiv.org/abs/2607.14051)
- [PDF](https://arxiv.org/pdf/2607.14051)

