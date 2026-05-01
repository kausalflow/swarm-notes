---
# CSL-compatible fields
title: "Deflation-Free Optimal Scoring"
author:
  - literal: "Sharmin Afroz"
  - literal: "Brendan Ames"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25664"

# Custom fields
paper_id: "2604.25664"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "text-classification"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "deflation-free-sparse-optimal-scoring-dfsos"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:43Z"
created_at: "2026-05-01T07:22:43Z"
---

# Deflation-Free Optimal Scoring

**Authors**: Sharmin Afroz, Brendan Ames
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25664](https://arxiv.org/abs/2604.25664)

## Summary

Sparse Optimal Scoring (SOS) provides a feature selection approach to linear discriminant analysis but is traditionally limited by error-prone sequential deflation. This paper introduces Deflation-Free Sparse Optimal Scoring (DFSOS), which estimates all discriminant vectors simultaneously under explicit global orthogonality constraints. By utilizing Bregman iteration and an augmented Lagrangian approach, the method ensures convergence to stationary points. Extensive evaluations confirm that this framework provides a more robust and accurate alternative for high-dimensional classification tasks.

## Key Contributions

- Introduces Deflation-Free Sparse Optimal Scoring (DFSOS), a method that estimates multiple discriminant vectors simultaneously to avoid the error propagation of sequential deflation.
- Combines Bregman iteration with orthogonality-constrained optimization, providing a structured decomposition into tractable subproblems.
- Proves convergence to stationary points of the augmented Lagrangian under mild conditions.
- Demonstrates superior or comparable classification accuracy on high-dimensional synthetic and real-world time series datasets compared to standard SOS methods.

## Open Questions & Future Work

- [[dfsos-convergence-rates-and-consistency]]

## Key Concepts

- [[deflation-free-sparse-optimal-scoring-dfsos]]: A simultaneous optimization framework for sparse linear discriminant analysis that uses global orthogonality constraints to improve accuracy and stability.

## Archivist Review

The submission introduces a robust alternative to sequential deflation by leveraging simultaneous optimization under global constraints. I approved the DFSOS framework as a reusable concept for projection-based high-dimensional statistics. The question on convergence rates was approved for its foundational importance to the reliability of such estimators, while the request for further empirical comparisons was rejected as routine experimentation.

### Approved Concepts
- Deflation-Free Sparse Optimal Scoring (DFSOS): It addresses the fundamental error propagation and suboptimality issues inherent in traditional sequential deflation-based discriminant analysis by framing the problem as a global, simultaneous optimization.

### Approved Open Questions
- DFSOS Convergence Rates and Consistency: Theoretical convergence rates and consistency bounds are foundational for verifying algorithmic performance and ensuring that numerical solutions accurately reflect the underlying statistical model in high-dimensional domains.

### Rejected Candidates
- [open_question] Efficient Manifold Optimization for SOS (`efficient-manifold-optimization-for-sos`) - low_impact: The request for empirical comparison of state-of-the-art manifold optimization algorithms is routine future work and lacks a specific, novel bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2604.25664)
- [PDF](https://arxiv.org/pdf/2604.25664)

