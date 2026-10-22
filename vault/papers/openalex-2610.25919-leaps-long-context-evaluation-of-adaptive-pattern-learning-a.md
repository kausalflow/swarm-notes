---
# CSL-compatible fields
title: "LEAPS: Long-context Evaluation of Adaptive Pattern Learning and State Tracking"
author:
  - literal: "Howard H Yen"
  - literal: "Nitya Mani"
  - literal: "Alex Renda"
  - literal: "Christopher S. Hardin"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.25919"

# Custom fields
paper_id: "2610.25919"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "long-context"
  - "benchmark"
  - "evaluation"
  - "reasoning"
architectures:
  - "decoder-only"
datasets:
  - "leaps"
concept_slugs:
  []
dataset_slugs:
  - "leaps"
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:45:11Z"
created_at: "2026-10-22T09:45:11Z"
---

# LEAPS: Long-context Evaluation of Adaptive Pattern Learning and State Tracking

**Authors**: Howard H Yen, Nitya Mani, Alex Renda, Christopher S. Hardin
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.25919](https://arxiv.org/abs/2610.25919)

## Summary

The paper introduces LEAPS, a collection of 12 contamination-resistant datasets designed to evaluate long-context language models beyond simple recall, specifically targeting state tracking and adaptive pattern learning across up to millions of input tokens. Evaluating 30 API and open models reveals that while models may excel at recall, their state tracking and pattern learning capabilities degrade significantly as input length increases, with thinking models often underperforming base models due to budget exhaustion or oversimplification.

## Key Contributions

- Introduces LEAPS, a collection of 12 contamination-resistant datasets spanning agentic workflows, behavioral modeling, and forecasting across up to millions of input tokens.
- Evaluates 30 API and open long-context language models, revealing that state tracking and pattern learning abilities degrade much more dramatically with input length compared to recall tasks.
- Finds that reasoning/thinking models often underperform their base counterparts on these tasks by exhausting their generation budget or oversimplifying.

## Limitations

Evaluations are limited to models ranging from 8K to 512K input tokens.

## Open Questions & Future Work

- [[effective-post-training-for-state-tracking-and-pattern-learning]]

## Archivist Review

Applied strict selection criteria for the vault. Approved the named dataset collection LEAPS and the associated open question on post-training for long-context capabilities, while rejecting LEAPS as a concept since it is primarily a benchmark dataset suite rather than an algorithmic modeling primitive.

### Approved Open Questions
- Effective Post-Training for Long-Context Capabilities: Crucial for guiding the design of future alignment and post-training algorithms so that reasoning enhancements do not degrade native long-context utilization and representation.

### Rejected Candidates
- [concept] LEAPS (`leaps`) - not_reusable: LEAPS is fundamentally a benchmark/dataset collection rather than a modeling concept or algorithmic mechanism.

## Datasets

- [[leaps]]

## Links

- [Abstract](https://arxiv.org/abs/2610.25919)
- [PDF](https://arxiv.org/pdf/2610.25919)

