---
# CSL-compatible fields
title: "Beyond Model Ranking: Regime Diagnosis for Distributional-Statistical Misspecification in Industrial Time-Series Forecasting"
author:
  - literal: "Pengyu Nie"
  - literal: "Chenglang Xu"
  - literal: "Yaoshi Chen"
  - literal: "Chaogan Ren"
  - literal: "Wei Hu"
  - literal: "Chao Yang"
  - literal: "Jiangong Zhang"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.40117"

# Custom fields
paper_id: "2609.40117"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  - "m5-competition"
concept_slugs:
  - "regime-wise-relative-bias-vector"
dataset_slugs:
  - "m5-competition"
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:26Z"
created_at: "2026-10-03T10:07:26Z"
---

# Beyond Model Ranking: Regime Diagnosis for Distributional-Statistical Misspecification in Industrial Time-Series Forecasting

**Authors**: Pengyu Nie, Chenglang Xu, Yaoshi Chen, Chaogan Ren, Wei Hu, Chao Yang, Jiangong Zhang
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.40117](https://arxiv.org/abs/2609.40117)

## Summary

This paper identifies distributional-statistical misspecification as a key driver of the train-deploy gap in industrial time-series forecasting, where fixed statistical priors in canonical losses fail across pathological regimes like zero-inflation and high variability. To address this, the authors propose the Regime-wise Relative Bias Vector (RBV), a metric-agnostic diagnostic tool that decomposes bias across subpopulations and separates intrinsic loss floors from training excess. Extensive experiments across 60,000+ series demonstrate that regime-aware evaluation and training resolve pooling-induced bias that model capacity scaling cannot.

## Key Contributions

- Characterizes distributional-statistical misspecification in industrial time-series forecasting arising from fixed statistical priors in canonical losses mixed across benign and pathological regimes.
- Introduces the Regime-wise Relative Bias Vector (RBV) as a metric-agnostic, regime-decomposed diagnostic tool to audit systematic mismatch across subpopulations.
- Performs a large-scale evaluation across 13 loss objectives, 3 seeds, and 60,000+ series spanning RetailShiftBench and M5, demonstrating that regime-aware training resolves pooling-induced bias that capacity scaling cannot.

## Limitations

Focuses primarily on diagnostic analysis and loss objectives; comprehensive mitigation across all neural architectures remains an open exploration.

## Open Questions & Future Work

- [[foundation-model-regime-diagnosis]]

## Key Concepts

- [[regime-wise-relative-bias-vector]]: A metric-agnostic, regime-decomposed diagnostic that audits how pooled training allocates systematic mismatch across pathological subpopulations.

## Archivist Review

Approved the Regime-wise Relative Bias Vector concept as a robust, metric-agnostic diagnostic tool for distributional misspecification in time series, along with the M5 dataset and an open question on foundation model regime diagnosis. RetailShiftBench was rejected as a low-impact or paper-local benchmark dataset.

### Approved Concepts
- Regime-wise Relative Bias Vector: Central metric-agnostic diagnostic introduced to evaluate distributional-statistical misspecification across regimes.

### Approved Open Questions
- Foundation Model Regime Diagnosis: This connects diagnostic auditing frameworks directly with the evaluation and alignment of modern zero-shot time-series foundation models and robust loss design.

### Rejected Candidates
- [dataset] RetailShiftBench (`retailshiftbench`) - low_impact: Dataset is newly introduced or domain-specific without established archival presence compared to canonical benchmarks.

## Datasets

- [[m5-competition]]

## Links

- [Abstract](https://arxiv.org/abs/2609.40117)
- [PDF](https://arxiv.org/pdf/2609.40117)

