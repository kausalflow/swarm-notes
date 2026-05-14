---
# CSL-compatible fields
title: "Benchmarking Sensor-Fault Robustness in Forecasting"
author:
  - literal: "Alexander Windmann"
  - literal: "Philipp Wittenberg"
  - literal: "Gianluca Manca"
  - literal: "Marcel Dix"
  - literal: "Jens U. Brandt"
  - literal: "Oliver Niggemann"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10822"

# Custom fields
paper_id: "2605.10822"
paper_source: "openalex"
domain: "time-series"
tags:
  - "benchmark"
  - "time-series"
  - "forecasting"
  - "robustness"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sensorfault-bench"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:37:45Z"
created_at: "2026-05-14T07:37:45Z"
---

# Benchmarking Sensor-Fault Robustness in Forecasting

**Authors**: Alexander Windmann, Philipp Wittenberg, Gianluca Manca, Marcel Dix, Jens U. Brandt, Oliver Niggemann
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10822](https://arxiv.org/abs/2605.10822)

## Summary

This paper addresses the gap between clean-data forecasting performance and real-world robustness by introducing SensorFault-Bench, a stress-test protocol for cyber-physical systems. Through an operational taxonomy and standardized fault-transfer evaluation, the benchmark reveals that high-performing models under clean conditions often suffer sharp degradation in fault-prone scenarios. The study highlights that forecasting architectures and robustness-improvement methods must be evaluated against worst-case metrics, as clean-MSE rankings frequently misrepresent a model's true resilience.

## Key Contributions

- Introduces SensorFault-Bench, a standardized stress-test protocol for evaluating time-series forecasting robustness against sensor faults like bias, noise, and missing data.
- Establishes an operational taxonomy for model comparison and a disjoint fault-transfer evaluation split to assess generalization across fault types.
- Demonstrates that standard forecasting models and zero-shot foundation models often exhibit severe performance degradation under fault scenarios that are not captured by clean-MSE metrics.

## Open Questions & Future Work

- [[transferability-of-sensor-fault-robustness-methods]]

## Key Concepts

- [[sensorfault-bench]]: A shared, CPS-grounded stress-test protocol for evaluating forecasting robustness against various sensor faults.

## Archivist Review

I approved the SensorFault-Bench protocol for its contribution to standardized robustness evaluation in forecasting and the associated open question on transferability, as these address the critical gap between clean-data performance and resilience in cyber-physical systems. Other candidates like the specific datasets (ETTh1, Traffic) were rejected as they are common, well-established benchmarks and do not merit standalone vault notes under current criteria.

### Approved Concepts
- SensorFault-Bench: It establishes a standardized framework for evaluating model robustness under sensor faults in cyber-physical systems, addressing a critical gap where clean-data performance does not correlate with robustness.

### Approved Open Questions
- Transferability of Sensor-Fault Robustness: This question addresses the core challenge of ensuring the reliability of predictive models in critical industrial infrastructure where data quality is inherently non-stationary and fault-prone. Tracking this helps identify if current robustness methods are universal or merely overfit to specific fault types or model architectures.

## Links

- [Abstract](https://arxiv.org/abs/2605.10822)
- [PDF](https://arxiv.org/pdf/2605.10822)

