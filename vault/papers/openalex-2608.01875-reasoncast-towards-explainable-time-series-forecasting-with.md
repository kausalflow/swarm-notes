---
# CSL-compatible fields
title: "ReasonCast: Towards Explainable Time Series Forecasting with Reasoning"
author:
  - literal: "Seunghan Lee"
  - literal: "Jun Seo"
  - literal: "Jaehoon Lee"
  - literal: "Junhyuk Kang"
  - literal: "Sangjun Han"
  - literal: "Sungdong Yoo"
  - literal: "Minjae Kim"
  - literal: "Tae Yoon Lim"
  - literal: "Dongwan Kang"
  - literal: "Hwanil Choi"
  - literal: "Soonyoung Lee"
  - literal: "Wonbin Ahn"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01875"

# Custom fields
paper_id: "2608.01875"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "llm"
  - "language-model"
  - "multimodal"
  - "reasoning"
  - "explainability"
  - "benchmark"
  - "autoregressive"
architectures:
  - "decoder-only"
datasets:
  - "ReasonTS-Bench"
concept_slugs:
  - "reasoncast"
dataset_slugs:
  - "reasonts-bench"
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:31:10Z"
created_at: "2026-08-06T07:31:10Z"
---

# ReasonCast: Towards Explainable Time Series Forecasting with Reasoning

**Authors**: Seunghan Lee, Jun Seo, Jaehoon Lee, Junhyuk Kang, Sangjun Han, Sungdong Yoo, Minjae Kim, Tae Yoon Lim, Dongwan Kang, Hwanil Choi, Soonyoung Lee, Wonbin Ahn
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01875](https://arxiv.org/abs/2608.01875)

## Summary

ReasonCast introduces a task-fused framework for time series forecasting that jointly generates numerical predictions and interpretable text reasoning in a single autoregressive pass. To evaluate this capability, the authors present ReasonTS-Bench, a benchmark covering five fundamental time series patterns. Experiments show that ReasonCast improves prediction accuracy over standalone TS models and LLMs while offering verifiable causal explanations.

## Key Contributions

- Proposes ReasonCast, a task-fused model that jointly produces numerical TS forecasting and interpretable text reasoning in a single autoregressive pass.
- Introduces ReasonTS-Bench, a benchmark capturing five fundamental time series patterns for joint evaluation of generation and understanding tasks.
- Demonstrates that ReasonCast outperforms existing LLMs and traditional TS models on prediction accuracy while providing verifiable causal explanations.

## Open Questions & Future Work

- [[multivariate-composite-time-series-reasoning]]

## Key Concepts

- [[reasoncast]]: A fine-tuning recipe and model for jointly generating time series forecasts and verifiable causal reasoning within a single autoregressive pass.

## Archivist Review

Approved the core task-fused fine-tuning recipe and the primary benchmark dataset along with a key open question regarding multivariate scaling. Rejected the redundant concept entry for the benchmark to prevent duplication with approved datasets.

### Approved Concepts
- ReasonCast: Core methodology for fusing numerical time series forecasting and text-based reasoning within a single autoregressive pass.

### Approved Open Questions
- Multivariate and Composite Time Series Reasoning: Extending explainable time series reasoning architectures from synthetic univariate primitives to complex multivariate settings and composite patterns is critical for deploying task-fused models in real-world industrial and financial applications.

### Rejected Candidates
- [concept] ReasonTS-Bench (`reasonts-bench`) - duplicate_existing: Redundant with the approved dataset ReasonTS-Bench.

## Datasets

- [[reasonts-bench]]

## Links

- [Abstract](https://arxiv.org/abs/2608.01875)
- [PDF](https://arxiv.org/pdf/2608.01875)

