---
# CSL-compatible fields
title: "State Forecasting in an Estimation Framework with Surrogate Sensor Modeling"
author:
  - literal: "Sriram Narayanan"
  - literal: "Mohamed Naveed Gul Mohamed"
  - literal: "Ishan Paranjape"
  - literal: "Indranil Nayak"
  - literal: "Suman Chakravorty"
  - literal: "Mrinal Kumar"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2604.19442"

# Custom fields
paper_id: "2604.19442"
paper_source: "openalex"
domain: "robotics"
tags:
  - "robotics"
  - "state-space-model"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "surrogate-sensor-modeling-for-state-estimation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:00:21Z"
created_at: "2026-04-24T07:00:21Z"
---

# State Forecasting in an Estimation Framework with Surrogate Sensor Modeling

**Authors**: Sriram Narayanan, Mohamed Naveed Gul Mohamed, Ishan Paranjape, Indranil Nayak, Suman Chakravorty, Mrinal Kumar
**Date**: 2026-04-21
**Paper ID**: [openalex:2604.19442](https://arxiv.org/abs/2604.19442)

## Summary

This paper introduces a framework for state estimation in complex physical systems, specifically addressing partial observability in aerospace tracking. The method integrates simplified reference physics models with learned surrogate measurement models to compensate for sparse radar and optical observational data. Numerical validation demonstrates that this fusion approach effectively reconstructs system dynamics where traditional sensor models might fail.

## Key Contributions

- Proposes an estimation framework integrating simplified reference dynamics with a data-driven surrogate measurement model.
- Enhances state reconstruction capabilities under partial observability for aerospace applications.
- Demonstrates robustness through consistency analysis of the surrogate modeling approach across numerical experiments.

## Open Questions & Future Work

- [[surrogate-extrapolation-reliability-limits]]

## Key Concepts

- [[surrogate-sensor-modeling-for-state-estimation]]: A hybrid state estimation framework that compensates for partial observability by integrating physics-based reference models with data-driven surrogate measurement models.

## Archivist Review

The paper contributes a well-defined hybrid estimation architecture. I approved the surrogate sensor modeling concept as it represents a reusable fusion pattern for state-space problems. I also refined the open question regarding surrogate model reliability to better focus on the fundamental issues of bias and error accumulation in long-term estimation.

### Approved Concepts
- Surrogate Sensor Modeling for State Estimation: It provides a reusable hybrid approach for state estimation by fusing physics-based dynamics with learned surrogate observation models to overcome partial observability.

### Approved Open Questions
- Surrogate Extrapolation Reliability Limits: This is a fundamental bottleneck for deploying hybrid state estimation frameworks in real-world systems where model drift and prediction error accumulation are unavoidable.

## Links

- [Abstract](https://arxiv.org/abs/2604.19442)
- [PDF](https://arxiv.org/pdf/2604.19442)

