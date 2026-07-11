---
# CSL-compatible fields
title: "ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation"
author:
  - literal: "Xuan-Thong Truong"
  - literal: "Trung-Kien Le"
  - literal: "Tung Kieu"
  - literal: "Thi-Thu Nguyen"
  - literal: "Nhat-Hai Nguyen"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07640"

# Custom fields
paper_id: "2607.07640"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "retrieval-augmented-generation"
  - "embedding"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "latent-embedding-alignment-lea"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:04:53Z"
created_at: "2026-07-11T07:04:53Z"
---

# ALER-TI: Aligned Latent Embedding Retrieval for Time Series Imputation

**Authors**: Xuan-Thong Truong, Trung-Kien Le, Tung Kieu, Thi-Thu Nguyen, Nhat-Hai Nguyen
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07640](https://arxiv.org/abs/2607.07640)

## Summary

ALER-TI is a retrieval-augmented framework designed to improve time series imputation by leveraging historical patterns to complement limited local temporal context. Central to its approach is the Latent Embedding Alignment (LEA) mechanism, which addresses representation mismatches between corrupted query sequences and clean historical candidates via post-hoc latent masking. The method is model-agnostic, allowing for efficient integration with existing imputation backbones through cached, pre-computed historical embeddings. Experimental results show that ALER-TI consistently enhances the accuracy and robustness of baseline imputation models across diverse real-world datasets.

## Key Contributions

- Proposes ALER-TI, a model-agnostic retrieval-augmented framework that supplements local temporal context with historical patterns for time series imputation.
- Introduces Latent Embedding Alignment (LEA), a mechanism that uses post-hoc latent masking to mitigate representation mismatch between corrupted inputs and historical candidates.
- Demonstrates through experiments on six real-world datasets that ALER-TI consistently improves imputation performance and robustness across various missing rates.

## Open Questions & Future Work

- [[retrieval-augmented-imputation-complex-missingness]]

## Key Concepts

- [[latent-embedding-alignment-lea]]: A technique to align corrupted query embeddings with complete historical candidates through post-hoc latent space masking.

## Archivist Review

I have approved the core mechanism (LEA) as it represents a generalizable strategy for latent-space alignment in retrieval tasks. The open question was approved for capturing the specific challenge of systematic missingness patterns, a known limitation in current retrieval-based imputation methods. Other candidates were not submitted.

### Approved Concepts
- Latent Embedding Alignment (LEA): LEA addresses the critical problem of representation mismatch in retrieval-augmented imputation by performing post-hoc masking in the latent space.

### Approved Open Questions
- Retrieval for Complex Missingness: Real-world sensor systems experience sustained outages rather than just random point-wise errors, making robust imputation for systematic failure modes critical for reliability.

## Links

- [Abstract](https://arxiv.org/abs/2607.07640)
- [PDF](https://arxiv.org/pdf/2607.07640)

