---
# CSL-compatible fields
title: "Robust Transformer-Based One-Step Stock Index Forecasting via Shifted Data Augmentation"
author:
  - literal: "Tien Thanh Thach"
issued:
  date-parts:
    - [2026, 6, 14]
url: "https://arxiv.org/abs/2606.15701"

# Custom fields
paper_id: "2606.15701"
paper_source: "openalex"
domain: "finance"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  - "encoder-only"
datasets:
  - "VN30"
  - "S&P 500"
concept_slugs:
  - "shifted-data-augmentation-sda"
dataset_slugs:
  - "vn30"
  - "sp-500"
skill: "TimeSeriesSkill"
processed_at: "2026-06-17T09:25:58Z"
created_at: "2026-06-17T09:25:58Z"
---

# Robust Transformer-Based One-Step Stock Index Forecasting via Shifted Data Augmentation

**Authors**: Tien Thanh Thach
**Date**: 2026-06-14
**Paper ID**: [openalex:2606.15701](https://arxiv.org/abs/2606.15701)

## Summary

This paper addresses the limitations of applying Transformers to noisy financial time series by introducing a modified architecture combined with a novel Shifted Data Augmentation (SDA) technique. The study investigates optimal learning-rate scheduling, identifying cosine annealing with warmup as superior for forecasting accuracy. Evaluation on the VN30 and S&P 500 benchmarks confirms that the SDA method significantly improves robustness and reduces error, suggesting that strategic data augmentation is more critical than scaling model complexity for financial prediction.

## Key Contributions

- Proposes a modified Transformer architecture paired with Shifted Data Augmentation (SDA) for robust one-step stock index forecasting.
- Demonstrates that cosine annealing with warmup consistently outperforms generalized inverse-power scheduling for financial forecasting.
- Shows that SDA reduces both forecasting error and run-to-run variability, highlighting the efficacy of data augmentation over increased model scale in financial settings.

## Open Questions & Future Work

- [[generalizability-of-sda-across-architectures]]

## Key Concepts

- [[shifted-data-augmentation-sda]]: A data augmentation technique for financial time series that improves forecasting accuracy and robustness to hyperparameter selection.

## Archivist Review

I have approved the core data augmentation concept and the associated architectural generalizability question. I have also added the two central stock index datasets used in the study. Generic training techniques like cosine annealing were rejected as they are standard practice and not novel to this contribution.

### Approved Concepts
- Shifted Data Augmentation (SDA): Addresses the inherent noise and distributional shift challenges in financial time series without requiring increased model complexity.

### Approved Open Questions
- Generalizability of SDA across Architectures: Establishing the generalizability of SDA across architectures is critical for identifying whether this augmentation strategy addresses fundamental challenges in financial time series modeling or if it only resolves limitations specific to the Transformer architecture.

## Datasets

- [[vn30]]
- [[sp-500]]

## Links

- [Abstract](https://arxiv.org/abs/2606.15701)
- [PDF](https://arxiv.org/pdf/2606.15701)

