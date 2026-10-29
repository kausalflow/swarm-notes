---
# CSL-compatible fields
title: "LEAP: a Latent Embedding Anomaly Patch-Transformer for time-series anomaly detection"
author:
  - literal: "Cristhian Moya-Mota"
  - literal: "Ignacio Aguilera-Martos"
  - literal: "Diego García‐Gil"
  - literal: "Julián Luengo"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35190"

# Custom fields
paper_id: "2610.35190"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "transformer"
  - "self-supervised-learning"
  - "benchmark"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "leap"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:10:28Z"
created_at: "2026-10-29T11:10:28Z"
---

# LEAP: a Latent Embedding Anomaly Patch-Transformer for time-series anomaly detection

**Authors**: Cristhian Moya-Mota, Ignacio Aguilera-Martos, Diego García‐Gil, Julián Luengo
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35190](https://arxiv.org/abs/2610.35190)

## Summary

The paper introduces LEAP (Latent Embedding Anomaly Patch-Transformer), a novel time-series anomaly detection framework that avoids the flaws of direct reconstruction by combining masked patch prediction with latent representation-based anomaly evidence. LEAP uses deterministic complementary group masking to ensure every time step is scored while hidden, and integrates three label-free evidence sources: density-calibrated latent novelty, local temporal contrast, and multi-criteria per-channel novelty pooling. Evaluated under the TSB-AD protocol, LEAP demonstrates competitive performance on both multivariate and univariate benchmarks.

## Key Contributions

- Proposes LEAP, a Latent Embedding Anomaly Patch-Transformer that combines masked prediction with latent representation-based anomaly evidence without relying on direct input reconstruction.
- Introduces deterministic complementary group masking to ensure every time step is scored while hidden with identical visible fractions during training and inference.
- Incorporates three label-free evidence sources including latent-embedding novelty calibrated by local density, local temporal contrast, and per-channel novelty pooled over criteria-selected channels.
- Achieves a VUS-PR of 0.5179 on 180 held-out multivariate series under the TSB-AD protocol and 0.6194 on 350 held-out series using the univariate TSB-AD-U variant.

## Open Questions & Future Work

- [[learned-channel-weighting-for-tsad]]

## Key Concepts

- [[leap]]: A latent embedding anomaly patch-transformer that combines masked prediction with latent representation-based anomaly evidence for time-series anomaly detection.

## Archivist Review

Approved the core framework LEAP as a reusable anomaly detection approach avoiding direct reconstruction flaws. Approved one open question on learned channel weighting while rejecting paper-local parameter fusion and standard coreset questions. No standalone raw datasets were approved as TSB-AD is an evaluation benchmark protocol.

### Approved Concepts
- LEAP: LEAP serves as the core framework combining masked prediction with latent representation-based anomaly evidence for time-series anomaly detection.

### Approved Open Questions
- Learned Channel Weighting Mechanisms: This is technically important as it moves away from heuristic channel selection toward data-driven, adaptive channel reliability modeling.

### Rejected Candidates
- [open_question] Property-Dependent Fusion Coefficients (`property-dependent-fusion-coefficients`) - paper_local: Too paper-local and incremental regarding specific hyperparameter fusion schemes in anomaly detection.
- [open_question] Structured Coreset Representation Banks (`structured-coreset-representation-banks`) - not_novel: Standard application of existing coreset concepts to representation banks without a deep unique bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.35190)
- [PDF](https://arxiv.org/pdf/2610.35190)

