---
# CSL-compatible fields
title: "Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting"
author:
  - literal: "Yifan Hu"
  - literal: "Hongzhou Chen"
  - literal: "Peiyuan Liu"
  - literal: "Yiding Liu"
  - literal: "Zewei Dong"
  - literal: "Jie Yang"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13571"

# Custom fields
paper_id: "2606.13571"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "evaluation"
architectures:
  []
datasets:
  - "shadow-benchmark"
concept_slugs:
  - "timeflies-framework"
  - "observation-value-joint-entropy-ovje-metric"
dataset_slugs:
  - "shadow-benchmark"
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:37:03Z"
created_at: "2026-06-14T08:37:03Z"
---

# Existence Precedes Value: Joint Modeling of Observational Existence and Evolving States in Time Series Forecasting

**Authors**: Yifan Hu, Hongzhou Chen, Peiyuan Liu, Yiding Liu, Zewei Dong, Jie Yang
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13571](https://arxiv.org/abs/2606.13571)

## Summary

Timeflies is a unified forecasting framework that addresses the challenge of irregular and incomplete time series by jointly modeling observation existence and value evolution. Unlike traditional approaches that assume future observation timestamps are known at inference, Timeflies explicitly predicts both when a valid observation will occur and what its value will be. By employing a dual-stream architecture with reliability-aware modules, the model captures the interaction between observability and state dynamics. Performance is validated on the new Shadow benchmark using the proposed Observation-Value Joint Entropy (OVJE) metric, demonstrating improved robustness in realistic, event-driven environments.

## Key Contributions

- Introduces Timeflies, a joint modeling framework that simultaneously predicts the occurrence of future observations and their corresponding values.
- Identifies and addresses the 'oracle assumption' limitation in current irregular time-series forecasting methods.
- Constructs the Shadow benchmark, a comprehensive suite incorporating natural missingness and real-world industrial data for joint prediction evaluation.
- Proposes the Observation-Value Joint Entropy (OVJE) metric to quantify predictability in coupled observability and value estimation tasks.

## Open Questions & Future Work

- [[adaptive-observability-gating-efficiency]]
- [[cross-channel-missingness-modeling]]

## Key Concepts

- [[timeflies-framework]]: A unified framework that performs joint inference of future observability and value estimation for irregular time series.
- [[observation-value-joint-entropy-ovje-metric]]: A metric designed to evaluate the coupled predictability of observation existence and value estimation.

## Archivist Review

The submission is approved because it formally introduces the 'oracle assumption' problem in irregular time-series forecasting and provides a robust framework and metric to address it. I approved the framework and the metric as they are foundational for this research area. I renamed the open questions for better clarity and slug uniqueness, and approved the Shadow benchmark as a critical new tool for the field.

### Approved Concepts
- Timeflies Framework: It addresses the 'oracle assumption' limitation by treating observation existence as a core prediction task alongside value estimation, which is central to realistic irregular time-series forecasting.
- Observation-Value Joint Entropy (OVJE) Metric: It offers a rigorous, standardized approach to evaluate models on the dual task of predicting both observation occurrence and the values, filling a gap in standard forecasting metrics.

### Approved Open Questions
- Adaptive Observability Gating Efficiency: Improving computational efficiency is crucial for deploying time series forecasting models in real-time, large-scale industrial settings.
- Cross-Channel Missingness Modeling: Explicitly modeling joint missingness across channels can significantly improve forecast accuracy and uncertainty estimation in multivariate systems.

## Datasets

- [[shadow-benchmark]]

## Links

- [Abstract](https://arxiv.org/abs/2606.13571)
- [PDF](https://arxiv.org/pdf/2606.13571)

