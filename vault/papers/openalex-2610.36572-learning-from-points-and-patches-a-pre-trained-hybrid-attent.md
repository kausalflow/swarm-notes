---
# CSL-compatible fields
title: "Learning from Points and Patches: A Pre-trained Hybrid Attention Transformer for Time Series Analysis"
author:
  - literal: "Peiwang Tang"
  - literal: "Cheng HE"
  - literal: "Yupeng Ye"
  - literal: "Weitai Zhang"
  - literal: "Qinghua Sun"
  - literal: "Defu Lian"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.36572"

# Custom fields
paper_id: "2610.36572"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "few-shot-learning"
  - "zero-shot-learning"
  - "anomaly-detection"
  - "imputation"
  - "classification"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "timehat"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-30T11:04:46Z"
created_at: "2026-10-30T11:04:46Z"
---

# Learning from Points and Patches: A Pre-trained Hybrid Attention Transformer for Time Series Analysis

**Authors**: Peiwang Tang, Cheng HE, Yupeng Ye, Weitai Zhang, Qinghua Sun, Defu Lian
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.36572](https://arxiv.org/abs/2610.36572)

## Summary

The paper introduces TimeHAT, a general-purpose pre-training framework for time-series analysis that employs a Unified Point-Patch Masking Strategy (UPPMS) for point- and patch-level contextual reconstruction and a Hybrid Attention Encoder (HAE) to mitigate rank degeneration. Evaluated across classification, long-term forecasting, imputation, and anomaly detection in fine-tuning, few-shot, and zero-shot settings, TimeHAT demonstrates robust transferability and competitive performance on heterogeneous time-series data.

## Key Contributions

- Proposes TimeHAT, a general-purpose pre-training framework for time-series analysis combining a Unified Point-Patch Masking Strategy and a Hybrid Attention Encoder.
- Introduces a Unified Point-Patch Masking Strategy (UPPMS) that integrates point-level and patch-level supervision for contextual reconstruction and causal extrapolation.
- Develops a Hybrid Attention Encoder (HAE) combining prefix-constrained bidirectional attention and directional hybrid attention to prevent rank degeneration while preserving contextual interactions.
- Demonstrates competitive performance across classification, long-term forecasting, imputation, and anomaly detection under fine-tuning, few-shot, and zero-shot transfer settings.

## Key Concepts

- [[timehat]]: A general-purpose pre-training framework for time-series analysis combining point-patch masking and hybrid attention.

## Archivist Review

The primary framework TimeHAT was approved as a high-level architectural concept for time-series pre-training, while its internal masking strategy and encoder subcomponents were rejected to avoid redundancy with the overarching vault entry.

### Approved Concepts
- TimeHAT: Serves as the core pre-trained hybrid attention transformer framework combining point-patch masking and hybrid attention for time-series analysis.

### Rejected Candidates
- [concept] Unified Point-Patch Masking Strategy (`unified-point-patch-masking-strategy`) - subcomponent_of_broader_mechanism: Subcomponent of the broader TimeHAT framework and adequately captured by the primary concept note.
- [concept] Hybrid Attention Encoder (`hybrid-attention-encoder`) - subcomponent_of_broader_mechanism: Subcomponent of the broader TimeHAT framework and adequately captured by the primary concept note.

## Links

- [Abstract](https://arxiv.org/abs/2610.36572)
- [PDF](https://arxiv.org/pdf/2610.36572)

