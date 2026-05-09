---
# CSL-compatible fields
title: "Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series"
author:
  - literal: "Ruichao Guo"
  - literal: "Xingyao Han"
  - literal: "Luo Wenshui"
  - literal: "Zhe Liu"
  - literal: "Chen Gong"
  - literal: "Hesheng Wang"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04957"

# Custom fields
paper_id: "2605.04957"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "conformal-prediction"
  - "graph-neural-network"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spectral-graph-conditional-exchangeability-sgce"
  - "scale-spectral-conformal-prediction-via-wavelet-transform"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:01:37Z"
created_at: "2026-05-09T07:01:37Z"
---

# Delving into Non-Exchangeability for Conformal Prediction in Graph-Structured Multivariate Time Series

**Authors**: Ruichao Guo, Xingyao Han, Luo Wenshui, Zhe Liu, Chen Gong, Hesheng Wang
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04957](https://arxiv.org/abs/2605.04957)

## Summary

This paper addresses the challenge of rigorous uncertainty quantification in graph-structured multivariate time series, where cross-node dependencies violate the exchangeability assumption required by traditional conformal prediction (CP). The authors introduce Spectral Graph Conditional Exchangeability (SGCE) to decompose signals into high-frequency (exchangeable) and low-frequency (non-exchangeable) components. By conformalizing the high-frequency residuals conditioned on low-frequency embeddings, their proposed framework, SCALE, successfully restores valid coverage guarantees. Empirical evaluation on traffic forecasting benchmarks demonstrates that SCALE outperforms existing CP methods in the coverage-efficiency trade-off.

## Key Contributions

- Identifies that cross-node coupling in graph-structured time series violates the exchangeability assumption required for standard conformal prediction.
- Introduces Spectral Graph Conditional Exchangeability (SGCE) to maintain global trends while allowing valid conformal estimation of high-frequency components.
- Proposes SCALE, which uses graph wavelets and adaptive gating to achieve state-of-the-art coverage-efficiency trade-offs in traffic forecasting benchmarks.

## Open Questions & Future Work

- [[spectral-decomposition-optimality-dynamic-graphs]]

## Key Concepts

- [[spectral-graph-conditional-exchangeability-sgce]]: A formalization that conditions exchangeable high-frequency spectral components on non-exchangeable low-frequency trends to enable valid conformal prediction in graph-structured time series.
- [[scale-spectral-conformal-prediction-via-wavelet-transform]]: A conformal prediction framework that decomposes graph time series into frequency components using wavelets to perform adaptive conformalization on high-frequency residuals.

## Archivist Review

I have approved the core theoretical concept (SGCE) and the corresponding framework (SCALE) as they provide a reusable approach to applying conformal prediction in structured domains where exchangeability is violated. The open question was approved for its focus on the fundamental bottleneck of optimal spectral filtering in non-stationary graphs, which is a significant research gap. No specific datasets were approved as the paper only referenced broad categories of traffic datasets.

### Approved Concepts
- Spectral Graph Conditional Exchangeability (SGCE): It provides a theoretical mechanism to address the violation of exchangeability in graph-structured time series by leveraging spectral graph theory.
- Spectral Conformal prediction via wAveLEt transform (SCALE): It is the primary method proposed to realize valid coverage and improved coverage-efficiency for multivariate graph time series.

### Approved Open Questions
- Spectral Decomposition Optimality in Dynamic Graphs: The validity of the proposed conformal prediction method is fundamentally tied to the quality of the spectral decomposition; identifying universal principles for optimal filtering in this context is critical for broadening the applicability of spectral-based UQ to non-stationary or dynamic networks.

## Links

- [Abstract](https://arxiv.org/abs/2605.04957)
- [PDF](https://arxiv.org/pdf/2605.04957)

