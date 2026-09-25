---
# CSL-compatible fields
title: "Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models"
author:
  - literal: "Jinmyeong Choi"
  - literal: "Jinkwan Jang"
  - literal: "Seul Lee"
  - literal: "Taesup Kim"
  - literal: "Jinmyeong Choi"
  - literal: "Jinkwan Jang"
  - literal: "Seul Lee"
  - literal: "Taesup Kim"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25980"

# Custom fields
paper_id: "2609.25980"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
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
processed_at: "2026-09-25T09:54:06Z"
created_at: "2026-09-25T09:54:06Z"
---

# Interweaving Marginals into Multivariate Sample Paths: Training-Free Dependence Construction for Probabilistic Time Series Foundation Models

**Authors**: Jinmyeong Choi, Jinkwan Jang, Seul Lee, Taesup Kim, Jinmyeong Choi, Jinkwan Jang, Seul Lee, Taesup Kim
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25980](https://arxiv.org/abs/2609.25980)

## Summary

Probabilistic time series foundation models typically yield coordinate-wise predictive distributions that lack joint multivariate dependencies. This paper investigates training-free coupling methods to interweave these frozen marginals into coherent multivariate sample paths. By isolating coupling effects through fixed empirical marginal multisets and evaluating native backbone inference, the authors show that leveraging historical temporal and channel relations significantly improves dependence diagnostics.

## Key Contributions

- Formulates dependence reconstruction as a distinct training-free post-processing problem for probabilistic time series foundation models.
- Evaluates coupling strategies by fixing empirical marginal sample multisets to isolate dependence reconstruction performance across channels and horizons.
- Demonstrates that historical temporal and channel relations substantially enhance dependence diagnostics across both constrained marginal and native multivariate backbone evaluations.

## Open Questions & Future Work

- [[richer-post-hoc-dependence-models]]

## Archivist Review

Applied strict scarcity and reusability standards. No novel standalone concepts or named datasets qualified for permanent vault entry, but one open question addressing post-hoc dependence reconstruction limits was approved.

### Approved Open Questions
- Richer Post-Hoc Dependence Models: It highlights an explicit methodological limitation in current separable copula formulations and outlines a concrete direction for improving training-free dependence construction in time series foundation models.

## Links

- [Abstract](https://arxiv.org/abs/2609.25980)
- [PDF](https://arxiv.org/pdf/2609.25980)

