---
# CSL-compatible fields
title: "Global probabilistic forecasting of air pollution"
author:
  - literal: "Ammar Kheder"
  - literal: "Michael Boy"
  - literal: "Zhi-Song Liu"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.25941"

# Custom fields
paper_id: "2610.25941"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "foehn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:44:03Z"
created_at: "2026-10-22T09:44:03Z"
---

# Global probabilistic forecasting of air pollution

**Authors**: Ammar Kheder, Michael Boy, Zhi-Song Liu
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.25941](https://arxiv.org/abs/2610.25941)

## Summary

The paper introduces Foehn, a generative model for global kilometre-scale probabilistic forecasting of fine particulate matter (PM2.5) that computes air provenance to prevent blurring extremes. Evaluated over a year of retrospective forecasts, Foehn outperforms operational forecasts at three out of four stations and provides calibrated ensembles capable of detecting local pollution extremes four days in advance.

## Key Contributions

- Introduces Foehn, a generative model for global kilometre-scale PM2.5 probabilistic forecasting that explicitly computes air provenance.
- Demonstrates superior performance over operational forecasts at three out of four stations in retrospective evaluations over a year.
- Achieves calibrated ensembles whose mean detects local pollution extremes four days ahead with comparable accuracy to operational one-day forecasts.

## Limitations

Relies on the availability of kilometre-scale data in real time to provide operational warnings for affected populations.

## Open Questions & Future Work

- [[forecast-reliability-sparse-regions]]

## Key Concepts

- [[foehn]]: A generative model for global kilometre-scale probabilistic PM2.5 forecasting that computes air provenance to capture local pollution extremes.

## Archivist Review

Approved the central generative forecasting model Foehn and an open question on evaluating high-resolution air pollution forecasts in data-sparse regions, maintaining high selectivity.

### Approved Concepts
- Foehn: It is the core generative model proposed for global kilometre-scale probabilistic PM2.5 forecasting, overcoming traditional blurring of extremes.

### Approved Open Questions
- Air Quality Forecast Reliability in Data-Sparse Regions: Crucial for ensuring global equity and trustworthiness of air-quality warning systems in data-sparse regions, particularly across the Global South.

## Links

- [Abstract](https://arxiv.org/abs/2610.25941)
- [PDF](https://arxiv.org/pdf/2610.25941)

