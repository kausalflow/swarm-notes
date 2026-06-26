---
# CSL-compatible fields
title: "RAVEN: A Regime-Aware Variable-context Expert Network for Financial Time Series Forecasting"
author:
  - literal: "Cheng He"
  - literal: "Zhenyu Guan"
  - literal: "Xijie Liang"
  - literal: "Defu Lian"
  - literal: "Jiajia Li"
  - literal: "Enhong Chen"
  - literal: "Patrick P. C. Lee"
  - literal: "Geng Hu"
  - literal: "Zehao Chen"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24062"

# Custom fields
paper_id: "2606.24062"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "moe"
architectures:
  []
datasets:
  []
concept_slugs:
  - "raven-framework"
  - "cumulative-importance-thresholding-cit"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:00Z"
created_at: "2026-06-26T08:25:00Z"
---

# RAVEN: A Regime-Aware Variable-context Expert Network for Financial Time Series Forecasting

**Authors**: Cheng He, Zhenyu Guan, Xijie Liang, Defu Lian, Jiajia Li, Enhong Chen, Patrick P. C. Lee, Geng Hu, Zehao Chen
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24062](https://arxiv.org/abs/2606.24062)

## Summary

Financial time series forecasting is often hindered by fixed context windows that fail to capture time-varying, regime-dependent dynamics. To address this, the authors propose the Regime-Aware Variable-context Expert Network (RAVEN), a Mixture-of-Experts framework that dynamically constructs hierarchical input windows using a Cumulative Importance Thresholding (CIT) mechanism. A Global Compressed Representation branch and a Correlation-Aware Weighting (CAW) strategy are incorporated to ensure global temporal coherence and mitigate output overlap. Empirical results demonstrate significant performance gains over state-of-the-art models across financial log-return and fund sales benchmarks, as well as traffic forecasting tasks.

## Key Contributions

- Introduced RAVEN, a Mixture-of-Experts model that adaptively selects temporal context windows for non-stationary time series forecasting.
- Developed the Cumulative Importance Thresholding (CIT) mechanism for data-driven, hierarchical context window derivation.
- Introduced Correlation-Aware Weighting (CAW) to align expert outputs and maintain temporal coherence in structural expert ensembles.
- Achieved SOTA results on log-return prediction (HS300, S&P500) and fund sales forecasting, including a 20.2% Pearson correlation improvement on S&P500.

## Open Questions & Future Work

- [[variable-resolution-financial-forecasting]]

## Key Concepts

- [[raven-framework]]: A Mixture-of-Experts time series architecture that adaptively determines input context length through hierarchical window routing based on cumulative importance thresholding.
- [[cumulative-importance-thresholding-cit]]: A data-driven mechanism that selects optimal context windows by aggregating patch-level importance scores in reverse chronological order.

## Archivist Review

The paper introduces a structured mixture-of-experts approach to dynamic windowing in time series, which is a sufficiently novel and reusable paradigm to warrant conceptual status. I have approved the framework and its primary thresholding mechanism, while rejecting the datasets as standard benchmarks. The identified open question captures a significant gap regarding the intersection of variable context windowing and multiscale resolution in financial forecasting.

### Approved Concepts
- Regime-Aware Variable-context Expert Network: RAVEN offers a novel approach to addressing fixed look-back window limitations by using adaptive hierarchical routing, a concept likely to influence future ensemble architectures for non-stationary time series.
- Cumulative Importance Thresholding: CIT provides a generalized technique for data-driven context window derivation based on patch importance, serving as a modular alternative to static window selection in deep learning models.

### Approved Open Questions
- Variable-resolution Financial Time Forecasting: This addresses a fundamental limitation in current time series models that treat resolution and windowing as static hyperparameters rather than time-varying parameters driven by data content.

### Rejected Candidates
- [dataset] HS300 (`hs300-dataset`) - not_novel: Commonly used benchmark; does not merit a permanent standalone note.
- [dataset] S&P500 (`sp500-dataset`) - not_novel: Commonly used benchmark; does not merit a permanent standalone note.

## Links

- [Abstract](https://arxiv.org/abs/2606.24062)
- [PDF](https://arxiv.org/pdf/2606.24062)

