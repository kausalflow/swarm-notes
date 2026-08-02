---
# CSL-compatible fields
title: "Train Often, Deploy Selectively: Forward-Gated Model Replacement in Crypto Markets"
author:
  - literal: "Aditya Dutta"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28577"

# Custom fields
paper_id: "2607.28577"
paper_source: "openalex"
domain: "finance"
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
processed_at: "2026-08-02T07:27:23Z"
created_at: "2026-08-02T07:27:23Z"
---

# Train Often, Deploy Selectively: Forward-Gated Model Replacement in Crypto Markets

**Authors**: Aditya Dutta
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28577](https://arxiv.org/abs/2607.28577)

## Summary

Production forecasting systems frequently retrain models, but newly trained candidates often fail to outperform continuously maintained incumbents. This paper introduces Shadow Before Swap (SBS), a deployment policy that warm-refits candidate models off the serving path and promotes them only after achieving a fixed paired negative-log-likelihood advantage over the incumbent on delayed labels. Evaluated on Binance crypto market data across 48 UTC weeks, SBS improves probabilistic forecasting performance while reducing deployed model transitions by 78.4%.

## Key Contributions

- Introduces Shadow Before Swap (SBS), a forward-gated model replacement deployment policy that evaluates warm-refit challengers against incumbents on delayed labels before promotion.
- Achieves a NLL reduction of 0.1472% over calendar replacement and 0.0428% over continuous maintenance across two Binance episodes spanning 48 UTC weeks.
- Reduces deployed model changes by 78.4% by promoting only 114 of 528 candidate models based on a fixed paired NLL advantage.

## Archivist Review

The paper introduces 'Shadow Before Swap (SBS)', a deployment policy for model replacement in forecasting. However, deployment management policies are systems/engineering strategies rather than core forecasting mechanisms, representations, or temporal inductive biases. The proposed open question is standard boilerplate future work. Thus, no permanent vault notes are approved.

### Rejected Candidates
- [open_question] Live Deployment and Broader Asset Classes (`live-deployment-and-broader-asset-classes`) - low_impact: Standard boilerplate future work proposing extension to new asset classes and live deployment without identifying a specific unresolved algorithmic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.28577)
- [PDF](https://arxiv.org/pdf/2607.28577)

