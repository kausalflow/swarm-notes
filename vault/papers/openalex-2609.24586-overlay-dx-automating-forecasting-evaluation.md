---
# CSL-compatible fields
title: "Overlay_dx - Automating forecasting evaluation"
author:
  - literal: "Long Ngo"
  - literal: "Mohammed Amine Chamli"
  - literal: "Jonathan Rivalan"
  - literal: "Thomas Jaillon"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24586"

# Custom fields
paper_id: "2609.24586"
paper_source: "openalex"
domain: "time-series"
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
processed_at: "2026-09-24T09:38:04Z"
created_at: "2026-09-24T09:38:04Z"
---

# Overlay_dx - Automating forecasting evaluation

**Authors**: Long Ngo, Mohammed Amine Chamli, Jonathan Rivalan, Thomas Jaillon
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24586](https://arxiv.org/abs/2609.24586)

## Summary

Traditional time series evaluation metrics provide numerical summaries but often lack intuitive comprehensibility for model comparison. To address this, the authors introduce overlay_dx, a visual evaluation metric representing the percentage of predictions falling within a confidence interval around actual values. By computing the area under the resulting overlay curve, overlay_dx yields a quantitative measure of prediction-actual alignment across various thresholds.

## Key Contributions

- Introduces overlay_dx, a novel visual and quantitative evaluation metric for time-series forecasting that measures the percentage of predictions falling within a confidence interval across thresholds.
- Computes the area under the overlay curve to provide a single quantitative measure of alignment between predicted and actual values.
- Demonstrates through extensive experiments that overlay_dx provides a unified evaluation framework combining visual and numerical assessment for improved model comparison.

## Archivist Review

No concepts met the strict threshold for novelty and long-term reusability; overlay_dx is a specific evaluation utility rather than a foundational technique.

## Links

- [Abstract](https://arxiv.org/abs/2609.24586)
- [PDF](https://arxiv.org/pdf/2609.24586)

