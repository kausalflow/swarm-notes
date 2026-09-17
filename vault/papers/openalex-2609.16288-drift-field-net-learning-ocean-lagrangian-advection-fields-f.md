---
# CSL-compatible fields
title: "Drift Field Net: Learning Ocean Lagrangian advection fields from in-situ and satellite observations"
author:
  - literal: "Théo Archambault"
  - literal: "Pierre Garcia"
  - literal: "Mattia Romero"
  - literal: "Anastase Charantonis"
  - literal: "Dominique Béréziat"
  - literal: "Théo Archambault"
  - literal: "Pierre Garcia"
  - literal: "Mattia Romero"
  - literal: "Anastase Charantonis"
  - literal: "Dominique Béréziat"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.16288"

# Custom fields
paper_id: "2609.16288"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "physics-informed-neural-networks"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:44:55Z"
created_at: "2026-09-17T09:44:55Z"
---

# Drift Field Net: Learning Ocean Lagrangian advection fields from in-situ and satellite observations

**Authors**: Théo Archambault, Pierre Garcia, Mattia Romero, Anastase Charantonis, Dominique Béréziat, Théo Archambault, Pierre Garcia, Mattia Romero, Anastase Charantonis, Dominique Béréziat
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.16288](https://arxiv.org/abs/2609.16288)

## Summary

The paper introduces Drift Field Net (DFN), a deep neural network designed to predict ocean surface flow fields in the North Pacific Subtropical Gyre using satellite observations. DFN is trained via a two-stage approach leveraging simulation pretraining followed by physics-informed Lagrangian fine-tuning with an advection-consistent loss function. Evaluations on in-situ drifter trajectories demonstrate that DFN significantly outperforms operational physics-based forecasting systems by reducing 7-day positioning errors.

## Key Contributions

- Introduces Drift Field Net (DFN), a deep neural network predicting ocean surface flow fields from operational satellite observations.
- Proposes a two-stage training strategy combining simulation pretraining and Lagrangian fine-tuning with an advection-consistent loss function.
- Reduces mean positioning error by 20 km on in-situ drifter trajectories after a 7-day forecast compared to operational physics-based models, with an additional 10 km reduction from Lagrangian fine-tuning.

## Limitations

Evaluated primarily on the North Pacific Subtropical Gyre region; generalizability to other ocean basins requires further validation.

## Archivist Review

Adhered to strict vault selectivity by rejecting paper-specific architectures and domain-localized ocean forecasting questions that do not generalize broadly across machine learning and time-series forecasting literature.

### Rejected Candidates
- [concept] Drift Field Net (`drift-field-net`) - paper_local: Drift Field Net is a paper-specific architecture and application note for ocean surface flow prediction, lacking broader independent reusability across general time-series forecasting.
- [open_question] Basin-Scale Long-Term Ocean Drift Forecasting (`basin-scale-long-term-ocean-drift-forecasting`) - low_impact: This open question is extremely narrow and domain-specific to ocean drift simulation, offering limited methodological utility to broader time-series forecasting research.

## Links

- [Abstract](https://arxiv.org/abs/2609.16288)
- [PDF](https://arxiv.org/pdf/2609.16288)

