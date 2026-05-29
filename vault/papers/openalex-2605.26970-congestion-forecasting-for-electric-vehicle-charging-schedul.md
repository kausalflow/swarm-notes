---
# CSL-compatible fields
title: "Congestion Forecasting for Electric Vehicle Charging Scheduling with Fluid Queues"
author:
  - literal: "Joas Kahlert"
  - literal: "Ruiting Wang"
  - literal: "Jonas Mårtensson"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26970"

# Custom fields
paper_id: "2605.26970"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "planning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fluid-based-congestion-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:38:15Z"
created_at: "2026-05-29T08:38:15Z"
---

# Congestion Forecasting for Electric Vehicle Charging Scheduling with Fluid Queues

**Authors**: Joas Kahlert, Ruiting Wang, Jonas Mårtensson
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26970](https://arxiv.org/abs/2605.26970)

## Summary

This paper introduces a fluid-queue-based forecasting method to address the challenge of predicting electric vehicle (EV) charging station availability amid uncertain demand. By modeling charging stations as fluid queues with capacity constraints, the method effectively integrates both known and unforeseen vehicle arrival patterns into scheduling decisions. Extensive evaluation demonstrates that this approach significantly lowers waiting times in EV scheduling scenarios compared to standard baseline models. The results further characterize the sensitivity of system efficiency to arrival forecasting accuracy and overall station congestion levels.

## Key Contributions

- Introduced a fluid-queue-based congestion forecasting method that explicitly handles uncertain EV arrival patterns and station capacity constraints.
- Demonstrated that incorporating the fluid forecasting model into EV charging scheduling reduces waiting-related downtime by up to 14% compared to baseline methods.
- Quantified the impact of arrival information fidelity and station utilization levels on aggregate system performance for electric transport networks.

## Open Questions & Future Work

- [[partial-communication-service-scheduling-tradeoffs]]

## Key Concepts

- [[fluid-based-congestion-forecasting]]: A fluid-queue modeling approach for predicting congestion in service networks under stochastic arrival patterns and capacity constraints.

## Archivist Review

The fluid-based congestion forecasting approach is approved as a reusable concept for modeling capacity-constrained service networks, shifting away from discrete arrival models to fluid flows. The open question was reframed to focus on the broader architectural trade-offs between centralized coordination and partial communication in service-based systems, which is a substantial bottleneck for real-world infrastructure deployment.

### Approved Concepts
- Fluid-based congestion forecasting: It provides a novel, uncertainty-aware approach to infrastructure congestion by modeling vehicle flows as fluid queues, which is highly relevant for capacity-constrained service network forecasting.

### Approved Open Questions
- Partial-Communication Service Scheduling Tradeoffs: This defines the fundamental limit of centralized coordination efficiency when network information is incomplete, non-uniform, or privacy-sensitive.

## Links

- [Abstract](https://arxiv.org/abs/2605.26970)
- [PDF](https://arxiv.org/pdf/2605.26970)

