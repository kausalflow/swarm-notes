---
# CSL-compatible fields
title: "Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity"
author:
  - literal: "Blaise Delaney"
  - literal: "Salil Patel"
  - literal: "Yuji Xing"
  - literal: "Dominic Dootson"
  - literal: "Karin Sevegnani"
issued:
  date-parts:
    - [2026, 4, 20]
url: "https://arxiv.org/abs/2604.18058"

# Custom fields
paper_id: "2604.18058"
paper_source: "openalex"
domain: "medicine"
tags:
  - "language-model"
  - "representation-learning"
  - "time-series"
  - "forecasting"
  - "clinical-data"
  - "wearable-sensors"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sonata-hybrid-world-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-23T06:57:09Z"
created_at: "2026-04-23T06:57:09Z"
---

# Sonata: A Hybrid World Model for Inertial Kinematics under Clinical Data Scarcity

**Authors**: Blaise Delaney, Salil Patel, Yuji Xing, Dominic Dootson, Karin Sevegnani
**Date**: 2026-04-20
**Paper ID**: [openalex:2604.18058](https://arxiv.org/abs/2604.18058)

## Summary

Sonata is a compact 3.77M-parameter hybrid latent world model developed specifically for inertial kinematics representation learning in data-scarce clinical environments. Unlike traditional masked-reconstruction objectives, Sonata learns through a predictive world-model objective that anticipates future states rather than reconstructing raw sensor signals. Empirical results demonstrate that Sonata provides more structured latent representations and stronger performance in fall-risk prediction and cross-cohort transfer compared to standard autoregressive baselines. Its efficiency enables on-device deployment for real-time neurological assessment using trunk-worn IMUs.

## Key Contributions

- Introduced Sonata, a compact 3.77M parameter latent world model for 6-axis IMU representation learning.
- Outperformed autoregressive MAE-based baselines in clinical discrimination, prospective fall-risk prediction, and cross-cohort transfer tasks across 14 evaluation benchmarks.
- Demonstrated efficiency and structure in latent representations, suitable for on-device inference in clinical neurological assessment.

## Open Questions & Future Work

- [[generalizing-kinematic-world-models-across-sensor-configurations]]

## Key Concepts

- [[sonata-hybrid-world-model]]: A compact (3.77M parameter) latent world model designed for kinematic representation learning under small-scale, data-scarce clinical regimes.

## Archivist Review

I approved the Sonata architecture as a distinct, reusable concept for small-scale IMU representation learning and the open question regarding the generalization of such models across heterogeneous sensor setups. These items effectively address the identified bottleneck of clinical data scarcity in time-series forecasting and biomechanical modeling. Other generic concepts or boilerplate future work suggestions were rejected to maintain the focus on the paper's primary methodological contribution.

### Approved Concepts
- Sonata: Represents a specialized hybrid world model architecture for inertial measurement units (IMU) tailored for clinical scenarios where traditional large-scale pre-training is infeasible.

### Approved Open Questions
- Generalizing Kinematic World Models: Handling heterogeneous, multi-site, and multi-sensor data is essential for enabling the clinical adoption of digital biomarkers in neurology, where data scarcity is a fundamental barrier to scalability.

## Links

- [Abstract](https://arxiv.org/abs/2604.18058)
- [PDF](https://arxiv.org/pdf/2604.18058)

