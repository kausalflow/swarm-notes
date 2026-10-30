---
# CSL-compatible fields
title: "Deep Bayesian Approaches for Interpretable Nonlinear Structural System Identification"
author:
  - literal: "Wei Liu"
  - literal: "Konstantinos Vlachas"
  - literal: "Eleni Chatzi"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36633"

# Custom fields
paper_id: "2610.36633"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "uncertainty"
  - "forecasting"
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
processed_at: "2026-10-30T11:06:13Z"
created_at: "2026-10-30T11:06:13Z"
---

# Deep Bayesian Approaches for Interpretable Nonlinear Structural System Identification

**Authors**: Wei Liu, Konstantinos Vlachas, Eleni Chatzi
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36633](https://arxiv.org/abs/2610.36633)

## Summary

This tutorial provides a systematic introduction to deep Bayesian filtering for nonlinear structural system identification, focusing on the interplay between learned dynamics, physical inductive biases, and posterior inference. It examines the Deep Markov Model, Physics-guided Deep Markov Model (PgDMM), and Neural Extended Kalman Filter (Neural EKF) for joint state and parameter estimation on a 3D shear-frame benchmark with hysteretic Bouc-Wen connections. The findings reveal key insights regarding measurement-conditioned reconstruction versus open-loop forecasting and the impact of physical structure on latent-state interpretability.

## Key Contributions

- Provides a systematic tutorial on deep Bayesian filtering for nonlinear structural system identification, integrating learned dynamics with physical inductive biases and posterior inference.
- Compares the Deep Markov Model, Physics-guided Deep Markov Model (PgDMM), and Neural Extended Kalman Filter (Neural EKF) on dynamic state and joint state-parameter estimation.
- Evaluates models on a three-dimensional shear-frame benchmark featuring hysteretic Bouc-Wen connections and sparse acceleration measurements.
- Examines trade-offs between measurement-conditioned reconstruction and open-loop forecasting, highlighting how physical structure aids latent-state interpretability.

## Limitations

Challenges remain in uncertainty calibration, model identifiability, and real-world validation under sparse measurements.

## Open Questions & Future Work

- [[calibrated-uncertainty-deep-bayesian-filtering]]
- [[balancing-physics-and-learning-identification]]

## Archivist Review

The paper is a comprehensive tutorial on deep Bayesian filtering for structural system identification rather than a primary technical contribution introducing a new core model or dataset. Therefore, no standalone concepts or datasets were approved, but two valuable open questions regarding uncertainty calibration and the balance between physics and learning were retained.

### Approved Open Questions
- Uncertainty Calibration in Filtering: Uncertainty quantification and calibration are vital for reliable digital twinning and structural health monitoring, where uncalibrated confidence bounds can lead to faulty structural assessment decisions.
- Balancing Physics and Learning: Balancing physics and learning is central to building robust hybrid digital twins that generalize accurately beyond training conditions without overfitting to measurement noise or violating physical laws.

### Rejected Candidates
- [concept] Uncertainty Calibration in Filtering (`calibrated-uncertainty-deep-bayesian-filtering`) - not_novel: The paper presents a tutorial and review of existing deep Bayesian filtering approaches rather than introducing a novel concept or model architecture.

## Links

- [Abstract](https://arxiv.org/abs/2610.36633)
- [PDF](https://arxiv.org/pdf/2610.36633)

