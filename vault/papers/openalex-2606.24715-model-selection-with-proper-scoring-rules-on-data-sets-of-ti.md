---
# CSL-compatible fields
title: "Model selection with proper scoring rules on data sets of time series"
author:
  - literal: "Giorgio Corani"
  - literal: "Stefano Damato"
  - literal: "Dario Azzimonti"
  - literal: "Lorenzo Zambon"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24715"

# Custom fields
paper_id: "2606.24715"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  - "m5-competition"
concept_slugs:
  []
dataset_slugs:
  - "m5-competition"
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:06Z"
created_at: "2026-06-26T08:25:06Z"
---

# Model selection with proper scoring rules on data sets of time series

**Authors**: Giorgio Corani, Stefano Damato, Dario Azzimonti, Lorenzo Zambon
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24715](https://arxiv.org/abs/2606.24715)

## Summary

This paper investigates the challenges of model selection for probabilistic time-series forecasting across multiple series. The authors identify how score distribution skewness leads to discrepancies between common metrics like mean score, median score, and mean rank. They demonstrate that the mean score is superior for small test sets, while all metrics converge as test length increases, emphasizing the necessity of large test sets in robust model evaluation.

## Key Contributions

- Demonstrates that conflicting decisions between mean score, median score, and mean rank metrics in time-series model selection stem from the skewness of score distributions.
- Establishes that the mean score is the most reliable criterion for identifying the true model when test sets are short.
- Proves that all three model selection criteria converge asymptotically as test set size increases.

## Open Questions & Future Work

- [[significance-testing-for-scaled-scores]]

## Archivist Review

The paper provides a rigorous analysis of the impact of score distribution skewness on model selection metrics for forecasting. I approved the open question regarding significance testing because it directly addresses the identified limitation of current evaluation practices (e.g., the tendency of Diebold-Mariano tests to yield false positives in large datasets). I rejected all conceptual candidates as the findings, while important, describe empirical properties of existing evaluation metrics rather than proposing new, reusable forecasting mechanisms or architectures.

### Approved Open Questions
- Significance testing for scaled scores: Reliable model selection in large-scale forecasting requires not only accurate point estimates of performance but also a rigorous way to determine if observed performance differences are statistically and practically significant. Without this, practitioners risk over-interpreting minor score improvements as evidence of model superiority.

### Rejected Candidates
- [dataset] M5 competition (`m5-competition`) - duplicate_existing: Dataset already exists as m5-competition in the vault.

## Datasets

- [[m5-competition]]

## Links

- [Abstract](https://arxiv.org/abs/2606.24715)
- [PDF](https://arxiv.org/pdf/2606.24715)

