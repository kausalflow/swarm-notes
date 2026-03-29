---
# CSL-compatible fields
title: "Dissimilarity-Based Persistent Coverage Control of Multi-Robot Systems for Improving Solar Irradiance Prediction Accuracy in Solar Thermal Power Plants"
author:
  - literal: "Haruki Kawase"
  - literal: "Taiga Sugawara"
  - literal: "A. Daniel Carnerero"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25139"

# Custom fields
paper_id: "2603.25139"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "robotics"
  - "sensor-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dissimilarity-map-coverage-control"
  - "persistent-coverage-control-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:49Z"
created_at: "2026-03-29T06:07:49Z"
---

# Dissimilarity-Based Persistent Coverage Control of Multi-Robot Systems for Improving Solar Irradiance Prediction Accuracy in Solar Thermal Power Plants

**Authors**: Haruki Kawase, Taiga Sugawara, A. Daniel Carnerero
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25139](https://arxiv.org/abs/2603.25139)

## Summary

This paper addresses the challenge of optimizing mobile sensor placement for real-time solar irradiance forecasting, a crucial task for controlling solar thermal power plants. The authors propose a novel framework that integrates a kriging-based prediction model with a persistent coverage control algorithm. Central to the method is a "dissimilarity map," derived from the kriging model, which explicitly identifies regions where new observations will most significantly improve prediction accuracy. Experimental results using mobile robots demonstrate that this dynamic sensing strategy leads to superior prediction accuracy compared to static or non-adaptive baseline methods across diverse simulated irradiance conditions.

## Key Contributions

- Introduction of a dissimilarity map derived from a kriging model to quantify areas needing new observations for irradiance forecasting.
- Proposal of a persistent coverage control algorithm that uses this map to dynamically guide mobile robots for optimizing prediction accuracy.
- Empirical demonstration that the proposed mobile sensing strategy achieves more accurate solar irradiance predictions compared to baseline methods under various irradiance fields.

## Limitations

The evaluation is based on emulated irradiance fields using mobile robots, and practical deployment challenges in a full-scale operational solar thermal plant are not detailed.

## Open Questions & Future Work

- [[generalizability-of-dissimilarity-map-models]]

## Key Concepts

- [[dissimilarity-map-coverage-control]]: A map derived from a kriging model used to guide mobile sensors to areas where new observations will yield the greatest reduction in prediction uncertainty or error.
- [[persistent-coverage-control-prediction]]: A control strategy for mobile robots that continuously directs them to sample spatial locations that minimize the prediction error of a concurrently updated spatial model, such as Kriging.

## Archivist Review

Two core reusable concepts were approved: the Dissimilarity Map derived from spatial modeling to drive active sensing, and the Persistent Coverage Control strategy that utilizes this map for optimizing predictive accuracy. The proposed open question regarding the generalizability of this approach across different spatial ML models is substantial enough for tracking. No datasets were approved as the evaluation relied on emulated fields rather than established public benchmarks.

### Approved Concepts
- Dissimilarity Map for Coverage Control: The dissimilarity map is the core mechanism for determining where mobile sensors should gather new data to maximize the expected improvement in the kriging-based solar irradiance prediction model.
- Persistent Coverage Control for Prediction Optimization: This algorithm couples the data collection strategy directly with the objective of improving an underlying prediction model (kriging), representing a specialized form of active learning or sensor management.

### Approved Open Questions
- Generalizability of Dissimilarity Map Models: The dependence on a specific kriging model limits the broad applicability of the proposed control scheme; testing against alternative uncertainty quantification methods (like Gaussian Processes with different kernels or other spatial ML models) is necessary to validate its general robustness.

### Rejected Candidates
- [concept] Kriging Model for Irradiance Forecasting (`kriging-model-for-irradiance-forecasting`) - not_novel: Kriging is a standard geostatistical technique, and its use here as a prediction backbone, rather than the novel control mechanism, does not warrant a dedicated vault entry.
- [concept] Solar Irradiance Prediction Optimization (`solar-irradiance-prediction-optimization`) - paper_local: This is too specific to the application domain (solar thermal power plants) and not a generally reusable ML concept.
- [concept] Mobile Robot Sensor Placement (`mobile-robot-sensor-placement`) - paper_local: This describes the agent type/application, not a novel machine learning concept or mechanism.
- [dataset] Emulated Irradiance Fields Evaluation (`emulated-irradiance-fields-evaluation`) - paper_local: This refers to a simulated experimental setup, not a named, reusable dataset.

## Links

- [Abstract](https://arxiv.org/abs/2603.25139)
- [PDF](https://arxiv.org/pdf/2603.25139)

