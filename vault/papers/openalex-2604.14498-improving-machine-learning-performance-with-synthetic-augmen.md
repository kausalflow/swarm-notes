---
# CSL-compatible fields
title: "Improving Machine Learning Performance with Synthetic Augmentation"
author:
  - literal: "Mel Sohm"
  - literal: "Charles Dezons"
  - literal: "Sami Sellami"
  - literal: "Oscar Ninou"
  - literal: "Axel Pinçon"
issued:
  date-parts:
    - [2026, 4, 16]
url: "https://arxiv.org/abs/2604.14498"

# Custom fields
paper_id: "2604.14498"
paper_source: "openalex"
domain: "finance"
tags:
  - "synthetic-data-augmentation"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "synthetic-data-augmentation-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-19T06:25:04Z"
created_at: "2026-04-19T06:25:04Z"
---

# Improving Machine Learning Performance with Synthetic Augmentation

**Authors**: Mel Sohm, Charles Dezons, Sami Sellami, Oscar Ninou, Axel Pinçon
**Date**: 2026-04-16
**Paper ID**: [openalex:2604.14498](https://arxiv.org/abs/2604.14498)

## Summary

This paper provides a rigorous statistical framework for evaluating the impact of synthetic data augmentation in financial machine learning. The authors demonstrate that synthetic samples alter the training distribution, inducing a bias-variance trade-off that determines whether performance improves or degrades. Through a block permutation test, the study shows that augmentation benefits variance-dominant tasks like volatility forecasting while hindering bias-sensitive tasks like efficient market directional prediction.

## Key Contributions

- Formalizes synthetic augmentation as a modification of the training distribution, revealing a structural bias-variance trade-off driven by distributional shifts.
- Introduces a size-matched null augmentation and a finite-sample, non-parametric block permutation test to isolate informational gains from sample-size effects.
- Demonstrates through extensive experimentation that synthetic data improves performance only in variance-dominant regimes (e.g., volatility forecasting) but harms bias-dominant settings (e.g., directional prediction).

## Open Questions & Future Work

- [[generalizability-of-synthetic-augmentation-trade-offs]]

## Key Concepts

- [[synthetic-data-augmentation-framework]]: A framework that treats synthetic data augmentation as a modification of the training distribution, exposing the structural bias-variance trade-off induced by generator deviation.

## Archivist Review

I approved the proposed framework for analyzing the bias-variance trade-off of synthetic augmentation, as it provides a valuable structural lens for future research on data generation. I rejected the initial concept as it was too generic, and requested a more focused open question about the theoretical validity of these findings across different temporal domains.

### Approved Concepts
- Synthetic Data Augmentation Framework: Provides a formal statistical grounding for the utility of synthetic data in time-series forecasting, explicitly defining the regime-dependent trade-offs between estimation error and distributional shift.

### Approved Open Questions
- Synthetic Augmentation Trade-off Generalizability: Validating whether the proposed statistical trade-offs are fundamental to synthetic learning or specific to financial volatility dynamics is critical for adopting these methods in other fields.

### Rejected Candidates
- [concept] synthetic-data-augmentation (`synthetic-data-augmentation`) - generic: This is a broad task description rather than a specific mechanism or methodological contribution.
- [open_question] Cross-Domain Generalizability of Framework (`cross-domain-generalizability-of-synthetic-augmentation-framework`) - low_impact: This is essentially a request for more experiments/applications across domains rather than a specific technical bottleneck or theoretical challenge.

## Links

- [Abstract](https://arxiv.org/abs/2604.14498)
- [PDF](https://arxiv.org/pdf/2604.14498)

