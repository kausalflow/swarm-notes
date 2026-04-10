---
# CSL-compatible fields
title: "Cross-Machine Anomaly Detection Leveraging Pre-trained Time-series Model"
author:
  - literal: "Yangmeng Li"
  - literal: "Kei Sano"
  - literal: "Toshihiro Kitao"
  - literal: "Ryoji Anzaki"
  - literal: "Yukiya Saitoh"
  - literal: "Hironori Moki"
  - literal: "Dragan Djurdjanović"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05335"

# Custom fields
paper_id: "2604.05335"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "pre-training"
architectures:
  []
datasets:
  []
concept_slugs:
  - "domain-invariant-feature-disentanglement"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:26:08Z"
created_at: "2026-04-10T06:26:08Z"
---

# Cross-Machine Anomaly Detection Leveraging Pre-trained Time-series Model

**Authors**: Yangmeng Li, Kei Sano, Toshihiro Kitao, Ryoji Anzaki, Yukiya Saitoh, Hironori Moki, Dragan Djurdjanović
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05335](https://arxiv.org/abs/2604.05335)

## Summary

This paper addresses the challenge of cross-machine anomaly detection in manufacturing by proposing a framework that adapts foundation model representations to new, unseen machines. By integrating the pre-trained MOMENT model with a Random Forest-based disentanglement module, the approach isolates process-relevant, condition-dependent features from machine-specific noise. This refined representation allows downstream unsupervised anomaly detection models to generalize effectively across different machines executing the same procedure. Evaluation on an industrial dataset confirms that this method significantly outperforms raw-signal and base embedding approaches.

## Key Contributions

- Proposes a cross-machine anomaly detection framework that achieves robust performance across nominally identical machines.
- Introduces a disentanglement strategy using Random Forest Classifiers on pre-trained MOMENT embeddings to isolate condition-invariant representations.
- Demonstrates superior cross-machine anomaly detection performance compared to raw-signal and standard pre-trained embedding baselines on an industrial dataset.

## Key Concepts

- [[domain-invariant-feature-disentanglement]]: A feature extraction strategy that disentangles machine-specific noise from condition-relevant signals within pre-trained time-series embeddings.

## Archivist Review

The paper is approved for its domain-invariant feature disentanglement concept, which provides a reusable architectural pattern for adapting time-series foundation models to cross-device industrial settings. Other candidates were rejected to maintain the vault's high barrier to entry for model-specific implementations or non-novel foundations.

### Approved Concepts
- Domain-Invariant Feature Disentanglement: The method addresses the bottleneck of machine-specific bias in cross-machine industrial monitoring, allowing for better generalization to unseen target machines using foundation model embeddings.

### Rejected Candidates
- [concept] MOMENT Foundation Model (`moment-foundation-model`) - not_novel: The paper utilizes an existing foundation model rather than contributing a new architectural primitive.

## Links

- [Abstract](https://arxiv.org/abs/2604.05335)
- [PDF](https://arxiv.org/pdf/2604.05335)

