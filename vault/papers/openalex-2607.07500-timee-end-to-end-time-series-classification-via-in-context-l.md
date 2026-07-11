---
# CSL-compatible fields
title: "TimEE: End-to-end Time Series Classification via In-Context Learning"
author:
  - literal: "Jaris Küken"
  - literal: "Shi Bin Hoo"
  - literal: "Martin Mráz"
  - literal: "Frank Hutter"
  - literal: "Lennart Purucker"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07500"

# Custom fields
paper_id: "2607.07500"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "in-context-learning"
  - "foundation-model"
  - "text-classification"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "timee"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:03Z"
created_at: "2026-07-11T07:05:03Z"
---

# TimEE: End-to-end Time Series Classification via In-Context Learning

**Authors**: Jaris Küken, Shi Bin Hoo, Martin Mráz, Frank Hutter, Lennart Purucker
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07500](https://arxiv.org/abs/2607.07500)

## Summary

TimEE is a 4.5M-parameter foundation model that treats time series classification (TSC) as an in-context learning task, eliminating the need for traditional two-stage feature engineering or per-dataset fine-tuning. The model is meta-trained exclusively on synthetic data generated from structured distributional shifts, allowing it to generalize to real-world tasks without ever encountering them during training. Experimental results on the UCR benchmark show that TimEE achieves state-of-the-art performance, outperforming both supervised baselines and prior foundation models.

## Key Contributions

- Introduces TimEE, an end-to-end foundation model for time series classification that performs in-context learning without requiring per-dataset training.
- Demonstrates that a model meta-trained exclusively on synthetic tasks can achieve state-of-the-art performance on the UCR benchmark.
- Provides a scalable, lightweight (4.5M parameters) alternative to traditional two-stage TSC paradigms that decouple feature learning from classification.

## Open Questions & Future Work

- [[multivariate-synthetic-prior-design]]
- [[scalable-multi-class-icl-inference]]

## Key Concepts

- [[timee]]: A 4.5M-parameter foundation model for end-to-end time series classification using in-context learning without per-dataset training.

## Archivist Review

I approved the TimEE framework as it establishes a new end-to-end in-context learning paradigm for TSC based solely on synthetic priors. I also approved two open questions that specifically address the current limitations of synthetic prior generation for multivariate data and the inference scaling challenges of multi-class classification, as these are clear, substantial research bottlenecks. I rejected the UCR benchmark as it is an established archive, not a novel dataset contribution.

### Approved Concepts
- TimEE: It represents a novel end-to-end foundation model approach for TSC, treating it as an in-context classification problem rather than a traditional two-stage paradigm.

### Approved Open Questions
- Multivariate Synthetic Prior Design: This is a fundamental barrier to scaling TSC foundation models beyond simple univariate or small-scale multivariate datasets.
- Scalable Multi-class ICL Inference: Handling large label spaces efficiently is essential for moving toward general-purpose, scalable foundation models for time series classification.

### Rejected Candidates
- [dataset] UCR benchmark (`ucr-benchmark`) - duplicate_existing: The UCR benchmark is a standard, widely-used archive of datasets rather than a novel or single dataset contribution.

## Links

- [Abstract](https://arxiv.org/abs/2607.07500)
- [PDF](https://arxiv.org/pdf/2607.07500)

