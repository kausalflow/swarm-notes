---
# CSL-compatible fields
title: "ChronoFlow: Hierarchical Flow Matching for Irregular Time Series Generation"
author:
  - literal: "Changhun Kim"
  - literal: "Sunguk Jang"
  - literal: "Jeongjun Lee"
  - literal: "Juhwan Choi"
  - literal: "Sangchul Hahn"
  - literal: "Grigorios G. Chrysos"
  - literal: "Eunho Yang"
  - literal: "Juho Lee"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33276"

# Custom fields
paper_id: "2609.33276"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "generative-adversarial-network"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "chronoflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:39Z"
created_at: "2026-09-30T10:49:39Z"
---

# ChronoFlow: Hierarchical Flow Matching for Irregular Time Series Generation

**Authors**: Changhun Kim, Sunguk Jang, Jeongjun Lee, Juhwan Choi, Sangchul Hahn, Grigorios G. Chrysos, Eunho Yang, Juho Lee
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33276](https://arxiv.org/abs/2609.33276)

## Summary

ChronoFlow is a hierarchical flow matching framework designed to address the heterogeneous generation problem of irregular time series, where models must jointly capture observation counts, irregular timings, feature co-observation patterns, and continuous feature values. By adopting a coarse-to-fine hierarchy ordered by statistical granularity, ChronoFlow decouples the complex joint distribution into structurally aligned subproblems while preserving interdependencies. Extensive evaluations across five benchmarks show substantial improvements in generation fidelity compared to existing baselines.

## Key Contributions

- Proposes ChronoFlow, a unified hierarchical flow matching framework designed for irregular time series generation that captures both feature values and observation timestamps.
- Implements a coarse-to-fine generation hierarchy that decomposes the joint irregular time series problem into observation counts, frequencies, timestamps, co-observation patterns, and value generation.
- Introduces complementary evaluation metrics for irregular time series spanning sample realism, sampling structure, value fidelity, and dependencies.
- Demonstrates strong generation fidelity improvements over existing baselines across five benchmarks.

## Open Questions & Future Work

- [[discrete-structure-conditioning-hierarchical-flow-matching]]

## Key Concepts

- [[chronoflow]]: A unified hierarchical flow matching framework organized by statistical granularity for generating irregular time series.

## Archivist Review

Approved the core framework ChronoFlow and the open question on conditioning shift in hierarchical generative models, keeping strictly to high-value architectural contributions and well-formulated technical bottlenecks.

### Approved Concepts
- ChronoFlow: Core methodological contribution for irregular time series generation using hierarchical flow matching.

### Approved Open Questions
- Discrete Structure and Conditioning Shift: Conditioning shift between ground-truth training inputs and generated upstream conditions is a central bottleneck in multi-stage hierarchical generative models, impacting error propagation and overall fidelity.

## Links

- [Abstract](https://arxiv.org/abs/2609.33276)
- [PDF](https://arxiv.org/pdf/2609.33276)

