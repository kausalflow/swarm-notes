---
# CSL-compatible fields
title: "TensorLOB: Structure-Preserving Tensor Learning for Limit Order Book Forecasting"
author:
  - literal: "Yuxuan Gu"
  - literal: "Danilo P. Mandic"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02866"

# Custom fields
paper_id: "2611.02866"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  - "fi-2010"
concept_slugs:
  - "tensorlob"
dataset_slugs:
  - "fi-2010"
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:40:51Z"
created_at: "2026-11-04T12:40:51Z"
---

# TensorLOB: Structure-Preserving Tensor Learning for Limit Order Book Forecasting

**Authors**: Yuxuan Gu, Danilo P. Mandic
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02866](https://arxiv.org/abs/2611.02866)

## Summary

The paper introduces TensorLOB, a structure-preserving tensor learning framework for limit order book (LOB) forecasting that avoids traditional matrix flattening by operating entirely in the tensor domain. By employing mode-wise tensor contractions and low-rank class-weight tensors, TensorLOB preserves the distinct multiway dimensions of time, market side, price level, and attributes. Experiments on the FI-2010 benchmark demonstrate that TensorLOB outperforms existing models, achieving superior accuracy, recall, and F1 scores across all evaluated horizons.

## Key Contributions

- Proposes TensorLOB, a structure-preserving tensor learning model for limit order book (LOB) forecasting that operates entirely in the tensor domain without flattening.
- Uses mode-wise tensor contractions for feature extraction and directly contracts learned representations with low-rank class-weight tensors for classification.
- Demonstrates top performance in accuracy, recall, and F1 score across all four evaluation horizons on the FI-2010 benchmark.

## Limitations

Future work could explore scaling TensorLOB to larger order books, deeper multi-layer tensor architectures, and additional high-frequency financial datasets.

## Key Concepts

- [[tensorlob]]: A structure-preserving tensor learning framework for limit order book forecasting that operates entirely in the tensor domain using mode-wise tensor contractions.

## Archivist Review

Approved TensorLOB as a novel structure-preserving tensor learning framework for financial limit order books, along with the FI-2010 dataset. All other potential additions were deemed paper-local or routine.

### Approved Concepts
- TensorLOB: Central framework introducing structure-preserving tensor learning for limit order book forecasting by operating entirely in the tensor domain.

## Datasets

- [[fi-2010]]

## Links

- [Abstract](https://arxiv.org/abs/2611.02866)
- [PDF](https://arxiv.org/pdf/2611.02866)

