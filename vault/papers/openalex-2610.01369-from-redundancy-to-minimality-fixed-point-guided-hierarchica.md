---
# CSL-compatible fields
title: "From Redundancy to Minimality: Fixed-Point-Guided Hierarchical Reduction of Learned Piecewise-Linear Dynamics"
author:
  - literal: "Hiroto Tamura"
  - literal: "Gouhei Tanaka"
issued:
  date-parts:
    - [2026, 10, 1]
url: "https://arxiv.org/abs/2610.01369"

# Custom fields
paper_id: "2610.01369"
paper_source: "openalex"
domain: "time-series"
tags:
  - "recurrent-neural-network"
  - "dynamical-systems"
  - "time-series"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-04T10:49:44Z"
created_at: "2026-10-04T10:49:44Z"
---

# From Redundancy to Minimality: Fixed-Point-Guided Hierarchical Reduction of Learned Piecewise-Linear Dynamics

**Authors**: Hiroto Tamura, Gouhei Tanaka
**Date**: 2026-10-01
**Paper ID**: [openalex:2610.01369](https://arxiv.org/abs/2610.01369)

## Summary

This paper introduces a fixed-point-guided hierarchical reduction procedure for almost-linear recurrent neural networks (AL-RNNs) to learn minimal dynamical representations from time series. Instead of directly training AL-RNNs with few ReLU units—which proves unreliable—the approach starts with excess nonlinear capacity as a scaffold, then progressively linearizes ReLU units and merges linear regions while preserving fixed-point-containing symbols. Theoretical analysis establishes that reproducing Q distinct fixed points requires at least Q such symbols, offering a minimality certificate. Experiments on the 3-scroll Chua system show that this learn-reduce-retrain strategy substantially improves success rates over direct training.

## Key Contributions

- Proposes a fixed-point-guided hierarchical reduction procedure for almost-linear recurrent neural networks (AL-RNNs) that systematically linearizes ReLU units to compress redundant nonlinear capacity into minimal dynamical representations.
- Establishes a theoretical bound proving that reproducing Q distinct fixed points requires at least Q FP-containing symbols, providing a certificate of symbol-level minimality.
- Demonstrates on the 3-scroll Chua system that the learn-reduce-retrain strategy increases the seed-macro success rate from 20% (direct training with minimal units) to approximately 71% at the same final nonlinear capacity.

## Open Questions & Future Work

- [[extending-hierarchical-reduction-to-real-world-data]]

## Archivist Review

All candidate concepts were rejected because they represent paper-local mechanisms (such as specific reduction schedules for AL-RNNs). The single open question was also rejected because it amounts to standard future work exploring generalization to real-world noisy data without specifying a precise technical formulation.

### Approved Open Questions
- Extending Hierarchical Reduction to Real-World Data: Assessing how well fixed-point-guided graph reduction and retraining perform under observational noise and partial observability is crucial for transitioning these methods from synthetic benchmarks to real-world scientific machine learning applications.

### Rejected Candidates
- [open_question] Extending Hierarchical Reduction to Real-World Data (`extending-hierarchical-reduction-to-real-world-data`) - low_impact: Although the open question discusses extending reduction frameworks to real-world data, it is a broad future work direction that lacks a specific algorithmic bottleneck or methodological formulation.

## Links

- [Abstract](https://arxiv.org/abs/2610.01369)
- [PDF](https://arxiv.org/pdf/2610.01369)

