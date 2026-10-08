---
# CSL-compatible fields
title: "Calibration-induced Systematics in SALT3 Training and Their Impact on Dark Energy Constraints from Stage IV Supernova Surveys"
author:
  - literal: "Kene Anumba"
  - literal: "David O. Jones"
  - literal: "Richard Kessler"
  - literal: "Daniel M. Scolnic"
  - literal: "W. D. Kenworthy"
  - literal: "Rebecca C. Chen"
  - literal: "Bastien Carreres"
  - literal: "M. Vincenzi"
  - literal: "Erik R. Peterson"
  - literal: "Maria Acevedo"
  - literal: "Benjamin M. Rose"
  - literal: "Dillon Brout"
  - literal: "Jillian Paulin"
  - literal: "Rujuta A. Purohit"
  - literal: "Rebekah Hounsell"
  - literal: "The Roman Supernova Cosmology Project Infrastructure Team"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2604.19746"

# Custom fields
paper_id: "2604.19746"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
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
processed_at: "2026-10-08T11:42:07Z"
created_at: "2026-10-08T11:42:07Z"
---

# Calibration-induced Systematics in SALT3 Training and Their Impact on Dark Energy Constraints from Stage IV Supernova Surveys

**Authors**: Kene Anumba, David O. Jones, Richard Kessler, Daniel M. Scolnic, W. D. Kenworthy, Rebecca C. Chen, Bastien Carreres, M. Vincenzi, Erik R. Peterson, Maria Acevedo, Benjamin M. Rose, Dillon Brout, Jillian Paulin, Rujuta A. Purohit, Rebekah Hounsell, The Roman Supernova Cosmology Project Infrastructure Team
**Date**: 2026-10-07
**Paper ID**: [openalex:2604.19746](https://arxiv.org/abs/2604.19746)

## Summary

This paper investigates how photometric calibration uncertainties in upcoming Stage IV supernova surveys, specifically the Vera Rubin Observatory's Rubin-LSST and the Nancy Grace Roman Space Telescope's HLTDS, propagate through SALT3 model training and light-curve fitting to impact dark energy constraints. By perturbing photometric zero-points and filter mean wavelengths in simulated data, the authors find that calibration uncertainties in light-curve fitting dominate over model training errors, causing a ~50% decrease in the dark energy Figure of Merit (FoM). These fitting uncertainties vary smoothly with redshift and exhibit near-degeneracy with cosmology, posing challenges for mitigation through self-calibration.

## Key Contributions

- Zero-point shifts of 5 mmag and filter mean wavelength shifts of 5 Å lead to a ~50% decrease in the dark energy Figure of Merit (FoM) relative to a statistical-only case when calibration uncertainties are propagated through light-curve fitting.
- Calibration shifts applied only during SALT3 model training produce a smaller ~13% degradation, demonstrating that calibration uncertainties in light-curve fitting dominate over those from model training.
- The effect of calibration uncertainties during light-curve fitting varies smoothly with redshift and is nearly degenerate with cosmology, preventing mitigation through self-calibration.

## Open Questions & Future Work

- [[unresolved-fom-calibration-shift-artifacts]]

## Archivist Review

The paper deals with specific astrophysical calibration systematics (SALT3, Rubin-LSST, Roman HLTDS) rather than general machine learning or time-series modeling mechanisms. Therefore, no generic vault concepts or datasets are approved. One specific open question regarding unexplained FoM calibration shift artifacts is approved because it targets broader systematic error modeling challenges in cosmological survey pipelines.

### Approved Open Questions
- Unresolved FoM Calibration Shift Artifacts: Resolving these nonlinearities and counterintuitive trends is vital for accurately modeling systematic error budgets and covariance matrices in upcoming Stage IV dark energy surveys.

### Rejected Candidates
- [open_question] Prism-Only SALT3 Training Artifacts (`prism-only-salt3-training-artifacts`) - low_impact: Too narrow to a specific astrophysical model pipeline and instrument setup (SALT3 prism training).

## Links

- [Abstract](https://arxiv.org/abs/2604.19746)
- [PDF](https://arxiv.org/pdf/2604.19746)

