---
# CSL-compatible fields
title: "TimeLAVA: Learning-Agnostic Data Valuation for Time Series"
author:
  - literal: "刘文琴"
  - literal: "Weizhi Quan"
  - literal: "Aoqi Zuo"
  - literal: "Erdun Gao"
  - literal: "Vu Nguyen"
  - literal: "Dino Sejdinović"
  - literal: "Howard Bondell"
  - literal: "Mingming Gong"
issued:
  date-parts:
    - [2026, 6, 17]
url: "https://arxiv.org/abs/2606.18729"

# Custom fields
paper_id: "2606.18729"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "selective-wavelet-based-wasserstein-discrepancy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-20T08:16:46Z"
created_at: "2026-06-20T08:16:46Z"
---

# TimeLAVA: Learning-Agnostic Data Valuation for Time Series

**Authors**: 刘文琴, Weizhi Quan, Aoqi Zuo, Erdun Gao, Vu Nguyen, Dino Sejdinović, Howard Bondell, Mingming Gong
**Date**: 2026-06-17
**Paper ID**: [openalex:2606.18729](https://arxiv.org/abs/2606.18729)

## Summary

TimeLAVA is a model-agnostic data valuation framework for time series that assigns quality scores to temporal segments without requiring model training. By leveraging a novel Selective Wavelet-based Wasserstein discrepancy, the method effectively captures multi-scale temporal dependencies and non-stationary dynamics while remaining robust to distributional shifts. Theoretical guarantees support the framework's effectiveness in improving generalization and robustness, with experimental results confirming its superiority in anomaly detection and data cleaning applications.

## Key Contributions

- Proposes TimeLAVA, a learning-agnostic framework for valuing time-series segments based on distributional discrepancy reduction.
- Introduces Selective Wavelet-based Wasserstein discrepancy, which uses multi-scale wavelet transforms and unbalanced optimal transport to capture non-stationary temporal dynamics.
- Provides theoretical guarantees linking the proposed valuation metric to model-agnostic generalization and proves robustness to outlier contamination.
- Demonstrates state-of-the-art performance in anomaly detection, data pruning, and label noise detection tasks compared to model-dependent valuation methods.

## Key Concepts

- [[selective-wavelet-based-wasserstein-discrepancy]]: A data valuation metric for time series that integrates multi-scale wavelet transforms and unbalanced optimal transport to quantify the marginal contribution of temporal segments.

## Archivist Review

I approved the selective wavelet-based Wasserstein discrepancy as it provides a robust, model-agnostic approach to temporal data valuation, addressing the challenge of handling non-stationary and sequential dependencies. I rejected the TimeLAVA framework as a standalone concept because the core mechanism adequately captures the contribution of the paper. No datasets or open questions were proposed, so none were approved.

### Approved Concepts
- Selective Wavelet-based Wasserstein Discrepancy: It serves as the core mechanism for identifying high-value temporal segments without requiring model training, enabling model-agnostic data valuation.

### Rejected Candidates
- [concept] TimeLAVA Framework (`timelava-framework`) - subcomponent_of_broader_mechanism: This is the name of the paper's specific implementation, which is better represented by its core component mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.18729)
- [PDF](https://arxiv.org/pdf/2606.18729)

