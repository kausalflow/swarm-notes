---
# CSL-compatible fields
title: "KairosHope: A Next-Generation Time-Series Foundation Model for Specialized Classification via Dual-Memory Architecture"
author:
  - literal: "Luis Balderas"
  - literal: "José Alberto Rodríguez"
  - literal: "Miguel Lastra"
  - literal: "Antonio Araúzo-Azofra"
  - literal: "José M. Benítez"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18657"

# Custom fields
paper_id: "2605.18657"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "language-model"
  - "pre-training"
  - "fine-tuning"
  - "attention-mechanism"
  - "contrastive-learning"
  - "text-classification"
  - "self-supervised-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hope-block"
  - "hybrid-decision-head"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:29:03Z"
created_at: "2026-05-21T08:29:03Z"
---

# KairosHope: A Next-Generation Time-Series Foundation Model for Specialized Classification via Dual-Memory Architecture

**Authors**: Luis Balderas, José Alberto Rodríguez, Miguel Lastra, Antonio Araúzo-Azofra, José M. Benítez
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18657](https://arxiv.org/abs/2605.18657)

## Summary

KairosHope is a specialized time-series foundation model designed to bridge the gap between massive-scale pre-training and rigorous classification tasks. It replaces traditional quadratic attention with the HOPE block, featuring a dual-memory system for dynamic short-term retention and long-term context abstraction. Furthermore, it incorporates a Hybrid Decision Head that integrates deep neural representations with classical statistical features to improve inductive bias. The model is pre-trained on the Monash archive and demonstrates superior classification performance on UCR benchmarks, particularly for causal temporal domains.

## Key Contributions

- Introduces the HOPE block, which utilizes a dual-memory system to eliminate quadratic complexity in time-series foundation models.
- Develops a Hybrid Decision Head that enhances classification accuracy by merging deep latent embeddings with deterministic statistical features.
- Demonstrates state-of-the-art performance on the UCR classification benchmark through a structured LP-FT adaptation protocol.

## Open Questions & Future Work

- [[geometric-invariance-time-series-modeling]]
- [[ultra-long-sequence-memory-compression]]

## Key Concepts

- [[hope-block]]: A time-series architecture block that replaces quadratic attention with a dual-memory system comprising short-term retention and long-term historical context abstraction.
- [[hybrid-decision-head]]: A neural network head that integrates deep latent representations with deterministic statistical features to enhance time-series classification.

## Archivist Review

I approved the HOPE block and Hybrid Decision Head as they represent distinct, reusable architectural mechanisms for time-series modeling. I also approved two open questions that specifically target the critical bottlenecks of non-causal geometric modeling and extreme long-sequence memory efficiency. Standard benchmark datasets mentioned were rejected as they are widely used, established repositories rather than unique contributions of this work.

### Approved Concepts
- HOPE block: It is the foundational architectural component replacing standard quadratic attention with a specialized dual-memory mechanism.
- Hybrid Decision Head: It provides a novel method for incorporating classical statistical priors into modern deep learning classification heads.

### Approved Open Questions
- Geometric Invariance Modeling: This addresses a performance bottleneck where foundation models optimized for causal time series fail when applied to non-causal geometric data, limiting their general applicability.
- Ultra-long Sequence Memory Compression: The ability to handle very long sequences is a major barrier for foundation models in many industrial and scientific applications.

### Rejected Candidates
- [dataset] Monash archive (`monash-archive`) - not_novel: The Monash archive is a widely established, multi-dataset benchmark repository rather than a novel or single dataset contribution.
- [dataset] UCR benchmark datasets (`ucr-benchmark-datasets`) - not_novel: The UCR benchmark is a well-known, foundational set of time-series classification datasets rather than a new or critical domain-specific dataset contribution.

## Links

- [Abstract](https://arxiv.org/abs/2605.18657)
- [PDF](https://arxiv.org/pdf/2605.18657)

