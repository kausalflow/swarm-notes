---
# CSL-compatible fields
title: "PRISM: Dynamic Primitive-Based Forecasting for Large-Scale GPU Cluster Workloads"
author:
  - literal: "Xin Wu"
  - literal: "Fei Teng"
  - literal: "Xingwang Li"
  - literal: "Bin Zheng"
  - literal: "Qiang Duan"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25378"

# Custom fields
paper_id: "2603.25378"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "scaling-law"
architectures:
  []
datasets:
  []
concept_slugs:
  - "primitive-based-compositional-forecasting"
  - "adaptive-spectral-refinement-workload"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:07:19Z"
created_at: "2026-03-29T06:07:19Z"
---

# PRISM: Dynamic Primitive-Based Forecasting for Large-Scale GPU Cluster Workloads

**Authors**: Xin Wu, Fei Teng, Xingwang Li, Bin Zheng, Qiang Duan
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25378](https://arxiv.org/abs/2603.25378)

## Summary

The paper introduces PRISM, a dynamic primitive-based compositional forecasting framework designed to accurately predict highly volatile and multi-periodic GPU cluster workloads essential for efficient AI infrastructure management. PRISM utilizes a dual representation method that merges dictionary-driven temporal decomposition with adaptive spectral refinement to extract stable and interpretable workload signatures. Evaluated on large-scale production traces, PRISM demonstrates state-of-the-art accuracy, showing significant improvement in reducing burst-phase forecasting errors. This robust approach provides a crucial foundation for enabling advanced, architecture-aware dynamic resource allocation in modern GPU-powered platforms.

## Key Contributions

- Proposal of PRISM, a novel primitive-based compositional forecasting framework for highly volatile and multi-periodic GPU cluster workloads.
- Introduction of a dual representation combining dictionary-driven temporal decomposition with adaptive spectral refinement to extract stable workload signatures.
- Achieving state-of-the-art forecasting performance on large-scale production GPU traces, particularly demonstrating significant error reduction in burst phases.
- Establishing an architecture-aware foundation for dynamic resource management in GPU-powered AI infrastructures.

## Limitations

The abstract does not explicitly detail known limitations, but the reliance on 'production traces' suggests potential challenges in generalization to entirely unseen cluster configurations or job types.

## Open Questions & Future Work

- [[synergistic-effect-of-decomposition-and-spectral-refinement]]

## Key Concepts

- [[primitive-based-compositional-forecasting]]: A forecasting framework that decomposes time series into primitive components for enhanced predictive accuracy on complex workloads.
- [[adaptive-spectral-refinement-workload]]: A technique to iteratively refine temporal workload signatures by incorporating spectral analysis following initial decomposition.

## Archivist Review

Two concepts related to the core mechanism of PRISM were approved: the overarching compositional approach and the specific spectral refinement technique used within it. One open question was approved as it rigorously probes the synergistic interaction between the two main components, which is a valuable architectural insight for future compositional models. Other proposed candidates were rejected as they were either application-specific results, application domains, or subcomponents of the approved core mechanisms.

### Approved Concepts
- Primitive-Based Compositional Forecasting: This compositional framework directly addresses the complexity of modern GPU workloads by decomposing them into stable, interpretable components.
- Adaptive Spectral Refinement: This adaptive technique refines the temporal decomposition using spectral methods, necessary for capturing subtle, rapidly changing dynamics in volatile GPU workloads.

### Approved Open Questions
- Characterize Primitive-Spectral Synergy: Understanding the synergistic interaction between component-based decomposition (primitives) and frequency-domain refinement (spectral) is key to designing future compositional forecasting models for complex systems.

### Rejected Candidates
- [concept] GPU Workload Forecasting (`gpu-workload-forecasting`) - paper_local: This is the application domain rather than a novel reusable method, concept, or architecture.
- [concept] Dictionary-Driven Temporal Decomposition (`dictionary-driven-temporal-decomposition`) - subcomponent_of_broader_mechanism: This is a component sub-function, and the broader, reusable concept is 'Primitive-Based Compositional Forecasting'.
- [concept] Burst-Phase Error Reduction (`burst-phase-error-reduction`) - low_impact: This is a result/benefit of the model, not a reusable technique or representation.

## Links

- [Abstract](https://arxiv.org/abs/2603.25378)
- [PDF](https://arxiv.org/pdf/2603.25378)

