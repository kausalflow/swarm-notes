---
# CSL-compatible fields
title: "AdaCast: Conditional Parameter Generation for Adaptive Time Series Forecasting"
author:
  - literal: "Darahaas Nallagatla"
  - literal: "Darryl Cherian Jacob"
  - literal: "Pan He"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12240"

# Custom fields
paper_id: "2610.12240"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "parameter-efficient-fine-tuning"
  - "zero-shot-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adacast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:51:45Z"
created_at: "2026-10-10T10:51:45Z"
---

# AdaCast: Conditional Parameter Generation for Adaptive Time Series Forecasting

**Authors**: Darahaas Nallagatla, Darryl Cherian Jacob, Pan He
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12240](https://arxiv.org/abs/2610.12240)

## Summary

Time-series foundation models typically rely on static adaptation methods that apply a single set of dataset-level parameters to all inputs, failing to capture heterogeneous temporal dynamics. To address this, the authors propose AdaCast, a conditional parameter generation framework that leverages a generator to produce input-specific low-rank parameter updates for a frozen pretrained model. Experiments across six public benchmarks demonstrate that AdaCast outperforms static adaptation baselines and enhances zero-shot generalization.

## Key Contributions

- Proposes AdaCast, a conditional parameter generation framework that produces input-specific low-rank parameter updates for frozen pretrained time-series foundation models.
- Enables dynamic model adaptation to unique temporal patterns, seasonality, and dynamics of individual input series during both training and inference.
- Consistently outperforms static adaptation baselines across six public benchmarks in in-domain forecasting and improves zero-shot generalization to held-out datasets.

## Open Questions & Future Work

- [[cross-variate-conditional-parameter-generation]]

## Key Concepts

- [[adacast]]: A conditional parameter generation framework that produces input-specific low-rank parameter updates for frozen pretrained time-series foundation models.

## Archivist Review

Approved the core concept AdaCast for its novel conditional parameter generation approach and one open question regarding its cross-variate extension. Rejected the decoder depth open question as low-impact and paper-local.

### Approved Concepts
- AdaCast: AdaCast introduces conditional parameter generation for time-series foundation models, dynamically producing input-specific low-rank parameter updates to handle heterogeneous inputs.

### Approved Open Questions
- Cross-Variate Conditional Parameter Generation: Crucial for real-world multivariate time series forecasting where cross-variable dependencies and inter-variable correlations are vital for accurate predictions.

### Rejected Candidates
- [open_question] Role of Decoder Depth in Adaptation (`decoder-depth-role-in-parameter-adaptation`) - low_impact: Paper-local analysis of layer perturbation sensitivity lacks broad standalone urgency compared to core architectural extensions.

## Links

- [Abstract](https://arxiv.org/abs/2610.12240)
- [PDF](https://arxiv.org/pdf/2610.12240)

