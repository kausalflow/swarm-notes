---
# CSL-compatible fields
title: "Does Synthetic Data Help? Empirical Evidence from Deep Learning Time Series Forecasters"
author:
  - literal: "Hugo Cazaux"
  - literal: "Eyjólfur Ingi Ásgeirsson"
  - literal: "Hlynur Stefánsson"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06032"

# Custom fields
paper_id: "2605.06032"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "synthetic-data-augmentation-for-time-series-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:20:46Z"
created_at: "2026-05-10T07:20:46Z"
---

# Does Synthetic Data Help? Empirical Evidence from Deep Learning Time Series Forecasters

**Authors**: Hugo Cazaux, Eyjólfur Ingi Ásgeirsson, Hlynur Stefánsson
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06032](https://arxiv.org/abs/2605.06032)

## Summary

This paper provides a large-scale empirical evaluation of synthetic data augmentation in deep learning-based time series forecasting. Across 4,218 experiments, the study reveals that the impact of synthetic data is highly sensitive to the model architecture: channel-mixing models often see significant performance gains, particularly in low-data regimes, while channel-independent models typically suffer. The authors provide practical guidelines for researchers, highlighting the necessity of matching augmentation strategies to architecture and data characteristics.

## Key Contributions

- Conducted a large-scale empirical study with 4,218 runs to evaluate the impact of synthetic data across five time-series forecasting architectures and seven datasets.
- Demonstrated that synthetic data augmentation's effectiveness is architecture-conditional, consistently benefiting channel-mixing models (e.g., TimesNet, iTransformer) while degrading channel-independent ones (e.g., DLinear, PatchTST).
- Established actionable guidelines for practitioners, identifying Seasonal-Trend generators as the most reliable augmentation method and finding that hard curriculum switching significantly harms performance.

## Open Questions & Future Work

- [[architecture-dependency-of-synthetic-augmentation]]
- [[synthetic-data-generator-transferability]]

## Key Concepts

- [[synthetic-data-augmentation-for-time-series-forecasting]]: A systematic analysis showing that synthetic data augmentation in time series forecasting is architecture-conditional, generally benefiting channel-mixing models while harming channel-independent ones.

## Archivist Review

I approved the main concept regarding the architecture-conditional nature of synthetic data augmentation and two critical open questions that categorize the research barriers revealed by the paper. The paper's contribution is primarily empirical and methodological, serving as a landmark study on a technique that was previously poorly understood in time-series forecasting. Datasets were rejected as they were routine or standard usage rather than being central, original assets introduced by the authors.

### Approved Concepts
- Synthetic Data Augmentation for Time Series Forecasting: Provides a comprehensive empirical investigation into a technique whose efficacy is shown to be highly dependent on architecture design, offering a taxonomy of success and failure modes for time series deep learning.

### Approved Open Questions
- Architecture-Dependent Augmentation Mechanisms: Understanding this dependency is critical for developing robust synthetic augmentation strategies for time series, as current practices lead to degradation in a majority of evaluated architecture/dataset combinations.
- Generator Selection and Matching: Without a formal approach to matching generator characteristics to target data, practitioners must rely on trial-and-error, which is costly and often leads to performance degradation.

## Links

- [Abstract](https://arxiv.org/abs/2605.06032)
- [PDF](https://arxiv.org/pdf/2605.06032)

