---
# CSL-compatible fields
title: "Closed-Loop Decision-Focused Learning for User-Aware Cloud Orchestration under Uncertainty"
author:
  - literal: "Dongbin Jiao"
  - literal: "X Zhang"
  - literal: "Huakang Lin"
  - literal: "Ke Shang"
  - literal: "Shi Yan"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05735"

# Custom fields
paper_id: "2608.05735"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "reinforcement-learning"
  - "graph-neural-network"
  - "optimization"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "closed-loop-decision-focused-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:41:32Z"
created_at: "2026-08-09T05:41:32Z"
---

# Closed-Loop Decision-Focused Learning for User-Aware Cloud Orchestration under Uncertainty

**Authors**: Dongbin Jiao, X Zhang, Huakang Lin, Ke Shang, Shi Yan
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05735](https://arxiv.org/abs/2608.05735)

## Summary

The paper introduces a closed-loop decision-focused learning (CL-DFL) framework for user-aware cloud orchestration under uncertainty, replacing traditional prediction-then-optimization pipelines with an end-to-end feedback pathway. By combining a Multivariate Time-series Graph Neural Network predictor with a zeroth-order DFL mechanism and the GNeuro-PLS strategy (incorporating group relative policy optimization), the approach effectively balances violation rate, user satisfaction, and resource utilization. Extensive evaluations on four real-world datasets show that CL-DFL maintains resilience and controls overload risks under both regular and highly saturated workloads.

## Key Contributions

- Proposes a closed-loop decision-focused learning (CL-DFL) framework integrating an MTGNN-based spatio-temporal predictor with a zeroth-order DFL mechanism to bridge the gap between resource perception and scheduling decisions.
- Develops the GNeuro-PLS strategy incorporating group relative policy optimization (GRPO) into cooperative local search to enhance robustness under heterogeneous workloads.
- Demonstrates through extensive experiments on four real-world datasets that CL-DFL achieves superior trade-offs among violation rate, user satisfaction, and resource utilization compared to baseline methods.

## Open Questions & Future Work

- [[distributed-cross-domain-cloud-orchestration]]

## Key Concepts

- [[closed-loop-decision-focused-learning]]: A closed-loop decision-focused learning framework that integrates spatio-temporal prediction with zeroth-order decision-focused learning for user-aware cloud orchestration.

## Archivist Review

Approved the overarching closed-loop decision-focused learning framework and the explicit open question on distributed cross-domain orchestration. Rejected the paper-local GNeuro-PLS scheduling strategy and pre-existing MTGNN architecture to maintain high selectivity and avoid local clutter.

### Approved Concepts
- Closed-Loop Decision-Focused Learning: Forms the core novelty of integrating spatio-temporal prediction with zeroth-order decision-focused learning for cloud orchestration.

### Approved Open Questions
- Distributed Cross-Domain Cloud Orchestration: Extending DFL and cloud orchestration beyond single-cluster or localized data centers to heterogeneous, multi-domain computing environments remains an important frontier for modern large-scale distributed systems.

### Rejected Candidates
- [concept] GNeuro-PLS Strategy (`gneuro-pls-strategy`) - paper_local: This is a paper-local algorithmic strategy combining specific local search and policy optimization heuristics for cloud scheduling rather than a broadly reusable standalone vault concept.
- [concept] Multivariate Time-series Graph Neural Network (`multivariate-time-series-graph-neural-network`) - not_novel: MTGNN is a well-established existing baseline model rather than a novel contribution of this paper.

## Links

- [Abstract](https://arxiv.org/abs/2608.05735)
- [PDF](https://arxiv.org/pdf/2608.05735)

