---
# CSL-compatible fields
title: "EvoTSC: Evolving Feature Learning Models for Time Series Classification via Genetic Programming"
author:
  - literal: "Xuanhao Yang"
  - literal: "Bing Xue"
  - literal: "Mengjie Zhang"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25499"

# Custom fields
paper_id: "2604.25499"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  []
concept_slugs:
  - "evotsc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:07Z"
created_at: "2026-05-01T07:22:07Z"
---

# EvoTSC: Evolving Feature Learning Models for Time Series Classification via Genetic Programming

**Authors**: Xuanhao Yang, Bing Xue, Mengjie Zhang
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25499](https://arxiv.org/abs/2604.25499)

## Summary

EvoTSC is a genetic programming-based approach developed to automatically evolve lightweight and generalizable feature learning models for time series classification. The framework utilizes a novel multi-layer program structure to integrate domain-specific expert knowledge into the evolution, effectively guiding the search process. Additionally, a custom Pareto tournament selection strategy is employed to reduce overfitting and ensure consistency across data subsets. Experimental results show that EvoTSC consistently outperforms state-of-the-art benchmarks while remaining computationally efficient.

## Key Contributions

- Introduces EvoTSC, a genetic programming framework that automatically evolves lightweight, effective feature learning models for time series classification.
- Proposes a multi-layer program structure that embeds prior expert knowledge into the evolutionary search process for improved feature extraction.
- Implements a Pareto tournament selection strategy that enhances model generalizability by balancing performance across diverse training subsets.
- Demonstrates significant performance improvements over eleven benchmark methods on univariate time series classification datasets while maintaining high resource efficiency.

## Open Questions & Future Work

- [[multivariate-tsc-gp-extension]]
- [[cross-dataset-knowledge-transfer]]

## Key Concepts

- [[evotsc]]: A genetic programming framework that automatically evolves lightweight and generalizable feature learning models for time series classification by embedding expert knowledge.

## Archivist Review

I approved EvoTSC as a distinct framework for evolving feature learners in time series tasks, along with two open questions regarding the scalability and extensibility of this genetic programming approach. I rejected other potential candidates as they were either specific to the implementation or already covered by standard evolutionary computation research. The review strictly followed the provided skill context regarding time series classification.

### Approved Concepts
- EvoTSC: It introduces a specific multi-layer program structure for evolving feature learners by embedding expert knowledge.

### Approved Open Questions
- Multivariate TSC GP Extension: Multivariate TSC is prevalent in real-world applications, and current GP approaches are limited by their univariate focus.
- Transferring GP Building Blocks: Improving search efficiency through knowledge reuse is essential for scaling GP-based feature learning to broader domains.

## Links

- [Abstract](https://arxiv.org/abs/2604.25499)
- [PDF](https://arxiv.org/pdf/2604.25499)

