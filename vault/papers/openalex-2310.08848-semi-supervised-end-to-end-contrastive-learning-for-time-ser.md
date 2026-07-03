---
# CSL-compatible fields
title: "Semi-Supervised End-To-End Contrastive Learning For Time Series Classification"
author:
  - literal: "Huili Cai"
  - literal: "Xiang Zhang"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2310.08848"

# Custom fields
paper_id: "2310.08848"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "contrastive-learning"
  - "semi-supervised-learning"
  - "embedding"
  - "text-classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "slots-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:54:17Z"
created_at: "2026-07-03T07:54:17Z"
---

# Semi-Supervised End-To-End Contrastive Learning For Time Series Classification

**Authors**: Huili Cai, Xiang Zhang
**Date**: 2026-06-30
**Paper ID**: [openalex:2310.08848](https://arxiv.org/abs/2310.08848)

## Summary

The paper introduces SLOTS (Semi-supervised Learning fOr Time clasSification), an end-to-end framework designed to improve time series classification in data-scarce scenarios. By moving away from traditional two-stage pre-training and fine-tuning pipelines, SLOTS optimizes an encoder and a classifier simultaneously using a joint loss function combining unsupervised contrastive, supervised contrastive, and classification components. This approach ensures that labeled data directly influences the feature embedding process, resulting in significantly higher classification performance across multiple benchmark datasets compared to conventional two-stage methods.

## Key Contributions

- Introduces SLOTS, a semi-supervised framework that jointly optimizes an encoder and classifier using unsupervised contrastive, supervised contrastive, and classification losses.
- Eliminates the performance gap inherent in two-stage pre-training/fine-tuning approaches by allowing supervised signals to guide feature representation learning directly.
- Demonstrates superior classification accuracy compared to ten state-of-the-art methods across five benchmark datasets while maintaining similar computational efficiency.

## Open Questions & Future Work

- [[balancing-performance-and-transferability]]

## Key Concepts

- [[slots-framework]]: A semi-supervised end-to-end learning framework for time series classification that jointly optimizes encoder and classifier using multi-objective loss functions.

## Archivist Review

The paper provides a straightforward improvement over two-stage semi-supervised pipelines by proposing an end-to-end joint optimization objective. I have approved the SLOTS framework for its clear methodological contribution to joint representation and task optimization, and the open question regarding the trade-off between task-specific performance and general transferability, which is a known challenge in semi-supervised representation learning. No new datasets were approved as the paper relies on standard benchmarks.

### Approved Concepts
- SLOTS framework: SLOTS integrates unsupervised contrastive, supervised contrastive, and classification losses into a unified end-to-end optimization objective, overcoming the limitations of standard two-stage pre-training/fine-tuning pipelines.

### Approved Open Questions
- Balancing Performance and Transferability: This is a fundamental limitation in the current paradigm of semi-supervised representation learning for time series, where performance improvements often come at the cost of generalization to new domains.

## Links

- [Abstract](https://arxiv.org/abs/2310.08848)
- [PDF](https://arxiv.org/pdf/2310.08848)

