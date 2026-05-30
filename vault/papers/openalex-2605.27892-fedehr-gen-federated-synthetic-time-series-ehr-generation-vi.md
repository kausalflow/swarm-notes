---
# CSL-compatible fields
title: "FedEHR-Gen: Federated Synthetic Time-Series EHR Generation via Latent Space Alignment and Distribution-Aware Aggregation"
author:
  - literal: "Jun Bai"
  - literal: "Ziyang Song"
  - literal: "Yue Li"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.27892"

# Custom fields
paper_id: "2605.27892"
paper_source: "openalex"
domain: "medicine"
tags:
  - "federated-learning"
  - "vae"
  - "time-series"
  - "privacy"
  - "data-augmentation"
architectures:
  []
datasets:
  - "eicu"
  - "mimic-iii"
concept_slugs:
  - "layer-wise-matching-aggregation"
dataset_slugs:
  - "eicu"
  - "mimic-iii"
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:35:53Z"
created_at: "2026-05-30T07:35:53Z"
---

# FedEHR-Gen: Federated Synthetic Time-Series EHR Generation via Latent Space Alignment and Distribution-Aware Aggregation

**Authors**: Jun Bai, Ziyang Song, Yue Li
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.27892](https://arxiv.org/abs/2605.27892)

## Summary

FedEHR-Gen addresses the limitations of centralized synthetic EHR generation by providing a privacy-preserving federated framework. The model employs a two-stage approach that first aligns distributed EHR features into a shared, compact latent space via a novel layer-wise matching aggregation mechanism. Subsequently, a federated temporal conditional variational autoencoder (TCVAE) with distribution-aware aggregation enables stable time-series generation despite significant cross-hospital heterogeneity. Experiments on eICU and MIMIC-III benchmarks confirm that the framework maintains high generation fidelity and utility without requiring raw data sharing.

## Key Contributions

- Introduces FedEHR-Gen, the first federated framework for synthetic time-series EHR generation that preserves data privacy across hospitals.
- Develops a two-stage paradigm with layer-wise matching aggregation to align local latent spaces and address high-dimensional cross-hospital EHR heterogeneity.
- Demonstrates that FedEHR-Gen achieves generation fidelity and downstream utility comparable to centralized approaches, while outperforming standard federated baselines on the eICU and MIMIC-III datasets.

## Open Questions & Future Work

- [[federated-generative-communication-efficiency]]
- [[formal-privacy-in-federated-generation]]

## Key Concepts

- [[layer-wise-matching-aggregation]]: A federated aggregation technique that aligns local encoder parameters to ensure a unified global latent space representation across distributed institutions.

## Archivist Review

The paper proposes a novel layer-wise alignment strategy for federated generative modeling, which is approved for its potential as a recurring technique in heterogeneous federated learning. Two open questions regarding communication efficiency and formal privacy were reframed into standard formats to avoid duplication and improve tracking. The eICU and MIMIC-III datasets are established benchmarks in the health-time-series domain and are approved for their central role in the paper's evaluation.

### Approved Concepts
- Layer-wise Matching Aggregation: Provides a novel federated alignment strategy specifically designed to maintain semantic consistency across heterogeneous feature spaces.

### Approved Open Questions
- Federated Generative Communication Efficiency: Communication bandwidth is a primary constraint in practical federated learning, particularly when training complex generative models across multiple institutions.
- Formal Privacy in Federated Generation: Mathematical privacy guarantees are essential for the widespread, ethical adoption of synthetic data generation in clinical collaborations.

### Rejected Candidates
- [open_question] Improve Federated Generative Communication Efficiency (`improving-communication-efficiency-federated-gen-models`) - duplicate_existing: Renamed for canonicalization and consistency with vault naming standards.
- [open_question] Integrate Formal Privacy Mechanisms (`integrating-formal-privacy-mechanisms`) - duplicate_existing: Renamed to a more standard, descriptive, and concise slug.

## Datasets

- [[eicu]]
- [[mimic-iii]]

## Links

- [Abstract](https://arxiv.org/abs/2605.27892)
- [PDF](https://arxiv.org/pdf/2605.27892)

