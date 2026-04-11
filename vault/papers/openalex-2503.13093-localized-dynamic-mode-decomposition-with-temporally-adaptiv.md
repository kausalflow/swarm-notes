---
# CSL-compatible fields
title: "Localized Dynamic Mode Decomposition with Temporally Adaptive Segmentation"
author:
  - literal: "Qiuqi Li"
  - literal: "Chang Liu"
  - literal: "Yifei Yang"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2503.13093"

# Custom fields
paper_id: "2503.13093"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "localized-dynamic-mode-decomposition-ldmd"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:56:28Z"
created_at: "2026-04-11T05:56:28Z"
---

# Localized Dynamic Mode Decomposition with Temporally Adaptive Segmentation

**Authors**: Qiuqi Li, Chang Liu, Yifei Yang
**Date**: 2026-04-08
**Paper ID**: [openalex:2503.13093](https://arxiv.org/abs/2503.13093)

## Summary

This paper introduces a Localized Dynamic Mode Decomposition (LDMD) framework designed to overcome the long-term predictive limitations of standard DMD methods. By partitioning temporal domains into localized subintervals and performing predictions within these segments, the approach significantly improves accuracy in modeling complex dynamical systems. The authors further refine this with an adaptive segmentation strategy to optimize computational efficiency and robustness, supported by a formal truncation error analysis. The method's effectiveness is validated across four classic physics-based benchmark problems: Burgers', Allen-Cahn, nonlinear Schrödinger, and Maxwell's equations.

## Key Contributions

- Proposes the LDMD framework, which segments temporal domains into subintervals to enhance the long-term predictive accuracy of standard dynamic mode decomposition.
- Introduces an adaptive segmentation strategy for LDMD that improves both computational efficiency and prediction robustness.
- Derives formal upper bounds for local and global truncation errors, providing a theoretical foundation for the proposed decomposition approach.

## Open Questions & Future Work

- [[data-driven-adaptive-segmentation-criteria]]

## Key Concepts

- [[localized-dynamic-mode-decomposition-ldmd]]: A forecasting framework that enhances long-term predictive accuracy in dynamical systems by integrating dynamic mode decomposition with time-domain segmentation.

## Archivist Review

The approved concept captures the primary algorithmic innovation (temporal segmentation for DMD) which is a reusable forecasting strategy. The open question was refined to be more general while preserving the technical bottleneck described in the paper regarding the reliance on governing equations for adaptive decision-making. No datasets were approved as those cited are classic physics benchmarks rather than novel, specialized datasets.

### Approved Concepts
- Localized Dynamic Mode Decomposition (LDMD): Provides a structured, modular approach to mitigating error accumulation in standard linear dynamic mode decomposition by utilizing temporal partitioning.

### Approved Open Questions
- Data-Driven Adaptive Segmentation Criteria: This is a fundamental bottleneck for deploying localized model reduction methods in real-world settings where governing physical equations are unknown or computationally prohibitive.

### Rejected Candidates
- [concept] Adaptive Segmentation Strategy (`adaptive-segmentation-strategy`) - subcomponent_of_broader_mechanism: This is a subcomponent of the broader LDMD framework and is captured by the primary LDMD concept.

## Links

- [Abstract](https://arxiv.org/abs/2503.13093)
- [PDF](https://arxiv.org/pdf/2503.13093)

