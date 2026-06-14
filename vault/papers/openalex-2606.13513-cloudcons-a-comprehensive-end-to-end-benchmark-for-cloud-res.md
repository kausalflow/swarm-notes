---
# CSL-compatible fields
title: "CloudCons: A Comprehensive End-to-End Benchmark for Cloud Resource Consolidation"
author:
  - literal: "Xiaobin Zhang"
  - literal: "Lefei Shen"
  - literal: "Mouxiang Chen"
  - literal: "Zhuo Li"
  - literal: "Hongkai Li"
  - literal: "Han Fu"
  - literal: "Jianling Sun"
  - literal: "Xiaoxue Ren"
  - literal: "Chenghao Liu"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13513"

# Custom fields
paper_id: "2606.13513"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cloudcons-benchmark"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:38:21Z"
created_at: "2026-06-14T08:38:21Z"
---

# CloudCons: A Comprehensive End-to-End Benchmark for Cloud Resource Consolidation

**Authors**: Xiaobin Zhang, Lefei Shen, Mouxiang Chen, Zhuo Li, Hongkai Li, Han Fu, Jianling Sun, Xiaoxue Ren, Chenghao Liu
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13513](https://arxiv.org/abs/2606.13513)

## Summary

CloudCons is an end-to-end benchmark that evaluates time series forecasting models by their decision utility in cloud resource consolidation, rather than solely by prediction error. The benchmark features diverse, high-quality workload datasets from Huawei Cloud, Microsoft Azure, and Google Borg to capture complex service behaviors. Systematic evaluations reveal a disconnect between zero-shot forecasting accuracy and operational effectiveness, while providing actionable strategies for quantile calibration to optimize the reliability-efficiency trade-off.

## Key Contributions

- Introduces CloudCons, an end-to-end benchmark linking time series forecasting accuracy to real-world cloud resource consolidation decision utility.
- Demonstrates that superior zero-shot forecasting accuracy in time series foundation models does not guarantee better downstream operational performance in resource consolidation.
- Provides empirical guidelines on predictive quantile calibration to balance cloud resource efficiency and service reliability.

## Open Questions & Future Work

- [[forecasting-vs-decision-utility]]

## Key Concepts

- [[cloudcons-benchmark]]: An end-to-end benchmark for evaluating forecasting models specifically for cloud resource consolidation and decision utility.

## Archivist Review

I have approved the CloudCons benchmark concept as a central contribution for its focus on decision-utility, which is a major research direction in the forecasting community. The open question regarding the misalignment between accuracy and decision-making is also a critical bottleneck for deploying ML models in industrial settings. I rejected the individual datasets as they are proprietary and not provided as standardized public artifacts.

### Approved Concepts
- CloudCons Benchmark: Provides a standardized decision-utility evaluation framework for forecasting models in cloud resource management, filling the gap between prediction error and operational effectiveness.

### Approved Open Questions
- Aligning Forecasting and Decision Utility: This is a fundamental challenge in applying machine learning to real-world infrastructure management, where optimizing for proxy objectives (like MAE) often leads to suboptimal system-level behavior (e.g., SLA violations).

### Rejected Candidates
- [dataset] Huawei Cloud dataset (`huawei-cloud-dataset`) - low_impact: These are proprietary workload samples rather than standalone public datasets suitable for the vault.
- [dataset] Microsoft Azure dataset (`microsoft-azure-dataset`) - low_impact: These are proprietary workload samples rather than standalone public datasets suitable for the vault.
- [dataset] Google Borg dataset (`google-borg-dataset`) - low_impact: These are proprietary workload samples rather than standalone public datasets suitable for the vault.

## Links

- [Abstract](https://arxiv.org/abs/2606.13513)
- [PDF](https://arxiv.org/pdf/2606.13513)

