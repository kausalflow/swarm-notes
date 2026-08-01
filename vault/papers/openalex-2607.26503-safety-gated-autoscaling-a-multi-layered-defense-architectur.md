---
# CSL-compatible fields
title: "Safety-Gated Autoscaling: A Multi-Layered Defense Architecture for Kubernetes Vertical Resource Optimization"
author:
  - literal: "Azra Karakaya"
  - literal: "Erva Şengül"
  - literal: "Ahmet Kaplan"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26503"

# Custom fields
paper_id: "2607.26503"
paper_source: "openalex"
domain: "nlp"
tags:
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-01T07:23:50Z"
created_at: "2026-08-01T07:23:50Z"
---

# Safety-Gated Autoscaling: A Multi-Layered Defense Architecture for Kubernetes Vertical Resource Optimization

**Authors**: Azra Karakaya, Erva Şengül, Ahmet Kaplan
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26503](https://arxiv.org/abs/2607.26503)

## Summary

The paper introduces the Intelligent Cluster Optimizer, an open-source Kubernetes operator designed to optimize container resource allocation while prioritizing safety through a multi-layered defense architecture. It features a five-layer safety pipeline—including a linear regression-based memory-leak detector that blocks scaling recommendations for broken workloads—combined with Holt-Winters forecasting and multi-objective Pareto optimization. Validated on Google Kubernetes Engine, the system achieves 20-40% estimated cost savings while maintaining high detection accuracy for software defects.

## Key Contributions

- Proposes the Intelligent Cluster Optimizer, an open-source Kubernetes operator featuring a five-layer safety pipeline for vertical resource optimization.
- Implements a memory-leak detector based on linear regression with R^2 scoring that acts as a blocking gate to prevent autoscalers from enlarging leaking containers.
- Combines percentile analysis and Holt-Winters forecasting with multi-objective Pareto optimization to right-size container workloads.
- Achieves 20-40% estimated cost savings in what-if projections and 83% memory leak detection accuracy on a live Google Kubernetes Engine deployment.

## Archivist Review

The paper describes a systems-engineering operator for Kubernetes resource optimization (Intelligent Cluster Optimizer) focusing on safety pipelines and memory-leak blocking gates. It does not introduce novel machine learning concepts or fundamental methodological shifts suitable for permanent standalone vault notes.

### Rejected Candidates
- [open_question] Safety-Gated Autoscaling Enhancements (`safety-gated-autoscaling-improvements`) - low_impact: The open question is broad future work focusing on system tuning, hardening, and incremental metric improvements for a specific Kubernetes operator rather than a fundamental theoretical or methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.26503)
- [PDF](https://arxiv.org/pdf/2607.26503)

