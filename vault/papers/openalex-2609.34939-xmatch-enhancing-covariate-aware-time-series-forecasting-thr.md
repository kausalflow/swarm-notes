---
# CSL-compatible fields
title: "XMatch: Enhancing Covariate-Aware Time Series Forecasting through Tree-Structured Exogenous Matching"
author:
  - literal: "Ziyang Zhang"
  - literal: "Hanyin Cheng"
  - literal: "Xiangfei Qiu"
  - literal: "Yang Shu"
  - literal: "Bin Yang"
  - literal: "Chenjuan Guo"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34939"

# Custom fields
paper_id: "2609.34939"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "xmatch"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:48:55Z"
created_at: "2026-09-30T10:48:55Z"
---

# XMatch: Enhancing Covariate-Aware Time Series Forecasting through Tree-Structured Exogenous Matching

**Authors**: Ziyang Zhang, Hanyin Cheng, Xiangfei Qiu, Yang Shu, Bin Yang, Chenjuan Guo
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34939](https://arxiv.org/abs/2609.34939)

## Summary

Future exogenous variables contain crucial information for forecasting endogenous time series, but existing covariate-aware models struggle to capture their complex, pattern-dependent influence. To address this, the authors propose XMatch, which matches future exogenous patterns against historical patterns to retrieve corresponding endogenous responses as explicit evidence. XMatch uses a ProtoTree structure and an adaptive matcher to balance matching precision and historical sample support across multiple exogenous dimensions. Extensive evaluations across 12 real-world datasets show that XMatch outperforms current state-of-the-art methods.

## Key Contributions

- Proposes XMatch, a covariate-aware time series forecasting framework that exploits associations between future exogenous patterns and historical endogenous patterns.
- Introduces the ProtoTree Creator to organize historical exogenous-endogenous correspondences into a tree where deeper levels incorporate additional exogenous variables.
- Designs the ProtoTree Matcher to adaptively determine the number of exogenous variables used for matching based on pattern similarity and historical support.
- Demonstrates state-of-the-art performance across 12 real-world datasets compared to existing covariate-aware forecasting baselines.

## Open Questions & Future Work

- [[adaptive-multiscale-exogenous-matching]]

## Key Concepts

- [[xmatch]]: A covariate-aware time series forecasting model that performs tree-structured exogenous matching to leverage historical endogenous response patterns as explicit evidence.

## Archivist Review

Approved the overarching XMatch framework concept and the explicit open question on adaptive multi-scale exogenous matching, while maintaining strict scarcity constraints and avoiding paper-local helper modules.

### Approved Concepts
- XMatch: Introduces a novel tree-structured exogenous matching framework for covariate-aware time series forecasting, resolving the dilemma between precise matching and sufficient historical support.

### Approved Open Questions
- Adaptive Multi-Scale Exogenous Matching: Addressing the fixed variable ordering and single patch scale limitations can improve the generalization and robustness of tree-structured exogenous matching models across complex real-world multi-covariate datasets.

## Links

- [Abstract](https://arxiv.org/abs/2609.34939)
- [PDF](https://arxiv.org/pdf/2609.34939)

