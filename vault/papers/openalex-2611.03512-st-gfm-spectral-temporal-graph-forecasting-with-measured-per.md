---
# CSL-compatible fields
title: "ST-GFM: Spectral-Temporal Graph Forecasting with Measured Perturbation Bounds and Masked Spectral Reconstruction"
author:
  - literal: "Aashish Bohra"
  - literal: "Vivek Vijay"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03512"

# Custom fields
paper_id: "2611.03512"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "attention-mechanism"
  - "self-supervised-learning"
  - "robustness"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  - "metr-la"
  - "pems-bay"
concept_slugs:
  []
dataset_slugs:
  - "metr-la"
  - "pems-bay"
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:52:26Z"
created_at: "2026-11-05T12:52:26Z"
---

# ST-GFM: Spectral-Temporal Graph Forecasting with Measured Perturbation Bounds and Masked Spectral Reconstruction

**Authors**: Aashish Bohra, Vivek Vijay
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03512](https://arxiv.org/abs/2611.03512)

## Summary

This paper proposes ST-GFM, a spectral-temporal graph forecasting model designed to handle regime shifts in sensor networks where sensor coupling and signal frequency content change. ST-GFM combines Chebyshev and bidirectional diffusion filters on a learned non-symmetric operator with per-node temporal attention, backed by proven Frobenius-norm perturbation bounds. Additionally, it introduces Masked Spectral Reconstruction (MSR), a self-supervised loss that matches log power spectra and aligns with an Itakura-Saito divergence. Evaluated on METR-LA and PEMS-BAY, ST-GFM achieves superior performance, establishing new state-of-the-art results among multiple published baselines.

## Key Contributions

- Proposed ST-GFM (Spectral-Temporal Graph Forecasting Model), which alternates Chebyshev and bidirectional diffusion filters on a learned non-symmetric operator with per-node temporal attention.
- Proved Frobenius-norm perturbation bounds for both graph branches, computing constants of 17.9 on METR-LA and 21.5 on PEMS-BAY.
- Introduced Masked Spectral Reconstruction (MSR), a self-supervised log power spectrum matching loss proven to be proportional to an Itakura-Saito divergence to leading order.
- Achieved state-of-the-art 60-minute MAE of 3.098 on METR-LA and 1.576 on PEMS-BAY, outperforming twelve published baselines.

## Archivist Review

Applied strict selection criteria. No standalone concepts were approved as the methods are paper-local architectures and losses. The METR-LA and PEMS-BAY datasets are approved as standard benchmark datasets. The open question is rejected as a paper-local scaling concern.

### Rejected Candidates
- [open_question] Sparse Learned Graph Operators (`sparse-learned-graph-operators-large-scale`) - low_impact: The open question largely concerns scaling dense matrix multiplications and perturbation bounds to larger networks via top-k approximations, which is a specialized engineering extension rather than a fundamental theoretical bottleneck.

## Datasets

- [[metr-la]]
- [[pems-bay]]

## Links

- [Abstract](https://arxiv.org/abs/2611.03512)
- [PDF](https://arxiv.org/pdf/2611.03512)

