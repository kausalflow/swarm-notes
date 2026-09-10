---
# CSL-compatible fields
title: "HypLTSF: A Hyperbolic Geometric View of Multi-Scale Hierarchies for Long-Term Time Series Forecasting"
author:
  - literal: "Namwoo Kim"
  - literal: "Hyungryul Baik"
  - literal: "Yoonjin Yoon"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2609.08286"

# Custom fields
paper_id: "2609.08286"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "long-context"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hypltsf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:15:40Z"
created_at: "2026-09-10T09:15:40Z"
---

# HypLTSF: A Hyperbolic Geometric View of Multi-Scale Hierarchies for Long-Term Time Series Forecasting

**Authors**: Namwoo Kim, Hyungryul Baik, Yoonjin Yoon
**Date**: 2026-09-08
**Paper ID**: [openalex:2609.08286](https://arxiv.org/abs/2609.08286)

## Summary

This paper introduces HypLTSF, a framework for long-term time series forecasting that models multi-scale temporal hierarchies through hyperbolic geometry by embedding scale-wise representations into the Poincaré ball. By enforcing radial constraints for abstraction levels and angular constraints for lineage grouping, HypLTSF explicitly captures hierarchical structures that naturally emerge across temporal scales. Extensive experiments demonstrate that this explicit geometric modeling achieves state-of-the-art performance on forecasting benchmarks.

## Key Contributions

- Introduces HypLTSF, a framework that embeds multi-scale temporal hierarchies into the Poincaré ball for long-term time series forecasting.
- Imposes a radial constraint to order embeddings by their level of abstraction within the hyperbolic space.
- Applies an angular constraint to group fine-scale patterns sharing a common coarser-scale ancestor.
- Achieves state-of-the-art performance on standard long-term time series forecasting benchmarks.

## Open Questions & Future Work

- [[hyperbolic-geometry-time-series-hierarchies]]

## Key Concepts

- [[hypltsf]]: A long-term time series forecasting framework that embeds multi-scale temporal hierarchies into the Poincaré ball using radial and angular constraints.

## Archivist Review

Approved the central framework 'HypLTSF' as a reusable geometric modeling approach for multi-scale time series forecasting, and the open question regarding hyperbolic geometry for temporal hierarchies. No datasets were provided or required approval.

### Approved Concepts
- HypLTSF: Central framework introduced in the paper that embeds multi-scale temporal hierarchies into hyperbolic space for long-term time series forecasting.

### Approved Open Questions
- Hyperbolic Geometry for Time Series Hierarchies: Bridging non-Euclidean representation learning with multi-scale time series dynamics is an emerging research direction that requires deeper investigation into how geometric inductive biases interact with temporal structures.

## Links

- [Abstract](https://arxiv.org/abs/2609.08286)
- [PDF](https://arxiv.org/pdf/2609.08286)

