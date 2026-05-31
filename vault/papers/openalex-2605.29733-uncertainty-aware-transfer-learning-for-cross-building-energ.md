---
# CSL-compatible fields
title: "Uncertainty-Aware Transfer Learning for Cross-Building Energy Forecasting: Toward Robust and Scalable District-Level Energy Management"
author:
  - literal: "Shadmehr Zaregarizi"
  - literal: "Khashayar Yavari"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29733"

# Custom fields
paper_id: "2605.29733"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "transfer-learning"
  - "uncertainty-estimation"
  - "parameter-efficient-fine-tuning"
  - "peft"
architectures:
  - "encoder-decoder"
datasets:
  - "NEST building dataset"
concept_slugs:
  - "transfer-robustness-index-tri"
dataset_slugs:
  - "nest-building-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:52Z"
created_at: "2026-05-31T08:09:52Z"
---

# Uncertainty-Aware Transfer Learning for Cross-Building Energy Forecasting: Toward Robust and Scalable District-Level Energy Management

**Authors**: Shadmehr Zaregarizi, Khashayar Yavari
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29733](https://arxiv.org/abs/2605.29733)

## Summary

This paper addresses the challenge of scaling energy forecasting to district levels by proposing an uncertainty-aware transfer learning framework based on the Temporal Fusion Transformer. The authors introduce the Transfer Robustness Index (TRI) to quantify model generalization quality across buildings and demonstrate that freezing the encoder while fine-tuning only the output layer yields optimal results. The approach is evaluated using cross-building data from Denmark and Switzerland, showing that the framework provides robust, scalable predictions even with limited target-domain data.

## Key Contributions

- Introduces the Transfer Robustness Index (TRI), an architecture-agnostic metric to quantify generalization quality in cross-domain energy forecasting.
- Demonstrates that Probe-Only fine-tuning on Temporal Fusion Transformers (TFTs) achieves superior transfer performance while updating only 0.05% of parameters.
- Establishes high-resolution energy forecasting benchmarks using a source-target setup across different building typologies (educational to multi-typology) with valid 93.2% prediction interval coverage via Monte Carlo Dropout.

## Open Questions & Future Work

- [[standardized-transfer-robustness-metrics]]

## Key Concepts

- [[transfer-robustness-index-tri]]: An architecture-agnostic metric for quantifying generalization quality and transfer performance across domain gaps.

## Archivist Review

The paper proposes a novel metric for cross-domain transfer evaluation in time-series forecasting, which is a valuable addition to the vault. I have approved the Transfer Robustness Index (TRI) and the associated open question regarding its standardization. The NEST building dataset is approved as a specific, named benchmark resource for this domain.

### Approved Concepts
- Transfer Robustness Index (TRI): Provides a standardized, architecture-agnostic way to evaluate the effectiveness of cross-domain transfer learning, which is critical for scalable district-level energy management.

### Approved Open Questions
- Standardizing Transfer Robustness Metrics: Without a standardized metric, it is difficult to benchmark progress in transfer learning for energy management, making it hard to determine which methods truly improve model scalability and robustness in real-world deployments.

## Datasets

- [[nest-building-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2605.29733)
- [PDF](https://arxiv.org/pdf/2605.29733)

