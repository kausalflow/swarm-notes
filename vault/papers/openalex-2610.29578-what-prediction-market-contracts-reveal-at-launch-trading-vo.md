---
# CSL-compatible fields
title: "What Prediction-Market Contracts Reveal at Launch: Trading Volume and Dispute Risk"
author:
  - literal: "Ahmed Mahrous"
  - literal: "Roberto Di Pietro"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29578"

# Custom fields
paper_id: "2610.29578"
paper_source: "openalex"
domain: "finance"
tags:
  - "benchmark"
  - "evaluation"
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
processed_at: "2026-10-24T09:13:06Z"
created_at: "2026-10-24T09:13:06Z"
---

# What Prediction-Market Contracts Reveal at Launch: Trading Volume and Dispute Risk

**Authors**: Ahmed Mahrous, Roberto Di Pietro
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29578](https://arxiv.org/abs/2610.29578)

## Summary

This paper investigates what launch-time contract metadata and text reveal about lifetime trading volume and dispute risk across over 800,000 Polymarket prediction markets. The authors find that interpretable features—particularly market topic—strongly predict trading volume (out-of-sample R^2 = 0.747), whereas neural text models yield marginal improvements. However, temporal distribution shifts caused by platform format changes severely degrade cross-quarter predictive accuracy, and while dispute risk can be effectively ranked (AUC 0.78), low base rates limit case-by-case precision.

## Key Contributions

- Predicts lifetime trading volume (out-of-sample log volume R^2 = 0.747) and settlement dispute risk (AUC 0.78) for prediction-market contracts using only launch-time metadata and text.
- Shows that market topic contributes the largest predictive gain (+0.289 R^2) over baselines, while neural text models add minimal value beyond interpretable features.
- Demonstrates severe temporal degradation under platform formatting shifts, where cross-quarter prediction accuracy for reaching $1,000 in volume drops from AUC 0.940 to 0.577 due to novel question forms and shifting feature-demand relationships.
- Finds that dispute risk predictors achieve good ranking performance (AUC 0.78) but suffer from low precision (average precision 0.012) due to a low base rate of 0.31%, making them suitable for ranking market groups rather than individual disputes.

## Limitations

Temporal distribution shifts in platform listing formats severely degrade cross-quarter predictive performance, and low dispute base rates limit case-by-case precision.

## Archivist Review

Reviewed the provided paper analysis on prediction market volume and dispute risk. The open question is specific to prediction-market forecasting and platform regime shifts rather than general time-series methodology, so no items meet our strict vault inclusion criteria.

### Rejected Candidates
- [open_question] Novelty-Aware Prediction Market Forecasting (`novelty-aware-prediction-market-forecasting`) - low_impact: The open question targets prediction market forecasting domain specifics rather than core time-series forecasting methodology or temporal dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2610.29578)
- [PDF](https://arxiv.org/pdf/2610.29578)

