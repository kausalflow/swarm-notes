---
# CSL-compatible fields
title: "GraphToolbox: A Configurable Python Framework for Graph Neural Network Forecasting"
author:
  - literal: "Eloi Campagne"
  - literal: "Yvenn Amara-Ouali"
  - literal: "Yannig Goude"
  - literal: "Argyris Kalogeratos"
issued:
  date-parts:
    - [2026, 9, 21]
url: "https://arxiv.org/abs/2609.24609"

# Custom fields
paper_id: "2609.24609"
paper_source: "openalex"
domain: "time-series"
tags:
  - "graph-neural-network"
  - "gnn"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-24T09:38:52Z"
created_at: "2026-09-24T09:38:52Z"
---

# GraphToolbox: A Configurable Python Framework for Graph Neural Network Forecasting

**Authors**: Eloi Campagne, Yvenn Amara-Ouali, Yannig Goude, Argyris Kalogeratos
**Date**: 2026-09-21
**Paper ID**: [openalex:2609.24609](https://arxiv.org/abs/2609.24609)

## Summary

GraphToolbox is an open-source Python framework built on PyTorch Geometric that unifies graph construction, model training, aggregation, and interpretation into a single configuration-driven pipeline for spatial time-series forecasting. The framework integrates 51 PyTorch Geometric convolutions and recurrent cells from PyTorch Geometric Temporal, alongside online expert aggregation and interpretability tools. Evaluations on French regional load and net-load case studies demonstrate its effectiveness in performing systematic architectural sweeps and improving forecasting accuracy through expert aggregation.

## Key Contributions

- We present GraphToolbox, an open-source Python framework built on PyTorch Geometric that unifies graph construction, model selection, training, aggregation, and interpretation in a configuration-driven pipeline.
- GraphToolbox integrates 51 of 65 PyTorch Geometric convolutions and recurrent cells from PyTorch Geometric Temporal, supporting online expert aggregation, forecasting interpretability, and significance testing.
- Evaluation on French regional load shows that 48 convolutions achieve error rates between 1.14% and 1.60%, which online aggregation reduces to 0.98% while outperforming classical additive and boosting baselines.
- Evaluation on net-load demonstrates that component-wise physical forecasting improves direct graph models, highlighting the framework's utility for systematic architectural evaluation.

## Links

- [Abstract](https://arxiv.org/abs/2609.24609)
- [PDF](https://arxiv.org/pdf/2609.24609)

