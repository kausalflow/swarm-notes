---
# CSL-compatible fields
title: "Align-RAG: Alignment Is All You Need for TSFM In-Context Learning"
author:
  - literal: "Mohammad Asadi"
  - literal: "Soheil Hor"
  - literal: "Bardiya Akhbari"
  - literal: "Jack W. O'Sullivan"
  - literal: "Tahoura Nedaee"
  - literal: "Layne C. Price"
  - literal: "Raviteja Anantha"
  - literal: "Euan Ashley"
  - literal: "Ehsan Adeli"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05571"

# Custom fields
paper_id: "2608.05571"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "rag"
  - "in-context-learning"
  - "pre-training"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "align-rag"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:37Z"
created_at: "2026-08-09T05:40:37Z"
---

# Align-RAG: Alignment Is All You Need for TSFM In-Context Learning

**Authors**: Mohammad Asadi, Soheil Hor, Bardiya Akhbari, Jack W. O'Sullivan, Tahoura Nedaee, Layne C. Price, Raviteja Anantha, Euan Ashley, Ehsan Adeli
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05571](https://arxiv.org/abs/2608.05571)

## Summary

This paper introduces Align-RAG, a training-free method for retrieval-augmented time series forecasting that applies closed-form amplitude rescaling and integer-lag phase shifts to retrieved context windows. By aligning these windows before they enter frozen time series foundation models (TSFMs), Align-RAG outperforms state-of-the-art learned retrieval adapters across standard benchmarks without requiring any training parameters. Furthermore, the approach improves zero-shot performance across multiple TSFM architectures, showing that frozen foundation models natively support effective in-context learning when retrievals are properly aligned.

## Key Contributions

- Introduces Align-RAG, a training-free retrieval-augmented forecasting method using closed-form per-pair amplitude rescaling and integer-lag phase shift.
- Outperforms state-of-the-art trained retrieval adapters on a frozen Chronos-Bolt across seven standard benchmark datasets with an average 3.75% reduction in MSE.
- Improves zero-shot MSE across four additional frozen TSFMs with various architectures by 2.5% to 13.7% without per-backbone tuning.
- Demonstrates through ridge prediction shift analysis and controls that frozen TSFMs natively support dynamic in-context use of aligned retrievals.

## Limitations

Evaluated primarily on standard public benchmarks and existing frozen TSFMs; potential interactions with extremely long-horizon forecasting or pathological distribution shifts remain to be fully explored.

## Open Questions & Future Work

- [[richer-retrieval-geometries-multivariate-covariates]]

## Key Concepts

- [[align-rag]]: A training-free retrieval-augmented forecasting method that applies closed-form amplitude rescaling and phase shifting to retrieved windows before feeding them into frozen time series foundation models.

## Archivist Review

Approved the central training-free alignment method for TSFM in-context learning (Align-RAG) along with its explicit open question on multivariate retrieval geometries. Kept selections scarce and adhered strictly to vault criteria.

### Approved Concepts
- Align-RAG: Central methodological contribution of the paper, demonstrating that training-free closed-form alignment outperforms learned fusion modules for retrieval-augmented forecasting in time series foundation models.

### Approved Open Questions
- Richer Retrieval Geometries and Covariates: Extending alignment-based retrieval-augmented forecasting to multivariate and covariate-rich time series is crucial for real-world deployment where univariate assumptions do not hold.

## Links

- [Abstract](https://arxiv.org/abs/2608.05571)
- [PDF](https://arxiv.org/pdf/2608.05571)

