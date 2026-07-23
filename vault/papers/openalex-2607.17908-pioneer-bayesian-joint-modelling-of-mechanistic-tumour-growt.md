---
# CSL-compatible fields
title: "PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials"
author:
  - literal: "Karim Naguib"
  - literal: "Roger Berché"
  - literal: "Lu Li"
  - literal: "Antonia Bevan"
  - literal: "Sajan Khosla"
  - literal: "Jessica Davies"
  - literal: "Paul Metcalfe"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17908"

# Custom fields
paper_id: "2607.17908"
paper_source: "openalex"
domain: "medicine"
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
processed_at: "2026-07-23T07:27:20Z"
created_at: "2026-07-23T07:27:20Z"
---

# PIONEER: Bayesian Joint Modelling of Mechanistic Tumour Growth and Time-to-Event Endpoints for Dynamic Prediction of Ongoing Oncology Trials

**Authors**: Karim Naguib, Roger Berché, Lu Li, Antonia Bevan, Sajan Khosla, Jessica Davies, Paul Metcalfe
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17908](https://arxiv.org/abs/2607.17908)

## Summary

High-stakes oncology trials often face immature survival data during interim cuts, requiring methods to predict endpoints from longitudinal tumour measurements. PIONEER is a Bayesian joint modelling framework that integrates a mechanistic two-component state-space submodel of tumour size dynamics with a multistate proportional-hazard submodel for competing clinical events under a unified posterior. By coupling sparse longitudinal sum-of-longest-diameter observations with competing hazard risks, the model enables forward simulation of clinical endpoints with fully propagated parameter uncertainty. Applied to small-cell lung cancer trials, PIONEER successfully forecasts mature progression-free and overall survival curves months in advance of final readouts.

## Key Contributions

- PIONEER couples a mechanistic two-component state-space model of tumour dynamics with a multistate proportional-hazard submodel for competing clinical events within a single Bayesian joint framework.
- All clinical endpoints such as progression-free and overall survival are derived directly from the joint posterior via forward simulation, eliminating two-stage plug-in biases and fully propagating uncertainty.
- Demonstrated on extensive-stage small-cell lung cancer trials (N = 497), achieving calibrated progression-free survival forecasts up to 8 months in advance of mature data readouts.

## Open Questions & Future Work

- [[cross-indication-parameter-transportability]]

## Archivist Review

We approved the open question on cross-indication parameter transportability as a substantial unresolved bottleneck in generalizing mechanistic joint survival models across diverse clinical trials. No new concepts or datasets met the strict novelty and reusability standards for permanent vault notes.

### Approved Open Questions
- Cross-Indication Parameter Transportability: Determining the limits of parameter transportability across different oncology indications is crucial for expanding the applicability of mechanistic joint models to rare or novel cancer types where historical trial data is extremely sparse.

### Rejected Candidates
- [open_question] Cross-Indication Parameter Transportability (`cross-indication-parameter-transportability`) - other: The candidate is approved.

## Links

- [Abstract](https://arxiv.org/abs/2607.17908)
- [PDF](https://arxiv.org/pdf/2607.17908)

