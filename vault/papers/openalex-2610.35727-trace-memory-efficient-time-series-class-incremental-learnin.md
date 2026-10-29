---
# CSL-compatible fields
title: "TRACE: Memory-Efficient Time Series Class-Incremental Learning via Temporal-Spectral Reconstruction"
author:
  - literal: "Junhui Mao"
  - literal: "Junru Zhang"
  - literal: "Liming Ye"
  - literal: "Cheng Peng"
  - literal: "Haoran Shi"
  - literal: "Xiaoli Tang"
  - literal: "Baokun Wang"
  - literal: "Bin Dou"
  - literal: "Yabo Dong"
  - literal: "Han Yu"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35727"

# Custom fields
paper_id: "2610.35727"
paper_source: "openalex"
domain: "time-series"
tags:
  - "continual-learning"
  - "time-series"
  - "representation-learning"
  - "generative-adversarial-network"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:38Z"
created_at: "2026-10-29T11:10:38Z"
---

# TRACE: Memory-Efficient Time Series Class-Incremental Learning via Temporal-Spectral Reconstruction

**Authors**: Junhui Mao, Junru Zhang, Liming Ye, Cheng Peng, Haoran Shi, Xiaoli Tang, Baokun Wang, Bin Dou, Yabo Dong, Han Yu
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35727](https://arxiv.org/abs/2610.35727)

## Summary

The paper introduces TRACE, a memory-efficient and replay-free framework for Time Series Class-Incremental Learning (TSCIL) that avoids sample rehearsal by employing compact temporal-spectral representations and lightweight class-specific autoencoders. It performs classification through reconstruction-based scoring without storing historical samples or large statistical matrices. Extensive evaluations across five TSCIL benchmarks show that TRACE drastically reduces retained memory while improving or matching classification accuracy compared to strong baselines.

## Key Contributions

- Proposes TRACE, a memory-efficient and replay-free framework for Time Series Class-Incremental Learning (TSCIL) that uses compact temporal-spectral representations and lightweight class-specific autoencoders.
- Eliminates the need for sample rehearsal or large statistical matrices by utilizing reconstruction-based scoring for classification.
- Reduces mean retained memory by approximately 98.26% compared to TS-ACL across five TSCIL benchmarks while achieving a 33.43% relative accuracy improvement on GrabMyo.

## Archivist Review

We reviewed the single proposed concept (TRACE) and determined that it represents a paper-specific framework name rather than a widely reusable standalone ML primitive or method. Therefore, no concepts or open questions are approved in this cycle, maintaining the vault's high bar for novelty and generality.

### Rejected Candidates
- [concept] TRACE (`trace`) - paper_local: TRACE is a paper-specific method acronym/framework name rather than a general, highly reusable conceptual primitive for the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.35727)
- [PDF](https://arxiv.org/pdf/2610.35727)

