---
# CSL-compatible fields
title: "FARE: Factor-Aware Retrieval with Error-Guided Fusion for Retail Forecasting"
author:
  - literal: "Chenghao Gu"
  - literal: "Zhuokang Shen"
  - literal: "Shenghao Wu"
  - literal: "Tingxuan Zhu"
  - literal: "Wei Luo"
  - literal: "Haifeng Tang"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.40160"

# Custom fields
paper_id: "2610.40160"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
architectures:
  []
datasets:
  - "favorita"
  - "rossmann"
concept_slugs:
  - "factor-aware-retrieval-with-error-guided-fusion"
dataset_slugs:
  - "favorita"
  - "rossmann"
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:33:39Z"
created_at: "2026-11-01T11:33:39Z"
---

# FARE: Factor-Aware Retrieval with Error-Guided Fusion for Retail Forecasting

**Authors**: Chenghao Gu, Zhuokang Shen, Shenghao Wu, Tingxuan Zhu, Wei Luo, Haifeng Tang
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.40160](https://arxiv.org/abs/2610.40160)

## Summary

The paper introduces FARE (Factor-Aware Retrieval with Error-Guided Fusion) to address retail forecasting challenges caused by rare factor combinations during promotions and calendar events. FARE separately ranks historical weeks for each target factor, constructs a factor reference, and uses an error-guided dual-gate mechanism to merge it with a shape reference, correcting backbone models. Experiments on Favorita, M5, Rossmann, and Rohlik demonstrate consistent error reductions across multiple forecasting backbones.

## Key Contributions

- Proposes FARE, which ranks historical weeks by individual target-week factors and merges them into a factor reference under a budget constraint.
- Employs a two-stage error-guided fusion strategy using fixed gates to combine factor references and shape references to correct backbone forecasts.
- Reduces WAPE across Favorita, M5, Rossmann, and Rohlik datasets by 11.46%, 4.06%, 14.63%, and 10.16% on average over five backbones.

## Open Questions & Future Work

- [[generalization-absent-factor-combinations]]

## Key Concepts

- [[factor-aware-retrieval-with-error-guided-fusion]]: A retail forecasting framework that ranks historical weeks by target-week factors and fuses them using error-guided gates to correct backbone predictions.

## Archivist Review

Applied strict selectivity guidelines. Approved the primary methodological contribution (Factor-Aware Retrieval with Error-Guided Fusion) and its key open question regarding out-of-distribution factor combinations. Selected two canonical retail datasets while keeping dataset selections strictly capped.

### Approved Concepts
- Factor-Aware Retrieval with Error-Guided Fusion: It introduces a novel dual-gate retrieval and fusion mechanism that handles complex factor combinations in retail forecasting by combining factor references and shape references.

### Approved Open Questions
- Generalization to Absent Factor Combinations: Understanding the limits of retrieval-augmented forecasting under complete out-of-distribution factor combinations is critical for deploying robust supply chain models in retail.

## Datasets

- [[favorita]]
- [[rossmann]]

## Links

- [Abstract](https://arxiv.org/abs/2610.40160)
- [PDF](https://arxiv.org/pdf/2610.40160)

