---
# CSL-compatible fields
title: "M-SDT: A modelling framework for dengue transmission, forecasting, and intervention strategies in Ahmedabad Municipal Corporation"
author:
  - literal: "Sourav Roy"
  - literal: "Rajendra Gadhavi"
  - literal: "Bhavin Solanki"
  - literal: "Chirag Shah"
  - literal: "Raj C. Sharma"
  - literal: "Indrajit Ghosh"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17975"

# Custom fields
paper_id: "2605.17975"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:34:21Z"
created_at: "2026-05-21T08:34:21Z"
---

# M-SDT: A modelling framework for dengue transmission, forecasting, and intervention strategies in Ahmedabad Municipal Corporation

**Authors**: Sourav Roy, Rajendra Gadhavi, Bhavin Solanki, Chirag Shah, Raj C. Sharma, Indrajit Ghosh
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17975](https://arxiv.org/abs/2605.17975)

## Summary

This paper introduces the Mechanistic Seasonal Dengue Transmission (M-SDT) model, a data-driven compartmental framework designed to simulate dengue transmission dynamics and evaluate intervention strategies in urban settings. Calibrated on 2020--2024 zone-wise data from the Ahmedabad Municipal Corporation, the model accounts for both symptomatic and asymptomatic infections while quantifying uncertainty through a bootstrap framework. Results demonstrate that the mosquito-to-human ratio significantly influences both endemic baseline and responsiveness to targeted vector control, with residual spraying showing superior effectiveness over fogging for outbreak suppression.

## Key Contributions

- Proposed the Mechanistic Seasonal Dengue Transmission (M-SDT) framework for modelling dengue dynamics with symptomatic and asymptomatic compartments.
- Calibrated the model using zone-wise surveillance data from Ahmedabad Municipal Corporation (2020-2024) to identify persistent hotspots and spatial heterogeneity.
- Quantified intervention efficacy, demonstrating that sustained residual spraying reduces incidence by over 80% compared to periodic fogging.

## Open Questions & Future Work

- [[hybrid-mechanistic-ml-forecasting-dengue]]

## Archivist Review

The paper presents a specific compartmental model for dengue transmission. I approved the open question regarding the hybridization of mechanistic and ML models as it represents a significant, recurring challenge in epidemiological forecasting. I rejected the M-SDT framework itself because compartmental models are a standard methodology and the specific implementation here is domain-local rather than a reusable machine learning architectural innovation.

### Approved Open Questions
- Hybridizing Mechanistic and ML Models: Addressing these gaps is essential for transitioning from static, population-level predictions to adaptive, precision-based public health interventions that can account for the heterogeneity observed in urban disease spread.

### Rejected Candidates
- [concept] Mechanistic Seasonal Dengue Transmission (M-SDT) Framework (`m-sdt-modelling-framework`) - not_novel: The framework is a specific application of standard compartmental epidemiological modeling (SEIR-like) rather than a novel, reusable ML mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2605.17975)
- [PDF](https://arxiv.org/pdf/2605.17975)

