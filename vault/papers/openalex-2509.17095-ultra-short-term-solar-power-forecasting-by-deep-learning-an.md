---
# CSL-compatible fields
title: "Ultra-short-term solar power forecasting by deep learning and data reconstruction"
author:
  - literal: "Jinbao Wang"
  - literal: "Jun Liu"
  - literal: "Shiliang Zhang"
  - literal: "Xuehui Ma"
  - literal: "Chenhui Yang"
  - literal: "Bairen An"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2509.17095"

# Custom fields
paper_id: "2509.17095"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "probabilistic-forecasting"
  - "neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "drdpn-data-reconstruction-based-deep-probabilistic-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:31Z"
created_at: "2026-06-11T09:07:31Z"
---

# Ultra-short-term solar power forecasting by deep learning and data reconstruction

**Authors**: Jinbao Wang, Jun Liu, Shiliang Zhang, Xuehui Ma, Chenhui Yang, Bairen An
**Date**: 2026-06-08
**Paper ID**: [openalex:2509.17095](https://arxiv.org/abs/2509.17095)

## Summary

The paper introduces the Data Reconstruction-based Deep Probabilistic Network (DRDPN) to improve ultra-short-term probabilistic solar power forecasting. The method utilizes ACEEMDAN decomposition to address non-stationarity in PV data, followed by a two-stage post-processing framework that reconstructs time-series into frequency-differentiated components for improved consistency. A heterogeneous multi-network architecture then processes these components to generate reliable probabilistic forecasts. Experiments demonstrate significant performance gains in both point and probabilistic metrics across volatile solar power generation conditions.

## Key Contributions

- Proposes the DRDPN framework, which integrates adaptive decomposition and a two-stage reconstruction process to handle non-stationary solar power data.
- Implements a heterogeneous multi-network architecture that performs component-specific feature extraction and adaptive cross-modal fusion.
- Achieves 4.57% improvement in R2 and 57.10% improvement in nMAE compared to existing baselines on real-world PV datasets.

## Open Questions & Future Work

- [[probabilistic-pv-distribution-approximation-limits]]

## Key Concepts

- [[drdpn-data-reconstruction-based-deep-probabilistic-network]]: A deep probabilistic forecasting framework that reconstructs time-series into frequency-differentiated components before feature extraction.

## Archivist Review

I have approved the DRDPN framework as a representative example of a modular, frequency-aware forecasting architecture, and the open question regarding the trade-offs between quantile-based approximation and true density estimation, which is a significant bottleneck in probabilistic forecasting. I rejected ACEEMDAN because it is a standard signal processing tool, not a novel contribution of the paper.

### Approved Concepts
- Data Reconstruction-based Deep Probabilistic Network (DRDPN): DRDPN introduces a modular forecasting approach that separates non-stationary time-series decomposition from component-specific deep learning, offering a structured way to handle volatile signals.

### Approved Open Questions
- Probabilistic Distribution Approximation Limitations: This addresses a fundamental limitation in current probabilistic time-series forecasting where computational efficiency (quantile estimation) often sacrifices density fidelity, which is critical for grid stability applications.

### Rejected Candidates
- [concept] Adaptive Complete Ensemble Empirical Mode Decomposition with Adaptive Noise (`aceemdan`) - not_novel: This is a known established technique in time-series analysis rather than a novel contribution of this paper.

## Links

- [Abstract](https://arxiv.org/abs/2509.17095)
- [PDF](https://arxiv.org/pdf/2509.17095)

