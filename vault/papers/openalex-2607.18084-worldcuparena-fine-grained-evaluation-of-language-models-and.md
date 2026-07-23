---
# CSL-compatible fields
title: "WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agents on Football Forecasting"
author:
  - literal: "Zhaokai Wang"
  - literal: "Tianlin Gui"
  - literal: "Jiayuan Rao"
  - literal: "Shangzhe Di"
  - literal: "Yihong Tang"
  - literal: "D Liang"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.18084"

# Custom fields
paper_id: "2607.18084"
paper_source: "openalex"
domain: "nlp"
tags:
  - "benchmark"
  - "evaluation"
  - "agent"
  - "language-model"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:01Z"
created_at: "2026-07-23T07:27:01Z"
---

# WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agents on Football Forecasting

**Authors**: Zhaokai Wang, Tianlin Gui, Jiayuan Rao, Shangzhe Di, Yihong Tang, D Liang
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.18084](https://arxiv.org/abs/2607.18084)

## Summary

The paper introduces WorldCupArena, a dynamic evaluation benchmark designed to assess language models and deep-research agents on fine-grained football match forecasting before kickoff. Tested on 104 matches from the 2026 FIFA World Cup across 13 systems, the benchmark goes beyond simple match outcomes to evaluate exact scores, event predictions, and tournament trajectories. Results reveal that while top systems show modest gains over human fans and betting markets in exact result accuracy, they exhibit clearer differences in detailed scoreline and event forecasting.

## Key Contributions

- Introduces WorldCupArena, a dynamic benchmark for evaluating language models and deep-research agents on fine-grained football forecasting using the 2026 FIFA World Cup.
- Evaluates 13 systems across 104 matches, testing granular predictions such as exact scores, player events, match statistics, and tournament outcomes.
- Compares model performance against betting-market and human-fan baselines, demonstrating that systems differ more clearly on detailed predictions than raw result accuracy.
- Provides an open-source framework with support for adding new schedules to evaluate future models without data leakage.

## Archivist Review

Both candidates were rejected because WorldCupArena is primarily a sports evaluation benchmark rather than a reusable algorithmic mechanism, and the open question concerns routine multimodal extension.

### Rejected Candidates
- [concept] WorldCupArena (`world-cup-arena`) - low_impact: WorldCupArena is a benchmark and evaluation framework rather than a fundamental algorithmic concept, representation, or modeling method.
- [open_question] Multimodal Dynamic Sports Forecasting (`multimodal-dynamic-sports-forecasting`) - weak_evidence: The open question is a routine call for multimodal integration and future scaling rather than a distinct unresolved theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.18084)
- [PDF](https://arxiv.org/pdf/2607.18084)

