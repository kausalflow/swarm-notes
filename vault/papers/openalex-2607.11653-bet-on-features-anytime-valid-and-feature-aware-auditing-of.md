---
# CSL-compatible fields
title: "Bet on Features: Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters"
author:
  - literal: "Ivane Antonov"
  - literal: "Sohom Mukherjee"
  - literal: "Richard Pibernik"
  - literal: "Yo Joong Choe"
issued:
  date-parts:
    - [2026, 7, 13]
url: "https://arxiv.org/abs/2607.11653"

# Custom fields
paper_id: "2607.11653"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "anytime-valid-conditional-quantile-auditing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-16T07:14:14Z"
created_at: "2026-07-16T07:14:14Z"
---

# Bet on Features: Anytime-Valid and Feature-Aware Auditing of Conditional Quantile Forecasters

**Authors**: Ivane Antonov, Sohom Mukherjee, Richard Pibernik, Yo Joong Choe
**Date**: 2026-07-13
**Paper ID**: [openalex:2607.11653](https://arxiv.org/abs/2607.11653)

## Summary

This paper addresses the critical need for continuous, anytime-valid auditing of conditional quantile forecasters in non-i.i.d. settings where fixed-horizon backtesting fails. The authors propose a game-theoretic, distribution-free framework that allows auditors to detect miscalibration using feature-aware contextual bets. By formalizing how information coarseness impacts test power, the method provides finite-time detection guarantees and generates interpretable diagnostics at the feature level. Experiments demonstrate the framework's effectiveness in revealing significant miscalibration in state-of-the-art models like Chronos-2.

## Key Contributions

- Introduces an anytime-valid, game-theoretic framework for monitoring conditional quantile forecasters without i.i.d. assumptions.
- Formalizes the relationship between the auditor's information set coarseness and the difficulty of detecting quantile miscalibration.
- Derives finite-time detection guarantees for contextual, feature-aware calibration tests that enable interpretable diagnostics.

## Open Questions & Future Work

- [[nonlinear-betting-audits]]
- [[joint-comparative-auditing]]

## Key Concepts

- [[anytime-valid-conditional-quantile-auditing]]: A game-theoretic framework for continuously auditing quantile forecasters using contextual betting strategies.

## Archivist Review

I approved the overarching auditing framework and the two critical research bottlenecks identified by the authors. Chronos-2 was rejected as it is a model, not a dataset. The concepts and questions selected are central to the paper's contribution and provide a clear, reusable research direction for robust time-series evaluation.

### Approved Concepts
- Anytime-Valid Conditional Quantile Auditing: This provides a robust, non-i.i.d. alternative to static backtesting for real-world deployment monitoring.

### Approved Open Questions
- Nonlinear Conditional Quantile Auditing: Linear methods may lack the representational power to detect subtle conditional miscalibration in high-dimensional settings, which is a major limitation for complex black-box models.
- Joint and Comparative Auditing: Aggregating evidence across quantiles and comparative evaluation are critical for holistic model monitoring and decision-making in real-world deployments.

### Rejected Candidates
- [dataset] Chronos-2 (`Chronos-2`) - other: Chronos-2 is a forecasting model, not a dataset.

## Links

- [Abstract](https://arxiv.org/abs/2607.11653)
- [PDF](https://arxiv.org/pdf/2607.11653)

