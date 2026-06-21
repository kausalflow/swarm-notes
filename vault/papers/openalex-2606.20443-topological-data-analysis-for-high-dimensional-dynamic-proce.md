---
# CSL-compatible fields
title: "Topological Data Analysis for High-Dimensional Dynamic Process Monitoring"
author:
  - literal: "Angan Mukherjee"
  - literal: "Tyler A. Soderstrom"
  - literal: "Michael J. Kurtz"
  - literal: "Ví­ctor M. Zavala"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2606.20443"

# Custom fields
paper_id: "2606.20443"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "neural-ordinary-differential-equations"
  - "topology"
architectures:
  []
datasets:
  []
concept_slugs:
  - "topological-event-detection-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:54:03Z"
created_at: "2026-06-21T08:54:03Z"
---

# Topological Data Analysis for High-Dimensional Dynamic Process Monitoring

**Authors**: Angan Mukherjee, Tyler A. Soderstrom, Michael J. Kurtz, Ví­ctor M. Zavala
**Date**: 2026-06-18
**Paper ID**: [openalex:2606.20443](https://arxiv.org/abs/2606.20443)

## Summary

This paper introduces a process monitoring framework that characterizes multivariate time-series data as manifolds, using topological data analysis to extract structural descriptors. These descriptors are then passed into a neural ordinary differential equation to capture the dynamic evolution of the system's topological structure over time. By tracking these topological trajectories, the approach identifies anomalous events in high-dimensional industrial datasets more effectively than standard reconstruction-based baselines.

## Key Contributions

- Introduces a hybrid methodology that combines topological data analysis descriptors with neural ordinary differential equations for monitoring dynamic systems.
- Demonstrates that modeling the trajectory of topological structures enables effective event detection in high-dimensional industrial time-series data.
- Provides empirical validation showing superior event detection performance compared to traditional reconstruction-based methods like PCA, autoencoders, and Koopman autoencoders.

## Open Questions & Future Work

- [[tda-causal-integration]]

## Key Concepts

- [[topological-event-detection-framework]]: A process monitoring approach that characterizes time-series as manifolds and models their topological evolution using neural ordinary differential equations.

## Archivist Review

I approved the Topological Event Detection Framework as it uniquely integrates TDA descriptors with neural ODEs for time-series monitoring, offering a distinct methodological advancement. The open question regarding TDA and causal integration is approved as it addresses a significant research gap in transitioning from detection to root-cause diagnosis, which is critical for industrial applications. I rejected the representation optimization question for being overly general and not providing a specific research bottleneck.

### Approved Concepts
- Topological Event Detection Framework: It provides a novel hybrid method that integrates TDA descriptors with neural ODEs for dynamic monitoring, which is the core innovation of the paper.

### Approved Open Questions
- Integration of TDA and causal analysis: Identifying the root cause of an anomaly is essential for effective mitigation and control; merging topological detection with causal diagnosis would significantly improve the practical utility of process monitoring frameworks.

### Rejected Candidates
- [open_question] Optimal data representations for TDA (`tda-representation-optimization`) - generic: The question regarding data representation is too broad and generic for a high-level research vault.

## Links

- [Abstract](https://arxiv.org/abs/2606.20443)
- [PDF](https://arxiv.org/pdf/2606.20443)

