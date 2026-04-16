---
# CSL-compatible fields
title: "Towards Situation-aware State Modeling for Air Traffic Flow Prediction"
author:
  - literal: "Anqi Liu"
  - literal: "Bin Wang"
  - literal: "Jigang Zhao"
  - literal: "Dechuan Ma"
  - literal: "Guiyuan Jiang"
  - literal: "Feng Hong"
  - literal: "Yanwei Yu"
  - literal: "Tianrui Li"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11198"

# Custom fields
paper_id: "2604.11198"
paper_source: "openalex"
domain: "nlp,time-series"
tags:
  - "time-series"
  - "forecasting"
  - "self-attention"
  - "interpretability"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "aerosense"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:42Z"
created_at: "2026-04-16T06:28:42Z"
---

# Towards Situation-aware State Modeling for Air Traffic Flow Prediction

**Authors**: Anqi Liu, Bin Wang, Jigang Zhao, Dechuan Ma, Guiyuan Jiang, Feng Hong, Yanwei Yu, Tianrui Li
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11198](https://arxiv.org/abs/2604.11198)

## Summary

AeroSense is a direct state-to-flow modeling framework designed to overcome the limitations of traditional time-series air traffic forecasting, which often obscures critical micro-level dynamics. By representing the terminal airspace as a dynamic set of individual aircraft states rather than aggregated flow sequences, the model explicitly captures high-resolution kinematics and proximity-based interactions. The architecture leverages masked self-attention to model inter-aircraft relationships and employs decoupled prediction heads for heterogeneous flow dynamics, achieving state-of-the-art performance on real-world airport data.

## Key Contributions

- Introduced AeroSense, a direct state-to-flow modeling framework that bypasses macroscopic time-series aggregation for air traffic prediction.
- Developed a situation-aware state representation that processes microscopic kinematics and aircraft proximity to airspace boundaries as a dynamic input set.
- Demonstrated superior predictive fidelity and robustness compared to traditional time-series baselines on a large-scale real-world airport dataset.

## Open Questions & Future Work

- [[set-based-air-traffic-modeling]]

## Key Concepts

- [[aerosense]]: A direct state-to-flow modeling framework that represents terminal airspace as a dynamic set of individual aircraft states.

## Archivist Review

I approved the AeroSense framework as it represents a novel methodological shift from aggregated time-series to set-based modeling, which is highly reusable in multi-agent flow scenarios. The open question was approved for capturing the core architectural tension between traditional time-series forecasting and agent-based set representation. I rejected other candidates as being either too specific to the application or subsumed by these more general contributions.

### Approved Concepts
- AeroSense: It introduces a paradigm for flow forecasting that replaces macroscopic time-series aggregation with direct processing of microscopic agent sets.

### Approved Open Questions
- Set-based Air Traffic Representation Learning: This addresses the fundamental architectural limitation of current forecasting systems, providing a path toward higher predictive fidelity in multi-agent control settings.

## Links

- [Abstract](https://arxiv.org/abs/2604.11198)
- [PDF](https://arxiv.org/pdf/2604.11198)

