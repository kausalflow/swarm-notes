---
# CSL-compatible fields
title: "Divide and Contrast: Learning Robust Temporal Features without Augmentation"
author:
  - literal: "Abdul-Kazeem Shamba"
  - literal: "Kerstin Bach"
  - literal: "Gavin Taylor"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21241"

# Custom fields
paper_id: "2605.21241"
paper_source: "openalex"
domain: "time-series"
tags:
  - "self-supervised-learning"
  - "contrastive-learning"
  - "time-series"
  - "representation-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "di-cot"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:26:07Z"
created_at: "2026-05-23T07:26:07Z"
---

# Divide and Contrast: Learning Robust Temporal Features without Augmentation

**Authors**: Abdul-Kazeem Shamba, Kerstin Bach, Gavin Taylor
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21241](https://arxiv.org/abs/2605.21241)

## Summary

Divide and Contrast (Di-COT) is a novel self-supervised learning framework for time-series that avoids common pitfalls of data augmentation and redundant encoder passes. By stochastically partitioning windows into overlapping sub-blocks, the model efficiently learns semantic structures without being sensitive to false positives at temporal transitions. Di-COT achieves state-of-the-art performance on multiple benchmarks while enabling training costs that are independent of sequence length, facilitating high scalability for large-scale time-series analysis.

## Key Contributions

- Introduces Di-COT, a self-supervised framework that contrasts stochastically partitioned sub-blocks instead of relying on traditional data augmentation.
- Achieves sequence-length-independent loss computation, leading to significant reduction in training time and improved scalability.
- Demonstrates state-of-the-art results across classification, clustering, kNN, and cross-dataset transfer tasks on six large-scale datasets plus UCR and UEA benchmarks.

## Open Questions & Future Work

- [[contrastive-learning-forecasting-transferability]]

## Key Concepts

- [[di-cot]]: An unsupervised time-series representation learning framework that contrasts informative substructures within a window to avoid data augmentation.

## Archivist Review

I approved the Di-COT framework as it introduces a distinct augmentation-free mechanism for temporal representation learning. I also approved the open question regarding the adaptation of contrastive learning for forecasting to address the identified gap between discriminative representation learning and sequence prediction. UCR/UEA datasets were rejected as they are standard community benchmarks.

### Approved Concepts
- Divide and Contrast (Di-COT): It is the core proposal of the paper, offering an augmentation-free and efficient alternative to standard contrastive learning for time-series.

### Approved Open Questions
- Adapting contrastive learning for forecasting: This is a critical limitation for bridging the gap between representation learning and forecasting in time-series analysis.

### Rejected Candidates
- [dataset] UCR and UEA benchmarks (`ucr-uea-benchmarks`) - generic: These are standard community benchmarks rather than a single novel or specific dataset presented for the first time in this paper.

## Links

- [Abstract](https://arxiv.org/abs/2605.21241)
- [PDF](https://arxiv.org/pdf/2605.21241)

