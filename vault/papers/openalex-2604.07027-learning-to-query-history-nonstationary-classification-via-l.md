---
# CSL-compatible fields
title: "Learning to Query History: Nonstationary Classification via Learned Retrieval"
author:
  - literal: "Jimmy Gammell"
  - literal: "Bishal Thapaliya"
  - literal: "Yoon Jung"
  - literal: "Riyasat Ohib"
  - literal: "Bilel Fehri"
  - literal: "Deepayan Chakrabarti"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07027"

# Custom fields
paper_id: "2604.07027"
paper_source: "openalex"
domain: "nlp, time-series"
tags:
  - "language-model"
  - "time-series"
  - "retrieval-augmented-generation"
  - "robustness"
  - "continual-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "learned-discrete-retrieval-mechanism"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:55:25Z"
created_at: "2026-04-11T05:55:25Z"
---

# Learning to Query History: Nonstationary Classification via Learned Retrieval

**Authors**: Jimmy Gammell, Bishal Thapaliya, Yoon Jung, Riyasat Ohib, Bilel Fehri, Deepayan Chakrabarti
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07027](https://arxiv.org/abs/2604.07027)

## Summary

This paper addresses model degradation caused by nonstationarity by reframing classification as a time series problem conditioned on historical data. To manage the high dimensionality of historical records, the authors introduce a learned discrete retrieval mechanism that samples relevant instances via input-dependent queries. This framework allows for efficient, end-to-end training and deployment while maintaining a scalable memory footprint, even when utilizing large historical datasets. Experiments show significant improvements in robustness against distribution shifts compared to traditional classification approaches.

## Key Contributions

- Reframes nonstationary classification as a time series prediction task by conditioning models on historical sequences.
- Proposes a learned discrete retrieval mechanism that enables input-dependent querying of large historical corpora without prohibitive VRAM costs.
- Demonstrates robust performance against distribution shift on synthetic benchmarks and the Amazon Reviews '23 electronics dataset compared to standard classification baselines.

## Open Questions & Future Work

- [[training-stability-discrete-retrieval-optimization]]

## Key Concepts

- [[learned-discrete-retrieval-mechanism]]: A retrieval framework that uses input-dependent queries to sample discrete historical instances for nonstationary classification, trained end-to-end via score-based gradient estimation.

## Archivist Review

The concept of a learned discrete retrieval mechanism was approved as it provides a scalable, re-usable architectural solution for incorporating large-scale historical information into classification tasks. One open question regarding training stability was approved due to the inherent difficulty of end-to-end optimization of discrete retrieval systems. Other candidates were rejected for being either too narrow or subcomponents of more general challenges.

### Approved Concepts
- Learned Discrete Retrieval Mechanism: This mechanism allows models to condition on large historical corpora for nonstationary tasks while maintaining a constant memory footprint, representing a scalable alternative to global context windows.

### Approved Open Questions
- Training stability in discrete retrieval: Understanding how to stabilize these joint training dynamics is essential for the effective scaling of retrieval-augmented systems.

### Rejected Candidates
- [open_question] Dynamic key generation for retrieval (`dynamic-key-generation-retrieval`) - subcomponent_of_broader_mechanism: This is a specific sub-problem of adaptive retrieval that is already covered by the broader need for nonstationary representation alignment.

## Links

- [Abstract](https://arxiv.org/abs/2604.07027)
- [PDF](https://arxiv.org/pdf/2604.07027)

