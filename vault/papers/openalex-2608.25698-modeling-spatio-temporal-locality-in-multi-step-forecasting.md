---
# CSL-compatible fields
title: "Modeling spatio-temporal locality in multi-step forecasting of geo-referenced time series"
author:
  - literal: "Annunziata D’Aversa"
  - literal: "Gianvito Pio"
  - literal: "Michelangelo Ceci"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25698"

# Custom fields
paper_id: "2608.25698"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multistep-forecasting"
  - "spatial-temporal"
  - "tree-based-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spalt"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:58:50Z"
created_at: "2026-08-28T16:58:50Z"
---

# Modeling spatio-temporal locality in multi-step forecasting of geo-referenced time series

**Authors**: Annunziata D’Aversa, Gianvito Pio, Michelangelo Ceci
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25698](https://arxiv.org/abs/2608.25698)

## Summary

This paper introduces SPALT, a linear model tree-based approach for multi-step forecasting of geo-referenced time series that captures spatio-temporal locality by grouping time series with similar trends and selectively injecting spatial features. SPALT utilizes a specialized Reduced Error Pruning strategy that considers spatio-temporal locality during tree simplification. Evaluated on three real-world renewable energy datasets, SPALT outperforms traditional tree-based models and state-of-the-art spatio-temporal neural networks across multiple forecasting horizons.

## Key Contributions

- Proposes SPALT, a novel method utilizing linear model trees to capture spatio-temporal locality and local spatial autocorrelation in geo-referenced time series forecasting.
- Introduces a novel Reduced Error Pruning strategy tailored to account for spatio-temporal locality during tree simplification.
- Demonstrates superior multi-step forecasting performance over tree-based models and state-of-the-art spatio-temporal neural networks across 3 real-world renewable energy datasets.

## Key Concepts

- [[spalt]]: A linear model tree method for multi-step forecasting of geo-referenced time series that captures spatio-temporal locality by grouping time series with similar trends and selectively injecting spatial features.

## Archivist Review

Approved the core framework SPALT as a reusable concept for localized spatio-temporal tree modeling. No datasets or open questions met the high selectivity bar or novelty requirements for permanent vault notes.

### Approved Concepts
- SPALT: Introduces a novel linear model tree framework with localized spatial autocorrelation injection and spatio-temporal reduced error pruning for multi-step forecasting of geo-referenced time series.

## Links

- [Abstract](https://arxiv.org/abs/2608.25698)
- [PDF](https://arxiv.org/pdf/2608.25698)

