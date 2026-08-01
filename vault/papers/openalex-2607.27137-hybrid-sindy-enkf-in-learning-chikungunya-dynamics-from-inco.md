---
# CSL-compatible fields
title: "Hybrid SINDy-EnKF in Learning Chikungunya Dynamics from Incomplete, Noisy or Partially Observed Data"
author:
  - literal: "Bernard Asamoah Afful"
  - literal: "Changhong Mou"
  - literal: "Luis Gordillo"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.27137"

# Custom fields
paper_id: "2607.27137"
paper_source: "openalex"
domain: "biology"
tags:
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
processed_at: "2026-08-01T07:23:46Z"
created_at: "2026-08-01T07:23:46Z"
---

# Hybrid SINDy-EnKF in Learning Chikungunya Dynamics from Incomplete, Noisy or Partially Observed Data

**Authors**: Bernard Asamoah Afful, Changhong Mou, Luis Gordillo
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.27137](https://arxiv.org/abs/2607.27137)

## Summary

This paper introduces a hybrid data-driven framework combining Sparse Identification of Nonlinear Dynamics (SINDy) with the Ensemble Kalman Filter (EnKF) to model Chikungunya virus transmission dynamics from incomplete and noisy observational data. While standalone SINDy struggles with noise sensitivity and partial observability, embedding the identification procedure within an EnKF data assimilation scheme corrects forecast states and accurately reconstructs unobserved variables. Numerical experiments show that this integration enhances prediction accuracy in real-world epidemiological surveillance scenarios.

## Key Contributions

- Proposes a hybrid SINDy-EnKF data-driven modeling framework to learn Chikungunya virus transmission dynamics from incomplete, noisy, or partially observed data.
- Combines Sparse Identification of Nonlinear Dynamics (SINDy) with the Ensemble Kalman Filter (EnKF) for sequential data assimilation to mitigate noise sensitivity in equation discovery.
- Demonstrates through numerical experiments that the hybrid approach improves prediction accuracy and reconstructs unobserved state trajectories under partial observability.

## Open Questions & Future Work

- [[noise-robust-sindy-epidemiology]]

## Archivist Review

Evaluated the paper combining SINDy and EnKF. The proposed open question is a duplicate or near-duplicate of existing open questions regarding noise-robust dynamics discovery and equation learning under noise, so no items were approved to maintain vault sparseness.

### Approved Open Questions
- Noise-Robust SINDy for Epidemiology: Crucial for applying data-driven discovery methods to real-world epidemiological data where noise and underreporting are major bottlenecks.

### Rejected Candidates
- [open_question] Noise-Robust SINDy for Epidemiology (`noise-robust-sindy-epidemiology`) - duplicate_existing: Already exists or is covered by existing open questions about robust equation discovery and noise handling.

## Links

- [Abstract](https://arxiv.org/abs/2607.27137)
- [PDF](https://arxiv.org/pdf/2607.27137)

