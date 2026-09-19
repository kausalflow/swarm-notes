---
# CSL-compatible fields
title: "CoRe: Coherence and Relational Alignment for Multivariate Time Series Forecasting"
author:
  - literal: "Xiaoyu Lin"
  - literal: "Hao-yu Duan"
  - literal: "Yining Liu"
  - literal: "Zhixiang Wu"
  - literal: "Chu Lin"
  - literal: "Lin Lu"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19670"

# Custom fields
paper_id: "2609.19670"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "core"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:02:55Z"
created_at: "2026-09-19T09:02:55Z"
---

# CoRe: Coherence and Relational Alignment for Multivariate Time Series Forecasting

**Authors**: Xiaoyu Lin, Hao-yu Duan, Yining Liu, Zhixiang Wu, Chu Lin, Lin Lu
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19670](https://arxiv.org/abs/2609.19670)

## Summary

Direct multivariate time-series forecasting often relies on pointwise supervision like MSE, which can weaken temporal coherence and cross-variable relational consistency. To address this, the authors propose CoRe, a model-agnostic learning objective comprising a frequency coherence loss and a low-rank relational graph loss in a PCA subspace. CoRe requires no trainable parameters, acts as a drop-in replacement for existing backbones, and consistently improves performance across standard benchmarks.

## Key Contributions

- Proposes CoRe, a model-agnostic output-space learning objective for direct multivariate time series forecasting that eliminates pointwise error limitations.
- Introduces a frequency coherence loss to align predicted and target spectra for preserving temporal structure.
- Introduces a low-rank relational graph loss to match pairwise differences in a target-derived PCA subspace, preserving cross-variable consistency.
- Demonstrates consistent performance improvements across diverse forecasting backbones and standard benchmarks without adding trainable parameters.

## Open Questions & Future Work

- [[non-linear-relational-alignment-mtsf]]

## Key Concepts

- [[core]]: A model-agnostic output-space learning objective for direct multivariate time series forecasting that enforces temporal coherence and relational consistency.

## Archivist Review

Approved the central CoRe learning objective as a highly reusable model-agnostic loss function for multivariate time-series forecasting, along with the open question regarding non-linear relational graph alignment. All other candidates were skipped or consolidated to maintain strict vault standards.

### Approved Concepts
- CoRe: Introduces a novel loss function combining frequency coherence and low-rank relational graph alignment for multivariate time series forecasting.

### Approved Open Questions
- Non-linear Relational Graph Alignment: Linear low-rank projections may fail to capture highly non-linear interactions among variables in complex real-world multivariate systems, making non-linear extensions crucial for improving relational graph losses.

## Links

- [Abstract](https://arxiv.org/abs/2609.19670)
- [PDF](https://arxiv.org/pdf/2609.19670)

