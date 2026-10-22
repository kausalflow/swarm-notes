---
# CSL-compatible fields
title: "Conflicting History in Foundation Model Return Forecasts"
author:
  - literal: "Levent Bulut"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.25822"

# Custom fields
paper_id: "2610.25822"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
  - "llm"
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
processed_at: "2026-10-22T09:44:05Z"
created_at: "2026-10-22T09:44:05Z"
---

# Conflicting History in Foundation Model Return Forecasts

**Authors**: Levent Bulut
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.25822](https://arxiv.org/abs/2610.25822)

## Summary

This paper investigates the trade-off between retaining older observations to learn predictive relationships and discarding them when relationships change, focusing on financial return forecasts made by foundation models. Using paired return histories with identical recent returns but conflicting older observations across simulated and empirical asset datasets, the study demonstrates that conflicting history impairs model usefulness even when signals are recoverable under stable conditions. Furthermore, empirical evaluations on 56 assets show that shortening input context length consistently increases mean absolute error across all models, highlighting the nuanced role of long historical contexts.

## Key Contributions

- Investigates the tension between learning predictive relationships from older observations and handling regime changes in financial return forecasting.
- Demonstrates across five foundation-model forecasting procedures and three simulated processes that conflicting history reduces the probability of improving upon a zero baseline in higher-signal comparisons.
- Shows through empirical evaluation on 56 assets that shortening input context from 256 to 64 returns increases mean absolute error by 1.77-4.58 basis points for every evaluated model.

## Archivist Review

No concepts or datasets met the strict novelty and reusability criteria for permanent vault notes.

## Links

- [Abstract](https://arxiv.org/abs/2610.25822)
- [PDF](https://arxiv.org/pdf/2610.25822)

