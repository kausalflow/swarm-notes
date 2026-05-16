---
# CSL-compatible fields
title: "GHGbench: A Unified Multi-Entity, Multi-Task Benchmark for Carbon Emission Prediction"
author:
  - literal: "Yifan Duan"
  - literal: "Siyuan Zheng"
  - literal: "Lihuan Li"
  - literal: "Chao Xue"
  - literal: "Flora D. Salim"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13743"

# Custom fields
paper_id: "2605.13743"
paper_source: "openalex"
domain: "time-series"
tags:
  - "benchmark"
  - "dataset"
  - "time-series"
  - "forecasting"
  - "multimodal"
architectures:
  []
datasets:
  - "ghgbench"
concept_slugs:
  - "ghgbench"
dataset_slugs:
  - "ghgbench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:11:14Z"
created_at: "2026-05-16T07:11:14Z"
---

# GHGbench: A Unified Multi-Entity, Multi-Task Benchmark for Carbon Emission Prediction

**Authors**: Yifan Duan, Siyuan Zheng, Lihuan Li, Chao Xue, Flora D. Salim
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13743](https://arxiv.org/abs/2605.13743)

## Summary

GHGbench is a new, unified benchmark designed to standardize carbon emission prediction across company- and building-level entities. The benchmark integrates diverse data sources—including financial disclosures for firms and remote-sensing embeddings for buildings—to evaluate model performance on in-distribution and cross-region transfer tasks. Results demonstrate that structural complexity and distribution shifts pose greater challenges than model choice alone, while highlighting the efficacy of tabular foundation models and multimodal integration in climate-aware forecasting.

## Key Contributions

- Introduces GHGbench, a comprehensive benchmark containing over 32,000 company records and nearly 500,000 building-year records across 26 metropolitan areas.
- Demonstrates that the performance gap between in-distribution and out-of-distribution transfer significantly exceeds differences between individual model architectures.
- Establishes that tabular foundation models provide a statistically significant improvement over traditional gradient-boosted trees in multi-city building emission prediction tasks.
- Reveals that multimodal remote-sensing embeddings mitigate performance degradation in scenarios where tabular data generalization is insufficient.

## Open Questions & Future Work

- [[cross-region-climate-forecasting-robustness]]

## Key Concepts

- [[ghgbench]]: A unified multi-entity, multi-task benchmark for predicting carbon emissions at the company and building levels.

## Archivist Review

I approved the GHGbench benchmark and its dataset as a significant contribution to the climate ML domain. I rejected the initial open question for being too broad, replacing it with a more focused question targeting the cross-region OOD gap identified as the central failure mode of the current state-of-the-art.

### Approved Concepts
- GHGbench: Provides a first-of-its-kind unified benchmark for carbon emission prediction covering both company and building levels.

### Approved Open Questions
- Cross-Region Climate Forecasting Robustness: The paper identifies the in-distribution to out-of-distribution transfer gap as the dominant bottleneck in climate forecasting, making this the primary research priority.

### Rejected Candidates
- [open_question] Advanced Multimodal Fusion and Forecasting (`advanced-multimodal-fusion-and-forecasting`) - generic: The proposed question is too generic and encompasses multiple distinct research areas rather than identifying a specific scientific bottleneck.

## Datasets

- [[ghgbench]]

## Links

- [Abstract](https://arxiv.org/abs/2605.13743)
- [PDF](https://arxiv.org/pdf/2605.13743)

