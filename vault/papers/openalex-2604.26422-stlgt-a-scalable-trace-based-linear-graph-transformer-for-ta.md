---
# CSL-compatible fields
title: "STLGT: A Scalable Trace-Based Linear Graph Transformer for Tail Latency Prediction in Microservices"
author:
  - literal: "Yongliang Ding"
  - literal: "Qigong Bi"
  - literal: "Peng Pu"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26422"

# Custom fields
paper_id: "2604.26422"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  - "deathstarbench"
concept_slugs:
  - "stlgt"
dataset_slugs:
  - "deathstarbench"
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:56:31Z"
created_at: "2026-05-02T06:56:31Z"
---

# STLGT: A Scalable Trace-Based Linear Graph Transformer for Tail Latency Prediction in Microservices

**Authors**: Yongliang Ding, Qigong Bi, Peng Pu
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26422](https://arxiv.org/abs/2604.26422)

## Summary

STLGT is a scalable forecasting framework designed for tail-latency prediction in microservice systems by encoding execution traces as span graphs. The model employs a structure-aware linear graph Transformer to propagate cross-service dependencies efficiently, paired with a decoupled temporal module to handle non-stationary, bursty workload dynamics. Evaluations on DeathStarBench and real-world Alibaba traces show significant improvements in both prediction accuracy and inference throughput compared to existing graph-based baselines.

## Key Contributions

- Proposed STLGT, a per-API predictor utilizing a structure-aware linear graph Transformer with linear inference complexity relative to span graph size.
- Introduced a decoupled architecture that explicitly separates cross-service dependency propagation from workload-specific temporal dynamics.
- Achieved an 8.5% average MAPE improvement over PERT-GNN on tail-latency forecasting tasks and demonstrated 12x faster CPU inference.

## Open Questions & Future Work

- [[online-adaptation-topology-drift]]

## Key Concepts

- [[stlgt]]: A scalable per-API tail-latency predictor that uses a structure-aware linear graph Transformer to capture long-range dependency propagation in microservices.

## Archivist Review

I have approved the core architecture (STLGT) and the associated dataset (DeathStarBench) as they represent a specific, reusable approach to system-level latency forecasting. I also approved the open question regarding topology drift, as it addresses a significant limitation in current graph-based forecasting frameworks. The 'decoupled temporal module' was rejected as it is a common architectural subcomponent rather than a standalone novel contribution.

### Approved Concepts
- STLGT: STLGT introduces a novel architecture that combines trace-based span graph encoding with linear-complexity transformer mechanisms for efficient system-level latency forecasting.

### Approved Open Questions
- Online Adaptation to Topology Drift: Topology drift is pervasive in cloud-native environments, and static graph assumptions limit the long-term utility of trace-based forecasting models.

### Rejected Candidates
- [concept] decoupled temporal module (`decoupled-temporal-module`) - subcomponent_of_broader_mechanism: This is a routine design pattern of decoupling features or modules in neural architectures and lacks distinct novelty.

## Datasets

- [[deathstarbench]]

## Links

- [Abstract](https://arxiv.org/abs/2604.26422)
- [PDF](https://arxiv.org/pdf/2604.26422)

