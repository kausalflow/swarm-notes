---
# CSL-compatible fields
title: "Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling"
author:
  - literal: "Eljas Linna"
  - literal: "Kęstutis Baltakys"
  - literal: "Derrick Manoharan"
  - literal: "Alexandros Iosifidis"
  - literal: "Juho Kanniainen"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.16930"

# Custom fields
paper_id: "2609.16930"
paper_source: "openalex"
domain: "finance"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "scenario-conditioned-market-impact-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:38Z"
created_at: "2026-09-17T09:44:38Z"
---

# Repurposing Deep Limit Order Book Forecasting for Scenario-Conditioned Market Impact Modeling

**Authors**: Eljas Linna, Kęstutis Baltakys, Derrick Manoharan, Alexandros Iosifidis, Juho Kanniainen
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.16930](https://arxiv.org/abs/2609.16930)

## Summary

This paper introduces a model-agnostic framework to repurpose pretrained deep limit order book forecasting models for scenario-conditioned market impact modeling by comparing predictive distributions before and after counterfactual message injection. Using a Transformer-based forecaster, the approach achieves high Spearman correlation and directional agreement with realized historical outcomes, demonstrating that existing forecasters can quantify counterfactual order book effects without retraining.

## Key Contributions

- Introduces a model-agnostic framework to evaluate and derive short-horizon model-implied market impact from pretrained deep limit order book forecasters via counterfactual message injection.
- Demonstrates that a Transformer-based forecaster recovers scenario rankings with a 0.99 Spearman correlation and 97.2% directional agreement with historical outcomes on non-neutral scenarios.
- Shows that observation-level impact estimates capture sequence-dependent variation beyond scenario identity and pre-event forecasts without requiring model retraining.

## Limitations

Focused primarily on short-horizon model-implied market impact and evaluated using specific Transformer-based architectures on historical limit order book data.

## Open Questions & Future Work

- [[generalizing-scenario-conditioned-impact-estimation]]

## Key Concepts

- [[scenario-conditioned-market-impact-modeling]]: A framework that repurposes pretrained limit order book forecasters to quantify counterfactual market impact through predictive distribution comparisons.

## Archivist Review

Approved the core concept of repurposing limit order book forecasters for counterfactual impact modeling along with its generalization open question. Kept selections strictly scarce in accordance with vault rules.

### Approved Concepts
- Scenario-Conditioned Market Impact Modeling: Repurposes deep limit order book forecasting models for counterfactual market impact estimation without retraining.

### Approved Open Questions
- Generalizing Scenario-Conditioned Impact Estimation: Determining whether scenario-conditioned response estimators generalize across diverse neural network architectures and multi-message counterfactuals is critical for robust execution algorithms and market surveillance systems.

## Links

- [Abstract](https://arxiv.org/abs/2609.16930)
- [PDF](https://arxiv.org/pdf/2609.16930)

