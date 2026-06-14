---
# CSL-compatible fields
title: "Positional encoding in transformer-based time series models: a survey"
author:
  - literal: "Habib Irani"
  - literal: "Vangelis Metsis"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2502.12370"

# Custom fields
paper_id: "2502.12370"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "positional-encoding"
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
processed_at: "2026-06-14T08:36:50Z"
created_at: "2026-06-14T08:36:50Z"
---

# Positional encoding in transformer-based time series models: a survey

**Authors**: Habib Irani, Vangelis Metsis
**Date**: 2026-06-11
**Paper ID**: [openalex:2502.12370](https://arxiv.org/abs/2502.12370)

## Summary

This paper provides a comprehensive survey of positional encoding techniques utilized in transformer-based models for time series tasks like forecasting, classification, and anomaly detection. The authors categorize methods into fixed, learnable, relative, and hybrid approaches, analyzing their performance across various data characteristics. The study highlights a clear performance-complexity trade-off, where more advanced encodings improve accuracy at the expense of higher computational costs. Finally, the work offers guidance for researchers and practitioners on selecting appropriate positional encodings based on dataset-specific features.

## Key Contributions

- Provides a systematic taxonomy and comparative survey of positional encoding techniques specifically adapted for transformer-based time series architectures.
- Identifies critical factors—including sequence length, signal complexity, and dimensionality—that dictate the performance of different positional encoding strategies.
- Quantitatively benchmarks multiple encoding methods, revealing an accuracy-complexity trade-off that informs practical design choices.
- Outlines future research directions to bridge the gap between performance gains and the associated computational overhead in advanced positional encodings.

## Open Questions & Future Work

- [[robustness-to-irregular-sampling-and-missing-data]]
- [[positional-encoding-for-forecasting-horizons]]

## Archivist Review

This survey is a useful organizational contribution but does not introduce a novel forecasting mechanism, representation, or framework that warrants a new concept entry. The open questions regarding irregular sampling and horizon-agnostic encodings are significant enough to track as they represent key bottlenecks for scaling transformer-based time series modeling.

### Approved Open Questions
- PE Robustness in Irregular Series: Understanding PE robustness to data irregularity is critical for the practical deployment of transformer models in healthcare and industrial monitoring where data quality is inconsistent.
- PE for Forecasting Horizons: Developing positional encodings that generalize across forecast horizons is essential for creating versatile, scalable time series forecasting models.

### Rejected Candidates
- [concept] Positional Encoding (`positional-encoding`) - generic: This is a fundamental ML concept that is too broad and generic for a specific standalone entry in this specialized vault.

## Links

- [Abstract](https://arxiv.org/abs/2502.12370)
- [PDF](https://arxiv.org/pdf/2502.12370)

