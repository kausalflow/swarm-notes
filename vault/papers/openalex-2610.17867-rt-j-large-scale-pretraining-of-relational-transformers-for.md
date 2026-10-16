---
# CSL-compatible fields
title: "RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions"
author:
  - literal: "Rishabh Ranjan"
  - literal: "Vignesh Kothapalli"
  - literal: "Harshvardhan Agarwal"
  - literal: "Charilaos I. Kanatsoulis"
  - literal: "Roshan Upendra"
  - literal: "Tom Palczewski"
  - literal: "Carlos Guestrin"
  - literal: "Jure Leskovec"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17867"

# Custom fields
paper_id: "2610.17867"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "llm"
  - "language-model"
  - "pre-training"
  - "in-context-learning"
  - "tabular"
  - "long-context"
  - "benchmark"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  - "relational-transformer-rt-j"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-16T09:25:03Z"
created_at: "2026-10-16T09:25:03Z"
---

# RT-J: Large-Scale Pretraining of Relational Transformers for Context-Efficient Predictions

**Authors**: Rishabh Ranjan, Vignesh Kothapalli, Harshvardhan Agarwal, Charilaos I. Kanatsoulis, Roshan Upendra, Tom Palczewski, Carlos Guestrin, Jure Leskovec
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17867](https://arxiv.org/abs/2610.17867)

## Summary

This paper introduces RT-J, an 85M-parameter relational foundation model designed for context-efficient predictions on tables and relational databases using minimal in-context examples. To support pretraining, the authors assemble 'The Join', a massive collection of 639 web-crawled databases featuring 6,023 LLM-generated forecasting tasks processed via a lightweight random-walk retriever. Evaluated on RelBench, RT-J matches strong feature engineering and gradient-boosting pipelines while requiring 10x fewer examples.

## Key Contributions

- Introduces RT-J, an 85M-parameter relational foundation model that achieves high-accuracy predictions using hundreds of in-context examples or fewer.
- Constructs 'The Join', a large pretraining dataset comprising 639 web-crawled databases with 6,023 LLM-generated forecasting tasks.
- Demonstrates on RelBench that RT-J requires 10x fewer examples on average to match strong feature engineering pipelines combined with traditional predictors.

## Open Questions & Future Work

- [[relational-link-prediction-recommendation]]

## Key Concepts

- [[relational-transformer-rt-j]]: An 85M-parameter relational foundation model pre-trained on a large collection of databases for context-efficient predictions.

## Archivist Review

Approved the core RT-J relational foundation model concept and the open question regarding relational link prediction and recommendation. Rejected 'The Join' dataset as it is a newly introduced, non-standard private collection without independent external community adoption yet.

### Approved Concepts
- Relational Transformer (RT-J): Central model introduced in the paper for context-efficient relational database prediction.

### Approved Open Questions
- Relational Link Prediction and Recommendation: Link prediction and recommendation are core tasks in relational learning and knowledge graph reasoning; enabling foundational support for them is crucial for broad enterprise adoption.

### Rejected Candidates
- [dataset] The Join dataset (`the-join`) - not_reusable: Newly created proprietary web-crawled dataset collection that lacks independent community validation or stable external availability.

## Links

- [Abstract](https://arxiv.org/abs/2610.17867)
- [PDF](https://arxiv.org/pdf/2610.17867)

