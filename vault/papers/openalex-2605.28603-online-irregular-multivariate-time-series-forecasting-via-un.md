---
# CSL-compatible fields
title: "Online Irregular Multivariate Time Series Forecasting via Uncertainty-Driven Dual-Expert Calibration"
author:
  - literal: "Haonan Wen"
  - literal: "Hanyang Chen"
  - literal: "Songhe Feng"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28603"

# Custom fields
paper_id: "2605.28603"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "online-learning"
  - "uncertainty"
architectures:
  []
datasets:
  []
concept_slugs:
  - "under-cali"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:34:55Z"
created_at: "2026-05-30T07:34:55Z"
---

# Online Irregular Multivariate Time Series Forecasting via Uncertainty-Driven Dual-Expert Calibration

**Authors**: Haonan Wen, Hanyang Chen, Songhe Feng
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28603](https://arxiv.org/abs/2605.28603)

## Summary

The paper addresses the challenge of online forecasting for irregularly sampled multivariate time series (IMTS), where dynamic shifts often lead to performance degradation in offline-trained models. To overcome this, the authors propose Under-Cali, a framework that uses an uncertainty estimator to dynamically route incoming samples between reliable and unreliable experts. This dual-expert approach enables continuous model adaptation without requiring updates to the frozen source forecasting model, significantly improving robustness against distribution shifts. Experimental results across IMTS benchmarks confirm the framework's effectiveness and computational efficiency.

## Key Contributions

- Introduces Under-Cali, an uncertainty-driven dual-expert calibration framework for online irregular multivariate time series (IMTS) forecasting.
- Develops an uncertainty-based routing mechanism that dynamically manages inference and model adaptation by segregating reliable and unreliable samples.
- Achieves stable and efficient online adaptation with a frozen base model and lightweight calibration, reducing computational overhead while maintaining performance.

## Open Questions & Future Work

- [[online-imts-adaptation-stability]]

## Key Concepts

- [[under-cali]]: An uncertainty-driven dual-expert calibration framework for online irregular multivariate time series forecasting that routes samples to reliable or unreliable experts based on uncertainty estimates.

## Archivist Review

I have approved the Under-Cali framework as a concept because it formalizes a distinct, reusable pattern for selective online adaptation in streaming forecasting tasks. I also approved the open question regarding online IMTS adaptation stability as it correctly identifies the fundamental bottleneck created by irregular sampling in non-stationary streaming scenarios. I have applied a conservative filtering policy, ensuring only novel, high-impact architectural patterns are admitted into the vault.

### Approved Concepts
- Under-Cali: Provides a modular, uncertainty-driven routing mechanism for online adaptation that decouples the base forecasting model from the calibration process.

### Approved Open Questions
- Stable Online IMTS Adaptation: As IMTS is prevalent in high-stakes fields like healthcare and climate monitoring, the inability to adapt to real-world distribution shifts significantly limits model reliability.

## Links

- [Abstract](https://arxiv.org/abs/2605.28603)
- [PDF](https://arxiv.org/pdf/2605.28603)

