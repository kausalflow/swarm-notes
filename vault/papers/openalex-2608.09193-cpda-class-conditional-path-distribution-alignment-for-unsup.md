---
# CSL-compatible fields
title: "CPDA: Class-Conditional Path Distribution Alignment for Unsupervised Time-Series Domain Adaptation"
author:
  - literal: "Felix Ott"
  - literal: "Christopher Mutschler"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09193"

# Custom fields
paper_id: "2608.09193"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "unsupervised-domain-adaptation"
  - "domain-adaptation"
  - "transfer-learning"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "class-conditional-path-distribution-alignment"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:08:57Z"
created_at: "2026-08-13T06:08:57Z"
---

# CPDA: Class-Conditional Path Distribution Alignment for Unsupervised Time-Series Domain Adaptation

**Authors**: Felix Ott, Christopher Mutschler
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09193](https://arxiv.org/abs/2608.09193)

## Summary

Unsupervised time-series domain adaptation addresses distribution shifts between source and target domains. Existing methods mainly align global marginal feature distributions. This paper proposes Class-Conditional Path Distribution Alignment (CPDA), a non-adversarial discrepancy-based framework that uses a composite signature-spectral kernel to align source and target class-conditional latent path distributions. Theoretical analysis shows CPDA yields a valid kernel discrepancy and a target-risk bound, and extensive experiments across 13 benchmarks demonstrate its effectiveness over numerous baselines.

## Key Contributions

- Proposes Class-Conditional Path Distribution Alignment (CPDA), a non-adversarial discrepancy-based time-series domain adaptation framework aligning class-conditional latent path distributions.
- Introduces a composite signature-spectral kernel capturing pooled semantic features, temporal path structure, frequency-domain information, and low-rank path-signature dynamics.
- Provides a theoretical analysis demonstrating that CPDA defines a valid kernel discrepancy and yields a class-conditional target-risk bound.
- Demonstrates superior performance across 13 time-series domain adaptation benchmarks against 30 baseline methods using CNN, ResNet18, and TCN backbones.

## Open Questions & Future Work

- [[class-conditional-path-alignment-small-noisy-datasets]]

## Key Concepts

- [[class-conditional-path-distribution-alignment]]: A non-adversarial discrepancy-based framework for time-series domain adaptation that aligns class-conditional latent path distributions using composite signature-spectral kernels.

## Archivist Review

Approved the core concept of class-conditional path distribution alignment for time-series domain adaptation and an open question regarding its performance bounds on small, noisy datasets with unstable pseudo-labels. No datasets qualified for standalone vault notes.

### Approved Concepts
- Class-Conditional Path Distribution Alignment: Introduces a novel non-adversarial discrepancy-based framework for time-series domain adaptation using composite signature-spectral kernels.

### Approved Open Questions
- Class-Conditional Path Alignment on Small Datasets: Understanding the failure modes and failure boundaries of pseudo-label-weighted class-conditional alignments is crucial for extending domain adaptation reliability to small, noisy, or highly complex time-series classification benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2608.09193)
- [PDF](https://arxiv.org/pdf/2608.09193)

