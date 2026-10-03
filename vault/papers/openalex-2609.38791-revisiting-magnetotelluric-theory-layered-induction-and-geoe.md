---
# CSL-compatible fields
title: "Revisiting magnetotelluric theory: layered induction and geoelectric fields"
author:
  - literal: "Dennies Bor"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.38791"

# Custom fields
paper_id: "2609.38791"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:09:24Z"
created_at: "2026-10-03T10:09:24Z"
---

# Revisiting magnetotelluric theory: layered induction and geoelectric fields

**Authors**: Dennies Bor
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.38791](https://arxiv.org/abs/2609.38791)

## Summary

This paper reviews the magnetotelluric theory of a horizontally layered Earth under plane wave forcing to calculate geoelectric fields, deriving the diffusion approximation and impedance recursion from Maxwell's equations. The theoretical formulation is evaluated through three empirical tests: modeling geoelectric fields during the May 2024 geomagnetic storm across 1614 EarthScope MT sites, reconstructing magnetic fields at withheld observatories, and interpolating conductivity via kriging into withheld regions. Results demonstrate that layered fits significantly improve geoelectric field precision compared to raw tensor or spatial magnetic reconstruction approaches.

## Key Contributions

- Reviewed magnetotelluric (MT) theory of horizontally layered Earth and derived impedance recursion from Maxwell's equations.
- Evaluated geoelectric field calculations against the May 2024 geomagnetic storm across 1614 EarthScope MT sites, showing layered fit errors of 1.9% compared to 46% raw tensor errors.
- Assessed spatial magnetic field reconstruction and kriging-based conductivity interpolation, quantifying median relative errors of 57.3% for predicted impedance in withheld regions.

## Open Questions & Future Work

- [[joint-spatial-conductivity-prediction]]

## Archivist Review

Applied strict scarcity and reusability standards. No new concepts or datasets qualified for permanent standalone vault notes as the paper focuses on a review of established magnetotelluric theory and geoelectric field evaluation. One open question addressing joint spatial conductivity prediction for regional networks was approved.

### Approved Open Questions
- Joint Spatial Conductivity Prediction: Essential for accurately propagating ground conductivity uncertainty through spatial networks and transmission lines during extreme space weather events.

### Rejected Candidates
- [open_question] Joint Spatial Conductivity Prediction (`joint-spatial-conductivity-prediction`) - other: Approved.

## Links

- [Abstract](https://arxiv.org/abs/2609.38791)
- [PDF](https://arxiv.org/pdf/2609.38791)

