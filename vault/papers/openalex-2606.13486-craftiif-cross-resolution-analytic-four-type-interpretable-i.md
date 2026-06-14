---
# CSL-compatible fields
title: "CRAFTIIF: Cross-Resolution Analytic Four-Type Interpretable Isolation Forest for Multivariate Time Series Anomaly Detection"
author:
  - literal: "William Smits"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.13486"

# Custom fields
paper_id: "2606.13486"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "interpretability"
  - "benchmark"
architectures:
  []
datasets:
  - "mTSBench"
concept_slugs:
  - "multi-type-anomaly-specific-feature-isolation"
dataset_slugs:
  - "mtsbench"
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:37:46Z"
created_at: "2026-06-14T08:37:46Z"
---

# CRAFTIIF: Cross-Resolution Analytic Four-Type Interpretable Isolation Forest for Multivariate Time Series Anomaly Detection

**Authors**: William Smits
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.13486](https://arxiv.org/abs/2606.13486)

## Summary

CRAFTIIF is a novel unsupervised framework for multivariate time-series anomaly detection designed to detect four distinct types of anomalies: point, distributional, temporal, and collective. The system utilizes a multi-resolution analytic wavelet decomposition to extract type-specific features, which are then processed by separate, specialized Isolation Forests to allow for inherent model interpretability. Extensive evaluation on the mTSBench benchmark demonstrates superior performance compared to existing methods, while also establishing a diagnostic framework to assess the fundamental detectability of complex time-series anomalies.

## Key Contributions

- Introduces CRAFTIIF, an unsupervised framework that simultaneously detects point, distributional, temporal, and collective anomalies.
- Achieves state-of-the-art performance on the mTSBench benchmark, specifically reaching 0.463 VUS-PR.
- Provides built-in interpretability by isolating anomaly detection logic into type-specific feature branches.
- Introduces a diagnostic framework for characterizing the detectability of multivariate time-series datasets.

## Open Questions & Future Work

- [[anomaly-detectability-limits-in-mtsad]]

## Key Concepts

- [[multi-type-anomaly-specific-feature-isolation]]: A framework for anomaly detection that uses type-specific wavelet feature extraction and independent isolation forests to attribute detected anomalies to specific structural categories.

## Archivist Review

I approved the core structural mechanism of type-specific isolation forests and the benchmark mTSBench, which is central to evaluating the proposed framework. I defined a new concept for the isolation methodology to ensure reusability while rejecting the paper-specific name 'CRAFTIIF' as a concept. I also established a new open question regarding dataset-level detectability, as the paper's diagnostic framework for this is an important contribution to the anomaly detection literature.

### Approved Concepts
- Multi-type Anomaly-specific Feature Isolation: It provides a modular, interpretable architecture for anomaly detection by decoupling feature extraction and detection logic for distinct structural anomaly types.

### Approved Open Questions
- Detectability Limits in MTSAD: Understanding detectability limits prevents the pursuit of infeasible performance gains on fundamentally ambiguous datasets.

### Rejected Candidates
- [concept] CRAFTIIF framework (`craftiif-framework`) - duplicate_existing: Redundant with the more general and descriptive 'Multi-type Anomaly-specific Feature Isolation' concept.
- [open_question] Automated Anomaly Rate Estimation (`automated-anomaly-rate-estimation-for-mtsad`) - paper_local: The description is highly specific to a single implementation detail rather than a broad, persistent research bottleneck.

## Datasets

- [[mtsbench]]

## Links

- [Abstract](https://arxiv.org/abs/2606.13486)
- [PDF](https://arxiv.org/pdf/2606.13486)

