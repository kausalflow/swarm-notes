---
# CSL-compatible fields
title: "Bridging short- and medium-range weather forecasting with machine learning"
author:
  - literal: "Timothy A. Smith"
  - literal: "Mariah Pope"
  - literal: "Sergey Frolov"
  - literal: "Brett Basarab"
  - literal: "Daniel Abdi"
  - literal: "Paul Madden"
  - literal: "Isidora Jankov"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26822"

# Custom fields
paper_id: "2608.26822"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:38Z"
created_at: "2026-08-30T10:10:38Z"
---

# Bridging short- and medium-range weather forecasting with machine learning

**Authors**: Timothy A. Smith, Mariah Pope, Sergey Frolov, Brett Basarab, Daniel Abdi, Paul Madden, Isidora Jankov
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26822](https://arxiv.org/abs/2608.26822)

## Summary

The paper presents Nested-EAGLE, an AI-based weather prediction model that bridges short- and medium-range forecasting by coupling a 0.25° global model with a 6 km regional refinement over the Contiguous United States (CONUS). By incorporating high-resolution regional analysis data into training, the model achieves lower mean-squared error in near-surface quantities compared to NOAA's operational GFS and HRRR systems while remaining competitive globally. Although deterministic training limits precipitation amount accuracy relative to HRRR, Nested-EAGLE delivers highly accurate storm location forecasts at longer lead times.

## Key Contributions

- Introduces Nested-EAGLE, a machine learning weather prediction model combining a 0.25° global domain with a 6 km regional refinement over CONUS.
- Achieves lower mean-squared error in near-surface and low-level quantities over CONUS compared to NOAA's GFS and HRRR operational models.
- Demonstrates that skill gains in near-surface fields derive from incorporating high-resolution regional analysis data during training via nesting.

## Limitations

Precipitation amounts are less skillful than HRRR due to deterministic training, and extrema are blurred.

## Archivist Review

Applied strict selectivity standards. Rejected the paper-local Nested-EAGLE model architecture as it is specific to this study's meteorological setup. Rejected the open question as it lacks a sufficiently concrete technical bottleneck.

### Rejected Candidates
- [concept] Nested-EAGLE (`nested-eagle`) - paper_local: This model architecture represents a specific application of regional-global nesting for weather forecasting, making it too paper-local to serve as a reusable standalone vault concept.
- [open_question] Observational Inputs in ML Weather Models (`observational-inputs-ml-weather-forecasting`) - low_impact: The question is too broad and general regarding observational integration in weather forecasting without a precise technical mechanism or formalization.

## Links

- [Abstract](https://arxiv.org/abs/2608.26822)
- [PDF](https://arxiv.org/pdf/2608.26822)

