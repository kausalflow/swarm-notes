---
# CSL-compatible fields
title: "Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection"
author:
  - literal: "Christos Panourgias"
  - literal: "Roberto Stanzione"
  - literal: "Adrien Petralia"
  - literal: "Themis Palpanas"
  - literal: "Paul Boniol"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20243"

# Custom fields
paper_id: "2610.20243"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ramsad"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:54:57Z"
created_at: "2026-10-17T08:54:57Z"
---

# Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection

**Authors**: Christos Panourgias, Roberto Stanzione, Adrien Petralia, Themis Palpanas, Paul Boniol
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20243](https://arxiv.org/abs/2610.20243)

## Summary

This paper proposes RAMSAD, a retrieval-based model selection framework for time-series anomaly detection that overcomes Out-of-Distribution (OOD) performance drops by querying a knowledge base of historical time series and transferring detector performance profiles via similarity search. Empirical results show that RAMSAD outperforms existing baselines in In-Distribution settings and matches or exceeds full-ensemble performance in OOD settings at a fraction of the cost.

## Key Contributions

- Introduces RAMSAD, a retrieval-based framework for model selection in time-series anomaly detection that queries a knowledge base of historical performance profiles.
- Demonstrates robust performance under Out-of-Distribution (OOD) settings, outperforming existing baseline model selectors.
- Matches or exceeds full-ensemble performance by selecting a small subset of detectors via similarity-based retrieval at a fraction of the computational cost.

## Open Questions & Future Work

- [[neighbor-disagreement-model-selection]]

## Key Concepts

- [[ramsad]]: A retrieval-based model selection framework for time-series anomaly detection that queries a knowledge base of performance profiles using similarity search.

## Archivist Review

Approved the RAMSAD framework concept and the open question regarding neighbor disagreement in model selection, following rigorous adherence to the review policy. No datasets were approved since none met the strict standalone criteria.

### Approved Concepts
- RAMSAD: RAMSAD introduces a novel retrieval-based framework for model selection in time-series anomaly detection, bridging the gap between similarity search and detector performance profiling.

### Approved Open Questions
- Handling Neighbor Disagreement in Selection: Understanding the robustness boundaries of profile aggregation under neighbor disagreement is theoretically critical for improving non-parametric model selection reliability.

## Links

- [Abstract](https://arxiv.org/abs/2610.20243)
- [PDF](https://arxiv.org/pdf/2610.20243)

