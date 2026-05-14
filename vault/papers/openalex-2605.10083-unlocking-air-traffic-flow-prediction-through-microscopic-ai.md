---
# CSL-compatible fields
title: "Unlocking air traffic flow prediction through microscopic aircraft-state modeling"
author:
  - literal: "Bin Wang"
  - literal: "Anqi Liu"
  - literal: "Jiangtao Zhao"
  - literal: "Yanyong Huang"
  - literal: "Peilan He"
  - literal: "Guiyuan Jiang"
  - literal: "Feng Hong"
  - literal: "Yanwei Yu"
  - literal: "Tianrui Li"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10083"

# Custom fields
paper_id: "2605.10083"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "aerosense"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:38:33Z"
created_at: "2026-05-14T07:38:33Z"
---

# Unlocking air traffic flow prediction through microscopic aircraft-state modeling

**Authors**: Bin Wang, Anqi Liu, Jiangtao Zhao, Yanyong Huang, Peilan He, Guiyuan Jiang, Feng Hong, Yanwei Yu, Tianrui Li
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10083](https://arxiv.org/abs/2605.10083)

## Summary

AeroSense is a novel air traffic flow prediction framework that shifts away from traditional aggregated time-series forecasting. By directly modeling the instantaneous microscopic states of aircraft derived from ADS-B trajectories, the framework captures fine-grained kinematic and control information. This approach improves predictive accuracy in terminal airspace, particularly during complex, high-density traffic conditions, without relying on historical look-back windows.

## Key Contributions

- Introduces AeroSense, a microscopic, state-to-flow modeling framework that bypasses historical time-series aggregation by mapping instantaneous aircraft-state sets to future flow.
- Demonstrates that using dynamic sets of aircraft states allows the model to naturally accommodate varying traffic densities without requiring historical look-back windows.
- Empirically validates that state-based microscopic modeling outperforms conventional aggregation-based forecasting methods on real-world air traffic data, especially during high-density scenarios.

## Open Questions & Future Work

- [[long-term-air-traffic-forecasting]]
- [[multi-modal-air-traffic-prediction]]

## Key Concepts

- [[aerosense]]: A state-to-flow modeling framework that predicts spatial flow from instantaneous sets of entity states rather than aggregated historical time-series.

## Archivist Review

I approved the AeroSense concept as it represents a significant methodological shift from aggregate-time-series to microscopic-set-based forecasting. The two open questions are approved as they address fundamental bottlenecks in scaling this new approach: extending horizons for strategic use and incorporating multi-modal context for environmental robustness. No datasets were approved as none were explicitly named as distinct benchmarks of high community reusability.

### Approved Concepts
- AeroSense: It establishes a paradigm shift from aggregated time-series forecasting to state-based microscopic modeling for complex flow domains.

### Approved Open Questions
- Long-term Air Traffic Forecasting: Increasing prediction horizons is vital for the transition from tactical air traffic management to strategic flow control.
- Multi-modal Air Traffic Prediction: Improving predictive robustness in volatile operational conditions requires accounting for external environmental and control variables beyond pure trajectory data.

## Links

- [Abstract](https://arxiv.org/abs/2605.10083)
- [PDF](https://arxiv.org/pdf/2605.10083)

