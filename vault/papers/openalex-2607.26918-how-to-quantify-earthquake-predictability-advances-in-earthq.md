---
# CSL-compatible fields
title: "How to quantify earthquake predictability? Advances in earthquake forecasting and predictability limits"
author:
  - literal: "Jiancang Zhuang"
  - literal: "Didier Sornette"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26918"

# Custom fields
paper_id: "2607.26918"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "anomaly-detection"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:23:17Z"
created_at: "2026-08-01T07:23:17Z"
---

# How to quantify earthquake predictability? Advances in earthquake forecasting and predictability limits

**Authors**: Jiancang Zhuang, Didier Sornette
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26918](https://arxiv.org/abs/2607.26918)

## Summary

This paper develops a unified information-theoretic framework to quantify earthquake predictability by framing it as an entropy gap between complete randomness and the true data-generating process using Shannon entropy and Kullback-Leibler divergence. The authors derive entropy rates for Poisson and ETAS point processes, identifying the intrinsic predictability rate as an information gain functional of the conditional intensity. Furthermore, they analyze predictability across time, space, and magnitude dimensions, showing how mutual information from high-dimensional pre-event observations establishes fundamental limits and guides future forecasting improvements.

## Key Contributions

- Develops a unified information-theoretic framework to quantify earthquake predictability using Shannon entropy and Kullback-Leibler divergence
- Derives entropy rates and intrinsic predictability rates for point processes including the Poisson process and ETAS model
- Clarifies how magnitude predictability requires separating marginal magnitude statistics from genuine inter-event dependence
- Reframes forecasting progress around extracting structured dependence via high-dimensional pre-event observations and mutual information

## Open Questions & Future Work

- [[earthquake-magnitude-dependence-predictability]]

## Archivist Review

Applied strict scarcity and domain-reusability criteria. No standalone concepts were approved as the information-theoretic formulation of predictability is standard for point processes. The open question is specific to seismological magnitude statistics and was rejected for low cross-domain impact.

### Approved Open Questions
- Quantifying Earthquake Magnitude Predictability: Resolving magnitude dependence is critical for advancing earthquake forecasting beyond standard ETAS models and determining the fundamental limits of magnitude predictability.

### Rejected Candidates
- [open_question] Quantifying Earthquake Magnitude Predictability (`earthquake-magnitude-dependence-predictability`) - low_impact: The paper provides a thorough review of information-theoretic frameworks and point process entropy rates, but the open question regarding magnitude predictability is domain-specific to seismology rather than broadly reusable across time-series machine learning.

## Links

- [Abstract](https://arxiv.org/abs/2607.26918)
- [PDF](https://arxiv.org/pdf/2607.26918)

