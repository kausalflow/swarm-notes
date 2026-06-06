---
# CSL-compatible fields
title: "Multi-objective probabilistic forecast combination for inventory demand"
author:
  - literal: "Shengjie Wang"
  - literal: "Yanfei Kang"
  - literal: "Evangelos Spiliotis"
  - literal: "Fotios Petropoulos"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.04900"

# Custom fields
paper_id: "2606.04900"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "decision-focused-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-objective-probabilistic-forecast-combination"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:39:56Z"
created_at: "2026-06-06T07:39:56Z"
---

# Multi-objective probabilistic forecast combination for inventory demand

**Authors**: Shengjie Wang, Yanfei Kang, Evangelos Spiliotis, Fotios Petropoulos
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.04900](https://arxiv.org/abs/2606.04900)

## Summary

This paper introduces a multi-objective probabilistic forecast combination framework designed to align statistical forecasting with downstream inventory management goals. By moving beyond simple accuracy metrics, the proposed approach optimizes for both forecast precision and decision-specific operational outcomes simultaneously. The framework generates a set of Pareto-optimal combinations, allowing decision-makers to manage trade-offs between conflicting operational objectives. Extensive evaluation using retail and spare parts datasets shows that this method achieves more robust performance than traditional single-objective combination models.

## Key Contributions

- Proposes a novel framework that optimizes probabilistic forecast combinations by balancing statistical accuracy with inventory decision-making performance.
- Formulates inventory-aware forecasting as a multi-objective optimization problem to generate Pareto-optimal forecast combinations.
- Demonstrates superior balanced performance on real-world retail and logistics inventory datasets compared to single-objective and simple averaging baselines.

## Key Concepts

- [[multi-objective-probabilistic-forecast-combination]]: A framework that optimizes forecast combinations to simultaneously minimize statistical loss and maximize inventory performance metrics.

## Archivist Review

I approved the proposed concept as it represents a significant methodological shift from accuracy-only to decision-focused forecast combination, which is highly relevant to the time-series skill context. I rejected the datasets because they are described as proprietary industry data rather than named, publicly accessible research benchmarks.

### Approved Concepts
- Multi-objective Probabilistic Forecast Combination: It bridges the gap between purely statistical forecasting and operational decision-making by optimizing for both accuracy and specific business cost structures.

### Rejected Candidates
- [dataset] Walmart retail data (`walmart-retail-data`) - low_impact: This is a generic industry dataset reference rather than a formal, publicly available repository name.
- [dataset] Royal Air Force spare parts data (`royal-air-force-spare-parts-data`) - low_impact: This is a proprietary dataset reference that is not a standard, reusable research benchmark.

## Links

- [Abstract](https://arxiv.org/abs/2606.04900)
- [PDF](https://arxiv.org/pdf/2606.04900)

