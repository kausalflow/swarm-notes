---
# CSL-compatible fields
title: "From Shared Demand Patterns to Local Uncertainty: Probabilistic Load Forecasting by Mixing Compact Adaptations"
author:
  - literal: "Haoran Li"
  - literal: "Zhe Cheng"
  - literal: "Yang Weng"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.08538"

# Custom fields
paper_id: "2610.08538"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
  - "parameter-efficient-fine-tuning"
  - "peft"
  - "adapter"
  - "mixture-of-experts"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:34:59Z"
created_at: "2026-10-09T11:34:59Z"
---

# From Shared Demand Patterns to Local Uncertainty: Probabilistic Load Forecasting by Mixing Compact Adaptations

**Authors**: Haoran Li, Zhe Cheng, Yang Weng
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.08538](https://arxiv.org/abs/2610.08538)

## Summary

This paper proposes a scalable probabilistic load forecasting framework designed to handle customer- and transformer-level load uncertainty by combining a shared base demand model with a small bank of low-dimensional, mixable adaptation components. This design captures common demand behavior while remaining flexible enough for heterogeneous customer patterns without the prohibitive storage and training costs of individual full models. Experiments on 590 load profiles from the SMART-DS dataset show that the framework outperforms various statistical, neural, Transformer, and pretrained time-series baselines in both deterministic and probabilistic metrics.

## Key Contributions

- Develops a scalable customer-aware probabilistic load forecasting framework that combines shared demand modeling with a small bank of low-dimensional adaptation components
- Learns to mix compact adaptation components per load profile to handle heterogeneous patterns and mixed load compositions without storing independent full models
- Demonstrates consistent improvements in deterministic accuracy and probabilistic quality over statistical, neural, Transformer-based, and pretrained baselines on 590 load profiles from the SMART-DS dataset while maintaining low storage and inference costs

## Archivist Review

The submitted paper presents an efficient parameter-adaptation strategy for customer-level load forecasting using a bank of mixable adapters. However, the core ideas closely mirror existing mixture-of-adapters and parameter-efficient adaptation frameworks already present in the knowledge vault, and no distinct new concepts or open questions met the strict novelty and reusability standards.

## Links

- [Abstract](https://arxiv.org/abs/2610.08538)
- [PDF](https://arxiv.org/pdf/2610.08538)

