---
# CSL-compatible fields
title: "Forecasting Downstream Performance of LLMs With Proxy Metrics"
author:
  - literal: "Arkil Patel"
  - literal: "Siva Reddy"
  - literal: "Marius Mosbach"
  - literal: "Dzmitry Bahdanau"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18607"

# Custom fields
paper_id: "2605.18607"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "language-model"
  - "pre-training"
  - "evaluation"
  - "benchmark"
  - "reasoning"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "expert-token-level-proxy-metrics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:32:50Z"
created_at: "2026-05-21T08:32:50Z"
---

# Forecasting Downstream Performance of LLMs With Proxy Metrics

**Authors**: Arkil Patel, Siva Reddy, Marius Mosbach, Dzmitry Bahdanau
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18607](https://arxiv.org/abs/2605.18607)

## Summary

This paper addresses the challenge of predicting downstream LLM performance without expensive direct evaluation or poorly aligned loss metrics. The authors propose using proxy metrics derived from token-level statistics, such as entropy and expert token rank, calculated over distributions of expert-written solutions. These proxies are shown to outperform existing compute-based and loss-based baselines across model selection, data selection, and training-time performance extrapolation tasks.

## Key Contributions

- Proposed proxy metrics based on aggregating token-level statistics over expert-written solutions for reliable downstream performance forecasting.
- Achieved a mean Spearman Rho of 0.81 for cross-family model selection, significantly outperforming cross-entropy loss (Rho = 0.36).
- Enabled reliable pretraining data selection at 10,000x less compute than direct downstream evaluation.
- Demonstrated superior training-time forecasting capabilities, extrapolating downstream accuracy across an 18x compute horizon with roughly half the error of existing methods.

## Open Questions & Future Work

- [[end-to-end-learned-proxy-aggregation]]

## Key Concepts

- [[expert-token-level-proxy-metrics]]: A method for forecasting downstream LLM performance by aggregating token-level statistics (e.g., entropy, top-k accuracy) from next-token distributions over expert-written solutions.

## Archivist Review

I have approved the core concept of expert-driven proxy metrics as it provides a reusable, model-agnostic framework for performance evaluation that addresses known limitations in cross-entropy loss. I have also approved one open question regarding end-to-end learned aggregation, as it identifies a clear pathway to closing the forecasting performance gap. The second open question regarding power-law generalizability was rejected as it primarily concerns empirical scope rather than a fundamental mechanistic bottleneck.

### Approved Concepts
- Expert Token-Level Proxy Metrics: These metrics overcome the limitation of cross-entropy loss in predicting downstream performance and significantly reduce the compute required for evaluation.

### Approved Open Questions
- End-to-End Learned Proxy Aggregation: The reported oracle gap suggests significant potential for improving forecasting accuracy; transitioning from manual, heuristic-based proxy selection to learned, adaptive methods is a standard and necessary evolution in improving predictive modeling robustness.

## Links

- [Abstract](https://arxiv.org/abs/2605.18607)
- [PDF](https://arxiv.org/pdf/2605.18607)

