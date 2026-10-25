---
# CSL-compatible fields
title: "Towards Field-Deployable Wearable IMU Systems for Occupational Activity Recognition"
author:
  - literal: "Ihsan Ul Haq"
  - literal: "James Brusey"
  - literal: "Farnad Nasirzadeh"
  - literal: "Chandan Karmakar"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.31160"

# Custom fields
paper_id: "2610.31160"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "benchmark"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:30:19Z"
created_at: "2026-10-25T09:30:19Z"
---

# Towards Field-Deployable Wearable IMU Systems for Occupational Activity Recognition

**Authors**: Ihsan Ul Haq, James Brusey, Farnad Nasirzadeh, Chandan Karmakar
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.31160](https://arxiv.org/abs/2610.31160)

## Summary

This paper investigates the viability of wearable IMU systems for construction worker occupational activity recognition by evaluating configuration sensitivity on the VTT-ConIoT benchmark under rigorous leave-one-subject-out (LOSO) protocols. The authors reveal that while aggregate accuracies are high, per-individual accuracy exhibits a massive 27 percentage point spread, highlighting significant inter-subject variance. Furthermore, the study tests data augmentation techniques—showing standard time-series augmentation yields minor gains while CTGAN augmentation harms performance—and demonstrates that lightweight personalised calibration can recover substantial accuracy for underperforming participants.

## Key Contributions

- Conducted a systematic configuration sensitivity analysis of the VTT-ConIoT benchmark for occupational activity recognition under strict leave-one-subject-out (LOSO) evaluation.
- Revealed a large per-subject accuracy variance (61.9% to 88.7%) in multi-sensor configurations, exposing limitations masked by aggregate reporting.
- Demonstrated that personalised calibration recovers 16.8 percentage points of accuracy for weakest participants using only 30% of their data, whereas CTGAN augmentation actively degrades performance.

## Limitations

Evaluated exclusively on laboratory-collected data rather than unconstrained field deployments.

## Archivist Review

Applied rigorous filtering based on vault standards. No candidate concepts or datasets were provided or met the criteria, and the sole open question was rejected as application-specific and low-impact for general methodology.

### Rejected Candidates
- [open_question] Field-Deployable Occupational IMU HAR (`scaling-occupational-imu-har-field-deployment`) - low_impact: The question focuses on scaling occupational IMU sensor networks and deployment challenges, which is too application-specific and domain-local rather than a general methodological time-series research question.

## Links

- [Abstract](https://arxiv.org/abs/2610.31160)
- [PDF](https://arxiv.org/pdf/2610.31160)

