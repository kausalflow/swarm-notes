---
# CSL-compatible fields
title: "Metropolis-scale resilient and trustworthy traffic flow inference using multi-source data"
author:
  - literal: "Qishen Zhou"
  - literal: "Yifan Zhang"
  - literal: "Michail Makridis"
  - literal: "Anastasios Kouvelas"
  - literal: "Yibing Wang"
  - literal: "Simon Hu"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2605.25004"

# Custom fields
paper_id: "2605.25004"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "uncertainty-quantification"
  - "meta-learning"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "task-aware-attentive-neural-process-ta-anp"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:56:32Z"
created_at: "2026-10-17T08:56:32Z"
---

# Metropolis-scale resilient and trustworthy traffic flow inference using multi-source data

**Authors**: Qishen Zhou, Yifan Zhang, Michail Makridis, Anastasios Kouvelas, Yibing Wang, Simon Hu
**Date**: 2026-10-15
**Paper ID**: [openalex:2605.25004](https://arxiv.org/abs/2605.25004)

## Summary

The paper introduces the Task-Aware Attentive Neural Process (TA-ANP), a probabilistic framework for global traffic state inference that fuses floating car data with sparse fixed-detector measurements. By leveraging neural processes and a task-aware multi-query attention module, TA-ANP jointly performs real-time estimation and forecasting across unobserved locations while quantifying both aleatoric and epistemic uncertainty. Evaluated on the newly introduced Metropolitan Multi-Source Traffic Dataset (MMTD) across 26,166 road segments, the approach demonstrates high accuracy, well-calibrated uncertainty, and robust resilience to sensor disruptions.

## Key Contributions

- Proposes the Task-Aware Attentive Neural Process (TA-ANP), a unified probabilistic framework that fuses floating car data with sparse fixed-detector measurements for global traffic state inference.
- Introduces a task-aware multi-query attention module with distinct spatiotemporal inductive biases to jointly handle real-time estimation and forecasting while mitigating cross-task interference.
- Constructs the Metropolitan Multi-Source Traffic Dataset (MMTD) covering an urban network of 26,166 road segments to support metropolis-scale evaluation under changing sensing configurations.

## Open Questions & Future Work

- [[cross-city-generalization-traffic-inference-neural-processes-open-question]]

## Key Concepts

- [[task-aware-attentive-neural-process-ta-anp]]: A unified probabilistic framework combining neural processes with task-aware multi-query attention for resilient and trustworthy global traffic state inference.

## Archivist Review

Approved the central framework concept TA-ANP as a valuable stochastic process architecture for spatial-temporal multi-task inference, along with the cross-city generalization open question. Datasets and local submodules were excluded in accordance with the strict volume and novelty limits.

### Approved Concepts
- Task-Aware Attentive Neural Process (TA-ANP): Core framework introduced for metropolis-scale global traffic state inference that handles multiple subtasks and uncertainty quantification simultaneously.

### Approved Open Questions
- Cross-City Generalization in Traffic Inference: Determining whether neural process models can generalize across cities is critical for deploying scalable, out-of-the-box traffic state inference systems without requiring extensive localized retraining or data collection.

## Links

- [Abstract](https://arxiv.org/abs/2605.25004)
- [PDF](https://arxiv.org/pdf/2605.25004)

