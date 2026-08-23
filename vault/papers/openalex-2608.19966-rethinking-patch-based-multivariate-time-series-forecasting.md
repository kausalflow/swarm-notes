---
# CSL-compatible fields
title: "Rethinking Patch Based Multivariate Time Series Forecasting with Semantic Structured Partitioning"
author:
  - literal: "Jiazhe Wang"
  - literal: "Zhiquan Huang"
  - literal: "Linjing Xue"
  - literal: "Ming Liu"
  - literal: "Meiwen Li"
  - literal: "Ruijuan Zheng"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.19966"

# Custom fields
paper_id: "2608.19966"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "graph-neural-network"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "semantic-structured-partitioning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:19:01Z"
created_at: "2026-08-23T05:19:01Z"
---

# Rethinking Patch Based Multivariate Time Series Forecasting with Semantic Structured Partitioning

**Authors**: Jiazhe Wang, Zhiquan Huang, Linjing Xue, Ming Liu, Meiwen Li, Ruijuan Zheng
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.19966](https://arxiv.org/abs/2608.19966)

## Summary

The paper introduces SCPaT, a Transformer-based framework for multivariate time series forecasting that addresses the limitations of traditional patch-based methods via semantic structured partitioning. SCPaT first decomposes input sequences into semantically consistent units, constructs a dynamic semantic graph to capture dependencies and form higher-order blocks, and leverages an importance-aware routing mechanism for expert-based customized modeling across 12 benchmark datasets.

## Key Contributions

- Proposes SCPaT, a Transformer-based framework built on semantic structured partitioning to overcome limitations of fixed, multi-scale, and extendable patching strategies in multivariate time series forecasting.
- Introduces adaptive semantic unit generation to decompose input sequences into semantically consistent units, coupled with a dynamic semantic graph to model directed dependencies and form higher-order semantic blocks.
- Employs an importance-aware routing mechanism to adaptively dispatch semantic blocks to specialized mixture-of-experts for customized modeling.
- Demonstrates superior performance across 12 real-world datasets for multivariate time series forecasting.

## Limitations

Future work could explore scaling semantic structured partitioning to extremely long horizons and more diverse multimodal domains.

## Open Questions & Future Work

- [[scalable-graph-construction-for-mtsf]]

## Key Concepts

- [[semantic-structured-partitioning]]: A time series partitioning approach that decomposes input sequences into semantically consistent units and organizes them via a dynamic semantic graph.

## Archivist Review

Approved Semantic Structured Partitioning as a core reusable mechanism for overcoming rigid patching boundaries in time series forecasting, alongside its corresponding open question on scalable graph construction. SCPaT was rejected as a paper-local model name.

### Approved Concepts
- Semantic Structured Partitioning: It introduces a novel semantic partitioning and dynamic graph organization approach to replace rigid patching in multivariate time series forecasting.

### Approved Open Questions
- Scalable Graph Construction Strategies: Important for scaling graph-based dependency modeling to massive multivariate time series domains with thousands of variables.

### Rejected Candidates
- [concept] SCPaT Framework (`scpat`) - not_reusable: Model name acronyms without broader conceptual novelty beyond the paper itself should not be stored as standalone concepts.

## Links

- [Abstract](https://arxiv.org/abs/2608.19966)
- [PDF](https://arxiv.org/pdf/2608.19966)

