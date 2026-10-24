---
# CSL-compatible fields
title: "GRAIL: From Saliency to Semantics in Time-Series Explanation"
author:
  - literal: "Enver Menadjiev"
  - literal: "Yiqiu Shen"
  - literal: "Jaesik Choi"
  - literal: "Julia Stoyanovich"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29036"

# Custom fields
paper_id: "2610.29036"
paper_source: "openalex"
domain: "nlp"
tags:
  - "interpretability"
  - "explainability"
  - "time-series"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:11:42Z"
created_at: "2026-10-24T09:11:42Z"
---

# GRAIL: From Saliency to Semantics in Time-Series Explanation

**Authors**: Enver Menadjiev, Yiqiu Shen, Jaesik Choi, Julia Stoyanovich
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29036](https://arxiv.org/abs/2610.29036)

## Summary

Explaining time-series models is often hindered by noisy per-timestep saliency and arbitrary counterfactual baselines. To overcome this, the authors propose GRAIL, a region-based explanation framework that treats domain-specific intervals and static covariates as cooperative players described by human-readable features. Using an on-manifold conditional generator for counterfactual baselines and Owen values for attribution, GRAIL produces faithful, robust explanations for domain experts.

## Key Contributions

- Proposes GRAIL, a region-based time-series explanation framework that utilizes domain-specific intervals as players.
- Incorporates human-readable features and an on-manifold conditional generator to avoid baseline domination in counterfactual evaluation.
- Integrates non-temporal static covariates as singleton players to attribute tabular evidence alongside temporal signals.
- Demonstrates faithful and robust explanations evaluated on synthetic and real datasets using Owen values with common-random-number variance reduction.

## Archivist Review

The candidate open question is routine future work suggesting user studies and handling non-stationary signals, which lacks the specificity required for permanent vault archiving. No concepts or datasets were proposed or deemed worthy under our strict sparsity and novelty guidelines.

### Rejected Candidates
- [open_question] User Studies and Non-Stationary Signals (`user-studies-and-non-stationary-signals-for-time-series-explanation`) - low_impact: Standard future work proposing user studies and handling non-stationary signals without formalizing a specific unresolved technical mechanism or bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.29036)
- [PDF](https://arxiv.org/pdf/2610.29036)

