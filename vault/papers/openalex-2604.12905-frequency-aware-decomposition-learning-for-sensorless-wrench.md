---
# CSL-compatible fields
title: "Frequency-aware Decomposition Learning for Sensorless Wrench Forecasting on a Vibration-rich Hydraulic Manipulator"
author:
  - literal: "Hyeonbeen Lee"
  - literal: "Min-Jae Jung"
  - literal: "Tae–Kyeong Yeu"
  - literal: "Jong-Boo Han"
  - literal: "Daegil Park"
  - literal: "Jin‐Gyun Kim"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12905"

# Custom fields
paper_id: "2604.12905"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "forecasting"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  - "frequency-aware-decomposition-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:29:36Z"
created_at: "2026-04-17T06:29:36Z"
---

# Frequency-aware Decomposition Learning for Sensorless Wrench Forecasting on a Vibration-rich Hydraulic Manipulator

**Authors**: Hyeonbeen Lee, Min-Jae Jung, Tae–Kyeong Yeu, Jong-Boo Han, Daegil Park, Jin‐Gyun Kim
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12905](https://arxiv.org/abs/2604.12905)

## Summary

The paper presents the Frequency-aware Decomposition Network (FDN) to address the challenge of sensorless wrench forecasting in high-vibration robotic tasks like grinding. FDN uses spectral decomposition to process wrench signals, employing a deterministic head for low-frequency components and a probabilistic head to model high-frequency residuals. The model incorporates frequency-aware adaptive filtering and is validated through pretraining and transfer learning on a 6-DoF hydraulic manipulator, where it significantly improves prediction accuracy in vibration-heavy scenarios.

## Key Contributions

- Introduces the Frequency-aware Decomposition Network (FDN) for short-term wrench forecasting in high-vibration robotic environments.
- Employs an asymmetric architecture using deterministic heads for low-frequency signals and probabilistic heads for high-frequency residuals.
- Demonstrates superior performance over baselines on real-world grinding excavation data from a 6-DoF hydraulic manipulator, particularly in capturing high-frequency dynamics.

## Open Questions & Future Work

- [[cross-platform-generalization-of-sensorless-force-estimation]]

## Key Concepts

- [[frequency-aware-decomposition-forecasting]]: A forecasting paradigm that utilizes asymmetric architectures to predict deterministic low-frequency signals and probabilistic high-frequency residuals.

## Archivist Review

I have approved the concept of frequency-aware decomposition forecasting as a reusable architectural paradigm for multi-scale time-series, while rejecting the paper-specific model name. I also approved one open question focused on the cross-platform generalization of sensorless estimation, which remains a key barrier to deployable robotic interaction systems. The other proposed open questions were either too generic or effectively duplicates of the established research gap.

### Approved Concepts
- Frequency-aware Decomposition Forecasting: The method explicitly handles signal dynamics by separating deterministic low-frequency components from stochastic high-frequency residuals, a common challenge in high-frequency time-series forecasting.

### Approved Open Questions
- Sensorless Estimation Generalization Limits: Determining whether these models learn universal physical dynamics or platform-specific noise is critical for the scalability of robot-environment interaction systems.

### Rejected Candidates
- [concept] Frequency-aware Decomposition Network (FDN) (`frequency-aware-decomposition-network-fdn`) - subcomponent_of_broader_mechanism: The specific network architecture (FDN) is a paper-local instance of the broader concept of Frequency-aware Decomposition Forecasting.
- [open_question] Generalization of Sensorless Estimation (`generalization-sensorless-wrench-estimation`) - duplicate_existing: This is a less precise version of the approved open question regarding cross-platform generalization.
- [open_question] Scaling and Transfer Learning (`scaling-transfer-learning-robotics`) - generic: This is too generic a research direction and does not capture a specific, actionable bottleneck in time-series forecasting or sensorless estimation.

## Links

- [Abstract](https://arxiv.org/abs/2604.12905)
- [PDF](https://arxiv.org/pdf/2604.12905)

