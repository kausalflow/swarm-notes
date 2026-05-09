---
# CSL-compatible fields
title: "Reducing robotic upper-limb assessment time while maintaining precision: a time series foundation model approach"
author:
  - literal: "Faranak Akbarifar"
  - literal: "Nooshin Maghsoodi"
  - literal: "Sean P. Dukelow"
  - literal: "Stephen Scott"
  - literal: "Parvin Mousavi"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2511.00193"

# Custom fields
paper_id: "2511.00193"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "robotics"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forecast-augmented-robotic-assessment"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:01:51Z"
created_at: "2026-05-09T07:01:51Z"
---

# Reducing robotic upper-limb assessment time while maintaining precision: a time series foundation model approach

**Authors**: Faranak Akbarifar, Nooshin Maghsoodi, Sean P. Dukelow, Stephen Scott, Parvin Mousavi
**Date**: 2026-05-06
**Paper ID**: [openalex:2511.00193](https://arxiv.org/abs/2511.00193)

## Summary

This study evaluates the utility of time series foundation models, specifically Chronos and MOMENT, in reducing the time burden of robotic Visually Guided Reaching (VGR) assessments. By training these models to forecast synthetic reaching trials from a small initial subset of recorded data, the authors demonstrate that kinematic biomarkers for stroke and control cohorts can be estimated with accuracy comparable to full-session protocols. The approach effectively reduces assessment duration for stroke survivors from several minutes to approximately one minute, providing a scalable solution for clinical motor assessment.

## Key Contributions

- Demonstrates that using Chronos foundation models to forecast synthetic trials from only 8 recorded reaches achieves kinematic biomarker agreement comparable to 24-28 traditional reaches.
- Reduces Kinarm Visually Guided Reaching (VGR) assessment time for stroke survivors from 4-5 minutes to approximately 1 minute without significant loss in feature reliability.
- Validates a forecast-augmented paradigm across multiple protocols and cohorts (461 stroke, 599 control participants) using standard clinical kinematic features.

## Open Questions & Future Work

- [[robotic-assessment-domain-shift-robustness]]

## Key Concepts

- [[forecast-augmented-robotic-assessment]]: A clinical assessment strategy that utilizes time series foundation models to synthesize unrecorded trials, effectively shortening robotic reaching protocols while maintaining biomarker precision.

## Archivist Review

The paper introduces a compelling approach to clinical assessment, reducing patient burden by substituting synthetic trials for recorded ones. I have approved the 'Forecast-Augmented Robotic Assessment' concept as it represents a novel clinical workflow enabled by time series foundation models. The open question on domain shift addresses the primary bottleneck for real-world clinical adoption of this methodology, as variations in hardware and firmware pose a significant risk to consistency.

### Approved Concepts
- Forecast-Augmented Robotic Assessment: Introduces a paradigm for reducing clinical assessment duration by using time series foundation models to synthesize missing data.

### Approved Open Questions
- Robotic Assessment Domain Shift Robustness: This is critical for the translational success of forecast-augmented assessment; without addressing domain shift, models may become biased or unreliable when moved beyond the original laboratory setting.

## Links

- [Abstract](https://arxiv.org/abs/2511.00193)
- [PDF](https://arxiv.org/pdf/2511.00193)

