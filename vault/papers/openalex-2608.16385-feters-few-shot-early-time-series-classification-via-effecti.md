---
# CSL-compatible fields
title: "FETERS: Few-Shot Early Time-Series Classification via Effective Ratio Selection"
author:
  - literal: "Chen-An Tai"
  - literal: "Yujia Wu"
  - literal: "Vincent S. Tseng"
issued:
  date-parts:
    - [2026, 8, 17]
url: "https://arxiv.org/abs/2608.16385"

# Custom fields
paper_id: "2608.16385"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "few-shot-learning"
  - "evaluation"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "feters"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-20T05:20:58Z"
created_at: "2026-08-20T05:20:58Z"
---

# FETERS: Few-Shot Early Time-Series Classification via Effective Ratio Selection

**Authors**: Chen-An Tai, Yujia Wu, Vincent S. Tseng
**Date**: 2026-08-17
**Paper ID**: [openalex:2608.16385](https://arxiv.org/abs/2608.16385)

## Summary

This paper introduces FETERS, a novel few-shot early time-series classification (ETSC) framework designed to make accurate predictions from partially observed time series under data scarcity. Instead of training an extra sample-level stopping module—which is prone to overfitting in low-data regimes—FETERS determines a dataset-level stopping ratio via class-wise leave-one-out (LOO) evaluation on the support set using a penalty-based reward function. Furthermore, it combines Rocket-based features with frozen Chronos representations to achieve superior classification performance. Extensive evaluations across 69 public datasets demonstrate that FETERS achieves state-of-the-art performance in the 5-shot setting while remaining competitive in full-shot scenarios.

## Key Contributions

- Proposes FETERS, a novel few-shot early time-series classification (ETSC) framework that avoids training an extra sample-level stopping module by selecting a dataset-level stopping ratio using class-wise leave-one-out (LOO) evaluation.
- Employs a penalty-based reward function to effectively balance the accuracy-earliness trade-off under limited supervision.
- Combines Rocket-based features with frozen Chronos representations for robust few-shot time-series classification.
- Achieves state-of-the-art performance in the 5-shot setting across 69 public datasets, recording the highest average harmonic mean (HM) and winning on 38 individual datasets.

## Open Questions & Future Work

- [[few-shot-etsc-systematic-study-and-evaluation]]

## Key Concepts

- [[feters]]: A few-shot early time-series classification framework that manages the accuracy-earliness trade-off without a dedicated stopping module via dataset-level stopping ratio selection.

## Archivist Review

Approved the core framework 'FETERS' and its associated open question regarding few-shot early time-series classification under data scarcity, adhering to scarcity limits and rigorous standards.

### Approved Concepts
- FETERS: Introduces a novel few-shot early time-series classification framework leveraging dataset-level stopping ratio selection and penalty-based reward functions.

### Approved Open Questions
- Systematic Study of Few-Shot ETSC: Crucial for enabling reliable early prediction in specialized, data-scarce domains such as healthcare and industrial monitoring where annotations are scarce.

### Rejected Candidates
- [concept] Few-Shot Early Time-Series Classification (`early-time-series-classification-few-shot`) - not_novel: Too broad and descriptive of the problem domain rather than a specific reusable methodological concept.

## Links

- [Abstract](https://arxiv.org/abs/2608.16385)
- [PDF](https://arxiv.org/pdf/2608.16385)

