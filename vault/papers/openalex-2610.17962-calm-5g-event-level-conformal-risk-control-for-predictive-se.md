---
# CSL-compatible fields
title: "CALM-5G: Event-Level Conformal Risk Control for Predictive Service-Assurance Alarms"
author:
  - literal: "Omer Faruk Iscanli"
  - literal: "Yağmur Sabucu Sandal"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17962"

# Custom fields
paper_id: "2610.17962"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "conformal-prediction"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "calm-5g"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:24:36Z"
created_at: "2026-10-16T09:24:36Z"
---

# CALM-5G: Event-Level Conformal Risk Control for Predictive Service-Assurance Alarms

**Authors**: Omer Faruk Iscanli, Yağmur Sabucu Sandal
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17962](https://arxiv.org/abs/2610.17962)

## Summary

The paper introduces CALM-5G, an event-level conformal risk control framework that operates on top of forecasting models to issue predictive service assurance alarms with finite-sample guarantees. By targeting violation onsets and employing cross-validated calibration, CALM-5G significantly reduces time-in-alarm while strictly maintaining certified miss rates across diverse cellular and 5G network corpora. Furthermore, the study highlights that online calibration is necessary to maintain compliance under label shift, addressing limitations of pooled batch calibration.

## Key Contributions

- Introduces CALM-5G, a conformal risk control assurance layer that sits above forecasting backbones to issue predictive alarms with finite-sample guarantees.
- Calibrates directly on service-level violation events and onset scoring, reducing time-in-alarm by 56.3% to 89.7% across evaluated corpora.
- Demonstrates that online calibration restores compliance under label shift where pooled batch calibration fails.
- Jointly certifies miss rate and alarm duty cycle when within-entity dependence preserves sufficient calibration units.

## Limitations

Pooled batch calibration fails under label shift by exceeding tolerance bounds, requiring online calibration to restore compliance.

## Open Questions & Future Work

- [[online-conformal-risk-control-under-drift]]

## Key Concepts

- [[calm-5g]]: An assurance layer operating above forecasting backbones to issue alarms with distribution-free, finite-sample guarantees on service violation events.

## Archivist Review

Approved the core framework concept 'CALM-5G' as a distinctive conformal risk control assurance layer and the open question regarding online conformal control under shift, keeping selections scarce and strictly adhering to review guidelines.

### Approved Concepts
- CALM-5G: Serves as the core proposed predictive service assurance framework for issuing event-level risk-controlled alarms.

### Approved Open Questions
- Online Conformal Risk Control Under Drift: Crucial for ensuring safety, robustness, and reliability of autonomous network management and control loops under real-world non-stationary telemetry.

## Links

- [Abstract](https://arxiv.org/abs/2610.17962)
- [PDF](https://arxiv.org/pdf/2610.17962)

