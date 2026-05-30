---
# CSL-compatible fields
title: "QuITE: Query-Based Irregular Time Series Embedding"
author:
  - literal: "JungHoon Lim"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28166"

# Custom fields
paper_id: "2605.28166"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "embedding"
  - "forecasting"
  - "text-classification"
  - "attention-mechanism"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quite-query-based-irregular-time-series-embedding"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:34:59Z"
created_at: "2026-05-30T07:34:59Z"
---

# QuITE: Query-Based Irregular Time Series Embedding

**Authors**: JungHoon Lim
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28166](https://arxiv.org/abs/2605.28166)

## Summary

QuITE addresses the challenge of modeling irregular multivariate time series by replacing interpolation-heavy embedding methods with a query-based aggregation mechanism. By utilizing learnable query tokens in a single self-attention layer, it effectively maps irregularly sampled observations into uniform latent representations. This approach preserves temporal dynamics while allowing existing, proven multivariate time series architectures to be applied directly to irregular data, resulting in significant performance gains across forecasting and classification tasks.

## Key Contributions

- Introduces QuITE, a plug-and-play embedding module that converts irregular multivariate time series to regular representations using learnable query tokens and self-attention.
- Enables the use of standard multivariate time series backbones for irregular data without requiring architectural modifications or interpolation-induced artificial values.
- Demonstrates performance improvements of up to 54.7% in forecasting and 15.8% in classification across diverse benchmarks.

## Key Concepts

- [[quite-query-based-irregular-time-series-embedding]]: A plug-and-play embedding module that uses learnable query tokens and self-attention to map irregular time series to regular, backbone-compatible representations.

## Archivist Review

I approved the QuITE concept as it represents a robust, architecture-agnostic method for handling irregular temporal data, which addresses a common bottleneck in time-series modeling without relying on distortion-heavy interpolation. No datasets or open questions were proposed or identified as sufficient for vault inclusion.

### Approved Concepts
- QuITE (Query-Based Irregular Time Series Embedding): It provides a model-agnostic, plug-and-play solution for irregular time series that bypasses the need for artificial interpolation or specialized, non-reusable architectures.

### Rejected Candidates
- [open_question] None provided (`none-provided`) - generic: No open questions were identified in the analysis.

## Links

- [Abstract](https://arxiv.org/abs/2605.28166)
- [PDF](https://arxiv.org/pdf/2605.28166)

