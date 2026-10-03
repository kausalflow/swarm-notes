---
# CSL-compatible fields
title: "When, Not How Much: Evaluating Time-Series Foundation Models on Sparse Events"
author:
  - literal: "Daniel Schoess"
  - literal: "Florian von Wangenheim"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39386"

# Custom fields
paper_id: "2609.39386"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
  - "in-context-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:32Z"
created_at: "2026-10-03T10:07:32Z"
---

# When, Not How Much: Evaluating Time-Series Foundation Models on Sparse Events

**Authors**: Daniel Schoess, Florian von Wangenheim
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39386](https://arxiv.org/abs/2609.39386)

## Summary

Pretrained time-series foundation models (TSFMs) are typically evaluated on continuous value forecasting, but many real-world applications require predicting sparse events (when activity occurs rather than how much). Evaluating 12 TSFMs across five sparse datasets reveals that their standard point forecasts offer minimal improvement over training-free references. However, adding lightweight linear probes or averaging predicted quantiles substantially improves event ranking, highlighting the need for comprehensive evaluation protocols including supervised probes and randomized controls for tasks beyond value forecasting.

## Key Contributions

- Evaluates 12 pretrained time-series foundation models (TSFMs) on sparse-event forecasting tasks across five sparse datasets, finding that standard point forecasts add little over simple training-free references.
- Demonstrates that lightweight event supervision (linear probes on frozen backbones) consistently improves sparse-event ranking over raw backbones in 29 of 30 pairs, with pretrained features outperforming random ones.
- Shows that averaging predicted quantiles instead of taking the median improves sparse-event ranking for TSFMs.
- Proposes an evaluation framework requiring raw-context, randomized controls, and supervised probes side by side when assessing pretrained forecasters on tasks beyond value forecasting.

## Limitations

Evaluated specifically on sparse-event ranking tasks rather than general continuous value forecasting.

## Open Questions & Future Work

- [[sparse-event-decision-benchmarks]]

## Archivist Review

Approved the open question regarding decision-aware sparse-event benchmarking as it targets a distinct methodological gap in time-series foundation model evaluation. No concepts or datasets met the strict novelty and reusability standards for permanent vault entries.

### Approved Open Questions
- Decision-Aware Sparse-Event Benchmarks: Important for extending time-series foundation models beyond value-forecasting to real-world operational decision-making tasks like inventory management and anomaly detection.

## Links

- [Abstract](https://arxiv.org/abs/2609.39386)
- [PDF](https://arxiv.org/pdf/2609.39386)

