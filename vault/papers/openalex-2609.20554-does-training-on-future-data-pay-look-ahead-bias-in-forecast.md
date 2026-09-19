---
# CSL-compatible fields
title: "Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models"
author:
  - literal: "Haiqiang Chen"
  - literal: "Li Chen"
  - literal: "Yunlong Chen"
  - literal: "Difang Huang"
  - literal: "Bo Zhang"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20554"

# Custom fields
paper_id: "2609.20554"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "finance"
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
processed_at: "2026-09-19T09:04:08Z"
created_at: "2026-09-19T09:04:08Z"
---

# Does Training on Future Data Pay? Look-Ahead Bias in Forecasting with Pretrained Models

**Authors**: Haiqiang Chen, Li Chen, Yunlong Chen, Difang Huang, Bo Zhang
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20554](https://arxiv.org/abs/2609.20554)

## Summary

This paper investigates look-ahead bias in financial forecasting with pretrained models by examining whether post-origin training information inflates measured accuracy and economic value. Evaluating five sets of financial foundation models across 14 equity markets and multiple horizons, the authors show that post-origin data revisions often degrade forecast accuracy and lower economic value in terms of certainty-equivalent returns. An exact squared-error decomposition reveals that the error-correcting benefits of such revisions frequently fail to exceed their mean squared magnitude under U.S. training environments.

## Key Contributions

- Evaluated five sets of financial time-series foundation models across 14 equity markets and four forecast horizons to quantify the impact of post-origin training information (look-ahead bias) on predictive accuracy and economic value.
- Demonstrated that pooled rolling comparisons yield higher mean squared forecast errors in 18 of 20 U.S. model-set-horizon combinations when using post-origin data.
- Showed through a constrained allocation rule that using post-origin forecasts leads to lower median annualized certainty-equivalent returns (-1.77 percentage points in the U.S. and -2.14 internationally).
- Established via an exact squared-error decomposition that error-correcting benefits of post-origin revisions generally fall short of their mean squared magnitude under U.S. training.

## Open Questions & Future Work

- [[look-ahead-bias-foundation-models-finance]]

## Archivist Review

The paper investigates look-ahead bias and temporal data leakage in financial time-series foundation models rather than proposing a new method, model architecture, or dataset. The sole open question about look-ahead bias in financial foundation models duplicates existing evaluation concerns regarding temporal contamination and leakage already tracked in the vault.

### Approved Open Questions
- Look-Ahead Bias in Financial Foundation Models: Crucial for machine learning in econometrics and finance to establish valid causal attribution of performance gains in foundation models versus temporal data leakage.

### Rejected Candidates
- [open_question] Look-Ahead Bias in Financial Foundation Models (`look-ahead-bias-foundation-models-finance`) - duplicate_existing: A very similar open question regarding look-ahead bias and temporal leakage in financial forecasting models already exists in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2609.20554)
- [PDF](https://arxiv.org/pdf/2609.20554)

