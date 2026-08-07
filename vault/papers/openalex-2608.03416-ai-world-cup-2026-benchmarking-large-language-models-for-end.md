---
# CSL-compatible fields
title: "AI World Cup 2026: Benchmarking Large Language Models for End-to-End Football Tournament Prediction"
author:
  - literal: "Jonaid Shianifar"
  - literal: "Iias Faiud"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03416"

# Custom fields
paper_id: "2608.03416"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "benchmark"
  - "evaluation"
  - "reasoning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:04:34Z"
created_at: "2026-08-07T06:04:34Z"
---

# AI World Cup 2026: Benchmarking Large Language Models for End-to-End Football Tournament Prediction

**Authors**: Jonaid Shianifar, Iias Faiud
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03416](https://arxiv.org/abs/2608.03416)

## Summary

This paper introduces the AI World Cup benchmark, evaluating ten large language models on end-to-end pre-tournament forecasting of the 2026 FIFA World Cup under identical conditions. Results reveal that overall tournament success is heavily driven by knockout phase accuracy rather than group-stage match-level predictability, exposing a divergence between match-level accuracy and bracket-based leaderboard performance.

## Key Contributions

- Evaluated ten LLM-based assistants on end-to-end forecasting of the 2026 FIFA World Cup under standardized prompts, data snapshots, and scoring rules.
- Found that overall leaderboard rankings correlated strongly with knockout phase performance ($r=0.986$) but showed no correlation with group-stage match point accuracy ($r=0.055$).
- Demonstrated that match-level predictive accuracy diverges from tournament-level success, where Claude Sonnet 4.6 achieved highest group-stage match accuracy but finished sixth overall.

## Open Questions & Future Work

- [[repeated-independent-forecasts-evaluation]]

## Archivist Review

Applied strict scarcity filters. No concepts or datasets met the bar for permanent standalone vault notes due to paper-local benchmark focus. Retained one open question concerning stochastic variance and robustness in tournament forecasting.

### Approved Open Questions
- Evaluating Stochastic Variance in Tournament Forecasting: Understanding sampling variance is essential for robust benchmarking of generative models on complex forecasting tasks, as single-run evaluations can be heavily influenced by decoding stochasticity rather than true model competence.

### Rejected Candidates
- [open_question] Evaluating Stochastic Variance in Tournament Forecasting (`repeated-independent-forecasts-evaluation`) - other: The open question was retained as the sole approved open question following rigorous evaluation.

## Links

- [Abstract](https://arxiv.org/abs/2608.03416)
- [PDF](https://arxiv.org/pdf/2608.03416)

