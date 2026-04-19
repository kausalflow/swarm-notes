---
# CSL-compatible fields
title: "Assessing the Performance-Efficiency Trade-off of Foundation Models in Probabilistic Electricity Price Forecasting"
author:
  - literal: "Jan Niklas Lettner"
  - literal: "Hadeer El Ashhab"
  - literal: "Veit Hagenmeyer"
  - literal: "Benjamin Schäfer"
issued:
  date-parts:
    - [2026, 4, 16]
url: "https://arxiv.org/abs/2604.14739"

# Custom fields
paper_id: "2604.14739"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "few-shot-learning"
  - "llm"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-19T06:24:07Z"
created_at: "2026-04-19T06:24:07Z"
---

# Assessing the Performance-Efficiency Trade-off of Foundation Models in Probabilistic Electricity Price Forecasting

**Authors**: Jan Niklas Lettner, Hadeer El Ashhab, Veit Hagenmeyer, Benjamin Schäfer
**Date**: 2026-04-16
**Paper ID**: [openalex:2604.14739](https://arxiv.org/abs/2604.14739)

## Summary

This paper conducts a comparative analysis of task-specific models and Time Series Foundation Models (TSFMs) for probabilistic electricity price forecasting across European bidding zones. The study evaluates models including NHITS with Quantile-Regression Averaging, Normalizing-Flows, Moirai, and ChronosX. Results indicate that while TSFMs provide strong performance in uncertainty quantification and interval calibration, traditional models are highly competitive and can sometimes outperform TSFMs when utilizing specific domain features or cross-market adaptation, highlighting a significant performance-efficiency trade-off.

## Key Contributions

- Evaluates the performance-efficiency trade-off between task-specific models (NHITS+QRA, Normalizing-Flow) and Time Series Foundation Models (Moirai, ChronosX) for day-ahead probabilistic electricity price forecasting.
- Demonstrates that while TSFMs achieve superior CRPS and Energy Scores, well-configured task-specific models remain highly competitive and can outperform TSFMs when augmented with domain-specific features or cross-market few-shot adaptation.
- Provides evidence that computational expense is a critical factor, as marginal performance gains from TSFMs may not justify the added complexity compared to optimized conventional deep learning architectures.

## Open Questions & Future Work

- [[performance-efficiency-trade-off-pepf]]

## Archivist Review

This paper provides a pragmatic comparative analysis of model types for electricity price forecasting. I have approved one open question that captures the central bottleneck of balancing foundation model capabilities against the efficiency and domain-specific strengths of traditional architectures. No new concepts were approved as the models and techniques used are existing standards within the forecasting domain.

### Approved Open Questions
- TSFM vs Task-Specific Model Efficiency: As foundation models proliferate in time series, understanding when to favor specialized architectures versus general ones is a critical decision-making bottleneck for practitioners.

### Rejected Candidates
- [open_question] Trade-off between TSFMs and task-specific models in PEPF (`performance-efficiency-trade-off-pepf`) - duplicate_existing: The candidate is a near-duplicate of the approved open question; the approved version is more concise and fits the vault style better.

## Links

- [Abstract](https://arxiv.org/abs/2604.14739)
- [PDF](https://arxiv.org/pdf/2604.14739)

