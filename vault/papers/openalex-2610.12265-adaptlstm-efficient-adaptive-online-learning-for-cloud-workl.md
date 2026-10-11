---
# CSL-compatible fields
title: "AdaptLSTM: Efficient Adaptive Online Learning for Cloud Workload Forecasting under Distribution Drift"
author:
  - literal: "Xinhua Miao"
  - literal: "Bowei Yang"
  - literal: "Zhengong Cai"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.12265"

# Custom fields
paper_id: "2610.12265"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "gru"
  - "transformer"
  - "online-learning"
  - "distribution-shift"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:04:41Z"
created_at: "2026-10-11T11:04:41Z"
---

# AdaptLSTM: Efficient Adaptive Online Learning for Cloud Workload Forecasting under Distribution Drift

**Authors**: Xinhua Miao, Bowei Yang, Zhengong Cai
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.12265](https://arxiv.org/abs/2610.12265)

## Summary

Accurate cloud workload forecasting is hindered by rapid distribution shifts that degrade offline models, while naive online learning incurs prohibitive computational costs. This paper introduces AdaptLSTM, an adaptive online learning framework that uses validation-calibrated thresholds to detect distribution drift and perform selective model updates. Evaluated on Alibaba Machine Trace and Container Trace datasets across LSTM, GRU, and Transformer backbones, AdaptLSTM significantly improves forecasting efficiency and accuracy over static and naive baselines.

## Key Contributions

- Proposes AdaptLSTM, an adaptive online learning framework for cloud workload forecasting that detects distribution drift via validation-calibrated thresholds and applies selective model updates.
- Achieves 54% of Naive Online's improvement at 20% cost on the Alibaba Machine Trace ($2.7\times$ efficiency).
- Achieves 96% of Naive Online's improvement at 20% cost on the Container Trace ($4.8\times$ efficiency, +75% MAE reduction over Static).
- Demonstrates model-agnostic Pareto improvements across LSTM, GRU, and Transformer backbones with a 1.33x throughput gain and 45% update-time reduction.

## Archivist Review

Applied strict selectivity: no concepts or open questions met the bar for permanent inclusion as they lacked generalizable algorithmic novelty or precise theoretical bottlenecks beyond paper-local application.

### Rejected Candidates
- [open_question] Multi-modal and Natural Drift Adaptation (`multimodal-workload-forecasting-natural-drift`) - low_impact: The proposed open question is boilerplate future work regarding evaluation on stronger natural non-stationarity and multi-modal features without a specific unresolved mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.12265)
- [PDF](https://arxiv.org/pdf/2610.12265)

