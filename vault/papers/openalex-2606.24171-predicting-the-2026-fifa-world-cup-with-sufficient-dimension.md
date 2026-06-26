---
# CSL-compatible fields
title: "Predicting the 2026 FIFA World Cup with Sufficient Dimension Reduction of Elo Rating Histories"
author:
  - literal: "Mina Rezaei"
  - literal: "S. Yaser Samadi"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24171"

# Custom fields
paper_id: "2606.24171"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "categorical-sdr-sports-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:51Z"
created_at: "2026-06-26T08:25:51Z"
---

# Predicting the 2026 FIFA World Cup with Sufficient Dimension Reduction of Elo Rating Histories

**Authors**: Mina Rezaei, S. Yaser Samadi
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24171](https://arxiv.org/abs/2606.24171)

## Summary

This paper presents a probabilistic forecasting framework for the 2026 FIFA World Cup, utilizing recent Elo rating histories to estimate team strength. The authors employ categorical sufficient dimension reduction (SDR) to extract informative, low-dimensional features from historical Elo differences, which are then integrated into a Poisson double-regression model to calculate full match outcome probabilities. Empirical results on 2018 and 2022 World Cup data demonstrate that the SDR-based Poisson approach captures latent predictive information missed by standard Elo ratings or baseline models like ARIMA and logistic regression.

## Key Contributions

- Introduces a categorical sufficient dimension reduction (SDR) framework to extract informative temporal features from Elo rating histories for sports forecasting.
- Proposes a Poisson double-regression model utilizing SDR-reduced scores to predict match outcome probabilities for the 48-team 2026 FIFA World Cup format.
- Demonstrates that SDR-based Poisson models outperform traditional approaches (ARIMA, standard Poisson, logistic regression) on 2018 and 2022 World Cup benchmark evaluations using the ranked probability score (RPS).

## Open Questions & Future Work

- [[holistic-sports-data-integration-stability]]

## Key Concepts

- [[categorical-sdr-sports-forecasting]]: A methodology that utilizes categorical sufficient dimension reduction to extract predictive latent features from time-series histories for sports forecasting.

## Archivist Review

I approved the categorical SDR concept for sports forecasting as it offers a reusable, systematic way to handle historical time-series context in predictive models. I approved the question regarding holistic integration of diverse sports data as it highlights a persistent challenge in sports science forecasting when moving beyond simple rating-based models. The dataset candidates were rejected as they refer to specific tournament editions rather than foundational, long-lived scientific data sources.

### Approved Concepts
- Categorical Sufficient Dimension Reduction (SDR) for Sports Forecasting: It provides a structured way to compress high-dimensional historical rating or performance features into low-dimensional latent spaces suitable for probabilistic outcome modeling in ranked-entity systems.

### Approved Open Questions
- Holistic Sports Data Integration: Transitioning from single-metric models to holistic, multi-modal forecasting is critical for improving predictive accuracy in sports, especially as tournament scales increase.

### Rejected Candidates
- [concept] Categorical Sufficient Dimension Reduction (SDR) for Elo Rating Histories (`categorical-sdr-elo-history`) - duplicate_existing: The concept was renamed for broader applicability and to avoid over-specification to Elo ratings alone.
- [open_question] Integrating Holistic Sports Data (`multi-modal-sports-forecasting-integration`) - duplicate_existing: The question was slightly reframed for standard naming convention and clarity.

## Links

- [Abstract](https://arxiv.org/abs/2606.24171)
- [PDF](https://arxiv.org/pdf/2606.24171)

