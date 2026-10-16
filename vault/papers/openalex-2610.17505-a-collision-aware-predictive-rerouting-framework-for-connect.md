---
# CSL-compatible fields
title: "A Collision-Aware Predictive Rerouting Framework for Connected and Automated Vehicles"
author:
  - literal: "Tony Kinchen"
  - literal: "Ting Bai"
  - literal: "Andreas A. Malikopoulos"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17505"

# Custom fields
paper_id: "2610.17505"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "autonomous-agent"
  - "reinforcement-learning"
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
processed_at: "2026-10-16T09:24:30Z"
created_at: "2026-10-16T09:24:30Z"
---

# A Collision-Aware Predictive Rerouting Framework for Connected and Automated Vehicles

**Authors**: Tony Kinchen, Ting Bai, Andreas A. Malikopoulos
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17505](https://arxiv.org/abs/2610.17505)

## Summary

This paper investigates mitigating non-recurrent urban traffic congestion via a collision-aware predictive rerouting framework for connected and automated vehicles (CAVs). The approach combines DCRNN-based spatiotemporal traffic forecasting, collision-window lookahead, and multi-objective route scoring within microscopic SUMO simulations. Evaluations across various urban scenarios and CAV penetration levels reveal that while the framework does not universally dominate all aggregate efficiency baselines, it achieves superior operational stability by significantly reducing rerouting frequency.

## Key Contributions

- Proposed a collision-aware predictive rerouting framework integrating DCRNN-based traffic forecasting, collision-window lookahead, and multi-objective route scoring for connected and automated vehicles (CAVs).
- Demonstrated through SUMO simulations across urban network scenarios and CAV penetration levels that the framework prioritizes operational stability, substantially reducing rerouting frequency compared to active baselines while maintaining network efficiency.
- Highlighted operational trade-offs and motivated future research directions in forecast calibration, uncertainty-aware prediction, and system-level fairness between CAV and non-CAV traffic.

## Limitations

Does not dominate all baseline strategies in aggregate travel time, distance, or emissions; exhibits trade-offs between rerouting frequency and overall network-level efficiency.

## Open Questions & Future Work

- [[uncertainty-aware-traffic-forecasting]]
- [[fairness-and-stability-in-cav-routing]]

## Archivist Review

The paper focuses on an application-specific traffic routing framework using microscopic simulation and DCRNN forecasting. No standalone foundational ML concepts or standard datasets meet the threshold for permanent notes, but two open questions regarding traffic forecasting uncertainty and routing fairness are approved as valuable directions.

### Approved Open Questions
- Uncertainty-Aware Traffic Forecasting and Calibration: Addressing prediction uncertainty is critical for preventing suboptimal routing decisions and maintaining control stability in safety-critical automated vehicle networks.
- Fairness and Stability in CAV Routing: Ensuring fairness and stability across mixed vehicle fleets prevents bottlenecks and discriminatory delays for human-driven or non-cooperative vehicles in real-world deployments.

## Links

- [Abstract](https://arxiv.org/abs/2610.17505)
- [PDF](https://arxiv.org/pdf/2610.17505)

