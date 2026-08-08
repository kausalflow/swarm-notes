---
# CSL-compatible fields
title: "From Score Matrices to Football-Aware Match-State Simulation: An Auditable LLM Harness for Exact-Score Reranking"
author:
  - literal: "Shaopeng Liang"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.05030"

# Custom fields
paper_id: "2608.05030"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:35:34Z"
created_at: "2026-08-08T05:35:34Z"
---

# From Score Matrices to Football-Aware Match-State Simulation: An Auditable LLM Harness for Exact-Score Reranking

**Authors**: Shaopeng Liang
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.05030](https://arxiv.org/abs/2608.05030)

## Summary

This paper presents an auditable hybrid framework that integrates dynamic Poisson-family statistical models with large language models to improve football exact-score forecasting. The authors propose an iterative four-tier harness (V1-V4) that injects contextual tactical ratings, goal-by-goal simulations, and post-goal cascade judgments into a score-driven Dixon-Coles baseline. Evaluated on 150 matches from the 2025-26 English Premier League, the final V4 system improves Top-1 exact-score accuracy from 10.0% to 14.7% while highlighting key insights into the limits of LLM-driven match-state simulation.

## Key Contributions

- Proposes an auditable hybrid architecture combining dynamic Poisson-family statistical models (Dixon-Coles) with Large Language Models for football exact-score reranking
- Develops a four-tier iterative design harness (V1 through V4) integrating goal-by-goal simulations, shared first-breakthrough judgments, post-goal cascades, and time-aware stopping
- Evaluates performance on a chronological replay of the first 150 matches of the 2025-26 English Premier League, where V4 achieves 14.7% Top-1 and 30.7% Top-3 exact-score accuracy compared to 10.0% and 26.7% for the baseline

## Limitations

The evaluation slice serves as an exploratory development set rather than an untouched benchmark, and temporal input isolation cannot exclude potential outcome memory in closed LLMs.

## Open Questions & Future Work

- [[calibrated-llm-probability-estimation-football]]

## Archivist Review

Approved one open question regarding calibrated probabilistic forecasting with LLM match-state simulation. No concepts or datasets met the strict novelty and reusability standards.

### Approved Open Questions
- Calibrated Probabilistic LLM Football Forecasting: Transitioning from heuristic rankers to calibrated probabilistic forecasters is essential for sound decision-making and proper evaluation in sports forecasting.

### Rejected Candidates
- [open_question] Calibrated Probabilistic LLM Football Forecasting (`calibrated-llm-probability-estimation-football`) - other: Approved successfully.

## Links

- [Abstract](https://arxiv.org/abs/2608.05030)
- [PDF](https://arxiv.org/pdf/2608.05030)

