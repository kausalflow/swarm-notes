---
# CSL-compatible fields
title: "An Isochron-Free Framework for Phase Reduction and Coupling Inference"
author:
  - literal: "Akari Matsuki"
  - literal: "Ryota Kobayashi"
  - literal: "Hiroshi Kori"
issued:
  date-parts:
    - [2026, 6, 24]
url: "https://arxiv.org/abs/2606.25892"

# Custom fields
paper_id: "2606.25892"
paper_source: "openalex"
domain: "time-series,biology"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "isochron-free-phase-reduction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-27T07:43:43Z"
created_at: "2026-06-27T07:43:43Z"
---

# An Isochron-Free Framework for Phase Reduction and Coupling Inference

**Authors**: Akari Matsuki, Ryota Kobayashi, Hiroshi Kori
**Date**: 2026-06-24
**Paper ID**: [openalex:2606.25892](https://arxiv.org/abs/2606.25892)

## Summary

This paper presents a theoretical framework for phase reduction in limit-cycle oscillators that avoids the traditional, often complex requirement of constructing isochrons. By using a generalized phase and a stroboscopic circle map, the authors show that valid coupling functions can be inferred directly from oscillatory data. This method provides a simpler and more robust approach to studying synchronization dynamics in weakly coupled systems. The framework is validated as a powerful tool for coupling inference where explicit isochron mapping is not feasible.

## Key Contributions

- Proved that a one-period stroboscopic circle map can describe coupled oscillator dynamics using only generalized phases, provided there is strong amplitude stability.
- Demonstrated that the circle map's coupling function matches that of the asymptotic phase equation.
- Introduced a robust method for coupling inference from oscillatory time series that bypasses the need for explicit isochron construction.

## Open Questions & Future Work

- [[high-dimensional-phase-reduction-validation]]
- [[synchronous-system-inference-limits]]

## Key Concepts

- [[isochron-free-phase-reduction]]: A framework for inferring coupling functions in limit-cycle oscillators using generalized phases instead of asymptotic phases defined by isochrons.

## Archivist Review

The approved concept captures a novel, theoretically-grounded alternative to traditional phase reduction methods that is highly reusable across oscillating systems. The open questions address specific, non-trivial bottlenecks in scaling this framework to higher dimensions and synchronous regimes, which are critical for the field of dynamical system identification. No datasets were approved as none were central to the paper's theoretical contributions.

### Approved Concepts
- Isochron-Free Phase Reduction: Enables phase reduction and coupling inference for complex oscillatory systems where calculating isochrons is computationally impractical or impossible.

### Approved Open Questions
- Higher-Dimensional Phase Reduction Validation: Generalizing phase reduction methods to high-dimensional systems is a persistent bottleneck for modeling complex phenomena in physics and biology.
- Synchronous System Inference Limits: Robust inference for synchronous systems is crucial for analyzing real-world neural and biological networks.

## Links

- [Abstract](https://arxiv.org/abs/2606.25892)
- [PDF](https://arxiv.org/pdf/2606.25892)

