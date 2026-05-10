---
# CSL-compatible fields
title: "Enabling Federated Inference via Unsupervised Consensus Embedding"
author:
  - literal: "Yui Hashimoto"
  - literal: "Takayuki Nishio"
  - literal: "Yuichi Kitagawa"
  - literal: "Takahito Tanimura"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05718"

# Custom fields
paper_id: "2605.05718"
paper_source: "openalex"
domain: "nlp"
tags:
  - "federated-learning"
  - "inference"
  - "embedding"
  - "image-classification"
  - "privacy"
architectures:
  []
datasets:
  []
concept_slugs:
  - "consensus-embedding-based-federated-inference-ce-fi"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:13Z"
created_at: "2026-05-10T07:23:13Z"
---

# Enabling Federated Inference via Unsupervised Consensus Embedding

**Authors**: Yui Hashimoto, Takayuki Nishio, Yuichi Kitagawa, Takahito Tanimura
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05718](https://arxiv.org/abs/2605.05718)

## Summary

The paper proposes Consensus Embedding-based Federated Inference (CE-FI), a framework designed for cooperative inference among heterogeneous, independently deployed machine learning models. Unlike existing methods, CE-FI requires no raw data or parameter sharing and functions without a shared encoder by mapping intermediate representations into a unified embedding space. This mapping and subsequent output prediction are trained using only unlabeled data, demonstrating effectiveness on CIFAR-10 and CIFAR-100 benchmarks while maintaining privacy across distributed, non-IID environments.

## Key Contributions

- Introduces Consensus Embedding-based Federated Inference (CE-FI), a framework enabling cooperative inference across independent, heterogeneous models without sharing raw data or parameters.
- Implements Consensus Embedding and Cooperative Output layers trained exclusively on unlabeled data, eliminating the need for labels during the cooperative deployment stage.
- Demonstrates that CE-FI maintains performance comparable to stronger conventional sharing methods on CIFAR-10 and CIFAR-100 benchmarks under non-IID conditions.

## Open Questions & Future Work

- [[federated-inference-representation-alignment-bottlenecks]]

## Key Concepts

- [[consensus-embedding-based-federated-inference-ce-fi]]: A privacy-preserving framework enabling heterogeneous pretrained models to cooperate at inference time by mapping intermediate representations into a common embedding space using unlabeled data.

## Archivist Review

The paper's core contribution, CE-FI, is a reusable architectural paradigm for federated inference and thus qualifies for a concept note. I approved one focused open question regarding representation alignment as a bottleneck, while rejecting the original overly broad open question candidate. No datasets were approved as they are standard, common benchmarks.

### Approved Concepts
- Consensus Embedding-based Federated Inference (CE-FI): It is the core methodological contribution, proposing a way to align heterogeneous models for collaborative inference without data or parameter sharing.

### Approved Open Questions
- Federated Inference Representation Alignment Bottlenecks: Representation alignment and ensemble strategy selection were identified as the primary performance bottlenecks, and the framework currently relies on specific architectural assumptions and empirical hyperparameter choices. Further work is needed to generalize the framework and address its practical limitations regarding communication efficiency and security.

### Rejected Candidates
- [open_question] Enhancing Federated Inference Scalability and Robustness (`enhancing-federated-inference-scalability-robustness`) - generic: This candidate is a broad, boilerplate future work description; I have renamed and refocused it to the core bottleneck of representation alignment identified by the paper.

## Links

- [Abstract](https://arxiv.org/abs/2605.05718)
- [PDF](https://arxiv.org/pdf/2605.05718)

