---
# CSL-compatible fields
title: "XCTFormer: Leveraging Cross-Channel and Cross-Time Dependencies for Enhanced Time-Series Analysis"
author:
  - literal: "Israel Zexer"
  - literal: "Omri Azencot"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18534"

# Custom fields
paper_id: "2605.18534"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "attention-mechanism"
  - "time-series"
  - "imputation"
  - "multivariate-time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cross-relational-attention-block-crab"
  - "dependency-compression-plugin-decop"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:30:22Z"
created_at: "2026-05-21T08:30:22Z"
---

# XCTFormer: Leveraging Cross-Channel and Cross-Time Dependencies for Enhanced Time-Series Analysis

**Authors**: Israel Zexer, Omri Azencot
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18534](https://arxiv.org/abs/2605.18534)

## Summary

XCTFormer is a channel-dependent transformer architecture designed to overcome the limitations of current models by explicitly capturing cross-temporal and cross-channel dependencies. Utilizing a novel token-to-token Cross-Relational Attention Block (CRAB), the model models pairwise interactions across the entire spatio-temporal space. To ensure efficiency, an optional Dependency Compression Plugin (DeCoP) is introduced, significantly improving scalability. The framework demonstrates state-of-the-art performance, particularly on multivariate imputation tasks, by effectively exploiting latent inter-variable relationships.

## Key Contributions

- Proposes XCTFormer, a transformer-based model that explicitly captures complex cross-channel and cross-temporal dependencies.
- Introduces the Cross-Relational Attention Block (CRAB) for high-capacity, token-to-token pairwise dependency modeling.
- Develops the Dependency Compression Plugin (DeCoP) to enhance scalability for high-dimensional multivariate sequences.
- Achieves state-of-the-art results on imputation benchmarks, outperforming existing methods by 20.8% in MSE and 15.3% in MAE.

## Open Questions & Future Work

- [[modeling-cross-channel-time-dependencies]]

## Key Concepts

- [[cross-relational-attention-block-crab]]: A transformer-based attention mechanism that captures pairwise dependencies between all tokens across both time and channel dimensions.
- [[dependency-compression-plugin-decop]]: A scalable plug-in module designed to reduce the computational complexity of dense attention mechanisms in multivariate models.

## Archivist Review

The approved concepts represent a novel architectural block for joint spatio-temporal attention and a specific, reusable strategy for mitigating its computational overhead, both of which are central to the paper's contribution. The open question regarding channel-dependent versus channel-independent modeling is a long-standing debate in the field, and the chosen formulation effectively captures the current research friction in multivariate time-series analysis. No datasets were approved as none were unique or central enough to the paper's contribution to warrant permanent vault status.

### Approved Concepts
- Cross-Relational Attention Block (CRAB): Central architectural component enabling explicit, token-to-token modeling of cross-temporal and cross-channel dependencies.
- Dependency Compression Plugin (DeCoP): Solves the computational bottleneck inherent in all-to-all token attention, enabling the model to scale to longer sequences or higher channel counts.

### Approved Open Questions
- Modeling Cross-Channel Time Dependencies: This addresses the paradoxical finding that simpler CI models often outperform more complex CD models in many forecasting benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2605.18534)
- [PDF](https://arxiv.org/pdf/2605.18534)

